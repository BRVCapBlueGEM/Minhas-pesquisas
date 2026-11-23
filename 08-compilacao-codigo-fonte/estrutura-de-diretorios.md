> **Navegação:** [Índice principal](../README.md) · [Capítulo 8](README.md) · [Ferramentas](ferramentas-oficiais.md) · [Método](metodo-de-compilacao.md) · [Segurança](seguranca-e-validacao.md)

---

# 📁 8. Estrutura lógica de diretórios e rastreabilidade

## 8.1. Objetivo

Propor uma **organização reutilizável** para estudos, montagens e compilações de qualquer origem ou linguagem. O modelo não pertence a um chat específico.

**Situação:** estrutura documental proposta. Não corresponde a diretórios efetivamente criados em Box, HD ou outro serviço nesta atualização.

## 8.2. Estrutura recomendada por projeto de software

    COMPILACAO_FONTES/
    └── NOME_DO_SOFTWARE/
        ├── 00_DOCUMENTACAO/
        │   ├── FICHA_TECNICA.md
        │   ├── FONTES_E_LICENCAS.md
        │   └── HISTORICO_E_DECISOES.md
        ├── 01_ORIGINAIS/
        │   └── PACOTES_E_SNAPSHOTS_RECEBIDOS/
        ├── 02_FONTES_TRABALHO/
        │   └── COPIA_DE_TRABALHO/
        ├── 03_DEPENDENCIAS/
        │   └── INVENTARIO_E_FONTES/
        ├── 04_CONFIGURACAO_BUILD/
        ├── 05_COMPILACAO/
        │   ├── DEBUG/
        │   └── RELEASE/
        ├── 06_ARTEFATOS_GERADOS/
        ├── 07_TESTES/
        ├── 08_RELATORIOS_E_LOGS/
        └── 09_RESULTADOS_VALIDADOS/

**Nota:** nomes são propostos, não diretórios já existentes. Não é necessário criar pastas vazias sem utilização. O modelo admite variações justificadas para projetos com submódulos, monorepos, container de desenvolvimento, vários alvos e builds multiplataforma.

## 8.3. Função e integridade de cada área

| Diretório | Finalidade | Regra |
|-----------|------------|-------|
| **00_DOCUMENTACAO** | Objetivo, fontes, licenças, decisões, versões, estados | Rastreabilidade legível |
| **01_ORIGINAIS** | Arquivos recebidos sem modificação intencional | Não editar nem sobrescrever |
| **02_FONTES_TRABALHO** | Cópia inspecionada, configuração e alterações controladas | Sempre diferenciar dos originais |
| **03_DEPENDENCIAS** | Registro de pacotes, versões, origem e hashes | Não presumir que todo cache é confiável |
| **04_CONFIGURACAO_BUILD** | Configurações e parâmetros específicos da montagem | Preservar alterações e versões |
| **05_COMPILACAO** | Saídas intermediárias das diferentes configurações | Separar Debug, Release e alvos |
| **06_ARTEFATOS_GERADOS** | Programas, bibliotecas e pacotes resultantes | Não marcar como aprovados automaticamente |
| **07_TESTES** | Evidências de comportamento observado | Registrar ambiente e resultado |
| **08_RELATORIOS_E_LOGS** | Erros, inventários, análises, hashes e inspeções | Não apagar falhas para mostrar só sucessos |
| **09_RESULTADOS_VALIDADOS** | Artefatos com critérios de validação documentados | Só ingressam após comprovação definida |

## 8.4. Separação entre repositório, nuvem e HD

- **GitHub / Minhas pesquisas:** repositório **documental transversal**; índice, fichas, links oficiais, método e exemplos confirmados. Não é depósito automático de binários, pacotes ou senhas.
- **Box:** possível armazenamento de originais, cópias de trabalho e resultados, mediante decisão de localização, capacidade, permissões e verificação de pastas existentes. **Nenhuma pasta Box foi criada por este documento.**
- **HD local:** local de compilação quando o projeto e o usuário escolherem e autorizarem; caminho, unidade e ferramentas reais precisam ser conferidos.
- **Google Drive:** mantém auditorias e demais documentos conforme seu fluxo próprio; não recebe automaticamente todos os binários ou cópias integrais.
- **BitBiblioteca:** consulta e organização canônica sob governança própria; não se converte no local de trabalho de builds.

**Compartilhar documentação entre projetos não transfere identidade, estado persistente, autoridade ou governança.**

## 8.5. Padrão mínimo de identificação de um original

Registrar em documentação:

| Campo | Exemplo de natureza do dado |
|-------|-----------------------------|
| Projeto de origem | Nome e URL oficial |
| Revisão | Tag e SHA de commit, quando disponíveis |
| Arquivo | Nome exato e formato |
| Proveniência | Download/clone, página usada, mantenedor |
| Data | Consulta, recebimento e validação, separadamente |
| Integridade | SHA-256 do arquivo local; assinatura/atestado se disponível |
| Licença | Projeto e componentes externos |
| Estado | Recebido / conferido / pendente |
| Relação | Local da cópia de trabalho e dos resultados |

**Não inventar** caminho, SHA, data de aquisição ou arquivo que ainda não existe.

## 8.6. Critério de não sobreposição

A área de originais é fonte de preservação. A de trabalho é modificável conforme escopo. A de build é descartável/derivada, mas a exclusão real só ocorre com autorização. A área validada jamais deve receber automaticamente toda saída de compilação.

Não mover, apagar ou reorganizar material existente em outros projetos por inferência deste modelo. A efetiva estrutura no Box deve ser precedida por conferência da árvore existente, escolha do destino e criação estritamente autorizada.

## 8.7. Estado

**Proposta documental:** confirmada como modelo escrito.  
**Criação de pastas na nuvem ou no HD:** não realizada.  
**Validação por projeto real:** pendente.

---

[↑ Capítulo 8](README.md)