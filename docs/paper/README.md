# Paper Scaffold

This folder holds a LaTeX article that mirrors the Markdown theory pages. The intent is to keep heavy, paper-style typesetting isolated here while the canonical theory remains in Markdown under `docs/theory/`.

- Edit `main.tex` for journal/thesis-style output. Its structure tracks the theory pages, so copy text from Markdown and adapt notation as needed.
- Add references to `refs.bib`. A few seed entries are provided; extend with volcano-specific datasets or station reports.
- Build locally with `latexmk -pdf main.tex` (requires a LaTeX distribution with `latexmk`, `amsmath`, `graphicx`, `hyperref`).

When the theory evolves, update Markdown first, then port key paragraphs or figures into this LaTeX scaffold to avoid divergence.
