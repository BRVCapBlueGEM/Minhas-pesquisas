> **Navegação:** [Índice principal](../README.md) · [Capítulo 8](README.md) · [Método](metodo-de-compilacao.md) · [Diretórios](estrutura-de-diretorios.md) · [Segurança](seguranca-e-validacao.md)

---

# 🔧 8. Ferramentas de compilação — fichas e downloads oficiais

## 8.1. Objetivo

Identificar **fontes mantidas pelos desenvolvedores**, canais de distribuição oficiais e papéis técnicos das principais ferramentas usadas para obter e montar projetos a partir do código-fonte.

**Não é uma lista de aplicativos que todos precisam instalar.** A escolha depende da linguagem, do arquivo de projeto, do sistema de destino e da toolchain exigida. Não se confundem compiladores, geradores de build, IDEs, runtimes e gerenciadores de pacotes.

Os links conduzem a páginas estáveis de download, releases ou instruções do mantenedor; **não são links diretos para executáveis escolhidos sem conferir a versão, a arquitetura e a licença**.

## 8.2. Ferramentas de obtenção e construção nativa

### Git — histórico e obtenção das fontes

- **Tipo:** sistema de controle de versões, não compilador.
- **Desenvolvimento:** comunidade Git; mantenedor e contribuidores do projeto Git.
- **Finalidade e funcionamento:** obter revisões, acompanhar alterações e fixar a identidade do código por commit/tag.
- **Linguagem predominante:** C, com scripts e componentes auxiliares.
- **Licença:** GPL v2, com exceções e licenças de arquivos conforme o projeto.
- **Sistemas:** Windows, Linux, macOS e outros, conforme distribuição.
- **Site/download oficial:** https://git-scm.com/downloads
- **Código-fonte e instruções oficiais:** https://git-scm.com/install/source
- **Repositório de fontes:** https://github.com/git/git
- **Dependências:** a compilação do próprio Git possui requisitos distintos dos de sua utilização; conferir documentação.
- **Limite:** obter um commit não garante que dependências externas foram fixadas ou auditadas.

### Microsoft C++ Build Tools / MSVC — compilação Windows

- **Tipo:** conjunto proprietário de compilador, linker, bibliotecas, SDKs e ferramentas de build.
- **Desenvolvedor:** Microsoft.
- **Finalidade:** compilar projetos C/C++ orientados à toolchain MSVC, inclusive projetos Visual Studio/MSBuild e CMake que a utilizam.
- **Linguagens:** C e C++ (com ferramentas adicionais conforme componentes).
- **Licença:** proprietária; conferir os termos aplicáveis à modalidade de uso.
- **Sistema:** Windows, conforme versões e componentes suportados.
- **Download oficial:** https://visualstudio.microsoft.com/downloads/
- **Documentação de aquisição:** https://learn.microsoft.com/en-us/cpp/overview/acquire-msvc
- **Documentação de build:** https://learn.microsoft.com/en-us/cpp/build/building-on-the-command-line
- **Dependências:** compilador, Windows SDK, toolset e workload devem corresponder ao projeto.
- **Limite:** uma instalação do Build Tools não cria compatibilidade automática com MinGW, outra ABI ou qualquer projeto C++.

### LLVM / Clang — toolchain de compilação

- **Tipo:** infraestrutura de compilação e otimização; Clang é frontend para C/C++ e outras linguagens conforme componentes.
- **Desenvolvimento:** LLVM Project e contribuidores.
- **Licença:** Apache 2.0 com LLVM Exceptions; componentes devem ser conferidos.
- **Sistemas:** Windows, Linux, macOS e outros alvos suportados, conforme distribuição.
- **Download oficial:** https://releases.llvm.org/
- **Página do projeto:** https://llvm.org/
- **Fontes e releases oficiais:** https://github.com/llvm/llvm-project/releases
- **Dependências:** linker, SDK, biblioteca padrão, target e runtime precisam ser compatíveis.
- **Limite:** Clang/LLVM não é sinônimo de ambiente Windows completo; o projeto pode exigir MSVC, MinGW ou SDK específico.

### MSYS2 — ambiente GNU no Windows

- **Tipo:** distribuição e ambiente de desenvolvimento com gerenciador de pacotes.
- **Desenvolvimento:** projeto MSYS2 e mantenedores de pacotes.
- **Linguagens:** múltiplas; fornece compiladores e bibliotecas, não é um único compilador.
- **Licença:** varia por componente e pacote.
- **Sistema:** Windows.
- **Download e documentação oficial:** https://www.msys2.org/
- **Instalador e critérios oficiais:** https://www.msys2.org/docs/installer/
- **Gerenciamento de pacotes:** https://www.msys2.org/docs/package-management/
- **Limite:** UCRT64, MINGW64, CLANG64 e outros ambientes não devem ser misturados sem revisar ABI, bibliotecas e configuração. Instalação/atualização de pacotes requer autorização específica.

### CMake — configuração/geração de builds

- **Tipo:** ferramenta de configuração e geração de sistemas de build; **não é compilador**.
- **Desenvolvedor:** Kitware e contribuidores.
- **Linguagem principal:** C++.
- **Licença:** BSD de 3 cláusulas, com licenças específicas de componentes.
- **Sistemas:** Windows, Linux e macOS.
- **Download oficial:** https://cmake.org/download/
- **Documentação:** https://cmake.org/documentation/
- **Fontes/releases:** https://github.com/Kitware/CMake
- **Dependências:** requer compilador e gerador compatíveis para construir o projeto de destino.
- **Limite:** a presença de **CMakeLists.txt** não define sozinha quais bibliotecas externas devem ser obtidas.

### Ninja — executor de builds

- **Tipo:** sistema de build pequeno e rápido; não é compilador.
- **Desenvolvimento:** projeto Ninja e contribuidores.
- **Linguagem:** C++.
- **Licença:** Apache 2.0.
- **Sistemas:** Windows, Linux e macOS.
- **Projeto/download e fontes:** https://github.com/ninja-build/ninja/releases
- **Site/documentação:** https://ninja-build.org/
- **Manual:** https://ninja-build.org/manual.html
- **Dependências:** necessita regras de build e toolchain definida; normalmente recebe arquivos gerados por CMake/Meson.
- **Limite:** Ninja sozinho não resolve dependências nem transforma qualquer repositório em executável.

### Meson — configuração de builds

- **Tipo:** sistema de configuração de builds, com frequência usado com Ninja.
- **Desenvolvimento:** Meson Build Project.
- **Linguagem:** Python.
- **Licença:** Apache 2.0.
- **Sistemas:** Windows, Linux e macOS.
- **Página oficial de obtenção:** https://mesonbuild.com/Getting-meson
- **Guia oficial:** https://mesonbuild.com/Quick-guide.html
- **Código-fonte:** https://github.com/mesonbuild/meson
- **Dependências:** Python ou pacote distribuído, além do compilador e executor de build exigidos.
- **Limite:** escolher somente quando o projeto usar Meson ou fornecer instruções compatíveis.

## 8.3. Linguagens, SDKs e ferramentas de ecossistema

| Ferramenta | Papel / linguagem | Desenvolvedor / licença principal | Sistemas e dependências | Download e documentação oficiais |
|-----------|-------------------|-----------------------------------|-------------------------|----------------------------------|
| **Python** | Interpretador e ambiente para pacotes/extensões; C/C++ quando há módulos nativos | Python Software Foundation; licença PSF e componentes | Windows, Linux, macOS; compatibilidade de versão/arquitetura deve ser verificada | [Python Windows](https://www.python.org/downloads/windows/) · [Documentação](https://docs.python.org/3/) · [Fontes](https://github.com/python/cpython) |
| **Node.js + npm** | Runtime JavaScript; ferramenta de build/empacotamento de projetos JS/TS | Node.js/OpenJS e contribuidores; licenças conforme distribuição e dependências | Windows, Linux, macOS; módulos nativos podem exigir C/C++ e SDKs | [Download oficial](https://nodejs.org/en/download/) · [Documentação](https://nodejs.org/en/docs/) · [Fontes](https://github.com/nodejs/node) |
| **Rust / rustup / Cargo** | Compilador e gerenciador de projetos/dependências Rust | Rust Project; Apache 2.0/MIT e licenças por componente | Windows, Linux, macOS; target MSVC/GNU e linkers dependem do projeto | [Instalação oficial](https://rust-lang.org/install) · [Cargo](https://doc.rust-lang.org/cargo/) · [Fonte do rustup](https://github.com/rust-lang/rustup) |
| **Go** | Compilador/toolchain e módulos Go | Go Project; licença BSD de 3 cláusulas para grande parte do projeto | Windows, Linux, macOS; cgo requer compilador C adequado | [Distribuições oficiais](https://go.dev/dl/) · [Documentação](https://go.dev/doc/) · [Fontes](https://go.googlesource.com/go) |
| **.NET SDK** | Compilação, build e execução de projetos .NET (C#, F# etc.) | Microsoft e comunidade; licenças de componentes devem ser verificadas | Windows, Linux, macOS; target framework e workloads específicos | [Download SDK](https://dotnet.microsoft.com/en-us/download/dotnet) · [Documentação](https://learn.microsoft.com/en-us/dotnet/) · [Fontes](https://github.com/dotnet) |
| **Eclipse Temurin JDK** | Compilação/execução Java e ferramentas do ecossistema JVM | Eclipse Adoptium; GPL v2 com Classpath Exception para OpenJDK e licenças de componentes | Windows, Linux, macOS; selecionar JDK/arquitetura e ferramenta Maven/Gradle conforme projeto | [Downloads oficiais](https://adoptium.net/temurin/releases/) · [Projeto](https://adoptium.net/) · [Fontes](https://github.com/adoptium) |

**Importante:** uma ferramenta de compilação nem sempre é necessária para executar o programa; versões de desenvolvimento e runtime são requisitos diferentes. Conferir sempre as licenças efetivamente incluídas no pacote e as notas da versão selecionada.

## 8.4. Gerenciamento de bibliotecas e dependências

| Ferramenta | Finalidade | Origem e documentação oficiais | Limite de uso |
|-----------|------------|-------------------------------|---------------|
| **vcpkg** | Gerência de bibliotecas C/C++; integrações com CMake/MSBuild | https://github.com/microsoft/vcpkg · https://learn.microsoft.com/en-us/vcpkg/ | Resolver pacotes pode iniciar downloads e builds de terceiros |
| **Conan 2** | Dependências C/C++ com perfis de compilação e pacotes | https://conan.io/downloads · https://docs.conan.io/2/ | Perfis, remotes e receitas requerem inspeção |
| **npm** | Dependências Node/JavaScript | https://docs.npmjs.com/ · https://docs.npmjs.com/cli/npm-ci/ | Scripts de ciclo de vida de pacotes podem executar comandos; lockfile não dispensa auditoria |
| **pip / PyPI** | Pacotes e dependências Python | https://pip.pypa.io/en/stable/ · https://pypi.org/ | PyPI é registro de pacotes; cada pacote precisa de avaliação de autoria, integridade e requisitos |

## 8.5. Identificar o fluxo a partir dos arquivos

| Indício no repositório | Fluxo provável | Verificação indispensável |
|------------------------|----------------|---------------------------|
| **CMakeLists.txt** | CMake + gerador + compilador | Toolchain, opções e dependências |
| **meson.build** | Meson, normalmente Ninja | Versão do Meson, backend, compilador |
| **.sln / .vcxproj** | Visual Studio / MSBuild / MSVC | Toolset, SDK, arquitetura e configuração |
| **Makefile / configure** | Make e, às vezes, Autotools/GNU | Ambiente suportado; scripts de configuração |
| **Cargo.toml / Cargo.lock** | Rust / Cargo | Toolchain, target, crates, build.rs |
| **go.mod / go.sum** | Go / módulos | Versão do Go, módulos, cgo |
| **pyproject.toml / setup.py** | Python / empacotamento | Backend, versão Python, extensões nativas, hooks |
| **package.json / lockfile** | Node/npm ou outro gerenciador | Scripts npm, gerenciador escolhido, dependências |
| **.csproj / .fsproj** | .NET SDK / MSBuild | SDK, TargetFramework, workloads |
| **pom.xml / build.gradle** | Maven/Gradle (Java/Kotlin) | JDK, plugins, repositórios de dependências |

**Indício não é diagnóstico completo.** Algumas ferramentas coexistem no mesmo repositório.

## 8.6. Estado de verificação

**Revisão:** 23/11/2026.  
**Confirmado:** páginas de referência e download dos mantenedores principais localizadas; funcionalidades gerais documentadas.  
**Não verificado:** versão estável específica exigida por qualquer repositório futuro, licenças de todas as dependências, assinatura/hash de arquivos baixados, compatibilidade no ambiente do usuário e compilação prática.  
**Próxima ação:** para cada projeto concreto, registrar quais ferramentas são de fato necessárias e a versão/arquitetura compatível antes de qualquer instalação.

---

[↑ Capítulo 8](README.md)