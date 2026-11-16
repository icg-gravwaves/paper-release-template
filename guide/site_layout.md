# How the site is put together

Every part of this site's navigation, header and footer comes from a
setting or file in the repository. This page says which, so you can change
any of it.

```text
┌──────────────────┬──────────────────────────────────────────┬────────────┐
│ ① Site title     │ ④ ☰   ⑤ GitHub  Download  ⛶  ◐  🔍       │ ⑥ Contents │
│ ② Search         │                                          │            │
│ ③ Navigation     │   Page content                           │            │
│   (captions,     │   (from the .md or .ipynb file)          │            │
│    page titles)  │                                          │            │
│                  │ ⑦ This page is generated from <file>     │            │
│                  │ ⑧ ← previous            next →           │            │
│                  │ ⑨ By ... © Copyright ...                 │            │
│                  │   Code and small data products ...       │            │
└──────────────────┴──────────────────────────────────────────┴────────────┘
```

## Left sidebar

| | Element | Comes from |
|---|---|---|
| ① | Site title (top of the sidebar, and the browser tab) | `title:` in `_config.yml`. A `logo:` image, if set, is shown above it. |
| ② | Search box | Built in to the theme. It searches the text of every page in `_toc.yml`. |
| ③ | Navigation | `_toc.yml`. Each `caption:` becomes a section heading ("The data release", "How this repository works"), each `file:` becomes a link, and `sections:` nest under their chapter. The link text is the **first heading** of that file, so `# Figure 1: measurements and fits` in a notebook's first Markdown cell is what appears here. |

The front page is the `root:` file in `_toc.yml`. Here that is the
repository's `README.md`, so GitHub and the site open on the same page;
its first heading is the front page's title. The overview of the example
data release, `intro.md`, is the first page after it.

## Header buttons

| | Element | Comes from |
|---|---|---|
| ④ | ☰ (show/hide sidebar) | Theme default. |
| ⑤ | GitHub button | `use_repository_button` and `repository_url` under `html_theme_options` in `_config.yml`. |
| ⑤ | Download (`.md`/`.ipynb`, `.pdf`) | Theme default. Downloads this page's source file, or prints the page to PDF. |
| ⑤ | ⛶ fullscreen, ◐ light/dark mode | Theme defaults. |
| ⑤ | 🔍 search icon | Shown on narrow screens, where the sidebar is hidden. The extra search box the newest theme versions put in a top bar is turned off with `navbar_persistent: []`. |

## Right sidebar

| | Element | Comes from |
|---|---|---|
| ⑥ | Contents | The `##` and `###` headings of the current page. |

## Bottom of each page

| | Element | Comes from |
|---|---|---|
| ⑦ | "This page is generated from …" | `_templates/source-file.html`, switched on by `article_footer_items` in `_config.yml`. The link uses `repository_url` and `repository_branch`. |
| ⑧ | Previous / next links | The order of files in `_toc.yml`. |
| ⑨ | "By …" | `author:` in `_config.yml`. |
| ⑨ | "© Copyright …" | `copyright:` in `_config.yml`. |
| ⑨ | "Code and small data products accompanying …" | `extra_footer` under `html_theme_options` in `_config.yml`. HTML is allowed. |

## Styling

`_static/custom.css` holds small style tweaks (the logo alignment and the
look of the "generated from" line) and is loaded through `html_css_files`
in `_config.yml`.

## A pitfall with `html_theme_options`

Jupyter Book normally builds the theme options itself from an `html:`
section in `_config.yml` (`use_repository_button`, `extra_footer`, ...).
As soon as `html_theme_options` is set under `sphinx: config:`, as this
template does, those derived options are **replaced, not merged**: the
GitHub button and footer text silently disappear. This template therefore
sets all of them in `html_theme_options` and has no `html:` section. To
check what the theme actually receives, run

```bash
jupyter-book config sphinx .   # writes the generated conf.py
```

and look at `html_theme_options` in `conf.py` (delete the file afterwards).

## Theme versions

All of the above is the
[sphinx-book-theme](https://sphinx-book-theme.readthedocs.io), built on the
[PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io). New
versions move or add elements, so both are pinned in `environment.yml`
(see [](software_versions.md)).
