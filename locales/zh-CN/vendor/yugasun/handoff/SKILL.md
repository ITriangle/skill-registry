---
name: handoff
description: 将当前对话压缩成交接文档，供另一个 agent 接手。
argument-hint: "下一次会话将用于什么？"
disable-model-invocation: true
---

编写交接文档，使新的 agent 能继续工作。

## 编写之前

1. 更新 `.scratch/<slug>/flow.state.yaml`——根据实际情况设置 `current_phase_id`、`current_issue`、`phases_done`、`gates_satisfied`。
2. 然后将交接文档写入**操作系统临时目录**（而不是工作区）。

## 交接正文

- **目标**——下一次会话应完成什么
- **决策**——哪些事项已经确定
- **待解决问题**——哪些事项尚未确定
- **工件**——PRD、issue、ADR、`flow.state.yaml` 的路径（只引用，不要复制内容）
- **建议的下一步**——带 slug 的 `/aiops` 或 `/aiops 继续`；或者 journey 中某个特定阶段的技能

隐去秘密信息。如果用户传入了参数，将其视为下一次会话的关注点。
