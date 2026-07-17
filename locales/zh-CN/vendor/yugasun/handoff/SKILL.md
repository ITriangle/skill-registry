---
name: handoff
description: 当用户要把当前对话压缩成交接文档，方便另一个 agent 或未来会话接手时使用。 当用户要立即继续当前实现，或需要创建后台 agent 而不只是交接文档时不要用。
---

# 中文导读

- 使用场景：当用户要把当前对话压缩成交接文档，方便另一个 agent 或未来会话接手时使用。
- 不适用：当用户要立即继续当前实现，或需要创建后台 agent 而不只是交接文档时不要用。

# 上游说明原文

Write a handoff so a fresh agent can continue.

## Before writing

1. Update `.scratch/<slug>/flow.state.yaml` — set `current_phase_id`, `current_issue`, `phases_done`, `gates_satisfied` as appropriate.
2. Then write handoff to the **OS temp directory** (not the workspace).

## Handoff body

- **Goal** — what the next session should accomplish
- **Decisions** — what is settled
- **Open questions** — what is not
- **Artifacts** — paths to PRDs, issues, ADRs, `flow.state.yaml` (reference, don't duplicate)
- **Suggested next** — `/aiops` or `/aiops 继续` with slug; or specific phase skill from journey

Redact secrets. If the user passed arguments, treat them as the next-session focus.
