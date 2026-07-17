---
name: aiops-implement
description: 交付层——通过子阶段门禁编排 lean ladder、tdd、prune、review；仅在用户批准后提交。
disable-model-invocation: true
---

# aiops-implement

根据 PRD、issue brief 或 tech-spec 进行实现。**不**用于 grill/alignment——lean 只在编写代码期间启用。

由 Flow Conductor 的 **delivery** 阶段（`builder` agent）调用。随着进展更新 `flow.state.yaml` → `delivery_sub_phase`。

## 前置条件

- Issue brief 或 `issues/<current>` AC，或者 `tech-spec.md` + `NOTES.md`
- 如果此流程运行了设计评审，则 `DESIGN_REVIEW.md` 必须为 APPROVE
- 如果运行了 `/prototype`：吸收原型结论前必须有 `VERDICT.md`

## 影响分析（实现之前）

如果存在 `graphify-out/graph.json`，先告诉用户“查询代码图谱评估修改影响面”，然后在写代码前运行 `/code-graph query impact <target-file>` 查询影响，以了解爆炸半径。将受影响模块记录到 journey 上下文，让 builder 知道哪些部分可能出问题。

## 编排（硬门禁——固定顺序）

按顺序运行子阶段。除非用户明确豁免某一步（例如机械性修复 → 跳过新测试），否则不得跳过。

| 子阶段 | `delivery_sub_phase` | 执行者 | 技能 / 操作 | 进入下一阶段的门禁 |
| --- | --- | --- | --- | --- |
| 1 | `implement` | builder | lean ladder + 编写代码 | 变更行为的测试通过 |
| 2 | `implement` | builder | 在公共接口上运行 `/tdd` | 约定表面完成 red-green |
| 3 | `prune` | quality-auditor | 对 diff 运行 `/prune` | 列出发现，或注明“Lean already” |
| 4 | `review` | code-reviewer | 对照 NOTES/tech-spec/issue 运行 `/review` | `REVIEW.md` 为 APPROVE |
| 5 | `ready_for_commit` | — | 设置 journey gate `ready_for_commit` | 用户可要求 gitops 发布 |

在 journey 的 `gates_satisfied` 中记录：`prune_done`、`review_approve`、`ready_for_commit`。

## 文件大小

如果触碰的任何文件接近 **500 行**，在进入 prune 前调用 `/file-refactor`——按该技能拆分（types → utils → hooks → sub-components）。只有用户豁免或文件有意保持单体时才能跳过。

## 基于 Wave 执行（tasks.md 含 front matter 时）

当 `.scratch/<slug>/tasks.md` 包含带 `waves:` 的 YAML front matter 时，逐 wave 执行任务：

1. 从 front matter 读取 `waves` 列表。
2. 对每个 wave，实现其中的所有任务（它们彼此独立）。
3. 完成一个 wave 后，确认测试通过，再开始下一个。
4. 同一个 wave 内，优先遵循 front matter 中列出的顺序。

如果 `tasks.md` 没有 front matter，则按照文档顺序依次实现任务。

**提交**——只有用户明确要求时才提交。绝不要自主提交。发布属于 conductor **ship** 阶段的 `/gitops`。

在 implement 期间运行类型检查和针对性测试；进入 `review` 前运行一次完整测试套件。

## 叙述（conductor 显示新手文本时）

子阶段 1–2：「写代码 + 测试」→ 子阶段 3：「精简 diff」→ 子阶段 4：「对照设计评审」→ 子阶段 5：「等你确认再提交」。

## Grill 期间关闭 Lean

Alignment 使用 `/grill-with-docs`，不启用 lean。子阶段 `implement` 开始时切换到 lean。
