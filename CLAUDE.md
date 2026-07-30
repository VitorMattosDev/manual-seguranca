# CLAUDE.md — Manual de Segurança da Informação

Instruções de trabalho para o Claude Code neste repositório.

## O que é este projeto

Livro Quarto (HTML + PDF) em português do Brasil, publicado no GitHub Pages via GitHub Actions. **107 capítulos, 16 volumes, 5 fases.** A fila autoritativa está no `ROADMAP.md`. A estrutura canônica vive em `scripts/estrutura.py` — qualquer mudança de capítulos começa por lá.

## Modo de execução

Execução autônoma. Você está pré-aprovado para criar e editar arquivos, gerar figuras, rodar comandos de validação e fazer commits sem pedir confirmação a cada passo. **Única condição de parada:** erro real de bloqueio.

Um capítulo por sessão. `/clear` entre capítulos, `/compact` perto de 80% de contexto.

## Bootstrap da toolchain (rodar se ainda não foi rodado)

Faça isso antes do primeiro `quarto preview`, sem esperar ser pedido:

```bash
quarto install tinytex
# tlmgr pode não estar no PATH — localizar sem -type f (são symlinks)
TLMGR="$(command -v tlmgr || find "$HOME" -name tlmgr | head -n1)"
"$TLMGR" update --self
"$TLMGR" install standalone pgf pgfplots dvisvgm xcolor amsmath amsfonts fvextra koma-script
```

E **prepend do bin do TinyTeX no PATH da sessão** — este é o motivo mais comum de figura TikZ não renderizar (falha em `tikz.lua`, `imgdata nil`, ~linha 587). Não é pacote faltando, é PATH:

- Windows: `$HOME/AppData/Roaming/TinyTeX/bin/windows`
- Linux/macOS: `~/.TinyTeX/bin/<plataforma>`

## Anatomia de um capítulo

````markdown
# Título do capítulo {#sec-capNNN}

Parágrafo de abertura situando o problema concreto — nunca começar com definição de dicionário.

## Seções de conteúdo

Texto explicativo, exemplos, diagramas TikZ, blocos de código comentados.

## ⚖️ Brasil em Foco

Conexão com legislação e instituições brasileiras (LGPD/ANPD, Marco Civil,
Lei 12.737, Anatel, CERT.br, Banco Central/Pix). OBRIGATÓRIA em todo capítulo.

## 🛠️ No Campo

Tradução para a operação real de infraestrutura — o que muda no dia a dia de
quem administra rede, servidores e clientes. OBRIGATÓRIA em todo capítulo.

## Resumo

3 a 6 bullets com o essencial.
````

Alvo: 2.500–4.000 palavras por capítulo. Densidade acima de volume.

## Política editorial (inegociável)

Material educacional com orientação defensiva. Técnicas ofensivas existem para que o leitor entenda, detecte e mitigue.

**Pode:** explicar mecanismos de ataque em profundidade, usar ferramentas públicas e consagradas em contexto de laboratório, mostrar trechos de código vulnerável para ensinar a corrigi-lo, reproduzir payloads didáticos clássicos e inofensivos (ex.: `' OR '1'='1`), analisar casos públicos.

**Não pode:** exploits armados ou prontos para uso, código de malware funcional, técnicas de evasão de EDR operacionalizadas, instruções passo a passo contra alvos reais, nada que dê vantagem prática a quem não tem autorização.

Regra prática: se o trecho encurta o caminho de alguém para atacar um sistema de terceiros, ele sai. Toda técnica ofensiva vem acompanhada da contramedida.

## Figuras

TikZ para diagramas esquemáticos e didáticos (fluxos de protocolo, topologias, cadeias de confiança, máquinas de estado). SVG/PNG embutido para o que depender de captura de tela ou fotografia.

- Extensão: `_extensions/danmackinlay/tikz/` com **patches locais**
- **NUNCA rodar `quarto add` ou `quarto update`** nessa extensão — baixa o upstream sem os patches e quebra tudo
- Filtro `tikz` vem **antes** de `quarto` na lista de filters
- O template sempre chama `\usepackage{pgfplots}` — todo figura precisa dele, mesmo uma seta simples
- Estilos predefinidos (`curva`, `destaque`, `auxiliar`, `eixo`, `ponto`, `vetor`; cores `manualblue`, `manualred`, `manualgreen`, `manualyellow`, `manualgray`) vêm do template: **usar direto, nunca redefinir**

Sintaxe:

````markdown
::: {#fig-handshake-tls}
```{.tikz}
%%| filename: handshake-tls
%%| alt: Diagrama do handshake TLS 1.3 entre cliente e servidor
\begin{tikzpicture}
  ...
\end{tikzpicture}
```
Handshake TLS 1.3 em suas quatro trocas de mensagem.
:::
````

Referência no texto via `@fig-handshake-tls`.

## Regras que já custaram build vermelho

- **Stub-first**: em projeto `book`, renderizar um `.qmd` isolado falha com "Book chapter not found" se qualquer capítulo listado no `_quarto.yml` não existir em disco. Rodar `python scripts/estrutura.py --stubs` após qualquer mudança de estrutura.
- **`--roadmap` e `--tudo` regravam o `ROADMAP.md` inteiro.** O `scripts/estrutura.py` hoje **preserva** os marcadores `[x]` e `[~]` (função `status_atuais`, que relê o arquivo antes de reescrever) — mas essa proteção é frágil por natureza: se o formato da linha (`- [x] **cap NNN**`) mudar, o regex para de casar e todo capítulo concluído volta a `[ ]` sem aviso. Não alterar o formato dessa linha, e conferir a contagem que o script imprime (`N concluidos preservados`) sempre que rodar. Na dúvida, usar só `--stubs`.
- **`quarto render --to pdf` limpa o `_book/`** e deixa apenas o PDF. As checagens de `?@`, de `<svg` e de `[?]` são feitas no HTML, então a ordem é sempre: render HTML → validar → render PDF. Invertido, o grep não acha os arquivos e o silêncio parece aprovação.
- **`execute: echo: true` vaza o fonte das células de diagrama.** Um bloco `{mermaid}` sai na página duas vezes: como `<pre class="sourceCode">` com botão de copiar (o vazamento) e como `<pre class="mermaid">` (o diagrama de verdade). Toda célula `{mermaid}` precisa de `%%| echo: false`. Blocos cercados estáticos (```` ```bash ````) não são células e não sofrem disso.
- **Crossrefs**: `@sec-`, `@fig-` e `@tbl-` **só** para o que já foi escrito (mesmo volume ou anterior). Referência a capítulo futuro é menção textual ("tema do Volume 12"), nunca link. Label não resolvido vira `?@sec-x` em vermelho no HTML e no PDF.
- **`lang: pt`** fica na raiz do `_quarto.yml`, não aninhado sob `book:`.
- **`styles.css`** precisa de `/*-- scss:rules --*/` na primeira linha (está listado em `theme:`). Evitar `*/` logo após o marcador.
- **Notação LaTeX**: usar `^{*}` e não `^\*` — quebra o PDF.
- **Substituição em massa** de notação LaTeX (`\`, `*`, `^`): usar `str.replace` do Python. Nunca `sed` (corrompe superscritos) nem `grep -c` (contagem enganosa).
- **Commits**: apenas `-m "..."` simples. Nada de here-string do PowerShell (`@'...'@`) dentro do Bash — o `@` vaza para a mensagem.
- **Emoji em `print()`** de script Python quebra no console do Windows. Em conteúdo de arquivo UTF-8 é seguro.
- **Write após heredoc**: se um arquivo foi modificado por bash/heredoc, a ferramenta Write exige um Read antes. Fazer um Read rápido depois de qualquer modificação externa.
- **Avisos inofensivos**: `LF will be replaced by CRLF` e "Node.js 20 is deprecated" — ignorar, nunca investigar.

## Validação antes de cada commit

Ordem obrigatória: **HTML primeiro, validar, PDF por último** — `--to pdf` apaga o HTML do `_book/`.

```bash
quarto render --to html
# 1. figuras: contar <svg no HTML gerado vs {.tikz} no .qmd
# 2. crossrefs quebrados — precisa retornar zero:
grep -rhoE '\?@[a-z-]+' _book/**/*.html
# 3. citações órfãs: procurar [?] no HTML
# 4. fonte de diagrama vazado: nenhum <pre class="sourceCode"> com o corpo
#    de um bloco {mermaid} (sintoma de célula sem `%%| echo: false`)
# 5. PDF local antes de qualquer push (LaTeX quebra no que o HTML aceita).
#    Este passo destrói o HTML acima, então roda só depois de 1–4:
quarto render --to pdf
```

Para conferir se uma figura TikZ entrou no PDF, contar Form XObjects por página com `pypdf` — `pdftotext` não recupera texto acentuado dos rótulos e dá falso negativo.

Commit no formato `cap NNN: <título>`, com o status do `ROADMAP.md` atualizado no mesmo commit.

## Validação antes do push

1. Render HTML completo do livro
2. Zero `?@` no grep
3. Todas as figuras TikZ produziram SVG
4. Nenhuma citação `@chave` crua sobrando no HTML
5. Após o push: `gh run watch <id> --exit-status` e depois `curl -I` na URL do Pages esperando 200

## Estratégia de produção

Fatia vertical: fechar um volume inteiro antes de abrir o próximo; fechar a Fase 1 antes da Fase 2. Em volume novo, o primeiro passo é o smoke test — validar que **uma** figura TikZ renderiza para SVG no HTML antes de escrever capítulo a capítulo.

`/model opus` para escrever capítulo. `/model sonnet` para tarefa mecânica (atualizar `_quarto.yml`, mover arquivo, ajustar ROADMAP).
