# Minhas pesquisas

Links de pesquisas e referências.

## Leitores de livros digitais

- [Pesquisar leitores de ebooks para Windows](https://github.com/search?q=ebook+reader+windows&type=repositories)
- [Projetos de leitores digitais — eReader](https://github.com/topics/ereader)
- [Projetos de leitores EPUB](https://github.com/topics/epub-reader)
- [Projetos de leitores de ebooks](https://github.com/topics/ebook-reader)

## ACSM — ferramentas e projetos

- [Projetos relacionados a ACSM](https://github.com/search?q=acsm&type=repositories)
- [Projetos com o tópico ACSM](https://github.com/topics/acsm)
- [Projetos relacionados a Adobe Digital Editions](https://github.com/search?q=adobe+digital+editions&type=repositories)

## Processamento e restauração de imagens

- [OpenCV — Processamento de imagens, detecção de linhas e restauração (Inpainting)](https://github.com/opencv/opencv)

## Mesas digitalizadoras XP-Pen — ferramentas independentes

Pesquisa de programas, drivers alternativos e scripts de código aberto para configurar mesas digitalizadoras XP-Pen sem depender do aplicativo proprietário do fabricante.

### Projetos e pesquisas no GitHub

- [OpenTabletDriver — Projeto de driver alternativo](https://github.com/OpenTabletDriver/OpenTabletDriver)
- [Pesquisar projetos XP-Pen](https://github.com/search?q=xp-pen&type=repositories)
- [Pesquisar drivers alternativos para mesas digitalizadoras](https://github.com/search?q=tablet+driver&type=repositories)
- [Pesquisar ferramentas de rotação e remapeamento](https://github.com/search?q=tablet+rotation&type=repositories)
- [Pesquisar AetherGUI](https://github.com/search?q=AetherGUI&type=repositories)

### Objetivos da pesquisa

- Rotação de 180° para utilização por canhotos.
- Remapeamento dos movimentos X e Y da caneta.
- Configuração dos botões físicos.
- Identificação e gerenciamento da conexão USB.
- Funcionamento no Windows sem o aplicativo proprietário XP-Pen.

**Hardware de referência:** `VID_28BD&PID_0918`.

**Estado:** projetos e pesquisas para avaliação. A compatibilidade específica, as dependências e o funcionamento ainda precisam ser verificados.

### Repositórios identificados — levantamento técnico

#### 1. OpenTabletDriver
- **GitHub:** https://github.com/OpenTabletDriver/OpenTabletDriver
- **Licença:** LGPL-3.0
- **Linguagem:** C# / .NET
- **Sistema operacional:** Windows, Linux e macOS.
- **Finalidade:** Driver alternativo de código aberto para mesas digitalizadoras.
- **Compatibilidade:** Família XP-Pen G960S/G960S Plus mencionada no levantamento.
- **Estado:** Ativo, conforme pesquisa.
- **Pendência:** Confirmar suporte ao identificador exato `VID_28BD&PID_0918`.

#### 2. AetherGUI
- **GitHub:** https://github.com/silentlag/AetherGUI
- **Licença:** Arquivo LICENSE.md identificado; modalidade ainda não confirmada.
- **Linguagem:** C++17
- **Sistema operacional:** Windows 10/11.
- **Finalidade:** Alternativa para gerenciamento de mesas digitalizadoras.
- **Compatibilidade:** G960/G960S/G960S Plus mencionadas no levantamento.
- **Estado:** Ativo, conforme pesquisa.
- **Pendência:** Confirmar suporte ao identificador `28BD:0918` e requisitos de funcionamento.

#### 3. Hawku TabletDriver
- **GitHub:** https://github.com/hawku/TabletDriver
- **Licença:** GPL-3.0
- **Linguagem:** C++
- **Sistema operacional:** Windows.
- **Finalidade:** Driver alternativo para mesas digitalizadoras.
- **Estado:** Descontinuado para versões modernas do Windows.
- **Observação:** O próprio projeto recomenda OpenTabletDriver como sucessor.
- **Pendência:** Compatibilidade específica com `28BD:0918` não confirmada.

#### 4. DIGImend Kernel Drivers
- **GitHub:** https://github.com/DIGImend/digimend-kernel-drivers
- **Licença:** GPL-2.0
- **Linguagem:** C
- **Sistema operacional:** Linux.
- **Finalidade:** Drivers de kernel para mesas digitalizadoras.
- **Referência:** O levantamento identificou uma issue relacionada ao dispositivo `28BD:0918`.
- **Aplicação:** Referência técnica para pesquisa do hardware; não é uma solução direta para Windows.

#### 5. Kuri Userspace Tablet Driver Daemon
- **GitHub:** https://github.com/kurikaesu/userspace-tablet-driver-daemon
- **Linguagem:** C++
- **Sistema operacional:** Linux.
- **Finalidade:** Driver de mesas digitalizadoras executado no espaço do usuário.
- **Compatibilidade:** Possui implementação genérica para XP-Pen.
- **Pendência:** G960S não aparece na lista oficial fornecida pelo levantamento. Compatibilidade não testada.

### Situação da pesquisa

Os cinco repositórios foram identificados como possíveis fontes de software ou conhecimento técnico.

**Prioridade de análise para Windows:**
1. OpenTabletDriver.
2. AetherGUI.

**Referências secundárias:**
- Hawku TabletDriver.
- DIGImend.
- Kuri Userspace Tablet Driver Daemon.

**Estado de validação:** levantamento documental. Os programas ainda não foram examinados integralmente, compilados ou testados com o hardware `VID_28BD&PID_0918`.


## 🗺️ Cartografia Digital — OpenStreetMap, PostGIS, Mapnik e Kosmtik

**Finalidade:** pesquisa de ferramentas, linguagens e tecnologias para criação, processamento, estilização e representação de mapas geográficos e vetoriais.

### Dados geográficos

**OpenStreetMap (OSM)** — base colaborativa de dados geográficos.  
https://www.openstreetmap.org/

**Geofabrik** — download de dados OSM por regiões.  
https://download.geofabrik.de/

### Bancos de dados e processamento

**PostgreSQL** — sistema de gerenciamento de bancos de dados.  
https://github.com/postgres/postgres

**PostGIS** — extensão espacial do PostgreSQL.  
https://github.com/postgis/postgis

**osm2pgsql** — importação de arquivos OSM para PostgreSQL/PostGIS.  
https://github.com/osm2pgsql-dev/osm2pgsql

**SQL** — linguagem de consultas e manipulação de bancos de dados.

### Estilos cartográficos e renderização

**OpenStreetMap Carto** — estilos, cores, padrões e símbolos utilizados na representação cartográfica.  
https://github.com/openstreetmap-carto/openstreetmap-carto

**CartoCSS** — linguagem para definir estilos cartográficos.  
https://github.com/mapbox/carto

**Mapnik** — motor de renderização de mapas.  
https://github.com/mapnik/mapnik

**Kosmtik** — ambiente de desenvolvimento e visualização de estilos cartográficos.  
https://github.com/kosmtik/kosmtik

### Edição cartográfica e vetorial

**QGIS** — processamento, análise e representação de dados geográficos.  
https://github.com/qgis/QGIS

**Inkscape** — edição vetorial e acabamento artístico de mapas SVG.  
https://inkscape.org/

**Autor:** BRV_Cap_Blue_GEM
