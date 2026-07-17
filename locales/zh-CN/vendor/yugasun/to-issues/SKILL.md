---
name: to-issues
description: 将计划或 PRD 拆分成项目 issue tracker 上的垂直切片 issue。
disable-model-invocation: true
---

将工作拆成 **tracer-bullet** 垂直切片——每个切片端到端贯穿所有层，并且可以独立演示。

如果缺少 tracker 配置，运行 `/aiops-setup`。

## 模式

- **多会话**（存在 PRD）：完整拆分 issue → 将 `issues/*.md` 发布到 tracker。
- **单会话**（没有 PRD，处于 `task_breakdown` 阶段）：轻量拆分 → 在 `.scratch/<slug>/` 中生成单个 `tasks.md`，不发布到 tracker。

## 流程

1. **上下文**——对话，或从 `docs/agents/issue-tracker.md` 获取的 issue/PR。单会话模式使用 `tech-spec.md` + `NOTES.md` 作为输入。
2. **探索**（可选）——代码库、领域词汇、prefactor 机会。
3. **起草切片**——标题、blocked-by、涵盖的用户故事。prefactor 切片放在最前。
4. **询问用户**——粒度、依赖、合并/拆分。迭代直到批准。
5. **发布**——按依赖顺序；除非另有要求，否则加 `ready-for-agent`。不要关闭父 issue。单会话模式则将 `tasks.md` 写入 `.scratch/<slug>/`。

### 单会话两阶段拆分（task_breakdown 阶段）

处于 `task_breakdown` 阶段（单会话）时，按两个子阶段运行，中间设置一个人工 checkpoint：

**阶段 1——父任务（3–5 项）**
- 从 `tech-spec.md` + `NOTES.md` 起草粗粒度父任务
- 每个父任务都是一个可演示的垂直切片
- 向用户展示：确认、排序、合并或拆分后才能继续

**阶段 2——展开子任务**（仅在用户确认父任务后）
- 将每个父任务展开为具体子任务，并写明 `blocked_by` 依赖
- 通过拓扑排序计算 wave
- 编写带 YAML front matter 的 `tasks.md`

## Issue 模板

**父项**——如适用，提供链接。

**要构建什么**——端到端行为，而不是分层检查清单。

**验收标准**——checkbox。

**被什么阻塞**——issue 引用或“无”。

## tasks.md 模板（单会话）

加入 YAML front matter，以便结构化追踪依赖：

```markdown
---
tasks:
  - id: t1
    title: "添加 WorkspacePaths dataclass"
    blocked_by: []
  - id: t2
    title: "接入 workspace_paths() resolver"
    blocked_by: [t1]
  - id: t3
    title: "更新 path helper 以使用 WorkspacePaths"
    blocked_by: [t1]
  - id: t4
    title: "集成测试"
    blocked_by: [t2, t3]
waves:
  - [t1]
  - [t2, t3]
  - [t4]
---

# 任务：<slug>

## Wave 1
- [ ] **t1**：添加 WorkspacePaths dataclass——<端到端行为>。被阻塞于：无

## Wave 2
- [ ] **t2**：接入 workspace_paths() resolver——<端到端行为>。被阻塞于：t1
- [ ] **t3**：更新 path helper 以使用 WorkspacePaths——<端到端行为>。被阻塞于：t1

## Wave 3
- [ ] **t4**：集成测试——<端到端行为>。被阻塞于：t2、t3
```

正文中按 wave 对任务分组。wave 通过 `blocked_by` 依赖的拓扑排序计算。
