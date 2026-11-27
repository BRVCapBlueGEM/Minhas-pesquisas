"""Malha hexagonal do Steel Jacket (módulo comum).

Hexágonos pointy-top (vértice para cima), 1000 m entre centros vizinhos,
em EPSG:23036 (ED50 / UTM 36N), com a mesma origem e espaçamento do
HEX_MAGRO (AUD_CARTOGRAFIA_2026-11-19_A: origem 399000 / 3232006,8066666666).

Coordenadas axiais globais (q, r): o mesmo hexágono tem o mesmo ID em
todos os mapas e setores.
    x = X0 + PASSO * (q + r / 2)
    y = Y0 + PASSO * sqrt(3) / 2 * r      (r cresce para o norte)
"""
import math

EPSG = 23036
X0, Y0 = 399000.0, 3232006.8066666666
PASSO = 1000.0                       # distância entre centros vizinhos (m)
LINHA = PASSO * math.sqrt(3) / 2     # distância entre linhas (866,03 m)
RAIO = PASSO / math.sqrt(3)          # centro ao vértice (577,35 m)


def centro(q, r):
    return X0 + PASSO * (q + r / 2.0), Y0 + LINHA * r


def vertices(q, r):
    cx, cy = centro(q, r)
    return [(cx + RAIO * math.cos(math.radians(90 + 60 * i)),
             cy + RAIO * math.sin(math.radians(90 + 60 * i))) for i in range(6)]


def hex_de(x, y):
    """Hexágono (q, r) que contém o ponto (x, y)."""
    rf = (y - Y0) / LINHA
    qf = (x - X0) / PASSO - rf / 2.0
    sf = -qf - rf
    q, r, s = round(qf), round(rf), round(sf)
    dq, dr, ds = abs(q - qf), abs(r - rf), abs(s - sf)
    if dq > dr and dq > ds:
        q = -r - s
    elif dr > ds:
        r = -q - s
    return int(q), int(r)


def hexes_no_retangulo(xmin, ymin, xmax, ymax):
    """Hexágonos cujo centro cai dentro do retângulo."""
    r0 = math.floor((ymin - Y0) / LINHA) - 1
    r1 = math.ceil((ymax - Y0) / LINHA) + 1
    out = []
    for r in range(r0, r1 + 1):
        q0 = math.floor((xmin - X0) / PASSO - r / 2.0) - 1
        q1 = math.ceil((xmax - X0) / PASSO - r / 2.0) + 1
        for q in range(q0, q1 + 1):
            cx, cy = centro(q, r)
            if xmin <= cx <= xmax and ymin <= cy <= ymax:
                out.append((q, r))
    return out


def distancia_hex(a, b):
    dq, dr = a[0] - b[0], a[1] - b[1]
    return int((abs(dq) + abs(dr) + abs(dq + dr)) / 2)
