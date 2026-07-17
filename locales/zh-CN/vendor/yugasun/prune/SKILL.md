---
name: prune
description: 当用户要收缩范围、删除多余复杂度、整理未完成计划或把方案削到可交付核心时使用。 当用户要新增功能、扩展范围，或尚未有可裁剪的方案和代码时不要用。
---

# 中文导读

- 使用场景：当用户要收缩范围、删除多余复杂度、整理未完成计划或把方案削到可交付核心时使用。
- 不适用：当用户要新增功能、扩展范围，或尚未有可裁剪的方案和代码时不要用。

# 上游说明原文

# Prune

Hunt unnecessary complexity in the diff. One line per finding. Goal: shorter diff.

## Format

`L<line>: <tag> <what>. <replacement>.`

Tags: `delete`, `stdlib`, `native`, `yagni`, `shrink`

## Scoring

End with `net: -<N> lines possible.` or `Lean already. Ship.`

## Boundaries

Complexity only — correctness and security belong in `/review`. Pre-delivery constraint: `/lean`. List cuts; do not apply unless asked.
