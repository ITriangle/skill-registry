# 综合页模板

用于高层地图、playbook、多来源综合。路径：`synthesis/<kebab-name>.md`

```markdown
---
title: 综合标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: synthesis
tags: [workflow]
sources: [raw/articles/source-a.md, raw/articles/source-b.md]
confidence: medium
contested: false
contradictions: []
---

# 综合标题

## 主张

提炼后的结论。

## 支撑证据

| 证据 | 来源 | 权重 |
| --- | --- | --- |
| …… | [[相关页面]] / raw/... | high/medium/low |

## 启示

- 因此应该改变什么。

## 观察项

- 哪些证据可能推翻当前结论。

## 相关

- [[相关页面]]
```
