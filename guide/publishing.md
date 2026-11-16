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

`.github/workflows/paper.yml` compiles `paper/main.tex` whenever `paper/`
changes and uploads the PDF as a workflow artifact. Co-authors who do not
use Overleaf can download the latest draft from the Actions tab.

## A citable, permanent archive

GitHub repositories can be deleted or rewritten; a paper should cite an
archived snapshot.

1. Log in to [Zenodo](https://zenodo.org) with GitHub and enable the
   repository under **GitHub** in your Zenodo account.
2. Fill in `CITATION.cff`; Zenodo uses it for the record's metadata.
3. Create a GitHub release (e.g. `v1.0` when the paper is submitted,
   `v1.1` after referee changes). Zenodo archives it and issues a DOI.
4. Put the DOI in `paper/bibliography.bib` and on the landing page.

Large data products that do not belong in git can be uploaded to a separate
Zenodo record and fetched by a script in `data/` (see [](../data/README.md)).

## Checklist before submission

- [ ] Every figure and table in `main.tex` has a notebook that produces it,
      listed on the landing page.
- [ ] No number in the text is typed by hand.
- [ ] `jupyter-book build .` passes from a clean clone with the released
      environment.
- [ ] Overleaf and `paper/` are in sync (`./overleaf_sync.sh pull`).
- [ ] A tagged release exists and its DOI is cited in the paper.
