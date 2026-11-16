# Open research across disciplines

The core of this release works in any field where results come from code:
notebooks that produce the paper's outputs, a rendered release, a pinned
software environment, licences, recorded provenance and a check that the
paper matches the code. What differs between fields is where papers and
data are shared, which identifiers and statements are expected, and how
papers are written.

This page is an overview with examples, not a complete or authoritative
list. Journals, funders and institutions set their own requirements, and
those take precedence.

## Where papers and data are shared

| Field | Preprint servers | Data repositories | Other common practices |
|---|---|---|---|
| Physics, astronomy, mathematics, computer science | arXiv | Zenodo; field archives and data centres | Software papers (e.g. JOSS); citing software and data |
| Engineering | arXiv, TechRxiv | Zenodo, Figshare | Artefact evaluation and badges (e.g. ACM's Artifact Evaluation) |
| Life sciences and medicine | bioRxiv, medRxiv | Dryad, Figshare; domain repositories (e.g. GEO, ENA); controlled access (e.g. EGA) | Trial and study registration; reporting guidelines (e.g. CONSORT, ARRIVE; see EQUATOR); protocols (e.g. protocols.io); research resource identifiers (RRIDs) |
| Psychology and social sciences | PsyArXiv, SocArXiv, SSRN, OSF Preprints | OSF; UK Data Service, ICPSR | Preregistration and registered reports; reporting guidelines (e.g. PRISMA) |
| Humanities | Institutional repositories, Humanities Commons | Institutional and national archives | Rights and permissions for source material; data are often texts, images or recordings |

General-purpose repositories (Zenodo, OSF, Figshare) and institutional
repositories accept outputs from any field.

## Identifiers

- **ORCID iDs** for people, linking them to their papers, data and software.
- **DOIs** for papers, datasets and archived software releases.
- **ROR IDs** for organisations, used in some metadata schemas.
- **Domain identifiers**, such as RRIDs for antibodies, cell lines and
  software in the life sciences, or accession numbers for sequence data.

## Statements journals commonly ask for

- Data availability, including how to access data that is not open (see
  [](restricted_data.md)).
- Code availability.
- Author contributions, often using the CRediT roles.
- Use of generative AI.
- Funding and competing interests.
- Ethics approval and consent, where people or animals are involved.

## Writing tools and languages

This template assumes a paper written in LaTeX, as is common in physics,
astronomy, mathematics, statistics and parts of computer science and
economics. Many other fields write in a word processor, where pasting LaTeX
tables and macros does not apply. Tools that combine code and manuscript in
one document, such as R Markdown, Quarto and knitr, are the usual
alternative in those fields, and in R-based ones.

The rest of the release (the website, data storage, environment,
licences and provenance) carries over unchanged.
