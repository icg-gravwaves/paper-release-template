# Data products

Data products are released in one of three places, depending on size and
type: directly in git, in git via [Git LFS](https://git-lfs.com), or in an
external archive such as [Zenodo](https://zenodo.org).

## Released here

The data products are licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (see
`data/LICENSE`); please cite the paper if you use them.


| File | Stored in | Contents | Produced by |
|---|---|---|---|
| `example_measurements.csv` | git (≈1 kB, text) | One row per measurement: group ID (0–3, labelled A–D), `x`, the mean reading `y` and its standard error `y_err` | `analysis/generate_example_data.py` |
| `raw/example_raw_readings.npz` | Git LFS (≈3.5 MB, binary) | Every individual reading: 10,000 repeated readings of `y` at each `x` for each group | `analysis/generate_example_data.py` |

The notebooks only read the small CSV, so the site builds without
downloading anything from LFS. The raw readings are released so others can
redo the reduction from scratch:

```python
import numpy as np

data = np.genfromtxt("data/example_measurements.csv", delimiter=",", names=True)

raw = np.load("data/raw/example_raw_readings.npz")
raw["readings"].shape   # (44, 10000): one row per (group, x) point
```

## Choosing where a file goes

| Store it in | When | Examples |
|---|---|---|
| **git** | Text files up to about 1 MB, and figures of normal size. Anything you want to see line-by-line diffs of. | CSV/JSON summaries, `.tex` source, figure PDFs/PNGs |
| **Git LFS** | Binary files over about 1 MB, and any file over about 10 MB, up to a few hundred MB each. | HDF5, `.npz`, FITS, tarballs, large text tables |
| **Zenodo** (or similar) | Single files over about 1 GB, a total over a few GB, or data nobody needs to run the notebooks. | Raw datasets, full simulation outputs, MCMC chains |

Why these limits:

- **Git keeps every version of every file forever.** A 5 MB binary
  regenerated ten times adds 50 MB to every clone, and binaries barely
  compress or delta between versions. Small text files are cheap and diff
  well, so git is the right place for them.
- **Git LFS stores only a small pointer in git** and downloads the content
  of the version you check out. Old versions no longer make clones bigger.
  GitHub also warns on files over 50 MB and refuses files over 100 MB in
  plain git, so anything near that size must use LFS.
- **LFS is not free storage.** Storage and download bandwidth count against
  the organisation's GitHub LFS quota, and each LFS file has a maximum size
  (2 GB on most plans). Very large or rarely-used data is better placed on
  Zenodo, which also gives it its own DOI.

## Using Git LFS

Patterns stored in LFS are listed in `.gitattributes` at the root of the
repository (here: everything in `data/raw/`, and `*.npz`, `*.hdf5`,
`*.fits`, ... anywhere). Track by extension or directory, not by
individual file name, so new files are caught automatically.

```bash
git lfs install                  # once per machine
git lfs track "data/raw/**"      # adds a pattern to .gitattributes
git add .gitattributes data/raw/new_file.npz
git commit -m "Add raw readings"
git lfs ls-files                 # list files stored in LFS
```

Commit `.gitattributes` **before** adding the large files: a file committed
to plain git first stays in the history even after it is moved to LFS.
Moving it properly needs `git lfs migrate import --include="<pattern>"`,
which rewrites history and must be coordinated with everyone using the
repository.

Clones fetch LFS content automatically once `git lfs install` has been
run. To skip it (for example on a slow connection) and fetch only what you
need:

```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/icg-gravwaves/paper-release-template.git
git lfs pull --include="data/raw/example_raw_readings.npz"
```

If a notebook in the book reads an LFS file, set `lfs: true` on the
checkout step in `.github/workflows/book.yml`. Every CI run then downloads
those files and uses LFS bandwidth.

## Large inputs (not in git)

Data too large for LFS should be archived on Zenodo or an institutional
repository and fetched with a script, for example:

```bash
# data/get_large_data.sh
curl -L -o data/large/raw_data.hdf \
    "https://zenodo.org/records/XXXXXXX/files/raw_data.hdf?download=1"
```

Add the download target to `.gitignore`, and list notebooks that need it
under `execute.exclude_patterns` in `_config.yml` so the site can still be
built in CI using their stored outputs.
