# Setores e malha — primeiro serviço completo

Gerado a partir de `pontos/pontos.csv` e `setores/setores.csv`:

```
python scripts\gerar_setores.py
python scripts\renderizar_setor.py B "X:\caminho\dos\blocos"
python scripts\renderizar_setor.py A "X:\caminho\dos\blocos"
python scripts\renderizar_setor.py C "X:\caminho\dos\blocos"
```

(`pip install pyproj pillow numpy`; os blocos são os `SIRIUS_Xnnnnn_Ynnnnn.png`.)

## Malha

- Hexágonos pointy-top, 1000 m entre centros vizinhos, EPSG:23036 (ED50 / UTM 36N).
- Mesma origem do HEX_MAGRO (399000 / 3232006,8067): o hexágono 0,0 é centrado nela.
- ID axial global `q,r`: o mesmo hexágono tem o mesmo ID em todos os setores. Uma peça que sai do setor A num hexágono entra no B pelo mesmo ID.
- Conferido: os 6 vizinhos de cada hexágono ficam a 1000,000 m do centro; o vértice superior está no topo.

## Setores

| Setor | Cenas | Tamanho | Hexágonos |
|---|---|---|---|
| B — Central (travessia) | 1, 2, 6, 7, 9–13, 15, 16 | 18,0 × 18,5 km | 378 |
| A — Aproximação | 3, 4, 5, 8 | 15,8 × 9,7 km | 170 |
| C — Sul (25ª Brigada) | 14 | 19,8 × 11,1 km | 260 |

O contorno de cada setor é o retângulo que contém os pontos das suas cenas, mais uma margem (`setores.csv`). Pundak 76, Mavdil 76 e Refidim ficam fora do mapa A e entram por hexágonos de borda (`entradas.csv`).

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `setores.geojson` | Contorno dos setores (WGS84) |
| `hexagonos.geojson` / `hexagonos.csv` | Hexágonos de cada setor, com centro em EPSG:23036, pontos e cenas |
| `entradas.csv` | Pontos fora do mapa e o hexágono de entrada |
| `resumo.md` | Hexágono de cada ponto e pontos que caem no mesmo hexágono |
| `mapa_A/B/C.png` + `.pgw` + `.prj` | Mapas de conferência: Sirius reprojetada + malha + pontos (5 m/px, georreferenciados) |

Os mapas são material de conferência e protótipo. A base vetorial final (Arquitetura C) é a etapa seguinte.
