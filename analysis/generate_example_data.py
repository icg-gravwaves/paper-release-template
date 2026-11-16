"""Generate the example data product used by the notebooks.

In a real release this script stands in for the expensive part of the
analysis (simulations, cluster jobs, long data processing, ...). Its
*output* is small, so it is committed to ``data/`` and the notebooks only
ever read that file. Re-run it with
``python analysis/generate_example_data.py`` to regenerate the CSV.

The example is a set of noisy measurements of a straight line,
``y = slope * x + intercept``, taken for several independent groups.
"""
import logging
from pathlib import Path

import numpy as np

OUT = Path(__file__).resolve().parents[1] / "data" / "example_measurements.csv"
SEED = 20261116
X_VALUES = np.linspace(0, 10, 11)
# True (slope, intercept) for each group
GROUPS = {"A": (0.5, 1.0), "B": (1.2, -0.5), "C": (0.9, 2.0), "D": (1.6, 0.5)}


def main():
    rng = np.random.default_rng(SEED)
    rows = []
    for gid, (slope, intercept) in enumerate(GROUPS.values()):
        y_err = rng.uniform(0.3, 0.8, X_VALUES.size)
        y = slope * X_VALUES + intercept + rng.normal(0, y_err)
        rows += [(gid, x, yi, ei) for x, yi, ei in zip(X_VALUES, y, y_err)]

    OUT.parent.mkdir(exist_ok=True)
    logging.info("Writing %d measurements to %s", len(rows), OUT)
    np.savetxt(OUT, np.array(rows), delimiter=",", comments="",
               header="group,x,y,y_err", fmt=["%d", "%.2f", "%.4f", "%.4f"])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
