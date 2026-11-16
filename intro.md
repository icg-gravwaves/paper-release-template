% TEMPLATE: replace the paper title and arXiv link below with your own
# Example Paper: data release

This is the data release for the paper *Example Paper: releasing code and
data alongside the text*, by Your Name, Second Author and Third Author
([arXiv:XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX)). The version used
for the paper is tagged
[`v1.0`](https://github.com/icg-gravwaves/paper-release-template/tree/v1.0).

We release the code and the small data products behind every figure, table
and number in the paper. Each page in the table of contents is executed when
this site is built, so what you see here is exactly what the code produces.

The source is at
<https://github.com/icg-gravwaves/paper-release-template>.

## Open research

Releasing the code and data behind a paper like this supports the
[FAIR principles](https://doi.org/10.1038/sdata.2016.18), that research
outputs should be **F**indable, **A**ccessible, **I**nteroperable and
**R**eusable. In this release:

- **Findable:** the paper links to this site and the repository.
- **Accessible:** everything is public, and the site needs nothing
  installed to read.
- **Interoperable:** data products are in open, documented formats (CSV,
  NumPy `.npz`) and the analysis uses standard open-source tools.
- **Reusable:** the code is under the MIT licence (`LICENSE`) and the data
  products under CC BY 4.0 (`data/LICENSE`), every figure, table and
  number can be traced to the notebook that made it (table below), and the
  software environment is pinned (`environment.yml`).

## Reproducing the environment

```bash
conda env create -f environment.yml
conda activate paper_release
```

`environment.yml` pins the exact versions used to produce the paper; see
[](guide/software_versions.md).

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
