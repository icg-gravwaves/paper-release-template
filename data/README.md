# Data products

Small data products (up to a few MB) are committed to this directory so the
notebooks run anywhere with no downloads. Large inputs are archived elsewhere
and fetched with a script.

## Released here

| File | Contents | Produced by |
|---|---|---|
| `example_measurements.csv` | One row per measurement: group ID (0–3, labelled A–D), `x`, `y` and the 1σ uncertainty `y_err` | `analysis/generate_example_data.py` |

The CSV can be read with no special tooling:

```python
import numpy as np
data = np.genfromtxt("data/example_measurements.csv", delimiter=",", names=True)
```

## Large inputs (not in git)

Anything too large for git (raw datasets, simulation outputs, MCMC samples)
should be archived on [Zenodo](https://zenodo.org) or an institutional
repository and fetched with a script, for example:

```bash
# data/get_large_data.sh
curl -L -o data/large/raw_data.hdf \
    "https://zenodo.org/records/XXXXXXX/files/raw_data.hdf?download=1"
```

Add the download target to `.gitignore`, and list notebooks that need it
under `execute.exclude_patterns` in `_config.yml` so the site can still be
built in CI using their stored outputs.
