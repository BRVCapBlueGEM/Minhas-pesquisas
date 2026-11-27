"""Gera pontos.geojson e verificacao.md a partir de pontos.csv.

Uso (CMD, na pasta 09-steel-jacket):
    python scripts\\gerar_pontos.py

Só usa a biblioteca padrão do Python. Não altera o CSV.
"""
import csv
import json
import math
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "pontos"
CSV = BASE / "pontos.csv"
GEOJSON = BASE / "pontos.geojson"
RELATORIO = BASE / "verificacao.md"

COLUNAS = ["id", "nome", "tipo", "margem", "lat", "lon", "incerteza_m",
           "grau", "metodo", "fonte", "restricao", "cenas"]

# Conferências de coerência: (ponto A, ponto B, distância mínima km, máxima km, motivo)
CONFERENCIAS = [
    ("MATZMED", "AERODROMO_DEVERSOIR", 1.0, 5.0,
     "Matzmed (margem leste) fica em frente a Deversoir (margem oeste)"),
    ("MATZMED", "FAZENDA_CHINESA", 0.5, 6.0,
     "A Fazenda Chinesa fica logo ao norte do cruzamento Lexicon-Tirtur (Matzmed)"),
    ("MATZMED", "REFIDIM", 70.0, 95.0,
     "Refidim fica a 80-90 km a leste do canal"),
]


def distancia_km(a, b):
    """Distância geodésica aproximada (haversine, raio médio 6371 km)."""
    lat1, lon1, lat2, lon2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = (math.sin((lat2 - lat1) / 2) ** 2
         + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2)
    return 2 * 6371.0 * math.asin(math.sqrt(h))


def ler_pontos():
    with CSV.open(encoding="utf-8", newline="") as f:
        leitor = csv.DictReader(f)
        if leitor.fieldnames != COLUNAS:
            raise SystemExit(f"Cabeçalho inesperado em {CSV}: {leitor.fieldnames}")
        pontos = []
        for n, linha in enumerate(leitor, start=2):
            if None in linha or any(linha[c] is None for c in COLUNAS):
                raise SystemExit(f"Linha {n}: número de colunas errado")
            pontos.append(linha)
    ids = [p["id"] for p in pontos]
    repetidos = {i for i in ids if ids.count(i) > 1}
    if repetidos:
        raise SystemExit(f"IDs repetidos: {sorted(repetidos)}")
    return pontos


def main():
    pontos = ler_pontos()
    coord = {}
    feicoes = []
    pendentes = []
    for p in pontos:
        if p["lat"] and p["lon"]:
            lat, lon = float(p["lat"]), float(p["lon"])
            if not (29.0 < lat < 32.0 and 31.0 < lon < 34.5):
                raise SystemExit(f"{p['id']}: coordenada fora da região do Canal/Sinai")
            coord[p["id"]] = (lat, lon)
            props = {k: p[k] for k in COLUNAS if k not in ("lat", "lon")}
            props["cenas"] = [int(c) for c in p["cenas"].split(";") if c]
            props["incerteza_m"] = int(p["incerteza_m"]) if p["incerteza_m"] else None
            feicoes.append({
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [lon, lat]},
                "properties": props,
            })
        else:
            pendentes.append(p)

    GEOJSON.write_text(json.dumps(
        {"type": "FeatureCollection", "features": feicoes},
        ensure_ascii=False, indent=2), encoding="utf-8")

    linhas = ["# Verificação da lista de pontos", "",
              "Gerado por `scripts/gerar_pontos.py` a partir de `pontos.csv`. Não editar à mão.", "",
              f"- Pontos no CSV: {len(pontos)}",
              f"- Com coordenada: {len(feicoes)}",
              f"- Pendentes: {len(pendentes)}", "",
              "## Conferências de coerência", "",
              "| A | B | Distância (km) | Esperado (km) | Resultado | Motivo |",
              "|---|---|---|---|---|---|"]
    falhas = 0
    for a, b, dmin, dmax, motivo in CONFERENCIAS:
        if a in coord and b in coord:
            d = distancia_km(coord[a], coord[b])
            ok = dmin <= d <= dmax
            falhas += not ok
            linhas.append(f"| {a} | {b} | {d:.2f} | {dmin:g}–{dmax:g} | "
                          f"{'OK' if ok else 'FALHOU'} | {motivo} |")
        else:
            linhas.append(f"| {a} | {b} | — | {dmin:g}–{dmax:g} | SEM DADOS | {motivo} |")
    linhas += ["", "## Pendentes (precisam de coordenada)", "",
               "| ID | Nome | Cenas | O que se sabe |", "|---|---|---|---|"]
    for p in pendentes:
        linhas.append(f"| {p['id']} | {p['nome']} | {p['cenas'].replace(';', ', ')} | {p['restricao']} |")
    RELATORIO.write_text("\n".join(linhas) + "\n", encoding="utf-8")

    print(f"{len(feicoes)} pontos com coordenada, {len(pendentes)} pendentes, "
          f"{falhas} conferência(s) com falha.")
    print(f"Gerados: {GEOJSON.name}, {RELATORIO.name}")
    if falhas:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
