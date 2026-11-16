"""Generate the example data products used by the notebooks.

In a real release this script stands in for the expensive part of the
analysis (simulations, cluster jobs, long data processing, ...). It writes
two outputs:

``data/raw/example_raw_readings.npz`` (a few MB, binary, stored with Git LFS)
    Every individual reading: for each group and ``x`` value, many noisy
    repeated readings of ``y``. Released so others can redo the reduction.

``data/example_measurements.csv`` (a few kB, text, stored directly in git)
    The reduced data the notebooks use: the mean of the readings at each
    point and its standard error.

Re-run it with ``python analysis/generate_example_data.py``.

The example is a straight line, ``y = slope * x + intercept``, measured for
several independent groups.
"""
import logging
from pathlib import Path

import numpy as np

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
RAW_OUT = DATA_DIR / "raw" / "example_raw_readings.npz"
SUMMARY_OUT = DATA_DIR / "example_measurements.csv"
SEED = 20261116
X_VALUES = np.linspace(0, 10, 11)
N_READINGS = 10_000
# True (slope, intercept) for each group
GROUPS = {"A": (0.5, 1.0), "B": (1.2, -0.5), "C": (0.9, 2.0), "D": (1.6, 0.5)}


def simulate_readings(rng):
    """Return group IDs, x values and an (n_points, N_READINGS) array of readings."""
    group_ids, xs, readings = [], [], []
    for gid, (slope, intercept) in enumerate(GROUPS.values()):
        # Per-point scatter chosen so the standard error of the mean is 0.3-0.8
        scatter = rng.uniform(0.3, 0.8, X_VALUES.size) * np.sqrt(N_READINGS)
        for x, sd in zip(X_VALUES, scatter):
            group_ids.append(gid)
            xs.append(x)
            readings.append(slope * x + intercept + rng.normal(0, sd, N_READINGS))
    return np.array(group_ids), np.array(xs), np.array(readings)


def reduce_readings(readings):
    """Mean and standard error of the mean for each row of readings."""
    mean = readings.mean(axis=1)
    sem = readings.std(axis=1, ddof=1) / np.sqrt(readings.shape[1])
    return mean, sem


def main():
    rng = np.random.default_rng(SEED)
    group_ids, xs, readings = simulate_readings(rng)

    RAW_OUT.parent.mkdir(parents=True, exist_ok=True)
    logging.info("Writing %s readings to %s", readings.shape, RAW_OUT)
    np.savez(RAW_OUT, group=group_ids, x=xs, readings=readings,
             group_names=np.array(list(GROUPS)))

    mean, sem = reduce_readings(readings)
    logging.info("Writing %d reduced measurements to %s", mean.size, SUMMARY_OUT)
    np.savetxt(SUMMARY_OUT, np.column_stack([group_ids, xs, mean, sem]),
               delimiter=",", comments="", header="group,x,y,y_err",
               fmt=["%d", "%.2f", "%.4f", "%.4f"])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
