# Paper release template

A skeleton repository for releasing the code and small data products behind
a paper as a [Jupyter Book](https://jupyterbook.org) website, with the
notebooks saving figures into the LaTeX source and printing tables and
quoted numbers to paste into it, and that source kept in sync with Overleaf.

<!-- TEMPLATE: update these links to your own repository's -->
- **Website:** https://icg-gravwaves.github.io/paper-release-template
- **The example data release:** [`intro.md`](intro.md), the overview of the
  example paper's release, with the notebooks that make its figures and
  tables.
- **How it works:** the *How this repository works* pages, starting at
  [`guide/repo_layout.md`](guide/repo_layout.md).

This README is also the front page of the website.

## Quick start

```bash
conda env create -f environment.yml
conda activate paper_release
jupyter-book build .          # runs every notebook, writes paper/ outputs
open _build/html/index.html
cd paper && make pdf          # compile the paper
```

## Using this template

1. Replace the repository links (`icg-gravwaves/paper-release-template`),
   titles and authors. Every place that needs changing is marked with a `TEMPLATE:` comment:

   ```bash
   grep -rn "TEMPLATE:" --exclude-dir=_build .
   ```
2. Replace `analysis/generate_example_data.py` and
   `data/example_measurements.csv` with your own data products.
3. Add notebooks that make your figures and tables under `analysis/`, and
   list them in `_toc.yml` and the table in `intro.md`.
4. Connect `paper/` to Overleaf: see [`guide/overleaf.md`](guide/overleaf.md).
5. Enable GitHub Pages (source: GitHub Actions), and optionally archive
   releases on Zenodo: see [`guide/publishing.md`](guide/publishing.md).
6. Rewrite this README as the front page for your own release.

## Licence

The code in this template is released under the [MIT licence](LICENSE),
and the data products in `data/` under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) ([`data/LICENSE`](data/LICENSE)).

<!-- TEMPLATE: review the licences for your own release -->
When you reuse it for a paper, choose the licences that fit your release
and update `LICENSE`, `data/LICENSE` and `license:` in `CITATION.cff`. MIT
is a common choice for code, and a Creative Commons licence such as CC BY
4.0 is more usual for data and text. Check whether your funder,
institution or collaboration requires a particular licence.

## Where data is stored

Small text data products (under about 1 MB) are committed directly to git;
larger binary files go through Git LFS (patterns in `.gitattributes`); data
over about 1 GB goes to Zenodo. See [`data/README.md`](data/README.md) for
the reasoning and the commands. Run `git lfs install` once before cloning.

## Notes for journal submission

- `paper/` is flat and `main.tex` is the only `.tex` file: figures are saved
  next to it, and tables and quoted numbers are printed by the notebooks for
  pasting into it, because many journals reject `\input` of other files.
- Quoted numbers are defined as `\newcommand` macros in the preamble of
  `main.tex`. Some publishers' production teams ask for custom macros to be
  expanded before typesetting. If yours does, have the notebook print each
  plain value and type it into the text instead; the CI check still flags
  a value that no longer matches the data (see
  [`guide/paper_outputs.md`](guide/paper_outputs.md)). Otherwise keep the
  macros, so each number is updated in one place.

This template uses Jupyter Book 1 (`_config.yml` / `_toc.yml`).
