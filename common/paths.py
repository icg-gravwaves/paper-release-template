"""Shared locations so every notebook writes paper outputs to the same place.

Figures are written directly into ``paper/`` with no subdirectories, and
tables and macros are printed for pasting into ``main.tex``, because many
journals require a single, flat LaTeX source.

Notebooks are executed with their own directory as the working directory
(both in Jupyter and during ``jupyter-book build``), so paths are resolved
from this file rather than from the current directory.
"""
import logging
from pathlib import Path

import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
PAPER_DIR = REPO_ROOT / "paper"
STYLE_FILE = REPO_ROOT / "paper.mplstyle"


def use_paper_style():
    """Apply the journal-column matplotlib style used for every figure."""
    logging.debug("Using matplotlib style %s", STYLE_FILE)
    plt.style.use(STYLE_FILE)


def save_paper_figure(fig, name, formats=("pdf", "png")):
    """Save ``fig`` into paper/ as ``name.<fmt>`` for each format.

    The PDF is what the LaTeX source includes; the PNG is a convenient
    preview for the repository and for Overleaf's file view.
    """
    for fmt in formats:
        path = PAPER_DIR / f"{name}.{fmt}"
        logging.debug("Writing figure %s", path)
        # Drop the creation date so re-running an unchanged notebook gives an
        # identical file and does not show up as a change in git
        metadata = {"CreationDate": None} if fmt == "pdf" else None
        fig.savefig(path, metadata=metadata)
    return PAPER_DIR / f"{name}.{formats[0]}"


MAIN_TEX = PAPER_DIR / "main.tex"
OUT_OF_DATE = "NOT FOUND in paper/main.tex"


def _normalise(tex):
    """Strip indentation and blank lines so only the LaTeX content is compared."""
    return "\n".join(line.strip() for line in tex.splitlines() if line.strip())


def show_for_paper(tex, location):
    """Print a LaTeX block to be copied by hand into paper/main.tex.

    Journals often reject sources that ``\\input`` other files, so tables and
    macro definitions are pasted into ``main.tex`` rather than written out.
    The function also reports whether ``main.tex`` already contains the
    block; CI searches the executed notebooks for ``OUT_OF_DATE`` to catch a
    paper that has fallen behind the data.
    """
    print(f"% ---- Copy this into {location} of paper/main.tex ----")
    print(tex.rstrip())
    print("% ---- end of block ----\n")
    in_paper = _normalise(tex) in _normalise(MAIN_TEX.read_text())
    logging.debug("Block for %s present in main.tex: %s", location, in_paper)
    if in_paper:
        print("Up to date: paper/main.tex already contains this block.")
    else:
        print(f"{OUT_OF_DATE}: paste the block above into {location}.")
    return in_paper
