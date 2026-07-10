#!/usr/bin/env bash
# rehash-raw.sh — recompute sha256 for raw markdown bodies (after frontmatter)
set -euo pipefail

if [[ $# -lt 1 || $# -gt 1 ]]; then
  echo "usage: $0 <wiki-root>" >&2
  exit 1
fi

wiki_root="$1"
if [[ "$wiki_root" == "~" || "$wiki_root" == "~/"* ]]; then
  wiki_root="$HOME${wiki_root#\~}"
fi

raw_root="$wiki_root/raw"
if [[ ! -d "$raw_root" ]]; then
  echo "raw/ not found under $wiki_root" >&2
  exit 1
fi

updated=0
skipped=0

while IFS= read -r -d '' f; do
  # extract body after closing --- of frontmatter
  if ! grep -q '^---$' "$f"; then
    skipped=$((skipped + 1))
    continue
  fi
  # body starts after second ---
  body="$(awk '
    BEGIN { n=0 }
    /^---$/ { n++; next }
    n>=2 { print }
  ' "$f")"
  if [[ -z "$body" ]]; then
    skipped=$((skipped + 1))
    continue
  fi
  sha="$(printf '%s' "$body" | shasum -a 256 | awk '{print $1}')"
  if grep -qE '^sha256:' "$f"; then
    # portable in-place replace of sha256 line
    tmp="$(mktemp)"
    awk -v sha="$sha" '
      BEGIN { done=0 }
      /^sha256:/ && !done { print "sha256: " sha; done=1; next }
      { print }
    ' "$f" >"$tmp"
    mv "$tmp" "$f"
    echo "updated: ${f#"$wiki_root"/} -> $sha"
    updated=$((updated + 1))
  else
    echo "no sha256 field: ${f#"$wiki_root"/}" >&2
    skipped=$((skipped + 1))
  fi
done < <(find "$raw_root" -type f -name '*.md' -print0)

echo "rehashed: $updated, skipped: $skipped"
