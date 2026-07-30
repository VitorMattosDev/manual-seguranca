# LIÇÕES — Produção dos Manuais

Compilado de erros que já custaram build vermelho. Todo manual novo nasce com este arquivo.

## CI / GitHub Actions

### Mermaid trava o PDF
O grafo mermaid do `index.qmd` bloqueia o render de PDF no runner Ubuntu (sem Chromium headless). Adicionar **antes** do render/publish:

```yaml
- run: quarto install chrome-headless-shell
```

A ferramenta é `chrome-headless-shell`, não `chromium`.

### Branch gh-pages precisa existir
`quarto-actions/publish@v2` aborta se `gh-pages` não existir no remoto. Uma vez, antes do primeiro push:

```bash
git push origin $(git commit-tree $(git hash-object -t tree /dev/null) -m 'init gh-pages'):refs/heads/gh-pages
```

### Passo "Preparar TeX" — versão definitiva
Quatro builds vermelhos no Manual de Economia identificaram quatro causas distintas:

1. `tlmgr` do TeX Live 2026 **aborta silenciosamente** qualquer `tlmgr install` enquanto `tlmgr update --self` não rodar. Sempre `update --self` primeiro.
2. **Nunca** mascarar o install com `|| true` — esconde a falha e o erro só aparece no render.
3. Binários do TinyTeX são **symlinks**. Detectar com `command -v pdflatex` ou `find` **sem** `-type f`. Com `-type f` o resultado é vazio e `TEXBIN` vira `.`.
4. Exportar o diretório com `echo "$TEXBIN" >> "$GITHUB_PATH"` **e** criar symlinks de fallback em `/usr/local/bin` para `pdflatex`, `latex`, `dvisvgm`, `kpsewhich`.

Fechar com verificações que falham alto: `kpsewhich standalone.cls`, `kpsewhich pgfplots.sty`, `dvisvgm --version`.

YAML de referência: ver `.github/workflows/publish.yml` deste repositório.

## Quarto

- **`styles.css` em `theme:`** → Quarto ≥1.9 trata como camada SCSS e exige `/*-- scss:rules --*/` na primeira linha. Sem isso o render inteiro falha com "doesn't contain at least one layer boundary". Cuidado com `*/` logo após o marcador.
- **Stub-first**: em projeto `book`, `quarto render arquivo.qmd` isolado falha com "Book chapter not found" se qualquer capítulo do `_quarto.yml` não existir em disco. Registrou um `part:`? Cria os stubs na hora.
- **Gerador de ROADMAP tem de preservar status.** Um script que regrava o `ROADMAP.md` a partir da estrutura canônica zera todo `[x]` se não reler os marcadores antes. Não é build vermelho, é pior: apaga silenciosamente a fila de produção e o próximo capítulo é reescrito por cima. Corrigido em `scripts/estrutura.py` (`status_atuais`), que imprime quantos concluídos preservou — conferir esse número.
- **`quarto render --to pdf` limpa o diretório de saída** e deixa só o PDF. Toda validação que faz grep no HTML (`?@`, `<svg`, `[?]`) tem de rodar antes do PDF. Se rodar depois, o grep não acha arquivo e o resultado vazio passa por aprovação.
- **`execute: echo: true` vaza o fonte de células de diagrama.** Um bloco `{mermaid}` é emitido duas vezes: `<pre class="sourceCode">` com botão de copiar (o vazamento visível na página) e `<pre class="mermaid">` (o diagrama). Toda célula `{mermaid}` precisa de `%%| echo: false`. Blocos cercados estáticos não são afetados.
- **Crossrefs**: `@sec-`/`@fig-`/`@tbl-` só para o que já existe. Futuro é menção textual. Label não resolvido vira `?@sec-x` em vermelho.
- **`lang: pt`** na raiz do `_quarto.yml`, nunca sob `book:`.
- **Notação**: `^{*}`, não `^\*` — quebra o PDF.
- **Química**: `\ce{...}` (mhchem) funciona em HTML e PDF. Evitar `siunitx` (só PDF, quebra MathJax) e o pacote `physics`.

## TikZ

- Extensão `danmackinlay/tikz` com **patches locais** (`figuras-tikz-kit.zip` / `FIGURAS.md`). **Nunca** `quarto add` ou `quarto update` — baixa o upstream sem patches.
- Filtro `tikz` **antes** de `quarto` na lista de filters; `tikz: svg-engine: dvisvgm`.
- O template sempre chama `\usepackage{pgfplots}` — toda figura depende dele, mesmo uma seta.
- Estilos e cores predefinidos vêm do template: usar direto, nunca redefinir.
- **`\\` dentro de grupo `{...}` aninhado no texto de um nó quebra a figura inteira.** Com `align=center`, o TikZ implementa `\\` como fim de linha do alinhamento; dentro de um grupo extra isso desbalanceia o grupo e o erro sai como `Undefined control sequence` em `\tikz@finish@orig ...=\tikzscope@linewidth`, seguido de `I do not know the key '/tikz/<estilo>'` nos nós seguintes — sintomas que não apontam para a causa. O SVG sai vazio (~220 bytes no HTML) e o render **não** falha alto. Regra: quebra de linha só no nível superior do texto do nó. Trocar `{\bfseries\color{x}Título}\\...` por `\textbf{\textcolor{x}{Título}}\\...`, e usar `\scriptsize\color{y}` como chave (switch) em vez de `{\scriptsize\color{y}...}` quando houver `\\` depois.
- **Conferir tamanho do SVG, não só a ausência de erro.** `grep -c '<svg'` conta figura quebrada como figura boa. Medir cada bloco `<svg>...</svg>`: abaixo de ~1 KB é figura vazia.
- **Bloqueio mais comum é PATH, não pacote faltando.** `quarto install tinytex` não adiciona o bin ao PATH da sessão. Sintoma: figura não renderiza e `tikz.lua` falha com `imgdata nil` (~linha 587). Prepend do bin do TinyTeX antes de qualquer render.
- Pacotes: `tlmgr install standalone pgf pgfplots dvisvgm xcolor amsmath amsfonts`

## Windows / Claude Code

- **`tlmgr` no Git Bash é `tlmgr.bat`.** `command -v tlmgr` e `tlmgr install ...` falham com *command not found*, porque o Bash não resolve `.bat` pelo PATH sem a extensão. Chamar pelo caminho completo: `"$HOME/AppData/Roaming/TinyTeX/bin/windows/tlmgr.bat" install ...`. O `find` acha (`-name 'tlmgr*'`), o `command -v` não. Nada a ver com o PATH estar errado.
- **`quarto install chrome-headless-shell` travando** quando a ferramenta já está instalada e só há atualização disponível. Checar antes com `quarto list tools`: se aparece "Update available", já dá para renderizar — não esperar o install.
- **PDF via `pdftotext` não recupera acentos** das figuras TikZ (glifos compostos no encoding padrão). Para conferir se a figura entrou no PDF, contar Form XObjects por página com `pypdf` em vez de procurar o texto do rótulo.
- Commits com `-m "..."` simples. Here-string do PowerShell (`@'...'@`) dentro do Bash vaza o `@` para a mensagem e exige `--amend`.
- Emoji em `print()` de Python quebra no console do Windows. Em conteúdo de arquivo UTF-8 é seguro.
- Substituição em massa de LaTeX (`\`, `*`, `^`): `str.replace` do Python. `sed` corrompe superscritos, `grep -c` dá contagem enganosa.
- Write após heredoc exige Read antes ("File has not been read yet").
- Ignorar sempre: `LF will be replaced by CRLF` e "Node.js 20 is deprecated".

## Processo

- Fatia vertical: fechar volume antes de abrir o próximo; fase antes da próxima fase.
- Um capítulo por sessão, `/clear` entre capítulos, `/compact` perto de 80%.
- `/model opus` para escrever; `/model sonnet` para tarefa mecânica.
- `ROADMAP.md` é a fila autoritativa. Commit `cap NNN: <título>` com status atualizado junto.
- Volume novo começa com smoke test de uma figura TikZ antes do primeiro capítulo.
- CSL ABNT: `raw.githubusercontent.com/citation-style-language/styles/master/associacao-brasileira-de-normas-tecnicas.csl`
