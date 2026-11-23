> **Navegação:** [Índice principal](../README.md) · [Capítulo 8](README.md) · [Ferramentas](ferramentas-oficiais.md) · [Método](metodo-de-compilacao.md) · [Diretórios](estrutura-de-diretorios.md)

---

# 🔐 8. Segurança, procedência e validação de builds próprios

## 8.1. Hipótese e limite de confiança

Compilar a partir de código-fonte oferece **mais oportunidade de inspeção e modificação controlada**, mas **não comprova ausência de comportamento malicioso**.

Um build pode executar scripts antes de gerar o binário; bibliotecas e compiladores também são software de terceiros. A análise deve abranger fonte, dependências, ferramenta de construção e comportamento do produto, não apenas o executável final.

## 8.2. Verificações por camada

| Camada | O que inspecionar | O que a verificação NÃO prova |
|--------|------------------|--------------------------------|
| **Repositório** | Autoria, site do mantenedor, releases, histórico, commits, tags, licença | Que o código é seguro por estar no GitHub |
| **Arquivo recebido** | Nome, caminho, tamanho, SHA-256, assinatura/atestado, integridade de arquivo compactado | Que conteúdo íntegro é benigno |
| **Scripts de build** | Comandos, hooks, scripts pre/post, downloads e subprocessos | Que um build bem-sucedido não executou ações indesejadas |
| **Dependências** | Lockfiles, hashes, registros, submódulos, scripts de instalação e transitivas | Que um pacote popular ou lockfile é automaticamente seguro |
| **Toolchain** | Origem, versão, compilador, linker, SDK, ambiente e permissões | Que o compilador necessariamente reproduz a semântica pretendida |
| **Artefato** | Arquivos produzidos, hash, bibliotecas vinculadas, manifestos, assinatura, importações | Que a assinatura ou a ausência de alerta equivale a segurança |
| **Execução** | Arquivos lidos/criados, processos, conexões de rede e resultados funcionais | Ausência universal de comportamentos ocultos |

## 8.3. Inspeção de URLs, domínios e endpoints

Identificar no código e nas configurações:

- Endereços de atualização, telemetria, rastreamento e relatórios de erro.
- APIs oficiais, serviços de autenticação, endpoints de licenciamento e servidores usados pelo aplicativo.
- Downloads automáticos durante o build, inclusive ferramentas auxiliares.
- Repositórios de pacotes, mirrors, submódulos e URLs transitivas.
- Permissões, credenciais, certificados, pins de segurança, armazenamento local e portas utilizadas.

**Critério:** primeiro documentar a finalidade e se o endpoint é essencial. Depois avaliar uma alternativa de configuração suportada pelo projeto. Qualquer mudança deve ocorrer em **cópia de trabalho**, com testes que demonstrem efeito e sem enfraquecer verificações de identidade e segurança.

**Não presumir que todo acesso à rede seja suspeito nem que remover todos os endpoints seja uma solução segura.**

## 8.4. Verificadores e detecções antivírus

- Um alerta do VirusTotal ou de outro mecanismo é **evidência para investigar**, não diagnóstico definitivo de trojan.
- Falsos positivos são possíveis; a quantidade de detecções isolada não determina risco.
- Verificar família da detecção, comportamento observado, procedência, assinatura, composição do arquivo e se o alerta se refere ao **payload realmente examinado**.
- Escanear somente o invólucro/arquivo compactado não equivale necessariamente à inspeção de todos os seus membros ou do comportamento em execução.
- Comparar o executável pré-compilado e o construído localmente só é conclusivo em condições documentadas; compilação não determinística pode gerar hashes diferentes em builds legítimos.
- Evitar colocar em serviços públicos arquivos privados, credenciais, documentos internos e binários cujo compartilhamento seja restrito.
- Nunca desabilitar antivírus, firewall, proteções de assinatura ou controles de segurança apenas para contornar alertas.

**Resultado correto:** confirmado, inconclusivo ou suspeito, conforme as evidências disponíveis — não rotular automaticamente como malware nem como falso positivo.

## 8.5. Cadeia de suprimentos

- Preferir releases e código obtidos de mantenedores identificáveis.
- Para cada repositório, fixar tag/commit; registrar alterações locais e submódulos.
- Se existirem checksums, assinaturas ou atestados, verificá-los **contra fonte confiável independente**.
- Conferir o tipo de arquivo distribuído: pacote de fontes gerado pelo GitHub, arquivo publicado pelo mantenedor e executável são objetos diferentes.
- Analisar pacotes transitivos e scripts que rodam na instalação (por exemplo, hooks Python, scripts npm, arquivos **build.rs** e comandos de **CMake**).
- Preferir ambiente com privilégios mínimos, isolamento e acesso de rede controlado segundo o teste.
- Registrar pacotes baixados, versões e alterações; não tratar um build que depende de rede mutável como integralmente reproduzível.

**Referências oficiais:**
- [GitHub Docs — verificação de integridade de releases](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/verify-release-integrity)
- [GitHub Docs — segurança da cadeia de suprimentos](https://docs.github.com/en/code-security/concepts/supply-chain-security/supply-chain-security)
- [npm — instalação conforme lockfile](https://docs.npmjs.com/cli/npm-ci/)

## 8.6. Critérios de aceite e evidência

Uma ficha de validação deve separar:

1. **Documentação consultada:** links abertos e data.
2. **Aquisição:** arquivo e revisão realmente obtidos.
3. **Integridade:** teste realmente executado e valor obtido.
4. **Inspeção estática:** arquivos/trechos analisados e limites.
5. **Build:** ambiente, parâmetros, resultado, logs, avisos e artefatos.
6. **Execução:** funções testadas, entradas e saídas observadas.
7. **Comportamento externo:** rede, arquivos e processos observados no escopo.
8. **Comparação:** referência original, alterações locais e diferenças justificadas.
9. **Estado final:** validado no escopo, parcialmente validado, falhou, pendente, rejeitado ou substituído.
10. **Próximo teste:** evidência necessária para superar cada pendência.

**Importante:** “validado no escopo” não significa segurança absoluta, ausência futura de vulnerabilidades nem adequação a qualquer máquina.

## 8.7. Política de operação

**Consulta documental ≠ autorização de download.**  
**Download ≠ autorização de instalação.**  
**Instalação ≠ autorização de execução.**  
**Execução ≠ autorização de conexão externa.**  
**Existência de ferramenta ≠ autorização de modificar sistemas.**

Cada operação exige escopo claro. Arquivos originais, ambientes e projetos alheios permanecem preservados. Scripts novos ou alterações de código devem ser desenvolvidos no projeto responsável por Código e Scripts, mediante briefing específico quando necessário.

## 8.8. Situação

**Estado:** referência de segurança documentada; nenhum binário ou repositório concreto foi auditado/compilado por esta pesquisa geral.  
**Pendências:** validação prática com fontes e artefatos reais, ferramentas escolhidas conforme o projeto e testes reproduzíveis.

---

[↑ Capítulo 8](README.md)