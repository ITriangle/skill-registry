---
name: aiops
description: aiops 套件的 Flow Conductor。单一入口——推断任务类型、用自然语言展示步骤、在 flow.state.yaml 中跟踪旅程，并为每个阶段分派 skill + agent。
disable-model-invocation: true
---

# aiops——Flow Conductor

套件的单一入口。普通用户只需使用此命令；专家仍可使用 `/aiops <agent> …`。

## 调用方式

```
/aiops <你想做的事>             # Conductor——推断、解说、分派
/aiops 继续 / resume             # 从 .scratch/<slug>/flow.state.yaml 恢复
/aiops <agent-name> <task>       # 专家模式——直接调用 agent；若处于 flow 中仍需更新旅程
```

代理：`architect`、`design-reviewer`、`planner`、`prototyper`、`builder`、`ui-designer`、`code-reviewer`、`quality-auditor`、`gitops`

## Conductor 循环（每一轮）

1. **恢复或开始**——如果用户要求恢复或 slug 已知，读取 `.scratch/<slug>/flow.state.yaml`。若 `current_phase_id` 为 `done`，告知用户旅程已经完成。否则从描述推断 slug（kebab-case；用户可以覆盖）。参见 [journey.md](journey.md)。
2. **引导初始化**——如果缺少 `docs/agents/`，就地运行 **bootstrap**：
   - 没有 `aiops.yaml` → 静默使用默认值：本地 Markdown issue + 1:1 分诊标签（[aiops-setup/aiops-yaml.md](../aiops-setup/aiops-yaml.md)）。
   - `aiops.yaml` 中 `issue_tracker.kind: github|gitlab` → 根据 yaml 初始化 GitHub/GitLab 跟踪器文档；除非 yaml 不完整，否则不要询问跟踪器。
   - 不要要求用户运行另一个命令。
3. **规划**——根据旅程和仓库信号构建 `FlowState`（见 [journey.md](journey.md)）。除非用户确认使用 multi，或启发式规则明确表明需要 multi，否则**默认 `delivery_mode: single_session`**。使用 `flow_cli.py plan` 生成阶段列表。
4. **解说**——使用 [narration.md](narration.md) 中的一个区块：中文 `title_zh`、`body_zh`、`artifact_zh`；只有 `title_en` 使用英文。除非用户询问，否则隐藏 skill/agent 名称。
5. **分派**——设置了 `agent` 时加载 `agents/<agent>.md`；调用该阶段的 `skill`。根据代理 Inputs 收集 `.scratch/<slug>/` 输入。
6. **门禁**——推进前运行 `flow_cli.py validate --slug <slug>` 验证门禁产物。如果验证失败，不得推进。成功后把门禁名称追加到 `gates_satisfied`。
7. **推进**——运行 `flow_cli.py advance --slug <slug>` 更新 `current_phase_id` 和 `phases_done`。交接时，先推进旅程，**再**写临时交接文档。
8. **交付**——当阶段为 `delivery` 时，交给 `/aiops-implement`（它负责 lean → tdd → prune → review）。Conductor 不要穿插这些门禁。

## 任务类型 → 阶段尾部（如有需要，在 bootstrap 之后）

| 任务类型 | 阶段（缩写） | Grill | 终点 |
| --- | --- | --- | --- |
| **Feature** | align → design → design_review → task_breakdown → delivery → drift_check → ship | 是 | `/gitops` |
| **Feature + UI** | 在 design_review 前增加 ui_mockup | 是 | `/gitops` |
| **Bug** | diagnose → delivery → drift_check → ship | 否 | `/gitops` |
| **Incoming** | triage →（不清楚时 align）→ delivery → drift_check → ship | 按条件 | `/gitops` |
| **Architecture health** | graph_build → architecture_scan → align → design → design_review → task_breakdown → delivery → drift_check → ship | 是 | `/gitops` |
| **Prototype** | 仅 prototype | — | `VERDICT.md` |
| **New personal skill** | skill_authoring 检查清单 | 是 | 新 `SKILL.md` |

`AGENTS.md` 的分派行位于 `skills/manifest.json` → `dispatch`。阶段顺序细节见 `skills/aiops/scripts/phases.py`。

**Explore**（主动选择）：当 `explore_requested` 为真时，在 bootstrap（如有）之后、特定任务阶段之前插入 `explore` 阶段。

**多会话**：design_review 之后依次为 `planning_prd` → `planning_issues` → `issue_session` → 每个 issue 的 delivery。单会话：design_review 之后依次为 `task_breakdown` → delivery。

**Prototype 分支**（可选）：handoff → `/prototype` → handoff 返回；进入 planner/builder 前必须有 `VERDICT.md`。

grill/alignment 阶段不启用 Lean。

## 多会话启发式规则

在以下情况下建议使用**多会话**：涉及 3 个以上模块、包含多个切片、接近 smart zone，或每个 issue 都采用 AFK 模式。**默认为单会话**——单会话仍包含 `task_breakdown`（轻量的 tasks.md）；多会话使用完整的 `planning_prd` → `planning_issues` → `issue_session`。

## 新建个人技能检查清单

1. 用途和触发场景
2. 用户调用还是模型调用
3. 步骤与参考文件（渐进式披露）
4. 编写 `SKILL.md`——Cursor **create-skill**（外部；`docs/skill-registry.md`）

## 参考资料

- 旅程文件格式：[journey.md](journey.md)
- 用户解说键：[narration.md](narration.md)
- 状态操作：`python3 <aiops-root>/skills/aiops/scripts/flow_cli.py {plan,init,advance,validate,satisfy-gate,phase-gates}`
- 项目配置 yaml：[aiops-setup/aiops-yaml.md](../aiops-setup/aiops-yaml.md)
- 词汇：目标项目的 `CONTEXT.md`；技能注册表：`docs/skill-registry.md`
