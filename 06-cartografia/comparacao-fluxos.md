> **Navegação:** [Índice principal](../README.md) · [Cartografia](README.md) · [Arquitetura A](arquitetura-a.md) · [Inventário A](arquitetura-a-inventario.md) · [Arquitetura B](arquitetura-b.md) · [Edição vetorial](edicao-vetorial.md) · [Comparação](comparacao-fluxos.md)

---

# 10. Comparação dos fluxos cartográficos

| Característica | Fluxo A — Mapnik | Fluxo B — MapLibre |
|---|---|---|
| Dados iniciais | OpenStreetMap | OpenStreetMap |
| Processamento típico | osm2pgsql | tilemaker |
| Armazenamento | PostgreSQL/PostGIS | MBTiles/PMTiles ou serviço compatível |
| Estilos | CartoCSS / OSM Carto | JSON / Maputnik |
| Visualização auxiliar | Kosmtik | Maputnik |
| Renderização | Mapnik | MapLibre GL JS |
| Resultado habitual | Mapa renderizado | Mapa interativo |
| Saída raster | Sim | Possível por procedimentos adicionais |
| Saída SVG/PDF | Possível com suporte Cairo | Exige solução específica |
| Alteração dinâmica de estilos | Requer atualizar renderização | Estilo pode ser reaplicado aos tiles |
| Dependências | Banco espacial, Mapnik e ferramentas de estilo | Gerador, fontes de tiles e visualizador |
| Principal vantagem | Produção cartográfica estática controlada | Estilização e apresentação interativa |
| Validação prática | Pendente | Pendente |

## 10.1. Renderização raster

Uma imagem raster contém pixels.

Exemplos:

- PNG.
- JPEG.
- TIFF.

A qualidade final depende da resolução, das dimensões e das condições de exportação.

## 10.2. Renderização vetorial

Um documento vetorial pode conter linhas, curvas, textos e outros objetos gráficos.

Exemplos:

- SVG.
- PDF com conteúdo vetorial.

Entretanto, **ser vetorial não significa automaticamente preservar os objetos GIS originais como entidades geográficas independentes**.

## 10.3. Tiles vetoriais

Tiles vetoriais transportam geometrias e atributos para um renderizador compatível.

Esse formato permite que um aplicativo altere sua representação visual mediante regras de estilo.

A imagem apresentada na tela ainda é rasterizada pelo mecanismo gráfico do dispositivo.

**Portanto, “tiles vetoriais” e “arquivo SVG editável” não são expressões equivalentes.**

---
