# Figure style

Every figure in the paper uses one matplotlib style file,
[`paper.mplstyle`](https://github.com/icg-gravwaves/paper-release-template/blob/main/paper.mplstyle)
at the root of the repository. Keeping the look in one file, rather than in
each notebook, means all figures match each other and the paper, and the
whole set can be restyled at once (for example for a different journal).

## What it sets

| Setting | Value | Why |
|---|---|---|
| `figure.figsize` | 3.25 × 2.0 in | One journal column, so the figure is included at `width=\columnwidth` with no scaling and the fonts stay the size set here |
| Font sizes | 8–9 pt | Close to the caption size of a two-column paper |
| `font.family`, `mathtext.fontset` | Serif, Computer Modern | Matches the LaTeX text and maths without needing LaTeX installed (`text.usetex: False`) |
| `axes.prop_cycle` | Seaborn "colorblind" palette | Line colours that stay distinguishable for colour-blind readers |
| Ticks | Inward, on all four sides, minor ticks on | Common style in physics journals |
| `savefig.bbox: tight` | Trim whitespace | Figures sit neatly in the column |
| `figure.dpi` | 200 | Sharp previews in notebooks and on this site |

## Using it

Apply it to a whole notebook:

```python
import matplotlib.pyplot as plt
plt.style.use("../paper.mplstyle")       # path relative to the notebook
```

In this repository the helper does the same thing without depending on the
working directory:

```python
from common import paths
paths.use_paper_style()
```

Apply it to one figure only, leaving the notebook's other plots unchanged:

```python
with plt.style.context("../paper.mplstyle"):
    fig, ax = plt.subplots()
    ...
```

Styles can be stacked; later ones override earlier ones. This is useful for
a talk version of the same figure:

```python
plt.style.use(["../paper.mplstyle", "talk.mplstyle"])
```

## Changing a figure without changing the style

Override a setting for one figure with an argument, rather than editing
the style file:

```python
# A figure spanning both columns (use width=\textwidth in LaTeX)
fig, ax = plt.subplots(figsize=(6.75, 3))

# A taller single-column figure
fig, axes = plt.subplots(2, 1, figsize=(3.25, 4), sharex=True)
```

or change a single setting for one block:

```python
with plt.rc_context({"legend.fontsize": 6}):
    ax.legend(ncols=3)
```

## Adapting it to a journal

1. Find the column width: put `\showthe\columnwidth` in the LaTeX source
   and read the value (in pt) from the log, or print `\the\columnwidth` in
   the document. Divide by 72.27 to get inches.
2. Set `figure.figsize` in `paper.mplstyle` to that width, and the
   two-column `figsize` in your notebooks to the `\textwidth`.
3. If the journal uses a different font, change `font.serif` and
   `mathtext.fontset`, or set `text.usetex: True` to use LaTeX itself for
   every label. This needs a LaTeX installation wherever the notebooks run,
   including CI.
4. Rebuild the book. Every figure is regenerated in the new style.

Never resize a figure in LaTeX to fit (`width=0.8\columnwidth` of a figure
made at a different size): the fonts shrink or grow with it and no longer
match the text.

## Using it outside this repository

Matplotlib also loads styles by name from its config directory:

```bash
mkdir -p "$(python -c 'import matplotlib; print(matplotlib.get_configdir())')/stylelib"
cp paper.mplstyle "$(python -c 'import matplotlib; print(matplotlib.get_configdir())')/stylelib/"
```

after which `plt.style.use("paper")` works in any script on that machine.
For a released repository, prefer the path to the file in the repository,
so others get the same style without installing anything.
