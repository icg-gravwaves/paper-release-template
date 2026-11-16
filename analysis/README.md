# Analysis and paper figures

Each notebook in this section makes one paper item. They all follow the
same pattern:

1. Read a released data product from `data/`.
2. Apply the shared style in `paper.mplstyle` ([](../guide/figure_style.md)) (journal single-column width,
   serif fonts, colour-blind-safe palette).
3. Save figures directly into `paper/`, and print tables and numbers as
   LaTeX to paste into `paper/main.tex` (journals often reject `\input`).

The notebooks are executed every time this site is built, so the plots shown
on these pages are the same files the paper uses.

The expensive step that creates the data product is kept separate, in
`analysis/generate_example_data.py`. In a real analysis this would be the
simulation, cluster job or long data processing; its small output is what gets committed and released.
