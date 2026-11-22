> **Navegação:** [Índice principal](../README.md) · [Cartografia](README.md) · [Arquitetura A](arquitetura-a.md) · [Inventário A](arquitetura-a-inventario.md) · [Arquitetura B](arquitetura-b.md) · [Edição vetorial](edicao-vetorial.md) · [Comparação](comparacao-fluxos.md)

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
