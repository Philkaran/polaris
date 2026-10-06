#!/usr/bin/env bash
# Pre-publish check: no IDs in the docs, and the site must build cleanly
set -e
if grep -rniE "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|/subscriptions/|onmicrosoft\.com" docs/; then
  echo "STOP: something in docs/ looks like an ID. Remove it before publishing."
  exit 1
fi
python3 -m mkdocs build --strict -q
echo "CHECK PASSED: no IDs found, site builds cleanly"
