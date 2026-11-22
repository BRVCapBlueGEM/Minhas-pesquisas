> **Navegação:** [Índice principal](../README.md) · [Cartografia](README.md) · [Arquitetura A](arquitetura-a.md) · [Inventário A](arquitetura-a-inventario.md) · [Arquitetura B](arquitetura-b.md) · [Edição vetorial](edicao-vetorial.md) · [Comparação](comparacao-fluxos.md)

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
