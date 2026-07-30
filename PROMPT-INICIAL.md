# Prompt de abertura — primeira sessão no Claude Code

Cole o texto abaixo na primeira sessão, dentro da pasta do repositório.

---

Você vai trabalhar no **Manual de Segurança da Informação**, um livro Quarto em português do Brasil. Leia `CLAUDE.md`, `LICOES-MANUAIS.md`, `FIGURAS.md` e `ROADMAP.md` antes de qualquer coisa — eles contêm as convenções e os erros já pagos em builds vermelhos de outros manuais.

Modo autônomo: você está pré-aprovado para criar e editar arquivos, gerar figuras, rodar validações e fazer commits sem me consultar a cada passo. Só pare em erro real de bloqueio.

**Tarefa desta sessão, em ordem:**

1. **Bootstrap da toolchain.** Instale TinyTeX e os pacotes LaTeX e instale o `chrome-headless-shell`. Localize o `tlmgr` com `find` sem `-type f` se ele não estiver no PATH, e rode `tlmgr update --self` antes de qualquer `install`. Faça o prepend do bin do TinyTeX no PATH da sessão — sem isso as figuras TikZ falham em silêncio.

2. **CSL da ABNT.** Baixe o arquivo de estilo de citação na raiz do repositório:

   ```bash
   curl -fsSL -o associacao-brasileira-de-normas-tecnicas.csl \
     https://raw.githubusercontent.com/citation-style-language/styles/master/associacao-brasileira-de-normas-tecnicas.csl
   ```

   Confirme que o download veio íntegro antes de seguir — se o servidor devolver uma página de erro, o Quarto só reclama na hora do render:

   ```bash
   head -n 3 associacao-brasileira-de-normas-tecnicas.csl   # deve começar com <?xml
   grep -c "<style" associacao-brasileira-de-normas-tecnicas.csl
   ```

   O `_quarto.yml` já aponta para esse nome de arquivo em `csl:`. Se o download falhar (rede, URL movida), me avise em vez de trocar o `csl:` por outro estilo ou removê-lo.

3. **Extensão TikZ.** Copie `_extensions/danmackinlay/tikz/` do `figuras-tikz-kit.zip` (vou deixar o zip na raiz). Não rode `quarto add` nem `quarto update` nessa extensão em hipótese alguma.

4. **Stubs.** Rode `python scripts/estrutura.py --tudo` e confirme que os 107 stubs existem em disco. Renderizar sem eles falha com "Book chapter not found".

5. **Smoke test.** Antes de escrever qualquer conteúdo, crie uma figura TikZ mínima em `vol01/cap001-*.qmd` e rode `quarto render --to html`. Confirme que ela virou `<svg` no HTML gerado. Se não virou, o problema é PATH — resolva antes de seguir. Depois rode `quarto render --to pdf` e confirme que o PDF sai.

6. **Bootstrap do gh-pages.** Rode o comando de `commit-tree` do README para criar o branch vazio no remoto.

7. **Primeiro capítulo.** Escreva o **cap 001 — "O que é segurança da informação"** por inteiro, seguindo a anatomia do `CLAUDE.md`: abertura por problema concreto, corpo denso de 2.500 a 4.000 palavras, e as duas seções obrigatórias — `⚖️ Brasil em Foco` e `🛠️ No Campo`. Sem crossref para capítulo que ainda não existe: referência a volume futuro é menção textual.

8. **Validação e commit.** Render HTML e PDF, `grep -rhoE '\?@[a-z-]+' _book/**/*.html` retornando zero, contagem de `<svg` batendo com os blocos `{.tikz}`. Commit como `cap 001: O que é segurança da informação`, com o status atualizado no `ROADMAP.md` no mesmo commit. Push e `gh run watch <id> --exit-status`.

Contexto que deve alimentar os exemplos: trabalho em um provedor de internet (fibra e rádio) atendendo zona rural, então analogias e casos de infraestrutura de rede são bem-vindos — mas o manual é geral, não um manual de ISP.
