# {标题}

> Sources: {作者或机构1, YYYY-MM-DD; 作者或机构2, YYYY-MM-DD}
> Raw: [{来源1}](../../raw/{topic1}/{filename1}.md); [{来源2}](../../raw/{topic2}/{filename2}.md)

## Overview

{一段话概括本文关键要点。}

## {正文分节}

{从来源材料中提炼并重组，形成连贯结构。不要整段照抄原文；重要原话可少量引用。}

{可选 — 仅在有交叉引用时加入：}

## See Also

{指向相关 wiki 文章的交叉引用。Lint 时维护。链接规则：
- 同主题目录：[其他文章](other-article.md)
- 跨主题目录：[其他文章](../other-topic/other-article.md)
- 若本 wiki 使用 Obsidian wikilink：[[其他文章]]
}

---

## PersonalWiki 变体（可选 frontmatter）

当 wiki 根目录使用 `entities/` / `concepts/` / `synthesis/` 等类型目录，且 `SCHEMA.md` 要求 YAML frontmatter 时，在标题块前增加：

```yaml
---
title: 文章标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | synthesis
tags: []
sources: [raw/topic/filename.md]
confidence: high | medium | low
contested: false
contradictions: []
---
```

此时 `Sources` / `Raw` 元数据行可与 frontmatter 的 `sources` 并存；主张级引用可用 `^[raw/topic/filename.md]`。
