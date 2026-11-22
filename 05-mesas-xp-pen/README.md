> **Navegação:** [Índice principal](../README.md) · [Catálogo Minhas pesquisas](https://github.com/BRVCapBlueGEM/Minhas-pesquisas)

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
