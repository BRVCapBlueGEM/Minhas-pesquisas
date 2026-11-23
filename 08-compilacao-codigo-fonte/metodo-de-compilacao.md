> **Navegação:** [Índice principal](../README.md) · [Capítulo 8](README.md) · [Ferramentas](ferramentas-oficiais.md) · [Diretórios](estrutura-de-diretorios.md) · [Segurança](seguranca-e-validacao.md)

---

# 🧩 8. Método geral de obtenção, montagem e compilação

## 8.1. Finalidade e escopo

Método documental para **qualquer projeto ou chat** interessado em compilar, empacotar ou estudar códigos-fonte disponibilizados por terceiros. A ferramenta estudada pode ser um aplicativo gráfico, biblioteca, CLI, serviço, extensão ou componente técnico.

Este método é **referência compartilhada**, não estado persistente de um projeto, não auditoria e não autorização geral para instalações.

## 8.2. Fase 0 — registrar o objetivo

Antes de selecionar aplicativos:

- Qual problema a ferramenta resolve?
- A intenção é **estudar**, **auditar**, **modificar**, **compilar**, **utilizar** ou **redistribuir**?
- Qual plataforma, versão de sistema, arquitetura, interface e recursos são necessários?
- Há fontes e versões oficiais acessíveis? Qual é a licença?
- Como será demonstrado o funcionamento?
- Quais operações de rede, arquivos, instalação e execução foram efetivamente autorizadas?

**Resultado esperado:** objetivo e critérios de aceitação, sem tratar opções de software como decisões já tomadas.

## 8.3. Fase 1 — localizar e identificar a origem

1. Localizar o site ou repositório indicado pelo mantenedor real, observando forks, mirrors, homônimos e projetos abandonados.
2. Identificar licença, mantenedores, tags/releases, notas e histórico.
3. Selecionar **uma revisão exata** (tag e SHA de commit), preferindo release estável compatível.
4. Distinguir **arquivo compactado de fontes**, **clone Git**, **submódulos**, **Git LFS**, **release asset** e **instalador pré-compilado**.
5. Registrar URLs, data de consulta, tamanho, SHA-256 recebido e assinaturas/atestados disponíveis, sem declarar verificação de hashes que não foi realizada.

**Resultado esperado:** origem e revisão identificadas; download somente mediante autorização.

## 8.4. Fase 2 — preservar o original

- Guardar o pacote ou snapshot recebido em área de **originais imutáveis no procedimento**.
- Preservar nome, URL, revisão, data e hash local quando calculado.
- Criar uma cópia de trabalho separada para inspeção e modificações.
- Para ZIP, verificar conteúdo e caminhos antes de extrair; evitar sobrescrita, arquivos com caminhos absolutos ou traversal, links inesperados e scripts não reconhecidos.
- A extração completa deve ser conferida; um ZIP íntegro não comprova que o conteúdo é seguro.

**Resultado esperado:** originais preservados e cópia de trabalho identificada.

## 8.5. Fase 3 — leitura e mapa do projeto

Examinar **README**, **INSTALL**, documentação de build e arquivos equivalentes:

- Linguagens e versões realmente exigidas.
- Sistema operacional e arquitetura declarados.
- Ferramentas de build e compiladores; toolchain/ABI.
- Dependências diretas, indiretas, de desenvolvimento e de runtime.
- Submódulos, pacotes baixados durante build, hooks e scripts.
- Arquivos de configuração, variáveis de ambiente, URLs, domínios, endpoints, portas e acessos esperados.
- Licenças do projeto e componentes de terceiros.
- Testes existentes e artefato esperado.

**Resultado esperado:** mapa de requisitos e pontos de risco; dúvida não resolvida permanece pendente.

## 8.6. Fase 4 — planejar o ambiente

1. Comparar os requisitos com o ambiente real.
2. Escolher a **menor toolchain compatível**, sem instalar indiscriminadamente todos os softwares do catálogo.
3. Evitar alterar instalações existentes, variáveis globais, registro ou componentes de terceiros sem necessidade comprovada e autorização.
4. Preferir isolamento operacional adequado (VM, ambiente temporário, usuário sem privilégios, diretório isolado), respeitando limites de segurança e compatibilidade.
5. Planejar controle de acesso à rede e registrar quais downloads de dependências serão necessários.
6. Registrar a origem e versão de cada compilador, SDK, pacote e biblioteca.

**Resultado esperado:** plano de build reproduzível, autorizado apenas dentro do escopo concedido.

## 8.7. Fase 5 — adaptar em cópia de trabalho

Quando o objetivo exigir personalização:

- Localizar a configuração **documentada** antes de alterar código hardcoded.
- Examinar scripts que mencionam URLs e serviços externos; determinar se são telemetria, atualizações, serviços essenciais, dependências ou infraestrutura de build.
- Modificar **somente** a cópia de trabalho e registrar arquivo, linha/trecho, motivo, efeito esperado e diferença.
- Não suprimir verificações de segurança, validação criptográfica, mecanismos de atualização ou conectividade essenciais apenas para conseguir compilar.
- Verificar termos de licença, marca, direitos de redistribuição e requisitos do serviço.

**Resultado esperado:** alterações rastreáveis, reversíveis e justificadas; nenhum código criado neste capítulo.

## 8.8. Fase 6 — executar o build autorizado

- Fixar versão de compilador, SDK, dependências e parâmetros.
- Usar instruções oficiais que correspondam à **revisão selecionada**, sem executar scripts cegamente.
- Registrar arquitetura (por exemplo, x64/ARM64), configuração Debug/Release e opções.
- Manter o build e os artefatos separados dos originais.
- Capturar saídas, warnings, erros e informações sobre dependências externas.
- Não considerar **build bem-sucedido** sinônimo de executável funcional ou seguro.

**Resultado esperado:** artefato de build com identificação, logs e hashes.

## 8.9. Fase 7 — verificar e validar

1. Conferir integridade dos artefatos, assinatura (se houver), componentes incluídos e diferenças em relação ao esperado.
2. Efetuar análise estática e verificações de segurança dentro do escopo autorizado.
3. Testar inicialmente em ambiente isolado e monitorar acessos a arquivos, serviços e rede quando aplicável.
4. Testar funções essenciais e tratamentos de erro; comparar os critérios da fase 0.
5. Se possível, reconstruir independentemente e comparar **com as ressalvas de builds não determinísticos**.
6. Registrar resultados, evidências, reproduções, limitações e problemas remanescentes.

**Resultado esperado:** situação classificada como *validado no escopo*, *parcial*, *falhou*, *pendente* ou *rejeitado*, com justificativa.

## 8.10. Fase 8 — documentação e reutilização

A ficha de um projeto concreto deve reunir:

| Campo | Registro necessário |
|-------|---------------------|
| Software e objetivo | Nome, finalidade, escopo do estudo |
| Fonte e autor | URL oficial, mantenedor, licença, revisão/tag/commit |
| Original | Nome, local, SHA-256, data e forma de obtenção |
| Ambiente | SO, arquitetura, toolchain, versões efetivas |
| Dependências | Lista, proveniência, lockfiles e status |
| Riscos | Scripts executáveis, rede, URLs, permissões, sinais de alerta |
| Modificações | Diferenças em relação ao original e motivação |
| Build | Processo realmente executado, logs e artefatos |
| Testes | Critérios, comandos aplicados pelo ambiente responsável, evidências e limitações |
| Estado | Confirmado / provisório / proposta não testada / falhou / rejeitado / substituído |
| Próxima ação | Etapa específica ainda necessária |

O **repositório Minhas pesquisas** guarda este método e fichas de referência. Cada contexto de aplicação mantém seus próprios registros e decisões. Quando houver transporte por auditoria, respeitar o comando e os registros do projeto de origem; um documento não se transforma automaticamente em acervo canônico.

## 8.11. Situação

**Estado documental:** método estabelecido como referência de pesquisa, não validado por uma compilação integral nesta atualização.  
**Próximo teste:** aplicar a um repositório real, etapa por etapa, sem ampliar permissões.

---

[↑ Capítulo 8](README.md)