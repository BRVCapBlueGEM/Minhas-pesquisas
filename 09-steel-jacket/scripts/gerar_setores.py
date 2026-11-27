"""Calcula os setores (mapas) e a malha hexagonal de cada um.

Uso (CMD, na pasta 09-steel-jacket):
    python scripts\\gerar_setores.py

Requer: pip install pyproj

Entradas: pontos/pontos.csv, sirius/areas.geojson, setores/setores.csv
Saídas (pasta setores/):
    setores.geojson     contorno de cada setor (WGS84)
    hexagonos.geojson   hexágonos de todos os setores (WGS84), com ID q,r
    hexagonos.csv       hexágonos com centro em EPSG:23036, pontos e cenas
    entradas.csv        pontos fora do mapa e o hexágono de borda por onde entram
    resumo.md           tamanho de cada setor, número de hexágonos, pontos
"""
import csv
import json
import math
import sys
from pathlib import Path

from pyproj import Transformer

sys.path.insert(0, str(Path(__file__).resolve().parent))
import malha  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
PARA_UTM = Transformer.from_crs(4326, malha.EPSG, always_xy=True)
PARA_GEO = Transformer.from_crs(malha.EPSG, 4326, always_xy=True)


def dist_segmento(c, a, b):
    """Distância do ponto c ao segmento a-b."""
    ax, ay = a; bx, by = b; cx, cy = c
    dx, dy = bx - ax, by - ay
    t = max(0.0, min(1.0, ((cx - ax) * dx + (cy - ay) * dy) / (dx * dx + dy * dy)))
    return math.hypot(cx - (ax + t * dx), cy - (ay + t * dy))


def ler_csv(caminho):
    with caminho.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main():
    pontos = {}
    for p in ler_csv(BASE / "pontos" / "pontos.csv"):
        if p["lat"] and p["lon"]:
            x, y = PARA_UTM.transform(float(p["lon"]), float(p["lat"]))
            pontos[p["id"]] = {"x": x, "y": y, "nome": p["nome"], "cenas": p["cenas"], "grau": p["grau"]}

    areas = {}
    for f in json.loads((BASE / "sirius" / "areas.geojson").read_text(encoding="utf-8"))["features"]:
        areas[f["properties"]["id"]] = [PARA_UTM.transform(lon, lat)
                                        for lon, lat in f["geometry"]["coordinates"][0]]

    setores = ler_csv(BASE / "setores" / "setores.csv")
    saida = BASE / "setores"
    feic_setores, feic_hex, linhas_hex, linhas_ent = [], [], [], []
    resumo = ["# Setores e malha", "",
              f"Malha: hexágonos pointy-top, {malha.PASSO:.0f} m entre centros, EPSG:{malha.EPSG}, "
              f"origem do HEX_MAGRO ({malha.X0:.0f}; {malha.Y0:.4f}). IDs axiais globais q,r.", "",
              "| Setor | Nome | Largura × altura | Hexágonos | Pontos dentro | Entradas pela borda |",
              "|---|---|---|---|---|---|"]

    # hexágono de cada ponto (global)
    hex_ponto = {pid: malha.hex_de(p["x"], p["y"]) for pid, p in pontos.items()}

    for s in setores:
        base = [b for b in s["pontos_base"].split(";") if b]
        faltam = [b for b in base if b not in pontos]
        if faltam:
            raise SystemExit(f"Setor {s['setor']}: pontos sem coordenada: {faltam}")
        xs, ys = [], []
        for b in base:
            xs.append(pontos[b]["x"]); ys.append(pontos[b]["y"])
            for x, y in areas.get(b, []):
                xs.append(x); ys.append(y)
        m = float(s["margem_m"])
        xmin, xmax, ymin, ymax = min(xs) - m, max(xs) + m, min(ys) - m, max(ys) + m
        hexes = malha.hexes_no_retangulo(xmin, ymin, xmax, ymax)
        conjunto = set(hexes)

        anel = [PARA_GEO.transform(x, y) for x, y in
                [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax), (xmin, ymin)]]
        feic_setores.append({"type": "Feature",
                             "geometry": {"type": "Polygon", "coordinates": [[list(map(lambda v: round(v, 6), p)) for p in anel]]},
                             "properties": {"setor": s["setor"], "nome": s["nome"], "cenas": s["cenas"],
                                            "xmin": round(xmin), "ymin": round(ymin),
                                            "xmax": round(xmax), "ymax": round(ymax), "epsg": malha.EPSG}})

        dentro = sorted(pid for pid, h in hex_ponto.items() if h in conjunto)
        for q, r in hexes:
            cx, cy = malha.centro(q, r)
            pids = [pid for pid in dentro if hex_ponto[pid] == (q, r)]
            cenas = sorted({int(c) for pid in pids for c in pontos[pid]["cenas"].split(";") if c})
            linhas_hex.append({"setor": s["setor"], "id": f"{q},{r}", "q": q, "r": r,
                               "cx": round(cx, 1), "cy": round(cy, 1),
                               "pontos": ";".join(pids), "cenas": ";".join(map(str, cenas))})
            anel = [list(map(lambda v: round(v, 6), PARA_GEO.transform(x, y))) for x, y in malha.vertices(q, r)]
            anel.append(anel[0])
            feic_hex.append({"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [anel]},
                             "properties": {"setor": s["setor"], "id": f"{q},{r}", "q": q, "r": r,
                                            "pontos": ";".join(pids)}})

        entradas = []
        for item in [e for e in s["fora_do_mapa"].split(";") if e]:
            # formato PONTO>DESTINO: entra pela borda no caminho em linha reta até o destino
            pid, _, destino = item.partition(">")
            if pid not in pontos or (destino and destino not in pontos):
                raise SystemExit(f"Setor {s['setor']}: ponto de entrada sem coordenada: {item}")
            p = pontos[pid]
            candidatos = hexes
            if destino:
                d = pontos[destino]
                candidatos = [h for h in hexes if dist_segmento(malha.centro(*h), (p["x"], p["y"]),
                                                                (d["x"], d["y"])) <= malha.RAIO * 1.2] or hexes
            borda = min(candidatos, key=lambda h: math.dist(malha.centro(*h), (p["x"], p["y"])))
            dist = math.dist(malha.centro(*borda), (p["x"], p["y"])) / 1000
            entradas.append(f"{pid}→{borda[0]},{borda[1]}")
            linhas_ent.append({"setor": s["setor"], "ponto": pid, "hex_entrada": f"{borda[0]},{borda[1]}",
                               "distancia_km": f"{dist:.1f}"})

        resumo.append(f"| {s['setor']} | {s['nome']} | {(xmax - xmin) / 1000:.1f} × {(ymax - ymin) / 1000:.1f} km | "
                      f"{len(hexes)} | {', '.join(dentro)} | {', '.join(entradas) or '—'} |")
        print(f"Setor {s['setor']}: {(xmax - xmin) / 1000:.1f} x {(ymax - ymin) / 1000:.1f} km, "
              f"{len(hexes)} hexágonos, {len(dentro)} pontos dentro, {len(entradas)} entrada(s)")

    geo = lambda feics: json.dumps({"type": "FeatureCollection", "features": feics}, ensure_ascii=False)
    (saida / "setores.geojson").write_text(geo(feic_setores), encoding="utf-8")
    (saida / "hexagonos.geojson").write_text(geo(feic_hex), encoding="utf-8")
    with (saida / "hexagonos.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["setor", "id", "q", "r", "cx", "cy", "pontos", "cenas"])
        w.writeheader(); w.writerows(linhas_hex)
    with (saida / "entradas.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["setor", "ponto", "hex_entrada", "distancia_km"])
        w.writeheader(); w.writerows(linhas_ent)

    resumo += ["", "## Hexágono de cada ponto", "", "| Ponto | Hexágono q,r | Grau |", "|---|---|---|"]
    for pid in sorted(hex_ponto):
        resumo.append(f"| {pid} | {hex_ponto[pid][0]},{hex_ponto[pid][1]} | {pontos[pid]['grau']} |")
    repetidos = {}
    for pid, h in hex_ponto.items():
        repetidos.setdefault(h, []).append(pid)
    juntos = [v for v in repetidos.values() if len(v) > 1]
    if juntos:
        resumo += ["", "## Pontos que caem no mesmo hexágono", ""] + [f"- {', '.join(v)}" for v in juntos]
    (saida / "resumo.md").write_text("\n".join(resumo) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
