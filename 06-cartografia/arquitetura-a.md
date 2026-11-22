> **Navegação:** [Índice principal](../README.md) · [Cartografia](README.md) · [Arquitetura A](arquitetura-a.md) · [Inventário A](arquitetura-a-inventario.md) · [Arquitetura B](arquitetura-b.md) · [Edição vetorial](edicao-vetorial.md) · [Comparação](comparacao-fluxos.md)

---

# 7. Arquitetura A — CartoCSS, Kosmtik e Mapnik

## 7.1. Sequência de funcionamento

**OpenStreetMap / Geofabrik**  
↓  
**osm2pgsql**  
↓  
**PostgreSQL + PostGIS**  
↓  
**OpenStreetMap Carto / CartoCSS**  
↓  
**Kosmtik — visualização e ajuste de estilos**  
↓  
**Mapnik — renderização cartográfica**  
↓  
**PNG, JPEG ou, com suporte adequado, SVG/PDF**

### O que acontece nesse processo?

Os dados geográficos são obtidos de fontes como OpenStreetMap.

O osm2pgsql importa as informações para PostgreSQL/PostGIS.

Os estilos definem cores, espessuras, padrões, símbolos e rótulos.

O Kosmtik permite visualizar e ajustar o resultado de determinados projetos CartoCSS.

O Mapnik executa a renderização cartográfica.

### Resultado artístico

É possível produzir mapas com aparência controlada, incluindo estradas, rios, vegetação, áreas urbanas, símbolos e textos.

A saída pode ser raster ou vetorial, dependendo do formato e da configuração de renderização.

**Importante:** um SVG/PDF gerado por um renderizador não necessariamente preserva a estrutura geográfica original como camadas GIS independentes.

---

## 7.2. OpenStreetMap

**Tipo:** projeto colaborativo de dados geográficos.

**Responsáveis:** comunidade OpenStreetMap, com apoio da OpenStreetMap Foundation.

**Site oficial:**  
https://www.openstreetmap.org/

**Dados oficiais:**  
https://planet.openstreetmap.org/

**Projetos no GitHub:**  
https://github.com/openstreetmap

**Documentação:**  
https://wiki.openstreetmap.org/

### Características

- **Dados:** nós, caminhos, relações e atributos.
- **Formato de distribuição importante:** OSM/PBF.
- **Licença dos dados:** ODbL.

### Finalidade

Fornecer dados geográficos para diferentes formas de análise, processamento e representação.

**Estado:** fonte identificada. A qualidade e a completude dos dados variam conforme a região.

---

## 7.3. Geofabrik

**Tipo:** fornecedora de extratos regionais de dados OSM.

**Responsável:** Geofabrik GmbH.

**Site oficial:**  
https://www.geofabrik.de/

**Download oficial dos dados:**  
https://download.geofabrik.de/

**Documentação sobre downloads:**  
https://www.geofabrik.de/en/data/download.html

### Finalidade

Disponibilizar recortes regionais do OpenStreetMap, frequentemente em formato `.osm.pbf`.

### Aplicação

Selecionar uma região e obter dados para processamento local.

**Estado:** serviço identificado.

---

## 7.4. PostgreSQL

**Tipo:** sistema gerenciador de banco de dados relacional.

**Responsável:** PostgreSQL Global Development Group.

**Linguagem principal:** C.

**Licença:** PostgreSQL License.

**Sistemas:** Windows, Linux e macOS.

**Site:**  
https://www.postgresql.org/

**Código-fonte oficial:**  
https://github.com/postgres/postgres

**Download oficial:**  
https://www.postgresql.org/download/

**Download Windows:**  
https://www.postgresql.org/download/windows/

**Documentação:**  
https://www.postgresql.org/docs/

### Finalidade

Armazenar e consultar grandes conjuntos de dados estruturados.

### Aplicação cartográfica

Trabalhar em conjunto com a extensão PostGIS.

**Estado:** projeto oficial identificado. Versão a selecionar conforme a compatibilidade exigida pelo PostGIS.

---

## 7.5. PostGIS

**Tipo:** extensão espacial do PostgreSQL.

**Responsáveis:** comunidade PostGIS e contribuidores.

**Linguagens:** C/C++ e SQL.

**Site:**  
https://postgis.net/

**Repositório:**  
https://github.com/postgis/postgis

**Instalação oficial:**  
https://postgis.net/documentation/getting_started/install_windows/

**Documentação:**  
https://postgis.net/documentation/

### Finalidade

Acrescentar recursos de geometria e análise espacial ao PostgreSQL.

**PostGIS não é um aplicativo gráfico independente.**

**Estado:** extensão identificada; combinações de versões devem ser verificadas antes da instalação.

---

## 7.6. osm2pgsql

**Tipo:** ferramenta de importação de dados OpenStreetMap.

**Responsáveis:** mantenedores e contribuidores do osm2pgsql.

**Linguagem principal:** C++.

**Site oficial:**  
https://osm2pgsql.org/

**Repositório:**  
https://github.com/osm2pgsql-dev/osm2pgsql

**Download e instalação:**  
https://osm2pgsql.org/doc/install.html

**Downloads Windows:**  
https://osm2pgsql.org/download/windows/

**Releases:**  
https://github.com/osm2pgsql-dev/osm2pgsql/releases

**Documentação:**  
https://osm2pgsql.org/doc/manual.html

### Finalidade

Importar dados OSM para tabelas PostgreSQL/PostGIS.

**Estado:** documentação e downloads oficiais identificados. Compatibilidade prática não testada.

---

## 7.7. SQL

**Tipo:** linguagem de consulta e manipulação de dados.

**Finalidade:** consultar, organizar e transformar informações armazenadas em bancos relacionais.

**Documentação de referência PostgreSQL:**  
https://www.postgresql.org/docs/current/sql.html

### Aplicação cartográfica

Selecionar feições, relacionar tabelas, consultar atributos e executar funções espaciais disponibilizadas pelo PostGIS.

---

## 7.8. OpenStreetMap Carto

**Tipo:** projeto de estilo cartográfico.

**Criador inicial:** Andy Allan.

**Responsáveis:** contribuidores do OpenStreetMap Carto.

**Repositório oficial:**  
https://github.com/openstreetmap-carto/openstreetmap-carto

**Releases e arquivos oficiais:**  
https://github.com/openstreetmap-carto/openstreetmap-carto/releases

**Instruções:**  
https://github.com/openstreetmap-carto/openstreetmap-carto/blob/master/INSTALL.md

**Documentação:**  
https://github.com/openstreetmap-carto/openstreetmap-carto#readme

### Características

- **Tecnologia principal:** CartoCSS.
- **Arquivos:** MSS, MML/YAML e outros recursos de configuração.
- **Licença principal do estilo:** CC0; verificar licenças de recursos adicionais.

### Finalidade

Definir a aparência visual dos mapas (cores, hidrografia, vegetação, símbolos, rótulos, hierarquia visual).

### Observação

É um conjunto de estilos e recursos, não um programa instalável independente.

---

## 7.9. CartoCSS / Carto

**Tipo:** linguagem e ferramenta de estilização cartográfica.

**Projeto de referência:** Mapbox Carto.

**Repositório:**  
https://github.com/mapbox/carto

**Pacote técnico:**  
https://www.npmjs.com/package/carto

**Documentação:**  
https://cartocss.readthedocs.io/

### Características

- **Linguagem do compilador:** JavaScript.
- **Ambiente:** Node.js.
- **Licença do compilador:** Apache-2.0.

### Finalidade

Descrever estilos cartográficos por regras semelhantes às utilizadas em CSS.

### Limitação

O repositório de referência foi arquivado. Sua utilização deve considerar dependências antigas e eventuais limitações de manutenção.

**Estado:** tecnologia preservada como parte do fluxo clássico. Instalação atual não validada.

---

## 7.10. Mapnik

**Tipo:** biblioteca e motor de renderização cartográfica.

**Criador:** Artem Pavlenko.

**Responsáveis atuais:** projeto Mapnik e contribuidores.

**Linguagem principal:** C++.

**Licença:** LGPL-2.1.

**Site oficial:**  
https://mapnik.org/

**Repositório:**  
https://github.com/mapnik/mapnik

**Download oficial:**  
https://mapnik.org/pages/downloads.html

**Releases:**  
https://github.com/mapnik/mapnik/releases

**Instruções de compilação:**  
https://github.com/mapnik/mapnik/blob/master/INSTALL.md

**Informações sobre renderizadores:**  
https://github.com/mapnik/mapnik/wiki/MapnikRenderers

**Versão estável identificada:** 4.3.2.

### Finalidade

Renderizar mapas utilizando fontes de dados e regras de estilo.

### Formatos de saída

O Mapnik pode produzir formatos raster, como PNG, e também trabalhar com saídas vetoriais mediante suporte apropriado.

**SVG e PDF dependem da disponibilidade do renderizador Cairo na compilação utilizada.**

### Limitações

- Exige configuração técnica.
- As dependências variam conforme a plataforma.
- Não presumir instalador Windows moderno pronto em todas as releases.
- Exportação SVG/PDF não garante editabilidade perfeita de todas as entidades.

**Estado:** versão e repositório oficial identificados. Renderização e compatibilidade prática pendentes.

---

## 7.11. Kosmtik

**Tipo:** ambiente de desenvolvimento e visualização de estilos cartográficos.

**Responsáveis:** comunidade e contribuidores do projeto Kosmtik.

**Linguagem:** JavaScript.

**Ambiente:** Node.js e dependências relacionadas ao Mapnik/Carto.

**Repositório oficial:**  
https://github.com/kosmtik/kosmtik

**Código-fonte e instruções oficiais:**  
https://github.com/kosmtik/kosmtik#install-or-update

**Página de releases:**  
https://github.com/kosmtik/kosmtik/releases

**Documentação:**  
https://github.com/kosmtik/kosmtik#readme

### Finalidade

Facilitar a visualização e o desenvolvimento de mapas baseados em projetos Carto/Mapnik.

### Recursos

- Carregamento de projetos MML/YAML.
- Configuração local.
- Pré-visualização de mapas.
- Servidor local para feedback visual.
- Exportações e extensões.

### Dependências

O Kosmtik utiliza Node.js.

O mantenedor informa que algumas versões recentes do Node.js podem não ser compatíveis com dependências do projeto.

### Download e instalação

O repositório recomenda instalação a partir do código-fonte.

**Não confundir a obtenção do código-fonte com um instalador Windows pronto.**

### Situação

O Kosmtik permanece nesta pesquisa como ferramenta do fluxo clássico.

**Estado:** fonte e requisitos documentados; funcionamento no ambiente de destino não testado.

---
