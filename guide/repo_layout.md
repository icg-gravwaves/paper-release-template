# Repository layout

```text
.
├── _config.yml            # Jupyter Book settings (execution, repo link, theme)
├── _toc.yml               # Table of contents: which pages make up the site
├── intro.md               # Landing page of the data release
├── environment.yml        # conda environment
├── requirements.txt       # pip equivalent, used by CI
├── paper.mplstyle         # One matplotlib style for every paper figure
├── CITATION.cff           # How to cite; shown by GitHub and read by Zenodo
├── common/
│   └── paths.py           # Shared paths + save_paper_figure / show_for_paper
├── data/                  # Small, released data products (committed)
├── analysis/              # Notebooks that make figures/tables + data generation
├── guide/                 # These "how it works" pages
├── paper/                 # The LaTeX paper, flat (synced to Overleaf)
│   ├── main.tex           # Single LaTeX file; tables and macros pasted in
│   ├── bibliography.bib
│   └── figure_*.pdf/.png  # Written by notebooks
├── overleaf_sync.sh       # git subtree push/pull of paper/ to Overleaf
├── build_push_pages.sh    # Build the site locally and push it to gh-pages
└── .github/workflows/
    ├── book.yml           # Build + deploy the site to GitHub Pages
    └── paper.yml          # Compile paper/main.tex to a PDF artifact
```

## The flow from data to paper

```text
 analysis/generate_example_data.py  (expensive step, run rarely)
              │
              ▼
  data/example_measurements.csv     (small data product, committed + released)
              │
              ▼
  analysis/*.ipynb                  (run on every site build)
     │                 │
     ▼                 ▼
  rendered on       paper/figure_*.pdf  ──────────────┐
  this website      LaTeX for tables + \newcommands   │
                    printed in the notebook output    │
                          │ copy and paste            │
                          ▼                           ▼
                   paper/main.tex ◄──► Overleaf (git subtree)
```

## Building the site locally

```bash
jupyter-book build .
open _build/html/index.html
```

`execute_notebooks: force` in `_config.yml` re-runs every notebook, which
also regenerates the paper outputs.

## Conventions worth keeping

- **One notebook per paper item**, named after it
  (`figure_1_...ipynb`, `table_1_...ipynb`), and the output file uses the
  same name. Anyone reading the paper can find the code from the filename.
- **Never type a number into the paper by hand.** Put it in
  a `\newcommand` printed by a notebook, paste it into the preamble of
  `main.tex`, and use the macro.
- **Keep `paper/` flat and to one `.tex` file.** Many journals want every
  source file in one directory and reject `\input` of other `.tex` files.
  Figures sit next to `main.tex`; tables and macros are pasted into it.
- **Paths come from `common/paths.py`**, not from the current working
  directory, so notebooks behave the same in Jupyter, in `jupyter-book build`
  and in CI.
- **Commit the generated figures.** Co-authors on Overleaf need them
  without running any code. CI checks that `main.tex` contains the tables
  and numbers the notebooks currently print.
