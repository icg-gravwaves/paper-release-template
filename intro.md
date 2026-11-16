% TEMPLATE: replace the paper title and arXiv link below with your own
# Data release

This is the data release for the paper *Example paper title*
([arXiv:XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX)).

We release the code and the small data products behind every figure, table
and number in the paper. Each page in the table of contents is executed when
this site is built, so what you see here is exactly what the code produces.

## Reproducing the environment

```bash
conda env create -f environment.yml
conda activate paper_release
```

or, with plain pip, `pip install -r requirements.txt`.

## Where each part of the paper comes from

| Paper item | Produced by | Output |
|---|---|---|
| Figure 1 | [](analysis/figure_1_measurements.ipynb) | `paper/figure_1_measurements.pdf` |
| Table 1 | [](analysis/table_1_fit_results.ipynb) | `tabular` printed for pasting into `main.tex` |
| Numbers in Section II | [](analysis/table_1_fit_results.ipynb) | `\newcommand`s printed for pasting into the `main.tex` preamble |

## Overview

- [](data/README.md) describes the released data products and how to fetch
  any large inputs.
- [](analysis/README.md) contains the notebooks that turn those data products
  into the paper's figures and tables.
- The *How this repository works* pages explain the layout, how outputs flow
  into the LaTeX source, how the paper is kept in sync with Overleaf, and how
  this site is published and archived.
