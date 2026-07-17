# 旅程状态——`flow.state.yaml`

用于记录 `/aiops` Flow Conductor 的可恢复进度。路径：`.scratch/<slug>/flow.state.yaml`。

## 通过 CLI 操作状态

协调器使用 `flow_cli.py` 子命令完成所有状态变更，绝不直接编辑 YAML。该 CLI 的底层实现模块是 `phases.py`、`gates.py` 和 `journey_state.py`。

```bash
# 启动新旅程
python3 <aiops-root>/skills/aiops/scripts/flow_cli.py init --slug <slug> --task-kind <kind> --configured --description "..."

# 进入下一阶段（门禁检查通过后）
python3 <aiops-root>/skills/aiops/scripts/flow_cli.py advance --slug <slug>

# 验证所有已满足门禁的产物均存在
python3 <aiops-root>/skills/aiops/scripts/flow_cli.py validate --slug <slug>

# 将阶段门禁标记为已满足（先验证产物）
python3 <aiops-root>/skills/aiops/scripts/flow_cli.py satisfy-gate --slug <slug> --phase-id <phase> --gate <gate_name>

# 列出某阶段要求的门禁
python3 <aiops-root>/skills/aiops/scripts/flow_cli.py phase-gates --phase-id <phase>

# 输出流程计划，但不写入状态
python3 <aiops-root>/skills/aiops/scripts/flow_cli.py plan --task-kind <kind> --configured
```

维护者：规范阶段列表来自 `python3 <aiops-root>/skills/aiops/scripts/flow_cli.py plan`（仅限本仓库）。

## 数据结构（版本 2）

```yaml
version: 2
slug: login
task_kind: feature_idea  # feature_idea | feature_with_ui | bug_fix | incoming_queue | architecture_health | new_personal_skill | prototype
delivery_mode: single_session  # single_session | multi_session
user_description: "做一个用户登录功能"
current_phase_id: alignment  # plan_flow 中的 phase_id | done（终止哨兵）
phases_done: []
gates_satisfied: []  # 例如 design_review_approve、review_approve
current_issue: null  # 多会话模式下例如 issues/001-add-auth.md
plan_hash: alignment|design_spec|design_review|task_breakdown|delivery|drift_check|ship
state:
  has_codebase: true
  issue_tracker_configured: true
  needs_runnable_answer: false
  triage_unclear: false
  explore_requested: false
```

`state:` 区块是 FlowState 快照，用于确保 `advance` 总能重建出与 `init` 创建时相同的计划。`plan_hash` 用于检测从初始化到恢复之间阶段定义是否发生变化（缺少这些字段的 v1 文件会使用合理的默认值，仍可正常工作）。

### 终止状态

当 `advance_journey` 越过最后一个阶段时，`current_phase_id` 会被设为 `done`。恢复时若 `current_phase_id` 为 `done`，协调器会告知用户旅程已完成，并且不再派发后续阶段。

## 门禁名称（追加到 `gates_satisfied`）

| 门禁 | 阶段 | 产物检查 |
| --- | --- | --- |
| `bootstrap_done` | bootstrap | `docs/agents/` directory exists |
| `design_review_approve` | design_review | `DESIGN_REVIEW.md` contains APPROVE |
| `prototype_verdict` | — | `VERDICT.md` exists |
| `prune_done` | delivery | `PRUNE.md` exists |
| `review_approve` | delivery | `REVIEW.md` contains APPROVE |
| `ready_for_commit` | delivery | `REVIEW.md` contains APPROVE |
| `drift_check_pass` | drift_check | `DRIFT_REPORT.md` exists |

阶段门禁通过 `flow_cli.py satisfy-gate` 和 `flow_cli.py phase-gates` 管理。允许继续前进之前，协调器会根据该阶段要求的门禁检查对应产物。

门禁产物由 `flow_cli.py satisfy-gate`（标记前验证）和 `flow_cli.py validate`（检查所有已满足门禁）进行验证。协调器会在向 `gates_satisfied` 追加记录之前运行验证。

## 何时读取和写入

- **启动**新的 `/aiops`：运行 `flow_cli.py init` 写入初始状态。
- **恢复** `/aiops`：读取 `flow.state.yaml`；如果 `current_phase_id` 为 `done`，则告知用户；否则加载当前阶段的智能体。
- **每个阶段结束时**：先运行 `flow_cli.py validate` 检查门禁，再运行 `flow_cli.py advance` 前进。
- **交接**（`/handoff`）：在写入临时交接文档**之前**更新旅程。

## 恢复

用户说“继续”“resume”或“上次”时，读取 `flow.state.yaml`。如果 `current_phase_id` 为 `done`，则告知用户旅程已完成；否则直接展示 `current_phase_id` 对应的引导说明，不要再次询问任务类型。

## FlowState 推断（新旅程）

| 信号 | 标志 |
| --- | --- |
| 空目录或没有 src | `has_codebase: false` → `/grilling` |
| Bug / 报错 / regression | `task_kind: bug_fix` |
| 优化架构 / 技术债 / refactor codebase | `task_kind: architecture_health` |
| 待办 / triage / issue #N | `task_kind: incoming_queue` |
| 界面 / UI / 页面 | `task_kind: feature_with_ui` |
| 用户确认 multi / 多会话 / 每个 issue 均可离线执行 | `delivery_mode: multi_session` |
| **默认值** | `delivery_mode: single_session` |
| 不存在 `docs/agents/` | `issue_tracker_configured: false` → bootstrap 阶段 |
| `aiops.yaml` 中 `issue_tracker.kind` 为 github 或 gitlab | bootstrap 会初始化远程跟踪器（见 `skills/aiops-setup/aiops-yaml.md`） |
| 不存在 `aiops.yaml` | bootstrap 会静默使用本地 Markdown 和一一对应的标签 |
