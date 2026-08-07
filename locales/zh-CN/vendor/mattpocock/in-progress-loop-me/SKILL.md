---
name: loop-me
description: 在本工作区内，就你想构建的工作流对你进行 grilling。
disable-model-invocation: true
argument-hint: "要设计的工作流，或留空以去找一个"
---

运行有状态的 `/grilling` 会话，唯一产出是**工作流** spec。使用 grilling discipline——relentless、每轮一批问题、每题附推荐答案——瞄准下方词汇与目标。随 grilling 解决而创建、编辑、删除 spec。

## Loop lens

**loop** 是用户生活中 recurring 模式：职业、一周、早晨、单一重复活动。把生活想象成 loop 套 loop，揭示活动多可预测——这正是**委托**值得的原因。用 lens 找值得 spec 的 loop，提议用户没注意到的。

**workflow** 是一个 loop 的 spec，具象化。你在 loop 上运行 workflow——loop 是其运行实例。workflow 在 `workflows/*.md`，是真相来源。

## 词汇

共享语言，仅在 workflow 需要时取用——从不是 checklist。**强制 nothing structural**：workflow 除非 grilling 表明需要，可以没有 AI、没有 checkpoint、没有 schedule。

- **Trigger**——每次运行由什么触发：**event**（新邮件、新 issue）或 **schedule**（每天早晨）。event 触发通常更高效。
- **Checkpoint**——人类在 loop 中验证或决定的点。有些 workflow 没有、全 autonomous；有些根本不用 AI。
- **Push right**——checkpoint 尽可能推迟。在人类介入前做 maximal work，使他们被问一次、晚问、一切已备好。
- **Brief**——checkpoint 呈现什么：紧凑、可决策的摘要——产出了什么、为何、链到 asset 本身——从不是 raw 输出。用户读 brief，不是 draft。审查速度 imperative。

## 完成定义

workflow spec 完成当 implementer agent 可不问任何问题就构建。grill 到那时；仍有 question 则未完成。

## 工作区

- `workflows/*.md`——每个 workflow 一份 spec。
- `NOTES.md`——用户世界的 raw notes：用的工具、处理的 channel、他们自己的术语。空或薄时，spec 任何东西前先采访他们的世界。模糊术语 surface 时 sharpen 成 canonical 并记录于此。
