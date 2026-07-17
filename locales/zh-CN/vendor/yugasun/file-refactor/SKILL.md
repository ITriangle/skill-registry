---
name: file-refactor
description: 当用户要对单个文件或少量文件做受控重构，保持行为稳定并减少局部复杂度时使用。 当需要跨系统架构重设、产品设计、或大范围迁移计划时不要用。
---

# 中文导读

- 使用场景：当用户要对单个文件或少量文件做受控重构，保持行为稳定并减少局部复杂度时使用。
- 不适用：当需要跨系统架构重设、产品设计、或大范围迁移计划时不要用。

# 上游说明原文

# File Refactor

Keep every source file under **500 lines**. Split before it crosses the limit.

## When to trigger

- A file exceeds 500 lines
- A module mixes types, utils, handlers, rendering, and constants
- A screen component contains inline sub-components that are extractable
- A service combines pure helpers, dataclasses, and orchestration in one file

## TypeScript / React splitting order

1. **Types** — interfaces, type aliases, enums → `types.ts`
2. **Pure utilities** — formatting, grouping, transforms → `utils.ts`
3. **Complex state logic** → `hooks/useXxx.ts`
4. **Sub-components** — UI pieces → `components/XxxYyy.tsx`
5. **Constants / config** — hardcoded arrays, config objects → `constants.ts`

## Python splitting order

1. **Data models** — `@dataclass`, `TypedDict`, `Protocol` → `models.py`
2. **Pure helpers** — side-effect-free formatting/parsing → `utils.py` or `*_format.py`
3. **Orchestration** — original file stays as coordinator (CLI entry, service facade)
4. **CLI groups** — subcommand handlers → dedicated modules
5. **Constants** — templates, frozensets → `constants.py`

## Rules

- **Single responsibility** — each file does one thing
- **Cohesion** — related code stays together
- **Preserve exports** — never break existing imports; re-export from original file if needed
- **Mirror neighbors** — follow existing package layout; don't invent new patterns
- After splitting: typecheck + lint must pass
