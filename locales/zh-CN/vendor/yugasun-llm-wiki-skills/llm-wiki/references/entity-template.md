# 实体页模板

用于人、组织、产品、项目、工具。路径：`entities/<kebab-name>.md`

```markdown
---
title: 实体名称
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity
tags: [organization]
sources: [raw/articles/source.md]
confidence: medium
contested: false
contradictions: []
---

# 实体名称

## 摘要

说明这个实体是什么，以及它为什么重要。

## 关键事实

- 带来源或证据的事实。^[raw/articles/source.md]

## 关系

- 与 [[相关页面]] 相关，因为……

## 开放问题

- 仍需证据回答的问题。
```
