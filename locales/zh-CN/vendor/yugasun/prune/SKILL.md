---
name: prune
description: >
  只审查 diff 中的过度工程。每个发现一行：位置、应删除什么、用什么替代。
  在 aiops 交付中是 `/review` 前的硬门禁。当用户提到 prune、简化审查、能删除什么或过度工程时使用。
---

# Prune

在 diff 中寻找不必要的复杂性。每个发现一行。目标：缩短 diff。

## 格式

`L<line>: <tag> <what>. <replacement>.`

标签：`delete`、`stdlib`、`native`、`yagni`、`shrink`

## 评分

以 `net: -<N> lines possible.` 或 `Lean already. Ship.` 结尾。

## 边界

只关注复杂性——正确性和安全性属于 `/review`。交付前约束：`/lean`。列出删减建议；除非用户要求，否则不要应用。
