"""Renderiza um setor: Sirius reprojetada para EPSG:23036 + malha hexagonal + pontos.

Uso (CMD, na pasta 09-steel-jacket):
    python scripts\\renderizar_setor.py B "X:\\caminho\\dos\\blocos" [metros_por_pixel]

Requer: pip install pyproj pillow numpy

Os blocos são os recortes sem redução da SIRIUS_COMPLETA_COMMONS.jpg com nome
SIRIUS_Xnnnnn_Ynnnnn.png (ex.: SIRIUS_X02000_Y06000.png), 2000 px ou menos.

Saídas (pasta setores/):
    mapa_<S>.png  mapa do setor (norte para cima, EPSG:23036)
    mapa_<S>.pgw  arquivo de georreferência (world file) do PNG
    mapa_<S>.prj  projeção (EPSG:23036)

O fundo é a Sirius convertida folha por folha (sirius/gcp_sirius.csv). Este mapa
é material de conferência e protótipo; a base vetorial final é outra etapa.
"""
import csv
import math
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from pyproj import CRS, Transformer

sys.path.insert(0, str(Path(__file__).resolve().parent))
import malha  # noqa: E402
import sirius_converter as sc  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
Image.MAX_IMAGE_PIXELS = None


def carregar_blocos(pasta):
    blocos = []
    for f in Path(pasta).glob("SIRIUS_X*_Y*.png"):
        m = re.match(r"SIRIUS_X(\d+)_Y(\d+)\.png$", f.name)
        if m:
            blocos.append((int(m.group(1)), int(m.group(2)), f))
    if not blocos:
        raise SystemExit(f"Nenhum bloco SIRIUS_Xnnnnn_Ynnnnn.png em {pasta}")
    return blocos


def transformacoes_inversas():
    """Para cada folha: (lon, lat) -> pixel da Sirius, por mínimos quadrados."""
    gcps = {}
    with (BASE / "sirius" / "gcp_sirius.csv").open(encoding="utf-8", newline="") as f:
        for g in csv.DictReader(f):
            gcps.setdefault(g["folha"], []).append(g)
    inv = {}
    for folha, lista in gcps.items():
        if len(lista) < 3:
            continue
        a = np.array([[float(g["lon"]), float(g["lat"]), 1.0] for g in lista])
        px = np.array([float(g["sirius_x"]) for g in lista])
        py = np.array([float(g["sirius_y"]) for g in lista])
        inv[folha] = (np.linalg.lstsq(a, px, rcond=None)[0], np.linalg.lstsq(a, py, rcond=None)[0])
    return inv


def fonte(tam):
    for nome in ("DejaVuSans.ttf", "arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(nome, tam)
        except OSError:
            pass
    return ImageFont.load_default()


def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    setor, pasta = sys.argv[1], sys.argv[2]
    res = float(sys.argv[3]) if len(sys.argv) > 3 else 5.0

    contorno = None
    import json
    for f in json.loads((BASE / "setores" / "setores.geojson").read_text(encoding="utf-8"))["features"]:
        if f["properties"]["setor"] == setor:
            contorno = f["properties"]
    if contorno is None:
        raise SystemExit(f"Setor {setor} não está em setores/setores.geojson; rode gerar_setores.py")
    xmin, ymin, xmax, ymax = contorno["xmin"], contorno["ymin"], contorno["xmax"], contorno["ymax"]
    largura, altura = int(math.ceil((xmax - xmin) / res)), int(math.ceil((ymax - ymin) / res))
    print(f"Setor {setor}: {largura} x {altura} px a {res} m/px")

    # coordenadas de cada pixel de saída -> lon/lat -> pixel da Sirius
    para_geo = Transformer.from_crs(malha.EPSG, 4326, always_xy=True)
    cols = xmin + (np.arange(largura) + 0.5) * res
    lins = ymax - (np.arange(altura) + 0.5) * res
    E, N = np.meshgrid(cols, lins)
    lon, lat = para_geo.transform(E, N)
    inv = transformacoes_inversas()
    sx = np.full(E.shape, np.nan); sy = np.full(E.shape, np.nan)
    for folha, (cx, cy) in inv.items():
        px = cx[0] * lon + cx[1] * lat + cx[2]
        py = cy[0] * lon + cy[1] * lat + cy[2]
        dentro = np.isnan(sx)
        fx = np.where(px < sc.EMENDA_X, "E", "D")
        fy = np.where(py < sc.EMENDA_Y, "1", "2")
        ok = dentro & (np.char.add(fx, fy) == folha) & (py >= sc.LIMITE_Y[0]) & (py <= sc.LIMITE_Y[1])
        sx[ok] = px[ok]; sy[ok] = py[ok]
    # junto às emendas um pixel pode não cair em nenhuma folha (as folhas não coincidem);
    # usa a folha cuja previsão fica mais perto dos próprios limites
    falta = np.isnan(sx)
    if falta.any():
        melhor = np.full(E.shape, np.inf)
        limites = {"E1": (0, sc.EMENDA_X, sc.LIMITE_Y[0], sc.EMENDA_Y), "E2": (0, sc.EMENDA_X, sc.EMENDA_Y, sc.LIMITE_Y[1]),
                   "D1": (sc.EMENDA_X, 1e9, sc.LIMITE_Y[0], sc.EMENDA_Y), "D2": (sc.EMENDA_X, 1e9, sc.EMENDA_Y, sc.LIMITE_Y[1])}
        for folha, (cx, cy) in inv.items():
            px = cx[0] * lon + cx[1] * lat + cx[2]
            py = cy[0] * lon + cy[1] * lat + cy[2]
            x0, x1, y0, y1 = limites[folha]
            fora = np.maximum.reduce([x0 - px, px - x1, y0 - py, py - y1, np.zeros_like(px)])
            usar = falta & (fora < melhor) & (fora < 60)
            sx[usar] = px[usar]; sy[usar] = py[usar]; melhor[usar] = fora[usar]

    saida = np.full((altura, largura, 3), 235, np.uint8)
    for bx, by, arq in carregar_blocos(pasta):
        im = np.asarray(Image.open(arq).convert("RGB"))
        h, w = im.shape[:2]
        m = (~np.isnan(sx)) & (sx >= bx) & (sx < bx + w) & (sy >= by) & (sy < by + h)
        saida[m] = im[(sy[m] - by).astype(int), (sx[m] - bx).astype(int)]
    falta = np.isnan(sx).mean()
    if falta > 0:
        print(f"Aviso: {falta:.1%} do setor sem folha convertida")

    img = Image.fromarray(saida)
    clara = Image.new("RGB", img.size, (255, 255, 255))
    img = Image.blend(img, clara, 0.25)          # clareia a Sirius para a malha aparecer
    d = ImageDraw.Draw(img)
    f_id, f_pt = fonte(max(10, int(110 / res))), fonte(max(16, int(150 / res)))
    para_px = lambda x, y: ((x - xmin) / res, (ymax - y) / res)

    for q, r in malha.hexes_no_retangulo(xmin, ymin, xmax, ymax):
        vs = [para_px(*v) for v in malha.vertices(q, r)]
        d.line(vs + [vs[0]], fill=(40, 40, 40), width=2)
        cx, cy = para_px(*malha.centro(q, r))
        d.text((cx, cy + malha.RAIO / res * 0.55), f"{q},{r}", fill=(30, 30, 30), font=f_id, anchor="mm")

    para_utm = Transformer.from_crs(4326, malha.EPSG, always_xy=True)
    with (BASE / "pontos" / "pontos.csv").open(encoding="utf-8", newline="") as f:
        for p in csv.DictReader(f):
            if not p["lat"]:
                continue
            x, y = para_utm.transform(float(p["lon"]), float(p["lat"]))
            if not (xmin <= x <= xmax and ymin <= y <= ymax):
                continue
            px, py = para_px(x, y)
            cor = {"A": (0, 110, 0), "B": (0, 70, 200), "C": (220, 120, 0)}.get(p["grau"], (200, 0, 0))
            rr = max(8, int(60 / res))
            d.ellipse((px - rr, py - rr, px + rr, py + rr), outline=cor, width=4)
            d.text((px + rr + 4, py), p["id"], fill=cor, font=f_pt, anchor="lm",
                   stroke_width=3, stroke_fill=(255, 255, 255))

    d.text((20, 20), f"STEEL JACKET — Setor {setor}: {contorno['nome']}   |   hexágono 1 km   |   "
                     f"EPSG:{malha.EPSG}   |   fundo: Sirius 1973", fill=(0, 0, 0), font=f_pt,
           stroke_width=3, stroke_fill=(255, 255, 255))

    destino = BASE / "setores" / f"mapa_{setor}.png"
    img.save(destino, optimize=True)
    destino.with_suffix(".pgw").write_text(
        f"{res}\n0\n0\n{-res}\n{xmin + res / 2}\n{ymax - res / 2}\n", encoding="utf-8")
    destino.with_suffix(".prj").write_text(CRS.from_epsg(malha.EPSG).to_wkt("WKT1_ESRI"), encoding="utf-8")
    print(f"Gerado: {destino}")


if __name__ == "__main__":
    main()
