# {标题}

> Sources: [{引用文章1}](article1.md); [{引用文章2}](../other-topic/article2.md)
> {路径必须相对本文件：同目录只用文件名；跨主题用 ../other-topic/filename.md；也可用 [[wikilink]]}
> Archived: {YYYY-MM-DD}

## Overview

{一段话概括问题与关键发现。}

## {正文分节}

{对话中的综合答案，略作 wiki 化整理。本页是时点快照；源文章后续变更时**不做级联更新**。}

{可选 — 仅在有交叉引用时加入：}

## See Also

{指向相关 wiki 文章：
- 同主题：[其他文章](other-article.md)
- 跨主题：[其他文章](../other-topic/other-article.md)
- 或：[[其他文章]]
}

---

## PersonalWiki 变体（可选 frontmatter）

归档到 `queries/`（或主题目录）且需要 frontmatter 时：

```yaml
---
title: 归档标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: query
tags: []
sources: []
confidence: medium
contested: false
contradictions: []
---
```

### 规则

- 始终**新建**页面；不要把归档问答合并进既有文章。
- 无 Raw 字段（内容来自 wiki 综合，不是 raw/）。
- `index.md` 摘要前缀：`[Archived]` 或 `[归档]`。
- `log.md`：`## [YYYY-MM-DD] query | Archived: <page title>`
