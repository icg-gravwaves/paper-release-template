# Publishing and archiving the release

## The website

`.github/workflows/book.yml` builds this site on every push and pull
request and deploys it to GitHub Pages from `main`.

One-off setup: in the repository on GitHub, **Settings → Pages → Build and
deployment → Source: GitHub Actions**. The site appears at
`https://<org>.github.io/<repo>`, for this template
<https://icg-gravwaves.github.io/paper-release-template>.

To publish from your own machine instead (for example when some notebooks
need data that CI cannot download), use

```bash
./build_push_pages.sh
```

which builds locally and pushes `_build/html` to the `gh-pages` branch with
`ghp-import`. In that case set Pages to deploy from the `gh-pages` branch.

## The paper PDF

The site workflow (`.github/workflows/book.yml`) compiles `paper/main.tex`
and publishes the PDF with the site, at
`https://<org>.github.io/<repo>/paper.pdf`. Anyone can read the latest draft
there, without a GitHub account, and the link does not expire.

`.github/workflows/paper.yml` also compiles the paper whenever `paper/`
changes, including on pull requests, so a change that breaks the LaTeX is
caught before it is merged. It keeps the PDF as a workflow artifact, which
needs a GitHub sign-in to download and is deleted after 90 days.

## Optional: a citable, permanent archive

Linking to the GitHub repository from the paper is enough for most
releases. If you also want a permanent snapshot with its own DOI, for
example because the repository might later be deleted or rewritten, or
because a journal or funder asks for one, archive tagged releases on
Zenodo:

1. Log in to [Zenodo](https://zenodo.org) with GitHub and enable the
   repository under **GitHub** in your Zenodo account.
2. Fill in `CITATION.cff`; Zenodo uses it for the record's metadata.
   If the repository uses Git LFS, also tick **Settings → General →
   Archives → Include Git LFS objects in archives** on GitHub. Otherwise
   the archive Zenodo stores contains only LFS pointer files, not the data.
3. Create a GitHub release (e.g. `v1.0` when the paper is submitted,
   `v1.1` after referee changes). Zenodo archives it and issues a DOI.
4. Cite the DOI in `paper/bibliography.bib` and the data availability
   statement, and add it to the README and `intro.md`.

Large data products that do not belong in git can be uploaded to a separate
Zenodo record and fetched by a script in `data/` (see [](../data/README.md)).

## Checklist before submission

- [ ] Every figure and table in `main.tex` has a notebook that produces it,
      listed in the table in `intro.md`.
- [ ] Numbers that come from the analysis match the latest data (for
      example, the notebooks report `main.tex` as up to date).
- [ ] `jupyter-book build .` passes from a clean clone with the released
      environment.
- [ ] Overleaf and `paper/` are in sync (`./overleaf_sync.sh pull`).
- [ ] `LICENSE` (and `license:` in `CITATION.cff`) is the licence you
      want for this release.
- [ ] Versions in `environment.yml` are pinned to what produced the paper
      (see [](software_versions.md)).
- [ ] The paper links to the repository (and to an archived DOI, if you
      made one).
