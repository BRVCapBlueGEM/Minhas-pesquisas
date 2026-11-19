
# 🔬 Minhas pesquisas

**Catálogo de pesquisas técnicas, ferramentas, tecnologias e projetos de desenvolvimento.**

**Autor:** BRV_Cap_Blue_GEM  
**Versão documental:** 2.0  
**Revisão:** 19/11/2026  
**Finalidade:** documentação técnica, consulta e localização de fontes e distribuições oficiais.

---

## 📖 Apresentação

Este repositório reúne pesquisas sobre programas, bibliotecas, linguagens, serviços, equipamentos e tecnologias.

Seu objetivo é permitir que cada ferramenta seja compreendida e localizada sem a necessidade de repetir toda a pesquisa original.

Cada ficha técnica procura responder:

1. O que é?
2. Quem desenvolveu?
3. Para que serve?
4. Como funciona?
5. Qual linguagem utiliza?
6. Qual é sua licença?
7. Em quais sistemas funciona?
8. Quais dependências exige?
9. Onde está o projeto original?
10. Onde obter a versão oficial?
11. Quais limitações e pendências foram identificadas?

### Critérios de documentação

- Priorizar fontes mantidas pelos desenvolvedores.
- Priorizar versões estáveis.
- Evitar versões beta, alpha, RC e nightly como recomendações principais.
- Diferenciar instaladores, código-fonte, bibliotecas, dados e serviços.
- Preservar links de pesquisa úteis.
- Registrar informações não confirmadas como pendentes.
- Não apresentar compatibilidade documental como teste prático.
- Preferir ferramentas independentes e de código aberto quando adequadas, sem ocultar dependências de plataformas proprietárias.
- Não pressupor que um projeto publicado no GitHub seja automaticamente seguro ou tenha instalador disponível.

**Importante:** os endereços de download apresentados são canais de distribuição, páginas oficiais de versões ou instruções do mantenedor. A disponibilidade de instaladores para cada sistema deve ser conferida antes da utilização.

---

# 📚 1. Leitores de livros digitais

## 1.1. Objetivo da pesquisa

Identificar programas para leitura de livros eletrônicos, documentos e publicações digitais, especialmente no Windows.

Formatos de interesse:

- EPUB.
- PDF.
- MOBI.
- FB2.
- CBZ e CBR.
- DjVu.
- Outros formatos documentados pelos respectivos projetos.

É necessário distinguir um **leitor de livros** de um **gerenciador de bibliotecas**.

O leitor prioriza a abertura e a apresentação do conteúdo. O gerenciador acrescenta catalogação, metadados, organização e conversões.

## 1.2. SumatraPDF

**Tipo:** aplicativo de leitura de documentos.

**Desenvolvedor:** Krzysztof Kowalczyk e contribuidores.

**Site oficial:**  
https://www.sumatrapdfreader.org/

**Código-fonte oficial:**  
https://github.com/sumatrapdfreader/sumatrapdf

**Download oficial — Windows:**  
https://www.sumatrapdfreader.org/download-free-pdf-viewer

**Releases no GitHub:**  
https://github.com/sumatrapdfreader/sumatrapdf/releases

**Documentação:**  
https://www.sumatrapdfreader.org/docs/SumatraPDF-documentation

### Características técnicas

- **Linguagem principal:** C/C++.
- **Licença:** família GPL/AGPL, com componentes sob outras licenças conforme o repositório.
- **Sistema operacional:** Windows.
- **Arquiteturas disponibilizadas:** 32 bits, 64 bits e ARM64, conforme a distribuição.
- **Versão estável identificada:** 3.6.1.
- **Distribuição:** instalador e versão portátil.

### Finalidade

Leitura rápida de documentos, livros digitais e histórias em quadrinhos.

### Principais recursos

- Abertura de PDF, EPUB, MOBI, FB2 e outros formatos.
- Navegação por páginas e sumários.
- Pesquisa de texto.
- Favoritos.
- Atalhos de teclado.
- Personalização visual.
- Uso portátil sem instalação convencional.

### Vantagens

Aplicativo relativamente pequeno, direto e adequado a quem prefere abrir documentos sem utilizar uma suíte completa.

### Limitações

Não é um gerenciador completo de bibliotecas, como o Calibre.

O suporte a EPUB e outros formatos deve ser avaliado conforme os recursos de leitura necessários.

**Estado:** projeto e distribuição oficial identificados. Teste prático pendente.

---

## 1.3. Thorium Reader

**Tipo:** leitor de livros digitais EPUB.

**Responsável:** EDRLab.

**Site oficial:**  
https://www.thoriumreader.com/

**Organização desenvolvedora:**  
https://www.edrlab.org/

**Repositório oficial:**  
https://github.com/edrlab/thorium-reader

**Download oficial — versões estáveis:**  
https://github.com/edrlab/thorium-reader/releases

**Documentação e desenvolvimento:**  
https://github.com/edrlab/thorium-reader#readme

### Características técnicas

- **Linguagens:** TypeScript e JavaScript.
- **Tecnologias:** Electron, React e componentes Readium.
- **Licença:** BSD-3-Clause.
- **Sistemas:** Windows, Linux e macOS.
- **Versão estável identificada:** 3.5.1.
- **Formato principal:** EPUB, com recursos adicionais conforme a versão.

### Finalidade

Oferecer um ambiente de leitura digital com especial atenção à acessibilidade e aos formatos de publicação eletrônica.

### Principais recursos

- Leitura de EPUB.
- Personalização da apresentação do texto.
- Navegação por sumário.
- Marcadores.
- Suporte a recursos de acessibilidade.
- Importação de publicações e catálogos OPDS.
- Interface disponível em português brasileiro.

### Requisitos

As distribuições oficiais permitem utilizar o aplicativo sem preparar manualmente um ambiente de desenvolvimento.

**Node.js é requisito para determinadas atividades de desenvolvimento e compilação, não para simplesmente utilizar um executável oficial já preparado.**

### Atenção às versões

A página de releases pode apresentar versões de teste automatizadas.

Selecionar uma versão numerada e estável, evitando arquivos identificados como beta ou pre-release.

**Estado:** projeto e release estável identificados. Instalação e compatibilidade prática não testadas.

---

## 1.4. Links complementares de pesquisa

- [Pesquisar leitores de ebooks para Windows](https://github.com/search?q=ebook+reader+windows&type=repositories)
- [Projetos de leitores digitais — eReader](https://github.com/topics/ereader)
- [Projetos de leitores EPUB](https://github.com/topics/epub-reader)
- [Projetos de leitores de ebooks](https://github.com/topics/ebook-reader)

**Resultado:** leitores concretos identificados, com desenvolvedores, documentação e canais oficiais de obtenção.

---

# 📕 2. ACSM — ferramentas e projetos

## 2.1. O que é ACSM?

**ACSM** significa *Adobe Content Server Message*.

Um arquivo ACSM não é propriamente um livro digital.

Ele contém informações utilizadas no processo de obtenção de uma publicação por um sistema compatível com a infraestrutura de distribuição da Adobe.

O livro obtido pode ser um EPUB ou PDF, eventualmente acompanhado de mecanismos de proteção por direitos digitais (DRM).

### Diferença entre formatos

| Elemento | Finalidade |
|---|---|
| ACSM | Participar do processo de obtenção/autorização do livro |
| EPUB | Armazenar uma publicação digital |
| PDF | Representar um documento com estrutura de páginas |
| DRM | Aplicar regras técnicas de controle de acesso ou utilização |

---

## 2.2. Adobe Digital Editions

**Tipo:** aplicativo de leitura e gerenciamento de publicações compatíveis com o ecossistema Adobe.

**Desenvolvedor:** Adobe.

**Site oficial:**  
https://www.adobe.com/solutions/ebook/digital-editions.html

**Download oficial:**  
https://www.adobe.com/solutions/ebook/digital-editions/download.html

**Suporte e documentação:**  
https://helpx.adobe.com/digital-editions.html

### Características técnicas

- **Licença:** proprietária.
- **Código-fonte:** não disponibilizado como projeto aberto.
- **Sistemas:** Windows e macOS, conforme as distribuições oficiais.
- **Versão indicada na página oficial consultada:** 4.5.12.
- **Linguagem interna:** não documentada publicamente de forma suficiente para classificação segura nesta pesquisa.

### Finalidade

Abrir publicações digitais e realizar a obtenção de livros vinculados a arquivos ACSM e sistemas de autorização compatíveis.

### Recursos

- Leitura de EPUB e PDF.
- Processamento de arquivos ACSM.
- Gerenciamento de publicações.
- Autorização de dispositivos e contas compatíveis.
- Tratamento de determinados empréstimos digitais.

### Limitações

- Software proprietário.
- Dependência de mecanismos específicos de distribuição e autorização.
- Restrições decorrentes de DRM, quando aplicável.

**Estado:** distribuição oficial identificada. Não instalado nem testado nesta pesquisa.

---

## 2.3. ACSM Input Plugin para Calibre

**Nome do projeto:** ACSM Input Plugin, anteriormente denominado DeACSM.

**Tipo:** extensão para o Calibre.

**Desenvolvedor:** Leseratte10 e contribuidores.

**Repositório original:**  
https://github.com/Leseratte10/acsm-calibre-plugin

**Download oficial — releases:**  
https://github.com/Leseratte10/acsm-calibre-plugin/releases

**Documentação:**  
https://github.com/Leseratte10/acsm-calibre-plugin#readme

**Licença:** verificar o arquivo LICENSE da versão utilizada.

**Linguagem:** Python.

**Ambiente:** Calibre e suas dependências internas.

### Finalidade

Implementar funcionalidades de processamento de arquivos ACSM como extensão do Calibre, utilizando componentes desenvolvidos pela comunidade.

### Funcionamento

O plugin interage com sistemas de autorização e obtenção de publicações para realizar determinadas operações normalmente associadas ao ecossistema Adobe Digital Editions.

### Versões

A release estável 0.0.16 foi identificada.

O repositório também documenta desenvolvimento posterior, com versões experimentais que não devem ser tratadas automaticamente como estáveis.

### Limitações e cuidados

- Não é um componente oficial da Adobe.
- Seu funcionamento depende das condições de autorização da publicação e do distribuidor.
- A obtenção de um EPUB/PDF não significa que o livro esteja livre de DRM.
- Compatibilidade com versões recentes do Calibre precisa ser verificada.
- O uso deve respeitar as licenças, os direitos aplicáveis e as condições dos serviços.

**Estado:** projeto oficial do mantenedor e página de releases identificados. Compatibilidade prática pendente.

---

## 2.4. Links complementares

- [Projetos relacionados a ACSM](https://github.com/search?q=acsm&type=repositories)
- [Projetos com o tópico ACSM](https://github.com/topics/acsm)
- [Projetos relacionados a Adobe Digital Editions](https://github.com/search?q=adobe+digital+editions&type=repositories)

---

# 📘 3. Calibre — gerenciamento de livros digitais

## 3.1. Identificação

**Nome oficial:** calibre.

**Tipo:** gerenciador de bibliotecas digitais.

**Criador e desenvolvedor principal:** Kovid Goyal.

**Site oficial:**  
https://calibre-ebook.com/

**Código-fonte oficial:**  
https://github.com/kovidgoyal/calibre

**Download oficial — todas as plataformas:**  
https://calibre-ebook.com/download

**Download oficial — Windows:**  
https://calibre-ebook.com/download_windows

**Documentação:**  
https://manual.calibre-ebook.com/

**Lançamentos e histórico:**  
https://calibre-ebook.com/whats-new

## 3.2. Características técnicas

- **Linguagem principal:** Python, com componentes adicionais em outras linguagens.
- **Licença:** GPL-3.0.
- **Sistemas:** Windows, Linux e macOS.
- **Distribuições:** instaladores e modalidade portátil conforme a plataforma.
- **Arquitetura Windows atual:** verificar o instalador de 64 bits fornecido pelo site.
- **Versão exibida na página Windows durante a consulta:** 9.18.0.

## 3.3. Finalidade

Organizar grandes coleções de livros digitais.

O Calibre não é apenas um leitor de livros.

Ele reúne ferramentas de catalogação, conversão, gerenciamento de metadados, leitura e edição.

## 3.4. Principais recursos

- Catalogação de livros.
- Organização por autores, títulos, séries e editoras.
- Pesquisa na biblioteca.
- Conversão entre formatos compatíveis.
- Edição de metadados.
- Visualização de livros.
- Editor de EPUB.
- Gerenciamento de capas.
- Integração com dispositivos compatíveis.
- Servidor de conteúdo para acesso à biblioteca.
- Sistema de extensões.

## 3.5. Dependências

As distribuições oficiais incluem diversos componentes necessários ao funcionamento.

Não se deve presumir que o Python instalado separadamente no computador precise ser utilizado pelo Calibre.

## 3.6. Limitações

- Conversões podem modificar a formatação original.
- Nem todo arquivo protegido por DRM poderá ser convertido.
- Extensões independentes precisam ser avaliadas quanto à compatibilidade e procedência.

**Estado:** ferramenta, desenvolvedor e downloads oficiais identificados. Instalação não realizada nesta pesquisa.

---

# 🖼️ 4. Processamento e restauração de imagens

## 4.1. OpenCV

**Nome oficial:** Open Source Computer Vision Library.

**Tipo:** biblioteca de programação para visão computacional e processamento de imagens.

**Responsável:** projeto OpenCV e seus contribuidores.

**Site oficial:**  
https://opencv.org/

**Repositório oficial:**  
https://github.com/opencv/opencv

**Downloads e versões:**  
https://opencv.org/releases/

**Releases no GitHub:**  
https://github.com/opencv/opencv/releases

**Documentação oficial:**  
https://docs.opencv.org/

**Pacote Python no PyPI:**  
https://pypi.org/project/opencv-python/

**Instruções oficiais para Python:**  
https://docs.opencv.org/5.0/py_tutorials/py_setup/py_pip_install/py_pip_install.html

## 4.2. Características técnicas

- **Linguagem principal:** C++.
- **Interfaces:** Python e outras linguagens.
- **Licença:** Apache-2.0 nas versões modernas.
- **Sistemas:** Windows, Linux, macOS e outras plataformas.
- **Tipo de distribuição:** biblioteca, pacotes de desenvolvimento e componentes compilados.
- **Versão identificada nas releases:** OpenCV 5.1.0.
- **Linha anterior:** OpenCV 4.x, ainda relevante para projetos que dependam dessa API.

## 4.3. Finalidade

Executar operações de análise, transformação e processamento de imagens por meio de programas e scripts.

O OpenCV não é um editor gráfico convencional.

## 4.4. Recursos importantes

### Processamento de imagens

- Redimensionamento.
- Rotação.
- Transformações geométricas.
- Conversão entre espaços de cores.
- Filtragem e suavização.

### Identificação de elementos

- Detecção de bordas.
- Detecção de linhas.
- Identificação de contornos.
- Segmentação.
- Reconhecimento de padrões.

### Restauração

- Tratamento de defeitos.
- Máscaras.
- Inpainting.
- Preenchimento de regiões danificadas.
- Operações morfológicas.

### Operações geométricas

- Transformações afins.
- Homografias.
- Correção de perspectiva.
- Extração de formas.

## 4.5. Dependências e utilização

O OpenCV pode ser utilizado diretamente com C++ ou por interfaces Python.

Para Python, a documentação oficial apresenta pacotes como:

- `opencv-python`
- `opencv-contrib-python`
- variantes `headless`

É necessário selecionar o pacote adequado ao ambiente, evitando instalar variantes conflitantes no mesmo interpretador.

A disponibilidade de pacotes compilados depende da versão e da arquitetura do Python.

## 4.6. Limitações

- Requer conhecimento de programação ou integração com outra aplicação.
- Algoritmos de restauração não recuperam automaticamente informações históricas inexistentes.
- Versões de API podem apresentar incompatibilidades.
- A compatibilidade do pacote Python precisa ser verificada antes da instalação.

**Estado:** projeto, documentação e distribuições oficiais identificados. Algoritmos e resultados práticos não testados nesta pesquisa.

---

# ✍️ 5. Mesas digitalizadoras XP-Pen — ferramentas independentes

## 5.1. Finalidade

Pesquisar programas, drivers e soluções alternativas para configuração de mesas digitalizadoras XP-Pen.

Objetivos:

- Rotação de 180° para uso por canhotos.
- Remapeamento dos eixos X e Y.
- Configuração dos botões.
- Identificação da conexão USB.
- Gerenciamento da área ativa.
- Funcionamento no Windows sem depender exclusivamente do aplicativo proprietário do fabricante.

**Hardware de referência:** `VID_28BD&PID_0918`.

A identificação correta do equipamento deve ser confirmada antes da escolha de qualquer driver.

## 5.2. OpenTabletDriver

**Tipo:** driver alternativo em modo de usuário.

**Responsável:** comunidade OpenTabletDriver.

**Repositório:**  
https://github.com/OpenTabletDriver/OpenTabletDriver

**Download oficial:**  
https://github.com/OpenTabletDriver/OpenTabletDriver/releases

**Documentação:**  
https://opentabletdriver.net/

### Características técnicas

- **Linguagem:** C#.
- **Tecnologia:** .NET.
- **Licença:** LGPL-3.0.
- **Sistemas:** Windows, Linux e macOS.

### Recursos

- Remapeamento da área da mesa.
- Mapeamento para monitores.
- Perfis e configurações.
- Modos de posicionamento.
- Extensões e filtros.

### Requisitos

Utilizar a distribuição compatível com o sistema e conferir os requisitos .NET especificados na release.

### Pendências

A existência de suporte a equipamentos da família XP-Pen não comprova automaticamente suporte ao identificador exato `28BD:0918`.

**Estado:** prioridade de investigação para Windows. Compatibilidade específica ainda não testada.

---

## 5.3. AetherGUI

**Tipo:** driver e interface nativa para mesas digitalizadoras no Windows.

**Desenvolvedor:** silentlag.

**Repositório:**  
https://github.com/silentlag/AetherGUI

**Download oficial:**  
https://github.com/silentlag/AetherGUI/releases

**Licença original:**  
https://github.com/silentlag/AetherGUI/blob/main/LICENSE.md

**Documentação:**  
https://github.com/silentlag/AetherGUI#readme

### Características técnicas

- **Linguagem:** C++.
- **Interface:** componentes nativos do Windows, incluindo Direct2D.
- **Sistemas:** Windows 10/11.
- **Arquitetura de compilação documentada:** x64.
- **Versão estável identificada:** 1.1.3.

### Finalidade

Oferecer uma solução de controle de mesas digitalizadoras com interface gráfica e processamento de entrada de baixa latência.

### Recursos

- Mapeamento da área ativa.
- Ajuste de monitores.
- Filtros.
- Perfis.
- Modos de entrada.
- Configurações de desempenho.
- Suporte a extensões compatíveis.

### Licença — observação importante

O repositório disponibiliza código-fonte, mas utiliza **licença própria com restrições de uso e redistribuição**.

Ela permite determinadas atividades pessoais e não comerciais, porém **não corresponde a uma licença tradicional de software livre**.

Não presumir permissão para redistribuição comercial, incorporação em outros produtos ou relicenciamento.

### Pendências

- Confirmar compatibilidade com `28BD:0918`.
- Confirmar requisitos adicionais de driver.
- Verificar comportamento no Windows utilizado.
- Testar filtros e remapeamento antes de considerar a solução aprovada.

**Estado:** alternativa nativa para Windows, documentalmente identificada e ainda não testada.

---

## 5.4. Hawku TabletDriver

**Tipo:** driver alternativo para mesas digitalizadoras.

**Desenvolvedor:** hawku.

**Repositório:**  
https://github.com/hawku/TabletDriver

**Download oficial:**  
https://github.com/hawku/TabletDriver/releases

**Documentação:**  
https://github.com/hawku/TabletDriver#readme

### Características

- **Linguagem:** C++.
- **Licença:** GPL-3.0.
- **Sistema:** Windows.

### Finalidade

Fornecer recursos de configuração de mesas gráficas, especialmente para aplicações que exigem controle de entrada.

### Limitação principal

Projeto antigo, sem indicação de manutenção equivalente à de alternativas mais recentes.

O próprio repositório recomenda considerar o OpenTabletDriver.

**Estado:** referência técnica secundária. Compatibilidade com versões modernas do Windows e com `28BD:0918` não confirmada.

---

## 5.5. DIGImend Kernel Drivers

**Tipo:** conjunto de drivers para kernel Linux.

**Responsável:** comunidade DIGImend.

**Repositório:**  
https://github.com/DIGImend/digimend-kernel-drivers

**Versões oficiais:**  
https://github.com/DIGImend/digimend-kernel-drivers/releases

**Documentação:**  
https://github.com/DIGImend/digimend-kernel-drivers#readme

### Características

- **Linguagem:** C.
- **Licença:** GPL-2.0.
- **Sistema:** Linux.

### Finalidade

Adicionar e aperfeiçoar suporte a diferentes mesas digitalizadoras no Linux.

### Aplicação na pesquisa

Estudo de protocolos, identificadores USB e comportamento de equipamentos.

**Não é uma solução direta de instalação no Windows.**

**Estado:** referência técnica secundária. Compatibilidade específica pendente.

---

## 5.6. Kuri Userspace Tablet Driver Daemon

**Tipo:** driver de mesa digitalizadora em espaço de usuário.

**Desenvolvedor:** kurikaesu.

**Repositório:**  
https://github.com/kurikaesu/userspace-tablet-driver-daemon

**Página para verificar distribuições:**  
https://github.com/kurikaesu/userspace-tablet-driver-daemon/releases

**Documentação e código-fonte:**  
https://github.com/kurikaesu/userspace-tablet-driver-daemon#readme

### Características

- **Linguagem:** C++.
- **Sistema:** Linux.
- **Distribuição:** verificar instruções de compilação; não presumir pacote pronto nas releases.
- **Licença:** consultar o arquivo LICENSE do projeto.

### Finalidade

Fornecer suporte a mesas digitalizadoras utilizando um serviço executado no espaço de usuário.

### Limitações

- Não constitui solução pronta para Windows.
- Compatibilidade específica com a XP-Pen G960S e `28BD:0918` ainda não comprovada.

**Estado:** referência documental.

---

## 5.7. Pesquisa complementar

- [Projetos XP-Pen](https://github.com/search?q=xp-pen&type=repositories)
- [Drivers para mesas digitalizadoras](https://github.com/search?q=tablet+driver&type=repositories)
- [Remapeamento e rotação](https://github.com/search?q=tablet+rotation&type=repositories)
- [AetherGUI](https://github.com/search?q=AetherGUI&type=repositories)

### Situação da pesquisa

**Prioridade documental para Windows:**

1. OpenTabletDriver.
2. AetherGUI.

**Referências complementares:**

- Hawku TabletDriver.
- DIGImend.
- Kuri Userspace Tablet Driver Daemon.

Nenhuma dessas ferramentas foi aprovada para o hardware específico apenas com base neste levantamento.

---

# 🗺️ 6. Cartografia digital — dados, renderização e estilos

## 6.1. Objetivo

Pesquisar ferramentas de obtenção, processamento, análise, edição, representação e estilização de informações geográficas.

A investigação contempla duas arquiteturas:

**Fluxo A — Cartografia com CartoCSS, Kosmtik e Mapnik.**

**Fluxo B — Cartografia com tiles vetoriais, Maputnik e MapLibre.**

As duas alternativas permanecem documentadas.

A existência de tecnologias mais recentes não determina automaticamente o abandono de ferramentas clássicas.

---

## 6.2. Compatibilidade de ambiente

O ambiente de trabalho deve ser considerado separadamente das características das ferramentas pesquisadas.

Um Python instalado em 32 bits pode coexistir com outras instalações independentes, inclusive de 64 bits, quando tecnicamente necessário.

Isso não significa que bibliotecas compiladas para 64 bits funcionem dentro de um interpretador de 32 bits.

QGIS, PostgreSQL, Mapnik, Node.js e outras ferramentas podem possuir seus próprios componentes e dependências.

**Nenhuma atualização ou instalação é necessária apenas para consultar este catálogo.**

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
- **Linguagem:** não se aplica uma única linguagem ao conjunto de dados.

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

### Requisitos

Não exige instalação de aplicativo para baixar os dados; o processamento depende das ferramentas escolhidas posteriormente.

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

### Recursos

- Tabelas e relacionamentos.
- Índices.
- Consultas SQL.
- Transações.
- Extensões.
- Gerenciamento de grandes volumes de informações.

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

### Recursos

- Geometrias de pontos, linhas e polígonos.
- Índices espaciais.
- Operações de interseção.
- Cálculos de distância.
- Consultas espaciais.
- Integração com sistemas GIS.

### Dependências

Requer uma instalação compatível do PostgreSQL.

**PostGIS não é um aplicativo gráfico independente.**

**Estado:** extensão identificada; combinações de versões devem ser verificadas antes da instalação.

---

## 7.6. osm2pgsql

**Tipo:** ferramenta de importação de dados OpenStreetMap.

**Responsáveis:** mantenedores e contribuidores do osm2pgsql.

**Linguagem principal:** C++.

**Outras tecnologias:** Lua em configurações de importação flex.

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

### Características

- Processamento de arquivos `.osm.pbf`.
- Importação de atributos e geometrias.
- Diferentes estratégias de organização das tabelas.
- Processamento de grandes conjuntos de dados.

### Requisitos

- Sistema compatível de 64 bits nas distribuições modernas.
- PostgreSQL.
- PostGIS.
- Espaço de armazenamento e memória adequados ao volume dos dados.

### Observação

A versão de linha de comando pode ser distribuída sem instalador gráfico.

**Estado:** documentação e downloads oficiais identificados. Compatibilidade prática não testada.

---

## 7.7. SQL

**Tipo:** linguagem de consulta e manipulação de dados.

**Finalidade:** consultar, organizar e transformar informações armazenadas em bancos relacionais.

**Linguagem:** SQL.

**Documentação de referência PostgreSQL:**  
https://www.postgresql.org/docs/current/sql.html

### Aplicação cartográfica

Selecionar feições, relacionar tabelas, consultar atributos e executar funções espaciais disponibilizadas pelo PostGIS.

**Download próprio:** não se aplica. SQL é uma linguagem; as ferramentas utilizadas para executá-la dependem do banco de dados escolhido.

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

Definir a aparência visual dos mapas, incluindo:

- Cores de vias.
- Hidrografia.
- Vegetação.
- Padrões de áreas.
- Símbolos.
- Rótulos.
- Espessuras.
- Hierarquia visual.

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

### Funcionamento

As regras definem como diferentes tipos de feições serão apresentados.

O compilador produz definições adequadas ao mecanismo de renderização correspondente.

### Limitação

O repositório de referência foi arquivado.

Sua utilização deve considerar dependências antigas e eventuais limitações de manutenção.

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

### Recursos

- Renderização de linhas.
- Polígonos.
- Símbolos.
- Rótulos.
- Padrões.
- Composição de diferentes camadas.
- Saída de imagens cartográficas.

### Formatos de saída

O Mapnik pode produzir formatos raster, como PNG, e também trabalhar com saídas vetoriais mediante suporte apropriado.

**SVG e PDF dependem da disponibilidade do renderizador Cairo na compilação utilizada.**

### Aplicação artística

Criar mapas com simbologia controlada, inclusive para tratamento posterior em editores gráficos.

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

A página de releases não apresentava instalador estável publicado na consulta realizada.

**Não confundir a obtenção do código-fonte com um instalador Windows pronto.**

### Situação

O Kosmtik permanece nesta pesquisa como ferramenta do fluxo clássico.

Não existe decisão de abandoná-lo.

**Estado:** fonte e requisitos documentados; funcionamento no ambiente de destino não testado.

---

# 8. Arquitetura B — tiles vetoriais, Maputnik e MapLibre

## 8.1. Sequência de funcionamento

**OpenStreetMap / Geofabrik**  
↓  
**tilemaker — geração de tiles vetoriais**  
↓  
**MBTiles / PMTiles ou estrutura compatível de tiles**  
↓  
**Martin ou serviço de tiles compatível, quando necessário**  
↓  
**Maputnik — edição do estilo JSON**  
↓  
**MapLibre GL JS — renderização no navegador**  
↓  
**Mapa interativo com representação vetorial estilizada**

### Observação

Maputnik e MapLibre não executam exatamente a mesma função.

**Maputnik edita os estilos.**

**MapLibre GL JS interpreta os estilos e renderiza o mapa.**

Ambos precisam de fontes de dados adequadas.

## 8.2. O que significa mapa vetorial estilizado?

As informações geográficas são representadas por geometrias e atributos organizados em tiles vetoriais.

O estilo define como esses dados aparecem visualmente.

Podem ser controlados:

- Cores.
- Espessuras.
- Tipos de símbolos.
- Camadas.
- Rótulos.
- Visibilidade.
- Regras dependentes do zoom.
- Aparência de diferentes classes de feições.

### Resultado artístico

O resultado inicial é um mapa interativo renderizado no navegador.

O estilo pode ser alterado sem necessariamente reconstruir todos os tiles geográficos.

**Entretanto, um mapa baseado em tiles vetoriais não é automaticamente um SVG ou PDF pronto para edição no Inkscape.**

A exportação para impressão ou edição vetorial exige procedimentos adicionais.

---

## 8.3. tilemaker

**Tipo:** gerador de tiles vetoriais.

**Desenvolvedor principal:** Richard Fairhurst e contribuidores.

**Linguagens:** C++ e Lua.

**Repositório oficial:**  
https://github.com/systemed/tilemaker

**Downloads oficiais:**  
https://github.com/systemed/tilemaker/releases

**Documentação:**  
https://github.com/systemed/tilemaker#readme

**Licença:** FTWPL, conforme `LICENCE.txt` do repositório.

**Versão estável identificada:** 3.2.0.

### Finalidade

Transformar dados OpenStreetMap em tiles vetoriais.

### Formatos relevantes

- Entrada: `.osm.pbf`.
- Saída: arquivos MBTiles, PMTiles e formatos suportados pela versão.

### Vantagens

Pode gerar tiles vetoriais sem exigir a utilização obrigatória de PostgreSQL/PostGIS como etapa intermediária.

### Dependências

Variam conforme a plataforma e o método de distribuição.

Scripts e configurações em Lua podem controlar o processamento.

### Limitações

- Não é editor visual de mapas.
- Não substitui Maputnik ou MapLibre.
- O formato de saída precisa ser compatível com o serviço e o visualizador utilizados.
- A disponibilidade de binários estáveis para Windows deve ser conferida na release correspondente.

**Estado:** código, licença e releases identificados. Geração prática não testada.

---

## 8.4. Martin

**Tipo:** servidor de tiles cartográficos.

**Responsável:** comunidade MapLibre.

**Linguagem:** Rust.

**Repositório oficial:**  
https://github.com/maplibre/martin

**Releases:**  
https://github.com/maplibre/martin/releases

**Documentação:**  
https://maplibre.org/martin/

**Instalação oficial:**  
https://maplibre.org/martin/installation/

### Finalidade

Disponibilizar dados cartográficos para aplicações que consomem tiles.

### Recursos

- Servir tiles vetoriais.
- Trabalhar com fontes de dados compatíveis.
- Integração com arquivos de tiles e fontes espaciais documentadas.
- Disponibilização de dados por serviços adequados à visualização web.

### Requisitos

Dependem da plataforma, distribuição e tipo de fonte de dados.

### Observação

Martin não é obrigatório em toda arquitetura MapLibre.

Ele representa uma alternativa de distribuição dos dados.

**Estado:** projeto identificado. Seleção de release estável e teste prático pendentes.

---

## 8.5. Maputnik

**Tipo:** editor visual de estilos de mapas.

**Criador inicial:** Lukas Martinelli.

**Responsável atual:** comunidade MapLibre.

**Linguagens:** TypeScript e JavaScript.

**Tecnologias:** React e componentes de renderização MapLibre.

**Licença:** MIT.

**Editor oficial no navegador:**  
https://maplibre.org/maputnik/

**Repositório oficial:**  
https://github.com/maplibre/maputnik

**Download oficial — releases:**  
https://github.com/maplibre/maputnik/releases

**Documentação:**  
https://github.com/maplibre/maputnik/wiki

**Especificação de estilos:**  
https://maplibre.org/maplibre-style-spec/

**Versão estável identificada:** 3.1.0.

### Finalidade

Permitir a criação e a edição visual de estilos para mapas vetoriais.

### Principais recursos

- Alteração de cores.
- Definição de camadas.
- Configuração de símbolos.
- Personalização de rótulos.
- Controle de espessuras.
- Regras de visibilidade.
- Edição de filtros.
- Organização das propriedades de estilo.

### Formato principal

`style.json`

O arquivo contém regras de aparência e referências às fontes utilizadas.

### Ambiente

A edição hospedada funciona em navegador compatível.

**Não é necessário instalar Python ou Node.js para simplesmente utilizar o editor web oficial.**

Para compilar ou desenvolver o Maputnik localmente, outros requisitos podem ser necessários.

### Limitações

- Não substitui o gerador de tiles.
- Não substitui necessariamente um servidor de dados.
- Não transforma automaticamente um mapa em documento SVG editável.
- A visualização depende de fontes de tiles, símbolos e fontes tipográficas compatíveis.

**Estado:** editor oficial e release estável identificados. Utilização prática não testada.

---

## 8.6. MapLibre GL JS

**Tipo:** biblioteca de renderização de mapas para aplicações web.

**Responsável:** comunidade MapLibre.

**Linguagem:** TypeScript/JavaScript.

**Tecnologia gráfica:** WebGL.

**Licença:** BSD-3-Clause.

**Site oficial:**  
https://maplibre.org/

**Repositório:**  
https://github.com/maplibre/maplibre-gl-js

**Distribuição oficial da biblioteca:**  
https://www.npmjs.com/package/maplibre-gl

**Releases:**  
https://github.com/maplibre/maplibre-gl-js/releases

**Documentação:**  
https://maplibre.org/maplibre-gl-js/docs/

**Versão estável identificada:** 6.18.0.

### Finalidade

Renderizar mapas interativos no navegador.

### Recursos

- Exibição de tiles vetoriais.
- Aplicação de estilos.
- Navegação.
- Zoom.
- Rotação.
- Rótulos.
- Renderização de camadas.
- Interatividade.

### Funcionamento

O MapLibre GL JS interpreta dados e regras visuais para apresentar o mapa na interface de uma aplicação web.

### Dependências

Para desenvolver uma aplicação, são necessários recursos web, como HTML e JavaScript, além das fontes cartográficas utilizadas.

Node.js pode participar do desenvolvimento e da construção de projetos, mas não é necessariamente exigido do usuário que apenas acessa um mapa já publicado.

### Limitações

- Não é um editor gráfico convencional.
- A visualização no navegador não produz automaticamente SVG/PDF vetorial editável.
- Depende de dados e recursos de estilo acessíveis.

**Estado:** biblioteca e releases identificadas. Implementação prática não testada.

---

# 9. Edição cartográfica e vetorial

## 9.1. QGIS

**Tipo:** sistema de informação geográfica de desktop.

**Responsável:** projeto QGIS e comunidade de desenvolvimento.

**Linguagens principais:** C++ e Python.

**Tecnologias:** Qt, GDAL, PROJ e outras bibliotecas geoespaciais.

**Licença:** GPL.

**Site oficial:**  
https://qgis.org/

**Repositório:**  
https://github.com/qgis/QGIS

**Download oficial:**  
https://qgis.org/download/

**Documentação:**  
https://docs.qgis.org/

**Versão LTR identificada:** 3.44.15.

### Finalidade

Analisar, processar, editar e representar informações geográficas.

### Recursos

- Sistemas de coordenadas.
- Georreferenciamento.
- Camadas vetoriais.
- Camadas raster.
- Operações espaciais.
- Medição de distâncias.
- Controle de escala.
- Processamento geográfico.
- Layouts cartográficos.
- Exportação de mapas.
- Automação com PyQGIS.

### Compatibilidade

Disponível para diferentes sistemas operacionais.

Os instaladores Windows atuais são distribuídos para ambientes compatíveis de 64 bits.

### Versões

O QGIS possui lançamentos com novas funcionalidades e uma linha LTR, voltada à estabilidade.

**Preferência de pesquisa:** linha LTR para aplicações que priorizam previsibilidade e continuidade.

### Observação

O ambiente Python utilizado internamente pelo QGIS não deve ser confundido automaticamente com outro interpretador Python instalado separadamente no computador.

**Estado:** projeto, documentação e distribuição LTR identificados. Adequação a cada aplicação depende de validação técnica.

---

## 9.2. Inkscape

**Tipo:** editor de gráficos vetoriais.

**Responsável:** projeto Inkscape e contribuidores.

**Linguagem principal:** C++.

**Licença:** GPL.

**Site oficial:**  
https://inkscape.org/

**Código-fonte oficial:**  
https://gitlab.com/inkscape/inkscape

**Download oficial:**  
https://inkscape.org/release/

**Documentação:**  
https://inkscape.org/learn/

### Finalidade

Criar e editar elementos gráficos vetoriais.

### Recursos

- Edição de SVG.
- Curvas.
- Traçados.
- Objetos.
- Símbolos.
- Texto.
- Cores.
- Composição gráfica.
- Ajuste de elementos importados.

### Aplicação cartográfica

Pode ser utilizado no acabamento artístico de mapas exportados por programas GIS ou renderizadores.

### Limitações

O Inkscape não substitui um sistema GIS.

A edição vetorial não garante preservação automática de projeções, escalas e coordenadas geográficas.

**Estado:** projeto e canais oficiais identificados. Procedimentos específicos de integração com arquivos cartográficos dependem de teste.

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

# 11. Critérios para comparação artística futura

Antes de decidir entre os fluxos, verificar:

1. Fidelidade das geometrias.
2. Preservação das coordenadas.
3. Precisão da escala.
4. Qualidade das linhas.
5. Qualidade dos textos.
6. Controle das cores.
7. Aparência dos símbolos.
8. Controle das camadas.
9. Qualidade de exportação raster.
10. Possibilidade real de exportação vetorial.
11. Editabilidade posterior.
12. Dependências técnicas.
13. Compatibilidade com o ambiente.
14. Facilidade de repetição do processo.
15. Estabilidade das versões utilizadas.

A decisão deve considerar resultados efetivamente obtidos em testes comparativos.

---

# 12. Política de versões estáveis

Este catálogo prioriza distribuições oficiais estáveis.

## 12.1. Preferências

**Preferir:**

- Stable release.
- Versão de manutenção.
- LTR, quando o projeto oferecer essa modalidade.
- Pacotes publicados pelos mantenedores originais.

**Não escolher automaticamente:**

- Alpha.
- Beta.
- Release Candidate.
- Nightly.
- Builds experimentais.
- Código de desenvolvimento sem release estável.

## 12.2. Verificações necessárias

Antes de instalar um programa:

- Confirmar autoria.
- Confirmar origem.
- Conferir a licença.
- Conferir arquitetura.
- Conferir sistema operacional.
- Verificar dependências.
- Examinar notas de versão.
- Verificar assinaturas e checksums, quando disponibilizados.
- Conferir se o arquivo é executável, instalador, biblioteca ou código-fonte.

**Um link de download oficial não constitui aprovação automática para instalação.**

---

# 13. Situação geral das pesquisas

| Área | Situação documental | Testes práticos |
|---|---|---|
| Leitores digitais | Programas e downloads oficiais identificados | Pendentes |
| ACSM | Ferramentas e diferenças técnicas documentadas | Pendentes |
| Calibre | Ficha técnica e download oficial identificados | Pendentes |
| OpenCV | Biblioteca, APIs e distribuição documentadas | Pendentes |
| Mesas XP-Pen | Cinco projetos identificados, com aprofundamento técnico | Compatibilidade específica pendente |
| Cartografia clássica | Fluxo e ferramentas documentados | Integração pendente |
| Cartografia vetorial moderna | Fluxo e ferramentas documentados | Integração pendente |
| Comparação artística | Critérios definidos | Resultados pendentes |

## Próximas pesquisas

- Comparar efetivamente os resultados dos dois fluxos cartográficos.
- Verificar requisitos das versões estáveis no ambiente de destino.
- Investigar métodos de exportação SVG/PDF no fluxo de tiles vetoriais.
- Confirmar compatibilidade das ferramentas XP-Pen com o hardware identificado.
- Avaliar leitores digitais conforme formatos e recursos desejados.
- Aprofundar exemplos documentados de processamento de imagens com OpenCV.

---

# 14. Conclusão

O objetivo deste repositório é reunir informações técnicas verificáveis e facilitar a localização de programas e tecnologias diretamente em suas fontes de desenvolvimento.

Cada pesquisa deve preservar a distinção entre:

**Ferramenta → Desenvolvedor → Finalidade → Funcionamento → Requisitos → Repositório → Download oficial → Estado de verificação.**

As opções tecnológicas devem ser comparadas por suas capacidades reais, suas limitações e seus resultados demonstráveis.

**Registrar uma ferramenta não significa instalá-la.**

**Identificar uma solução não significa validá-la.**

**Ter uma tecnologia mais recente não significa que ela seja automaticamente superior para todas as finalidades.**

---

**Autor:** BRV_Cap_Blue_GEM  
**Documento:** Minhas pesquisas — README v2.0  
**Data da revisão:** 19/11/2026  
**Estado:** conteúdo preparado para revisão e publicação manual no GitHub.
