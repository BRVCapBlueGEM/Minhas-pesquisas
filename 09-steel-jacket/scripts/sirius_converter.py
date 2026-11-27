"""Converte pixels da Sirius em latitude/longitude pelo quadriculado impresso.

Uso (CMD, na pasta 09-steel-jacket):
    python scripts\\sirius_converter.py

Entradas (pasta sirius/):
    gcp_sirius.csv        cruzamentos do quadriculado geográfico (pixel -> lon/lat)
    pontos_sirius_px.csv  pontos marcados na Sirius (pixel)
Saída:
    sirius/pontos_sirius_convertidos.csv

Os pixels são do recorte SIRIUS_recorte_X1500-4500_Y6500-9500_q96.jpg
(2576 x 2576 px), que é a região X 1500-4500, Y 6500-9500 da
SIRIUS_COMPLETA_COMMONS.jpg (6784 x 15819 px) reduzida para 2576 px.

A Sirius é um mosaico de folhas. Cada folha tem a sua transformação;
nunca se usa ponto de controle de uma folha para converter outra.
"""
import csv
import math
from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent / "sirius"
ORIGEM_X, ORIGEM_Y = 1500.0, 6500.0      # canto do recorte na Sirius completa
ESCALA = 3000.0 / 2576.0                  # px da Sirius completa por px do recorte
M_LAT = 110574.0                          # metros por grau de latitude (~30°N)


def m_lon(lat):
    return 111320.0 * math.cos(math.radians(lat))


def resolver(m, v):
    """Resolve sistema linear pequeno (eliminação de Gauss)."""
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
    atl = [0.0] * 3
    atb = [0.0] * 3
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
        gcps.setdefault(g["folha"], []).append(
            {"id": g["id"], "x": float(g["recorte_x"]), "y": float(g["recorte_y"]),
             "lon": float(g["lon"]), "lat": float(g["lat"])})

    transf = {}
    for folha, lista in gcps.items():
        if len(lista) < 3:
            print(f"Folha {folha}: {len(lista)} ponto(s) de controle; precisa de 3 ou mais. "
                  "Pontos desta folha não serão convertidos.")
            continue
        t = ajustar_afim(lista)
        transf[folha] = t
        folga = len(lista) - 3
        print(f"Folha {folha}: {len(lista)} pontos de controle (redundância: {folga})")
        for g in lista:
            lon, lat = aplicar(t, g["x"], g["y"])
            erro = math.hypot((lon - g["lon"]) * m_lon(lat), (lat - g["lat"]) * M_LAT)
            print(f"  {g['id']}: resíduo {erro:.1f} m")

    saida = []
    for p in ler("pontos_sirius_px.csv"):
        x, y = float(p["recorte_x"]), float(p["recorte_y"])
        sx, sy = ORIGEM_X + x * ESCALA, ORIGEM_Y + y * ESCALA
        if p["folha"] not in transf:
            print(f"{p['id']}: folha {p['folha']} sem transformação; não convertido")
            continue
        lon, lat = aplicar(transf[p["folha"]], x, y)
        saida.append({"id": p["id"], "folha": p["folha"],
                      "sirius_x": f"{sx:.0f}", "sirius_y": f"{sy:.0f}",
                      "lat": f"{lat:.5f}", "lon": f"{lon:.5f}",
                      "descricao": p["descricao"]})
        print(f"{p['id']}: Sirius ({sx:.0f}, {sy:.0f}) -> {lat:.5f}, {lon:.5f}")

    with (PASTA / "pontos_sirius_convertidos.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "folha", "sirius_x", "sirius_y",
                                          "lat", "lon", "descricao"])
        w.writeheader()
        w.writerows(saida)


if __name__ == "__main__":
    main()
