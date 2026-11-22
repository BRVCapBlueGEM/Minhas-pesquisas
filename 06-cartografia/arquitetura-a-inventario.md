> **Navegação:** [Índice principal](../README.md) · [Cartografia](README.md) · [Arquitetura A](arquitetura-a.md) · [Arquitetura B](arquitetura-b.md)

---

# Inventário — Arquitetura A (CartoCSS, Kosmtik e Mapnik)

**Revisão:** 22/11/2026  
**Autor:** BRV_Cap_Blue_GEM  

## Objetivo

Registrar os componentes necessários para o fluxo clássico de cartografia digital baseado em **OpenStreetMap Carto**, **CartoCSS**, **Kosmtik** e **Mapnik**, com ênfase no ambiente Windows.

## Sequência de funcionamento

OpenStreetMap / Geofabrik → osm2pgsql → PostgreSQL + PostGIS → OpenStreetMap Carto / CartoCSS → Kosmtik → Mapnik → PNG/JPEG (ou SVG/PDF com suporte adequado).

## Inventário de componentes

| # | Nome | Para que serve | Download / origem oficial | Situação |
|---|---|---|---|---|
| 1 | **PostgreSQL 18** | Armazena os dados do mapa em tabelas. | [Windows — PostgreSQL](https://www.postgresql.org/download/windows/) | Instalar primeiro |
| 2 | **PostGIS 3.7.0** | Acrescenta as funções geográficas ao PostgreSQL. | [PostGIS para Windows](https://postgis.net/windows_downloads/) | Compatível com PostgreSQL 18 |
| 3 | **pgAdmin 4** | Interface gráfica para executar SQL e consultar o banco. | Incluído no instalador do PostgreSQL / [pgAdmin](https://www.pgadmin.org/download/) | Já incluído no instalador principal |
| 4 | **osm2pgsql 2.3.1** | Importa os arquivos OSM para o banco. | [Releases oficiais (ZIP Windows)](https://github.com/osm2pgsql-dev/osm2pgsql/releases) | Download oficial disponível |
| 5 | **Node.js** | Executa o ambiente JavaScript do Kosmtik. | [Node.js para Windows](https://nodejs.org/) | Versão compatível pendente de validação com Kosmtik |
| 6 | **Carto / CartoCSS** | Compila as regras de estilo para o Mapnik. | [Repositório Carto](https://github.com/mapbox/carto) — instalação via npm | Instalação via npm; a validar |
| 7 | **Mapnik** | Desenha o mapa usando os dados e estilos. | [Repositório Mapnik](https://github.com/mapnik/mapnik) | Instalação Windows pendente de validação |
| 8 | **Kosmtik** | Estúdio visual para editar estilos e visualizar o mapa. | [Repositório oficial Kosmtik](https://github.com/kosmtik/kosmtik) | Compatibilidade Windows pendente |
| 9 | **OpenStreetMap Carto** | Fornece um conjunto de estilos cartográficos adaptáveis. | [Estilos oficiais no GitHub](https://github.com/gravitystorm/openstreetmap-carto) | Arquivos de estilo (não é aplicativo) |
| 10 | **OpenStreetMap** | Fornece os dados geográficos originais. | [openstreetmap.org](https://www.openstreetmap.org/) | Sem instalação |
| 11 | **Geofabrik** | Fornece extratos OSM compactados de regiões inteiras. | [download.geofabrik.de](https://download.geofabrik.de/) | Baixar dados quando necessário |
| 12 | **QGIS** | Permite examinar, analisar e corrigir dados geográficos visualmente. | [Download QGIS](https://qgis.org/download/) | Complementar |
| 13 | **Inkscape** | Permite editar o SVG e realizar o acabamento artístico. | [Download Inkscape](https://inkscape.org/release/) | Complementar |

## Ordem sugerida de preparação

1. Instalar **PostgreSQL 18** e **PostGIS 3.7.0**.
2. Obter **osm2pgsql 2.3.1**.
3. Instalar **Node.js** (versão a confirmar com Kosmtik).
4. Preparar **Carto** via npm e **Mapnik**.
5. Configurar **Kosmtik**.
6. Clonar/adaptar **openstreetmap-carto**.
7. Baixar extrato **Geofabrik** e importar com osm2pgsql.
8. Usar **QGIS** e **Inkscape** como apoio.

## Estado

Inventário documentado. Integração prática no Windows **pendente de teste**.
