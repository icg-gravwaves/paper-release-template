# Restricted and externally hosted data

Not all data behind a paper can be committed to its repository. This page
covers three common cases, and how this release can still show its working
for each.

| Case | Examples |
|---|---|
| **Sensitive** | Personal, clinical or survey data; data covered by consent conditions or data protection law |
| **Embargoed or proprietary** | Observations in a proprietary period before public release; data internal to a collaboration until publication; data under a commercial agreement |
| **Externally hosted** | Large public datasets in a field archive or data centre; third-party data whose licence does not allow redistribution |

## What can still be released

- **All of the code**, including the steps that read and process the data.
- **Derived products** that are allowed to be shared: aggregated
  results, summary statistics, or the reduced data behind each figure.
- **Synthetic or sample data** with the same format as the real data, so
  the notebooks run and can be checked even without access to the
  original.
- **Exact references to the data used**: the archive, dataset identifier
  or DOI, version or release, and the date it was accessed. Archives are
  sometimes reprocessed or updated.
- **A data availability statement** in the paper saying where the data is,
  who can access it, and how to apply.

## In this repository

- **Fetch scripts.** A script in `data/` downloads externally hosted data
  from its archive, ideally checking a checksum so a changed file is
  noticed. The download location is listed in `.gitignore`, so the data is
  never committed (see [](../data/README.md)).
- **Notebooks that need restricted data.** List them under
  `execute.exclude_patterns` in `_config.yml`. The site then shows the
  outputs saved when the notebook was last run with access to the data,
  instead of re-running it in CI, where the data is not available.
- **Tables and numbers from restricted data** still go through
  `show_for_paper`, so a reader can see the code that produced them, even
  if they cannot re-run it.

## Embargoed data

Data under an embargo or proprietary period can be released in steps. The
first release has the code, synthetic or sample data, and any products
already allowed to be shared. When the embargo ends, add the data or its
archive references, run the excluded notebooks in CI, and tag a new
version of the release.

## Sensitive data

- **Never commit it, even briefly.** Git keeps every version of every file,
  so data removed in a later commit is still in the history and in every
  clone. Removing it needs a history rewrite, coordinated with everyone
  who has a copy.
- **Check derived products as well.** Small counts in tables, or rare
  combinations of characteristics, can identify people. Apply your field's
  disclosure rules before releasing aggregated results.
- **Use a controlled-access repository** where data can be shared under
  conditions (for example the UK Data Service, or the European
  Genome-phenome Archive), and cite it in the data availability statement.
- **Ask early.** Your ethics committee, data protection officer or
  research data service can say what can be shared, and how.
