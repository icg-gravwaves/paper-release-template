# Paper release template

A skeleton repository for releasing the code and small data products behind
a paper as a [Jupyter Book](https://jupyterbook.org) website, with the
notebooks saving figures into the LaTeX source and printing tables and
quoted numbers to paste into it, and that source kept in sync with Overleaf.

<!-- TEMPLATE: update these links to your own repository's -->
- **Website:** https://icg-gravwaves.github.io/paper-release-template
- **How it works:** the *How this repository works* pages on the website,
  starting at [`guide/repo_layout.md`](guide/repo_layout.md).

## Quick start

```bash
conda env create -f environment.yml
conda activate paper_release
jupyter-book build .          # runs every notebook, writes paper/ outputs
open _build/html/index.html
cd paper && make pdf          # compile the paper
```

## Using this template

1. Replace the repository links (`icg-gravwaves/paper-release-template`), titles and authors. Every
   place that needs changing is marked with a `TEMPLATE:` comment:

   ```bash
   grep -rn "TEMPLATE:" --exclude-dir=_build .
   ```
2. Replace `analysis/generate_example_data.py` and
   `data/example_measurements.csv` with your own data products.
3. Add one notebook per figure/table under `analysis/` and list it in
   `_toc.yml` and the table on `intro.md`.
4. Connect `paper/` to Overleaf: see [`guide/overleaf.md`](guide/overleaf.md).
5. Enable GitHub Pages (source: GitHub Actions) and Zenodo archiving: see
   [`guide/publishing.md`](guide/publishing.md).

## Notes for journal submission

- `paper/` is flat and `main.tex` is the only `.tex` file: figures are saved
  next to it, and tables and quoted numbers are printed by the notebooks for
  pasting into it, because many journals reject `\input` of other files.
- Quoted numbers are defined as `\newcommand` macros in the preamble of
  `main.tex`. Some publishers' production teams ask for custom macros to be
  expanded before typesetting. If yours does, have the notebook print each
  plain value and type it into the text instead; the CI check still flags
  a value that no longer matches the data (see `guide/paper_outputs.md`). Otherwise keep the
  macros, so each number is updated in one place.

This template uses Jupyter Book 1 (`_config.yml` / `_toc.yml`).
