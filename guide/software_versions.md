# Software versions

Code that runs today may not run, or may give different results, with the
versions of its dependencies released in a few years. The release should
record exactly which versions produced the paper, so anyone can rebuild
that environment.

## One environment file

`environment.yml` is the single description of the software environment.
It is used to:

- set up the environment locally (`conda env create -f environment.yml`),
- build this site in CI (`.github/workflows/book.yml` creates the same
  environment with micromamba),
- tell readers what the paper was produced with.

Keep one file rather than an `environment.yml` and a `requirements.txt`
side by side: two lists drift apart, and readers cannot tell which one
produced the paper. Conda can also install packages pip cannot, such as
compiled libraries (for example LALSuite or FFTW), and packages that only
exist on PyPI can still go in a `pip:` section of the same file.

## Pin exact versions

Each package in `environment.yml` is pinned to one version:

```yaml
dependencies:
  - python=3.12.13
  - numpy=2.5.5
  - matplotlib-base=3.11.2
```

rather than left open (`- numpy`) or given a range (`- numpy>=2`). With
open versions, rebuilding the environment later installs whatever is
newest, which can change numbers, break code, or change how the site
looks.

This template shows why the last one matters: a new release of the site
theme, pulled in by Jupyter Book, added a second search box to every page.
Pinning `sphinx-book-theme` and `pydata-sphinx-theme` keeps the site the
way it was released.

### What to pin

- **Python itself**, and every package your code imports directly.
- **Packages that affect output** even if you do not import them, such as
  the site theme here.
- **Code from a git repository or fork**, by commit, not by branch:

  ```yaml
    - pip:
        - git+https://github.com/<org>/<package>.git@<full commit hash>
  ```

  A branch moves; a commit does not. Say in the release notes why a fork
  is needed.

Packages that only your dependencies need are left for conda to resolve.

### Finding the versions you used

In the environment that produced the results:

```bash
conda list numpy matplotlib        # versions of particular packages
conda env export --from-history    # the packages you asked for, by name
```

then copy the versions into `environment.yml`.

## A fully locked environment (optional)

Pinning direct dependencies is usually enough. For an exact, every-package
record, export the whole environment as well and release it alongside:

```bash
conda env export --no-builds > environment.lock.linux-64.yml
```

A full export is specific to the operating system (a Linux export may not
install on macOS), so name it by platform and keep `environment.yml` as the
main, portable file. [conda-lock](https://github.com/conda/conda-lock) can
produce lock files for several platforms from `environment.yml`.

## When to pin

- **While developing**, loose versions are fine and make upgrading easy.
- **When the results for the paper are final**, pin everything to what you
  ran, rebuild the environment from the file, and check that the notebooks
  still produce the same figures, tables and numbers. CI does this on every
  push.
- **At each tagged release** (submission, referee response, publication),
  the pins are archived with the code on Zenodo.

## Other versions to record

- **The code itself**: cite the tagged release and its Zenodo DOI, not the
  `main` branch.
- **GitHub Actions**: the workflows use major-version tags
  (`actions/checkout@v4`). These change rarely and are not part of the
  results, so pinning them further is optional.
- **Data products**: regenerate them with the pinned environment before the
  final release, so the files match the code that is archived.
