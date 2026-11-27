"""Converte pixels da Sirius em latitude/longitude pelo quadriculado impresso.

Uso (CMD, na pasta 09-steel-jacket):
    python scripts\\sirius_converter.py

Entradas (pasta sirius/), em pixels da SIRIUS_COMPLETA_COMMONS.jpg (6784 x 15819):
    gcp_sirius.csv         cruzamentos do quadriculado, separados por folha do mosaico
    pontos_sirius_px.csv   pontos marcados na Sirius
    areas_sirius_px.csv    contornos (vértices em ordem)
Saídas:
    sirius/pontos_sirius_convertidos.csv
    sirius/areas.geojson

A Sirius é um mosaico de folhas que não coincidem nas emendas. Cada pixel é
convertido com a transformação da folha onde ele está; a folha é decidida
pelas emendas abaixo (medidas nos blocos X 0-6000, Y 4000-10000).
"""
import csv
import json
import math
from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent / "sirius"
EMENDA_X = 3400        # emenda vertical entre a coluna oeste (E) e a leste (D)
EMENDA_Y = 7540        # emenda horizontal entre as folhas 1 (norte) e 2 (sul)
LIMITE_Y = (5700, 9400)  # faixa coberta pelas folhas 1 e 2; fora dela não converte
M_LAT = 110574.0


def m_lon(lat):
    return 111320.0 * math.cos(math.radians(lat))


def folha_de(x, y):
    if not (LIMITE_Y[0] <= y <= LIMITE_Y[1]):
        return None
    return ("E" if x < EMENDA_X else "D") + ("1" if y < EMENDA_Y else "2")


def resolver(m, v):
    n = len(v)
    a = [row[:] + [v[i]] for i, row in enumerate(m)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(a[r][c]))
        a[c], a[p] = a[p], a[c]
        for r in range(n):
            if r != c:
                f = a[r][c] / a[c][c]
                a[r] = [x - f * y for x, y in zip(a[r], a[c])]
    return [a[i][n] / a[i][i] for i in range(n)]


def ajustar_afim(gcps):
    """Mínimos quadrados: lon = a*x + b*y + c ; lat = d*x + e*y + f."""
    ata = [[0.0] * 3 for _ in range(3)]
    atl, atb = [0.0] * 3, [0.0] * 3
    for g in gcps:
        lin = [g["x"], g["y"], 1.0]
        for i in range(3):
            atl[i] += lin[i] * g["lon"]
            atb[i] += lin[i] * g["lat"]
            for j in range(3):
                ata[i][j] += lin[i] * lin[j]
    return resolver(ata, atl), resolver(ata, atb)


def aplicar(t, x, y):
    (a, b, c), (d, e, f) = t
    return a * x + b * y + c, d * x + e * y + f


def ler(nome):
    with (PASTA / nome).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main():
    gcps = {}
    for g in ler("gcp_sirius.csv"):
        x, y = float(g["sirius_x"]), float(g["sirius_y"])
        if folha_de(x, y) != g["folha"]:
            raise SystemExit(f"{g['id']}: folha declarada {g['folha']} não confere com a posição")
        gcps.setdefault(g["folha"], []).append(
            {"id": g["id"], "x": x, "y": y, "lon": float(g["lon"]), "lat": float(g["lat"])})

    transf = {}
    for folha in sorted(gcps):
        lista = gcps[folha]
        if len(lista) < 3:
            print(f"Folha {folha}: só {len(lista)} ponto(s) de controle; não convertida")
            continue
        t = ajustar_afim(lista)
        transf[folha] = t
        erros = []
        for g in lista:
            lon, lat = aplicar(t, g["x"], g["y"])
            erros.append(math.hypot((lon - g["lon"]) * m_lon(lat), (lat - g["lat"]) * M_LAT))
        rms = math.sqrt(sum(e * e for e in erros) / len(erros))
        print(f"Folha {folha}: {len(lista)} pontos de controle, "
              f"erro médio quadrático {rms:.0f} m, máximo {max(erros):.0f} m")

    def converter(x, y, rotulo):
        f = folha_de(x, y)
        if f not in transf:
            raise SystemExit(f"{rotulo}: pixel ({x}, {y}) fora das folhas convertidas")
        lon, lat = aplicar(transf[f], x, y)
        return f, lon, lat

    saida = []
    for p in ler("pontos_sirius_px.csv"):
        x, y = float(p["sirius_x"]), float(p["sirius_y"])
        f, lon, lat = converter(x, y, p["id"])
        saida.append({"id": p["id"], "folha": f, "sirius_x": p["sirius_x"], "sirius_y": p["sirius_y"],
                      "lat": f"{lat:.5f}", "lon": f"{lon:.5f}", "descricao": p["descricao"]})
        print(f"{p['id']}: Sirius ({x:.0f}, {y:.0f}) folha {f} -> {lat:.5f}, {lon:.5f}")
    with (PASTA / "pontos_sirius_convertidos.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "folha", "sirius_x", "sirius_y", "lat", "lon", "descricao"])
        w.writeheader()
        w.writerows(saida)

    areas = {}
    for v in ler("areas_sirius_px.csv"):
        areas.setdefault(v["id"], []).append(v)
    feicoes = []
    for ident, vs in areas.items():
        vs.sort(key=lambda v: int(v["ordem"]))
        anel = []
        for v in vs:
            _, lon, lat = converter(float(v["sirius_x"]), float(v["sirius_y"]), f"{ident}#{v['ordem']}")
            anel.append([round(lon, 6), round(lat, 6)])
        anel.append(anel[0])
        cx = sum(p[0] for p in anel[:-1]) / (len(anel) - 1)
        cy = sum(p[1] for p in anel[:-1]) / (len(anel) - 1)
        feicoes.append({"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [anel]},
                        "properties": {"id": ident, "centro_lat": round(cy, 5), "centro_lon": round(cx, 5)}})
        print(f"{ident}: área com {len(vs)} vértices, centro {cy:.5f}, {cx:.5f}")
    (PASTA / "areas.geojson").write_text(json.dumps(
        {"type": "FeatureCollection", "features": feicoes}, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
