> **Navegação:** [Índice principal](../README.md) · [Catálogo Minhas pesquisas](https://github.com/BRVCapBlueGEM/Minhas-pesquisas)

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
