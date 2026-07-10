#!/usr/bin/env bash
# lint-wiki.sh — deterministic health checks for an LLM wiki root
set -euo pipefail

if [[ $# -lt 1 || $# -gt 1 ]]; then
  echo "usage: $0 <wiki-root>" >&2
  exit 1
fi

wiki_root="$1"
if [[ "$wiki_root" == "~" || "$wiki_root" == "~/"* ]]; then
  wiki_root="$HOME${wiki_root#\~}"
fi

if [[ ! -d "$wiki_root" ]]; then
  echo "wiki root not found: $wiki_root" >&2
  exit 1
fi

index_file="$wiki_root/index.md"
issues=0
auto_fixed=0
report=()

add_issue() {
  report+=("$1")
  issues=$((issues + 1))
}

# Collect knowledge pages (exclude index/log/SCHEMA/raw/_archive)
knowledge_pages=()
while IFS= read -r -d '' f; do
  knowledge_pages+=("$f")
done < <(find "$wiki_root" \( -path "$wiki_root/raw" -o -path "$wiki_root/_archive" -o -path "$wiki_root/.obsidian" \) -prune -o \
  -type f -name '*.md' -print0 2>/dev/null | sort -z)

page_basenames=()
page_paths=()
for f in "${knowledge_pages[@]}"; do
  base="$(basename "$f" .md)"
  case "$base" in
    index|log|SCHEMA) continue ;;
  esac
  # skip files directly under wiki root that aren't typed pages
  rel="${f#"$wiki_root"/}"
  case "$rel" in
    index.md|log.md|SCHEMA.md) continue ;;
    entities/*|concepts/*|comparisons/*|queries/*|synthesis/*)
      page_basenames+=("$base")
      page_paths+=("$rel")
      ;;
  esac
done

# --- Index consistency ---
if [[ ! -f "$index_file" ]]; then
  add_issue "MISSING index.md"
else
  index_content="$(cat "$index_file")"
  for i in "${!page_basenames[@]}"; do
    base="${page_basenames[$i]}"
    if ! grep -q "\[\[${base}\]\]" <<<"$index_content"; then
      add_issue "INDEX_MISSING: ${page_paths[$i]} not in index.md"
    fi
  done
  # Index links to missing pages
  while IFS= read -r link; do
    [[ -z "$link" ]] && continue
    found=0
    for base in "${page_basenames[@]}"; do
      if [[ "$base" == "$link" ]]; then
        found=1
        break
      fi
    done
    # also allow raw inventory names referenced in index "原始来源"
    if [[ $found -eq 0 ]]; then
      if find "$wiki_root" \( -path "$wiki_root/.obsidian" \) -prune -o -type f -name "${link}.md" -print -quit | grep -q .; then
        found=1
      fi
    fi
    if [[ $found -eq 0 ]]; then
      add_issue "INDEX_BROKEN: [[${link}]] target missing"
    fi
  done < <(grep -oE '\[\[[^]]+\]\]' "$index_file" | sed 's/\[\[//;s/\]\]//;s/|.*//' | sort -u)
fi

# --- Frontmatter required fields on knowledge pages ---
required_fields=(title created updated type)
for i in "${!page_paths[@]}"; do
  f="$wiki_root/${page_paths[$i]}"
  head="$(head -n 20 "$f")"
  if ! grep -q '^---$' <<<"$head"; then
    add_issue "FRONTMATTER_MISSING: ${page_paths[$i]}"
    continue
  fi
  for field in "${required_fields[@]}"; do
    if ! grep -qE "^${field}:" <<<"$head"; then
      add_issue "FRONTMATTER_FIELD: ${page_paths[$i]} missing ${field}"
    fi
  done
done

# --- Wikilinks in knowledge pages ---
for i in "${!page_paths[@]}"; do
  f="$wiki_root/${page_paths[$i]}"
  while IFS= read -r link; do
    [[ -z "$link" ]] && continue
    # skip schema examples that look like placeholders
    case "$link" in
      *页面标题*|*example*) continue ;;
    esac
    if ! find "$wiki_root" \( -path "$wiki_root/.obsidian" \) -prune -o -type f -name "${link}.md" -print -quit | grep -q .; then
      add_issue "BROKEN_WIKILINK: ${page_paths[$i]} -> [[${link}]]"
    fi
  done < <(grep -oE '\[\[[^]]+\]\]' "$f" 2>/dev/null | sed 's/\[\[//;s/\]\]//;s/|.*//' | sort -u || true)
done

# --- Raw references in sources: frontmatter and body ---
for i in "${!page_paths[@]}"; do
  f="$wiki_root/${page_paths[$i]}"
  while IFS= read -r rawref; do
    [[ -z "$rawref" ]] && continue
    # normalize
    rawref="${rawref#raw/}"
    rawref="${rawref#./}"
    if [[ ! -f "$wiki_root/raw/$rawref" ]]; then
      # try as-is under wiki
      if [[ ! -f "$wiki_root/$rawref" ]] && [[ ! -f "$wiki_root/raw/${rawref}.md" ]]; then
        add_issue "RAW_MISSING: ${page_paths[$i]} -> raw/${rawref}"
      fi
    fi
  done < <(grep -oE 'raw/[A-Za-z0-9_./-]+\.md' "$f" 2>/dev/null | grep -vE 'YYYY|slug|example|PLACEHOLDER|<|\{' | sort -u || true)
done

# --- Orphan heuristic: knowledge pages with zero inbound wikilinks from other pages/index ---
for i in "${!page_basenames[@]}"; do
  base="${page_basenames[$i]}"
  inbound=0
  if grep -q "\[\[${base}\]\]" "$index_file" 2>/dev/null; then
    inbound=1
  fi
  if [[ $inbound -eq 0 ]]; then
    for j in "${!page_paths[@]}"; do
      [[ $i -eq $j ]] && continue
      if grep -q "\[\[${base}\]\]" "$wiki_root/${page_paths[$j]}" 2>/dev/null; then
        inbound=1
        break
      fi
    done
  fi
  if [[ $inbound -eq 0 ]]; then
    add_issue "ORPHAN: ${page_paths[$i]} (no inbound wikilinks)"
  fi
done

# --- Report ---
echo "wiki: $wiki_root"
echo "knowledge_pages: ${#page_paths[@]}"
echo "issues: $issues"
echo "auto_fixed: $auto_fixed"
if [[ ${#report[@]} -gt 0 ]]; then
  echo "---"
  printf '%s\n' "${report[@]}"
fi

if [[ $issues -gt 0 ]]; then
  exit 2
fi
exit 0
