# Repository layout

```text
.
├── _config.yml            # Jupyter Book settings (execution, repo link, theme)
├── _toc.yml               # Table of contents: which pages make up the site
├── _templates/            # Extra page templates (the "generated from" line)
├── _static/               # Custom CSS
├── intro.md               # Landing page of the data release
├── environment.yml        # Pinned conda environment (also used by CI)
├── LICENSE                # Licence for the release (MIT here)
├── paper.mplstyle         # One matplotlib style for every paper figure
├── CITATION.cff           # How to cite; shown by GitHub and read by Zenodo
├── common/
│   └── paths.py           # Shared paths + save_paper_figure / show_for_paper
├── .gitattributes         # Which files are stored with Git LFS
├── data/                  # Released data products
│   ├── *.csv              # Small text products, plain git
│   └── raw/               # Larger binary products, Git LFS
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
              ├──► data/raw/example_raw_readings.npz  (3.5 MB raw data, Git LFS)
              ▼
  data/example_measurements.csv     (1 kB reduced data, plain git)
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

## Suggestions

These are habits that worked well for this kind of release; adapt them to
your project.

- **Make it easy to find the code behind each paper item.** Name notebooks
  and output files after what they produce (`figure_1_...`,
  `table_1_...`), or after the analysis step when one notebook produces
  several items. The table on the landing page then maps each figure and
  table to its notebook.
- **Consider generating numbers quoted in the text.** For results that may
  change as the analysis evolves, a `\newcommand` printed by a notebook
  and pasted into the preamble means each value is updated in one place.
  Numbers that are fixed (survey sizes, published constants) can simply be
  typed.
- **Keep `paper/` flat and to one `.tex` file** if your journal requires it.
  Many journals want every source file in one directory and reject
  `\input` of other `.tex` files.
- **Take paths from `common/paths.py`**, not from the current working
  directory, so notebooks behave the same in Jupyter, in `jupyter-book build`
  and in CI.
- **Commit the generated figures**, so co-authors on Overleaf have them
  without running any code. CI checks that `main.tex` contains the tables
  and numbers the notebooks currently print.
