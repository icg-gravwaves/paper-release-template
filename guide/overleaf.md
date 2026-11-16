# Writing the paper on Overleaf

Most co-authors want to write in Overleaf, not in a git repository full of
notebooks. The aim is to keep **one copy of the paper**, `paper/`, that is
both what Overleaf edits and what the notebooks write into.

There are three ways to connect them. Pick based on which Overleaf plan your
group has.

| Approach | Overleaf plan needed | What Overleaf sees | Direction |
|---|---|---|---|
| [A. git subtree](overleaf-subtree) (recommended) | Git integration (paid or institutional) | Only `paper/` | Both ways |
| [B. GitHub sync](overleaf-github) | GitHub sync (paid or institutional) | The whole repository | Both ways |
| [C. Files from external URL](overleaf-url) | Free | Individual figures | Repository → Overleaf |

(overleaf-subtree)=
## A. git subtree of `paper/` (recommended)

Overleaf exposes every project as a git repository at
`https://git.overleaf.com/<project id>`, with a single branch called
`master`. `git subtree` lets that repository mirror just the `paper/`
directory here, so co-authors on Overleaf never see the code and data.

### One-off setup

1. Create a blank project on Overleaf and copy its id from the URL
   (`https://www.overleaf.com/project/<project id>`).
2. On Overleaf, go to **Account settings → Git integration** and generate a
   git authentication token. Git will ask for a username (`git`) and a
   password (the token). Store it in your credential helper.
3. In this repository:

   ```bash
   export OVERLEAF_URL=https://git.overleaf.com/<project id>
   ./overleaf_sync.sh init
   ```

   This replaces the blank project with the contents of `paper/`.
4. On Overleaf, open **Menu** and check that *Main document* is `main.tex`.
5. Share the Overleaf project with co-authors as usual.

### Day-to-day

```text
  co-authors edit text            you re-run notebooks
  on Overleaf                     (new figures, pasted tables/macros)
        │                                  │
        ▼                                  ▼
  ./overleaf_sync.sh pull   ◄──────►  ./overleaf_sync.sh push
        │                                  │
        └──────────► git push origin main ◄┘
```

- **Text changed on Overleaf:** `./overleaf_sync.sh pull`, then
  `git push` to GitHub. The edits arrive as a merge commit touching only
  `paper/`.
- **Figures changed here:** commit them, then `./overleaf_sync.sh push`.
  The script pulls first, so a push never overwrites a co-author's edits.
  Overleaf picks up the new commit within a few seconds; co-authors may need
  to recompile.
- **Conflicts** happen only when the same lines changed in both places. They
  are resolved in this repository like any other merge, then pushed.

### Things to know

- Keep generated files in `paper/` committed (see
  [](repo_layout.md)). Overleaf can only show what is in git.
- Do not rename `paper/` once the subtree is set up; the prefix is part of
  the history `git subtree` reconstructs.
- Overleaf's history and comments stay on Overleaf. Only file contents go
  through git.
- `git subtree push` replays the history of `paper/` each time, which slows
  down in very long-lived repositories. Pass `--rejoin` to the push in
  `overleaf_sync.sh` if that becomes a problem.

(overleaf-github)=
## B. Overleaf GitHub sync

Overleaf can link a project directly to a GitHub repository
(**Menu → GitHub**). It is simpler to set up, but it syncs the **whole
repository**, so notebooks, data and CI files all appear in the Overleaf
file tree.

To use it with this layout:

1. Create the Overleaf project from GitHub (**New project → Import from
   GitHub**) and select this repository.
2. Set **Menu → Main document** to `paper/main.tex`.
3. Use **Menu → GitHub → Pull GitHub changes into Overleaf** after pushing
   new figures, and **Push Overleaf changes to GitHub** after writing.

This works best when the data products are small and the repository is a
manageable size for Overleaf.

(overleaf-url)=
## C. Figures from an external URL (free plan)

Without git integration, Overleaf can still import individual files from a
URL and refresh them later. Because the figures are committed to a public
repository, each one has a stable URL:

```text
https://raw.githubusercontent.com/icg-gravwaves/paper-release-template/main/paper/figure_1_measurements.pdf
```

Replace the organisation and repository with your own.

1. In Overleaf, **Upload → From external URL**, paste the URL, and name the
   file `figure_1_measurements.pdf`.
2. When the notebook changes the figure, push to GitHub, then click the
   file in Overleaf and press **Refresh**.

Tables and numbers are pasted into `main.tex` directly. Text edits on
Overleaf do not come back to the repository in this mode, so copy the final
`.tex` into `paper/` (or download the project as a zip) before archiving
the release.
