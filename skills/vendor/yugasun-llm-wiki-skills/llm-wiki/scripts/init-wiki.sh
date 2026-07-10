#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "usage: $0 <wiki-root> [domain]" >&2
  exit 1
fi

wiki_root="$1"
if [[ "$wiki_root" == "~" || "$wiki_root" == "~/"* ]]; then
  wiki_root="$HOME${wiki_root#\~}"
fi

domain="${2:-用于研究、项目、决策、可复用工作流和长期学习的个人知识库。}"

if [[ -e "$wiki_root/SCHEMA.md" || -e "$wiki_root/index.md" || -e "$wiki_root/log.md" ]]; then
  echo "wiki already initialized at: $wiki_root" >&2
  exit 1
fi

if [[ -d "$wiki_root" ]] && find "$wiki_root" -mindepth 1 -maxdepth 1 | grep -q .; then
  echo "wiki root is not empty: $wiki_root" >&2
  exit 1
fi

mkdir -p \
  "$wiki_root/raw/inbox" \
  "$wiki_root/raw/articles" \
  "$wiki_root/raw/papers" \
  "$wiki_root/raw/transcripts" \
  "$wiki_root/raw/notes" \
  "$wiki_root/raw/git" \
  "$wiki_root/raw/lark" \
  "$wiki_root/raw/mail" \
  "$wiki_root/raw/meeting" \
  "$wiki_root/raw/assets" \
  "$wiki_root/entities" \
  "$wiki_root/concepts" \
  "$wiki_root/comparisons" \
  "$wiki_root/queries" \
  "$wiki_root/synthesis" \
  "$wiki_root/_archive"

cat >"$wiki_root/SCHEMA.md" <<EOF
# Wiki Schema

## 领域

$domain

## 文档语言

- 新增或修改的 Markdown 默认使用中文。
- 提炼页标题需有清晰中文语义；项目名、工具名、英文专有名词可保留。
- 路径、命令、代码标识、URL、文件名、frontmatter 字段名等事实标识不翻译。

## 目录与输入源

- raw/inbox/：随手记与待摄取暂存；编译后移入正式子目录。
- raw/articles|papers|transcripts|notes|git|lark|mail|meeting|assets/
- 来源类型：blog、pdf、chat-export、git、lark、mail、meeting、inbox，以及 article/paper/transcript/note/file。

## 约定

- 文件名使用小写 kebab-case。
- 每个综合页面都以 YAML frontmatter 开头。
- 内部链接使用 Obsidian 风格 [[wikilink]]。
- 新增或更新页面时，尽量包含至少两个有意义的出站链接。
- 每个综合页面都要加入 index.md。
- 每次 ingest、query 归档、lint、archive、schema 变更都要追加到 log.md（格式：## [YYYY-MM-DD] action | 主题）。
- raw/ 除 inbox 外捕获后不可变；解释修正在综合页面完成。
- 飞书/邮件/会议默认摘要化；Git 按项目摘要，不整库灌入。
- 多来源综合时，对具体主张使用来源标记，例如 ^[raw/articles/source-name.md]。

## 回顾节奏

- 周回顾：冲突、开放问题、高频未建页概念；跑 lint。
- 月回顾：更新工作地图类 synthesis 与覆盖范围页。

## Frontmatter

\`\`\`yaml
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | synthesis
tags: []
sources: []
confidence: high | medium | low
contested: false
contradictions: []
---
\`\`\`

## 标签分类

从小分类开始，谨慎扩展：

- knowledge-management
- ai
- engineering
- finance
- research
- writing
- workflow
- decision
- project
- person
- organization
- tool
- source
- blog
- pdf
- chat-export
- git
- lark
- mail
- meeting

新标签必须先加入这里再使用。

## 页面阈值

- 当概念或实体是来源核心、跨多个来源出现，或未来很可能复用时，创建页面。
- 对顺带提及或增量事实，优先更新既有页面。
- 不为琐事、一次性上下文或领域外材料创建页面。
- 当页面超过约 200 行且混合不同主题时拆分。
- 页面被取代时归档到 _archive/，不要静默删除。

## 更新策略

- 对快速变化的主题，优先使用较新的第一手来源；冲突重要时保留新旧来源。
- 用 contested: true 和 contradictions 标记未解决冲突。
- 不要在不保留原因的情况下覆盖旧结论。
- 未先说明预期变更集时，不要批量更新 10 个以上既有页面。
EOF

cat >"$wiki_root/index.md" <<'EOF'
# Wiki 索引

## 综合

## 实体

## 概念

## 比较

## 查询
EOF

created_on="$(date +%F)"
cat >"$wiki_root/log.md" <<EOF
# Wiki 日志

## [$created_on] init | 创建 wiki

- root: $wiki_root
- domain: $domain
- created: SCHEMA.md, index.md, log.md, raw/(inbox|articles|papers|transcripts|notes|git|lark|mail|meeting|assets)/, entities/, concepts/, comparisons/, queries/, synthesis/, _archive/
EOF
