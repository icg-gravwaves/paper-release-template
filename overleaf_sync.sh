#!/usr/bin/env bash
# Sync the paper/ directory of this repository with an Overleaf project
# using git subtree. Overleaf's git integration serves a single branch,
# "master", containing only the paper files.
#
#   ./overleaf_sync.sh init    # one-off: replace the Overleaf project with paper/
#   ./overleaf_sync.sh pull    # bring co-authors' Overleaf edits into paper/
#   ./overleaf_sync.sh push    # send regenerated figures/tables to Overleaf
#
# Set OVERLEAF_URL (https://git.overleaf.com/<project id>) or add a remote
# called "overleaf" yourself.
set -euo pipefail

REMOTE=overleaf
PREFIX=paper
BRANCH=master

if ! git remote get-url "$REMOTE" >/dev/null 2>&1; then
    : "${OVERLEAF_URL:?Set OVERLEAF_URL=https://git.overleaf.com/<project id>}"
    git remote add "$REMOTE" "$OVERLEAF_URL"
fi

case "${1:-}" in
    init)
        # Overwrites whatever is in the Overleaf project with paper/
        # --rejoin records the split so later subtree pull/push share its history
        git subtree split --prefix "$PREFIX" --rejoin -b overleaf-split
        git push --force "$REMOTE" overleaf-split:"$BRANCH"
        git branch -D overleaf-split
        ;;
    pull)
        git subtree pull --prefix "$PREFIX" "$REMOTE" "$BRANCH" \
            -m "Merge Overleaf edits into $PREFIX/"
        ;;
    push)
        # Pull first so Overleaf never rejects the push as non-fast-forward
        git subtree pull --prefix "$PREFIX" "$REMOTE" "$BRANCH" \
            -m "Merge Overleaf edits into $PREFIX/"
        git subtree push --prefix "$PREFIX" "$REMOTE" "$BRANCH"
        ;;
    *)
        echo "usage: $0 {init|pull|push}" >&2
        exit 1
        ;;
esac
