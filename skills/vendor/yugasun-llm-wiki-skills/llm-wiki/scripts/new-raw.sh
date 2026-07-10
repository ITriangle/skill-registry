#!/usr/bin/env bash
# new-raw.sh — scaffold a raw source markdown file
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
usage: new-raw.sh <wiki-root> <source-type> <title> [--url URL] [--slug SLUG] [--date YYYY-MM-DD]

source-type:
  inbox | blog | article | pdf | paper | chat-export | transcript | note
  git | lark | mail | meeting | file

examples:
  new-raw.sh PersonalWiki inbox "一个想法"
  new-raw.sh PersonalWiki blog "文章标题" --url https://example.com
  new-raw.sh PersonalWiki git "fincrawler 仓库摘要"
EOF
  exit 1
}

if [[ $# -lt 3 ]]; then
  usage
fi

wiki_root="$1"
source_type="$2"
title="$3"
shift 3

source_url=""
slug=""
date_prefix="$(date +%F)"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --url) source_url="$2"; shift 2 ;;
    --slug) slug="$2"; shift 2 ;;
    --date) date_prefix="$2"; shift 2 ;;
    *) echo "unknown arg: $1" >&2; usage ;;
  esac
done

if [[ "$wiki_root" == "~" || "$wiki_root" == "~/"* ]]; then
  wiki_root="$HOME${wiki_root#\~}"
fi

# map type -> subdirectory
subdir=""
case "$source_type" in
  inbox) subdir="inbox" ;;
  blog|article) subdir="articles" ;;
  pdf|note|git|lark|mail|meeting|file) subdir="notes" ;;
  paper) subdir="papers" ;;
  chat-export|transcript) subdir="transcripts" ;;
  *) echo "unknown source-type: $source_type" >&2; exit 1 ;;
esac

# Prefer typed subdirs when they exist for git/lark/mail/meeting
case "$source_type" in
  git|lark|mail|meeting)
    if [[ -d "$wiki_root/raw/$source_type" ]]; then
      subdir="$source_type"
    fi
    ;;
esac

if [[ -z "$slug" ]]; then
  # transliterate-ish: keep ascii alnum, replace spaces/others with -
  slug="$(printf '%s' "$title" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//; s/-+/-/g')"
  if [[ -z "$slug" || ${#slug} -lt 2 ]]; then
    slug="$source_type-note"
  fi
  slug="${slug:0:60}"
fi

dir="$wiki_root/raw/$subdir"
mkdir -p "$dir"

filename="${date_prefix}-${slug}.md"
path="$dir/$filename"
n=2
while [[ -e "$path" ]]; do
  filename="${date_prefix}-${slug}-${n}.md"
  path="$dir/$filename"
  n=$((n + 1))
done

url_line="source_url: "
if [[ -n "$source_url" ]]; then
  url_line="source_url: $source_url"
fi

body=$(cat <<EOF

# $title

## 来源

- 类型: $source_type
- 采集日期: $date_prefix

## 正文

（在此粘贴或写入来源内容。捕获后除 inbox 外视为不可变。）
EOF
)

# sha256 of body (everything after frontmatter)
sha="$(printf '%s' "$body" | shasum -a 256 | awk '{print $1}')"

cat >"$path" <<EOF
---
title: $title
$url_line
ingested: $date_prefix
published: Unknown
sha256: $sha
source_type: $source_type
---
$body
EOF

echo "$path"
