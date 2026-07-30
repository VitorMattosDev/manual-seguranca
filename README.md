# Manual de Segurança da Informação

Livro aberto em português do Brasil cobrindo segurança da informação do básico ao avançado: **107 capítulos, 16 volumes, 5 fases**.

📖 Leia em: `https://vitormattosdev.github.io/manual-seguranca/`

## Estrutura

| Fase | Volumes | Tema |
|---|---|---|
| 1 | 1–4 | Fundamentos: risco, redes e sistemas, criptografia, identidade |
| 2 | 5–8 | Segurança aplicada: redes, endpoints, aplicações, nuvem |
| 3 | 9–11 | Perspectiva ofensiva: pentest, fator humano, malware |
| 4 | 12–14 | Perspectiva defensiva: SOC, resposta a incidentes, continuidade |
| 5 | 15–16 | Governança, conformidade brasileira e temas de fronteira |

A fila de produção completa está no [`ROADMAP.md`](ROADMAP.md).

## Setup local

```bash
# 1. Quarto
#    https://quarto.org/docs/get-started/

# 2. TinyTeX + pacotes LaTeX
quarto install tinytex
TLMGR="$(command -v tlmgr || find "$HOME" -name tlmgr | head -n1)"
"$TLMGR" update --self
"$TLMGR" install standalone pgf pgfplots dvisvgm xcolor amsmath amsfonts fvextra koma-script

# 3. Chrome headless (mermaid no PDF)
quarto install chrome-headless-shell

# 4. CSL da ABNT (o Claude Code faz isso no passo 2 do PROMPT-INICIAL.md)
curl -fsSL -o associacao-brasileira-de-normas-tecnicas.csl \
  https://raw.githubusercontent.com/citation-style-language/styles/master/associacao-brasileira-de-normas-tecnicas.csl
```

⚠️ **Adicione o bin do TinyTeX ao PATH da sessão** antes de renderizar, ou as figuras TikZ falham silenciosamente:

- Windows: `$HOME/AppData/Roaming/TinyTeX/bin/windows`
- Linux/macOS: `~/.TinyTeX/bin/<plataforma>`

## Renderizar

```bash
quarto preview              # servidor local com hot reload
quarto render --to html     # HTML completo
quarto render --to pdf      # PDF (rodar antes de todo push)
```

## Bootstrap do branch `gh-pages` (uma única vez, antes do primeiro push)

O `quarto-actions/publish@v2` aborta se o branch `gh-pages` não existir no remoto. Crie um commit vazio nele:

```bash
git push origin $(git commit-tree $(git hash-object -t tree /dev/null) -m 'init gh-pages'):refs/heads/gh-pages
```

Depois disso, reative o workflow (`Actions` → `Publicar livro` → `Run workflow`).

## Manutenção da estrutura

`scripts/estrutura.py` é a fonte única de verdade dos capítulos:

```bash
python scripts/estrutura.py           # resumo (107 capítulos, 16 volumes)
python scripts/estrutura.py --stubs   # cria stubs faltantes (regra stub-first)
python scripts/estrutura.py --quarto  # imprime o bloco chapters: do _quarto.yml
python scripts/estrutura.py --roadmap # regrava o ROADMAP.md
python scripts/estrutura.py --tudo    # stubs + roadmap
```

## Extensão TikZ

`_extensions/danmackinlay/tikz/` é uma cópia **com patches locais**. Nunca rodar `quarto add` ou `quarto update` nela — o upstream sobrescreve os patches e quebra a renderização. Copiar de `figuras-tikz-kit.zip` conforme `FIGURAS.md`.

## Aviso legal

Material educacional com orientação defensiva. Técnicas ofensivas são apresentadas para permitir compreensão, detecção e mitigação. Testar sistemas sem autorização formal por escrito é crime no Brasil (Lei 12.737/2012). Use apenas em laboratório próprio ou ambientes que autorizem explicitamente.

## Licença

Conteúdo: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.pt-BR). Código: MIT.
