---
name: aiops-setup
description: 为目标项目配置 aiops bundle——issue tracker、分诊标签和领域文档布局。内联引导时静默采用默认值；显式运行 `/aiops-setup` 时完整提问。
disable-model-invocation: true
---

# aiops-setup

搭建每个仓库自己的配置：**issue tracker**、**分诊标签**、**领域文档**。

## 模式

### 静默引导（由 `/aiops` conductor 发起）

缺少 `docs/agents/` 时：

1. 如果仓库根目录存在 `aiops.yaml`，读取它——见 [aiops-yaml.md](aiops-yaml.md)。
2. **没有 yaml** → `issue_tracker.kind: local`、分诊标签一一对应、`domain.layout: single`。**无需询问**，直接写入 `docs/agents/*`。
3. **yaml 指定 `github` 或 `gitlab`** → 使用匹配的 `issue-tracker-*.md` 作为初始内容；应用 yaml 中的 `prs_as_triage` 和标签覆盖。除非 yaml 不完整，否则不要进行 A/B/C 问卷。
4. 更新 `CLAUDE.md` 或 `AGENTS.md` 的 `## Agent skills` 区块（缺少该节就创建；仅当两个文件都不存在时才询问）。

### 完整设置（显式运行 `/aiops-setup`）

交互式进行——先探索，逐节确认，然后写入。切换 tracker 或重新配置时使用。

## 完整设置流程

### 1. 探索

检查：`aiops.yaml`、`git remote`、`AGENTS.md` / `CLAUDE.md`、`CONTEXT.md`、`CONTEXT-MAP.md`、`docs/adr/`、`docs/agents/`、`.scratch/`。

### 2. 询问（每次一节）

跳过 `aiops.yaml` 已满足的章节——展示 yaml 值，只提供编辑选项。

**A——Issue tracker：**仅当用户没有 `aiops.yaml` 且明确要求远程 tracker 时，才在问卷中提供 GitHub/GitLab。否则默认本地 Markdown。

**B——分诊标签：**将五个角色映射到 tracker 字符串。默认一一对应。

**C——领域文档：**单上下文（`CONTEXT.md` + `docs/adr/`）或多上下文（`CONTEXT-MAP.md`）。

**D——宪法：**如果仓库根目录没有 `CONSTITUTION.md`，提议根据 [constitution-template.md](constitution-template.md) 生成。逐节处理（测试、代码质量、架构、性能、安全、流程），请用户填写项目特有原则。这些原则**不可妥协**——每个阶段的每个代理都会引用。

### 3. 确认草稿

展示 `## Agent skills` 区块，以及 `docs/agents/issue-tracker.md`、`triage-labels.md`、`domain.md`，让用户编辑。

### 4. 写入

使用以下模板作为初始内容：`issue-tracker-*.md`、`triage-labels.md`、`domain.md`。如果配置了宪法，则根据模板和用户回答写入 `CONSTITUTION.md`。

### 5. 完成

向用户指出 `docs/agents/*.md`。可选：根据 [aiops.yaml.example](aiops.yaml.example) 添加 `aiops.yaml`，为团队提供可复现的默认配置。
