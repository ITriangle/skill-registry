---
name: prototype
description: 当用户要做一次性原型来验证状态模型、业务逻辑手感或 UI 方向时使用。 当目标是生产级实现、长期维护代码，或问题无需原型验证时不要用。
---

# 中文导读

- 使用场景：当用户要做一次性原型来验证状态模型、业务逻辑手感或 UI 方向时使用。
- 不适用：当目标是生产级实现、长期维护代码，或问题无需原型验证时不要用。

# 上游说明原文

# Prototype

Throwaway code that answers **one question**. Capture the answer in `NOTES.md` (required before PRD or `/aiops-implement` absorption).

## Pick a branch

- **Logic / state / API shape** → tiny interactive terminal app. Pure logic module + thin TUI shell. One command to run. In-memory state unless persistence is the question.
- **Look and layout** → 3–5 **structurally different** UI variants on one route, switchable via `?variant=` and a floating bottom bar. Prefer embedding in an existing page over a new route.

If ambiguous: match surrounding code (backend → logic; page → UI) and state the assumption.

## Rules (both branches)

1. Name and locate so it's obviously throwaway, near the code it informs.
2. One command to run (`pnpm`, `python`, etc.).
3. No tests, minimal error handling, no abstractions beyond the question.
4. Surface full state after each action or variant switch.
5. Delete or absorb when done — don't leave rot.

## Logic branch

- State the question in one paragraph before coding.
- Isolate logic in a portable pure module (reducer, state machine, or pure functions). TUI is throwaway.
- TUI: clear screen each tick, show state + keyboard shortcuts, loop until quit.

## UI branch

- Variants must differ in layout/hierarchy, not just color.
- Switcher: bottom bar, URL param, arrow keys (skip when input focused), hidden in production.
- Winner gets folded into real code; losers and switcher deleted.
