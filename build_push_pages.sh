#!/usr/bin/env bash
# Build the data release site and push it to the gh-pages branch.
# Usage: ./build_push_pages.sh [extra jupyter-book build args]
set -e

rm -rf _build
jupyter-book build "$@" .
ghp-import -n -p -f _build/html
