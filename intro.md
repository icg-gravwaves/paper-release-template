% TEMPLATE: replace the paper title and arXiv link below with your own
# Example Paper: data release

This is the data release for the paper *Example paper title*
([arXiv:XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX)).

We release the code and the small data products behind every figure, table
and number in the paper. Each page in the table of contents is executed when
this site is built, so what you see here is exactly what the code produces.

The source is at
<https://github.com/icg-gravwaves/paper-release-template>.

## FAIR data and code

This release aims to follow the FAIR principles: research outputs should be
**F**indable, **A**ccessible, **I**nteroperable and **R**eusable
([Wilkinson et al. 2016](https://doi.org/10.1038/sdata.2016.18); for
software, [FAIR4RS, Barker et al. 2022](https://doi.org/10.1038/s41597-022-01710-x)).
What that means in practice here:

| Principle | How this release meets it |
|---|---|
| **Findable** | Each tagged release is archived on Zenodo with a DOI (a persistent identifier) and metadata from `CITATION.cff`, and is indexed there. The paper cites that DOI, and links to this site and the repository. |
| **Accessible** | Everything is public over standard HTTPS: this site, the GitHub repository, and the Zenodo archive, which keeps the record and its metadata even if the repository changes or disappears. Larger files come with the repository through Git LFS; very large inputs are fetched from Zenodo by a script. |
| **Interoperable** | Data products use open, documented formats (CSV with described columns, NumPy `.npz`; HDF5 is a good choice for larger, more structured data). Figures are PDF and PNG. The analysis uses standard, open-source Python tools. |
| **Reusable** | A clear licence (`LICENSE`), a recorded provenance for every figure, table and number (the table below), and an exactly pinned software environment (`environment.yml`), so results can be reproduced and built on. `CITATION.cff` says how to credit the work. |

See [](guide/publishing.md) for the steps that make a release FAIR, and
[](guide/software_versions.md) for how the environment is pinned.

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
