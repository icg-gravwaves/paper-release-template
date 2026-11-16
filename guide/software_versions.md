# Software versions

This page records the software used to produce the paper and this site,
and how that environment is described in the repository.

## The environment

The whole environment is described by one file, `environment.yml`, which
was used to:

- run the analysis and make the figures, tables and numbers in the paper,
- build this site, both locally and in CI
  (`.github/workflows/book.yml` creates the same environment with
  micromamba).

It can be recreated with

```bash
conda env create -f environment.yml
conda activate paper_release
```

All packages come from [conda-forge](https://conda-forge.org). Packages
that are only on PyPI could be added in a `pip:` section of the same file.

## Pinned versions

Each package is pinned to the exact version used:

| Package | Version | Used for |
|---|---|---|
| Python | 3.12.13 | |
| NumPy | 2.5.5 | Fits and data handling |
| Matplotlib (`matplotlib-base`) | 3.11.2 | Figures |
| Jupyter Book | 1.0.4.post1 | Building this site |
| ipykernel | 7.4.0 | Running the notebooks |
| ghp-import | 2.1.0 | Publishing the site from a local build |
| sphinx-book-theme | 1.2.0 | Site theme |
| pydata-sphinx-theme | 0.16.1 | Site theme |

Later versions of these packages may change results, stop the code from
running, or change how the site looks. The two theme packages are pinned
even though they are only pulled in by Jupyter Book for the last reason: a
newer theme release adds a second search box to every page.

Packages that are needed only by the ones above are not pinned, and conda
chooses compatible versions for them.

## If you are adapting this

A few notes for anyone reusing this setup for their own paper:

- `conda list <package>` in the environment you used shows the version to
  pin.
- Code installed from a git repository or a fork is best pinned by commit
  rather than branch, since a branch moves:

  ```yaml
    - pip:
        - git+https://github.com/<org>/<package>.git@<commit hash>
  ```

- For a record of every package, `conda env export --no-builds` writes the
  complete environment. That file is specific to the operating system it
  was made on, so it is best kept as a supplement to `environment.yml`.
  [conda-lock](https://github.com/conda/conda-lock) can produce lock files
  for several platforms.
- The GitHub Actions in `.github/workflows/` use major-version tags
  (`actions/checkout@v4`); they affect only CI, not the results.
