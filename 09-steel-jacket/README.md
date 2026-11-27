> **Navegação:** [Índice principal](../README.md) · [Cartografia digital](../06-cartografia/README.md)

---
# ⚔️ 9. Steel Jacket — cartografia da Missão Sharon (Yom Kippur 1973)

**Autor:** BRV_Cap_Blue_GEM
**Início:** 26/11/2026
**Estado:** lista de pontos iniciada; setores, malha e mapas ainda não gerados.

## 9.1. Objetivo

Produzir os mapas do cenário **Missão Sharon / Deversoir** do Steel Jacket. Em vez de um mapa contínuo, são vários mapas por setor, que seguem a cronologia das 17 cenas do roteiro (Even & Maoz, *At the Decisive Point in the Sinai*).

## 9.2. Fluxo de produção (Arquitetura C, sem QGIS e sem Inkscape)

1. **Lista de pontos** (`pontos/pontos.csv`): cada local citado nas cenas, com coordenada, fonte e grau de certeza. **← etapa atual**
2. **Setores**: a área de cada mapa é calculada no PostGIS a partir dos pontos das suas cenas, mais uma margem. Os setores não são desenhados à mão.
3. **Base física**: OSM/Geofabrik → osm2pgsql → PostGIS, sem o que for posterior a 1973.
4. **Camada de 1973**: estradas militares, fortes e pontos da Sirius, guardados como GeoJSON.
5. **Malha**: hexágonos de 1 km gerados no PostGIS (EPSG:23036), com a mesma origem do HEX_MAGRO; identificador global igual em todos os mapas.
6. **Atributos por hexágono**: terreno calculado por SQL, mais um CSV de ajustes de jogabilidade.
7. **Saída**: SVG pelo VersaTiles.

## 9.3. Fontes e papel de cada uma

| Fonte | Papel |
|---|---|
| Even & Maoz | Cenas, horários, distâncias e nomes de código |
| Carta Sirius (Israel, 1973) | Estradas militares, fortes e nomes de código de 1973 |
| AMS P502 NH 36-6 (Ismailia, 1:250.000, anos 1950–60) | Terreno estável; não mostra nada construído por Israel entre 1967 e 1973 |
| OSM / Geofabrik | Apenas o esqueleto geométrico; o que for posterior a 1973 é retirado |
| Wikipedia e outras fontes públicas | Coordenadas publicadas e posições relativas, sempre com o grau indicado |

## 9.4. Lista de pontos

- `pontos/pontos.csv`: **o único arquivo editado à mão.**
- `pontos/pontos.geojson` e `pontos/verificacao.md` são gerados pelo script:

```
cd 09-steel-jacket
python scripts\gerar_pontos.py
```

O script confere o CSV (colunas e IDs repetidos), rejeita coordenadas fora da região, gera o GeoJSON e verifica distâncias entre pontos conhecidos. Se alguma conferência falhar, ele termina com erro.

### Graus de certeza

| Grau | Significado |
|---|---|
| **A** | Fonte primária ou coordenada levantada para o próprio local |
| **B** | Coordenada publicada de um local que existia em 1973 e não mudou de lugar |
| **C** | Coordenada aproximada, arredondada ou herdada de registro do projeto que ainda não foi conferido |
| **PENDENTE** | Sem coordenada; a coluna `restricao` registra o que se sabe da posição |

### Tolerância

A malha usa 1 km entre centros. Um erro de até ~300 m não muda o hexágono na maioria dos casos. Os pontos de grau C (±500 m a ±1 km) podem cair no hexágono vizinho e precisam ser conferidos antes de definir objetivos e entradas.

## 9.5. Sirius → coordenadas

A pasta `sirius/` converte pixels da Sirius em latitude e longitude usando o quadriculado geográfico impresso na carta (ver [sirius/README.md](sirius/README.md)). Matzmed, Lakekan e a Fazenda Chinesa já foram convertidos por esse caminho.

```
python scripts\sirius_converter.py
python scripts\gerar_pontos.py
```

## 9.6. Próximos passos

1. Folha superior da Sirius: obter um terceiro cruzamento do quadriculado, ao norte de 30°35′, para converter Missouri e Tassa.
2. Marcar na Sirius os marcos da Akavish (42, 53, 55), o km 95,5, Hurva e Kishuf.
3. Calcular os setores a partir dos pontos.
