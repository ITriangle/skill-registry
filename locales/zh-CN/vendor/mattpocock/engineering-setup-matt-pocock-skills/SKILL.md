---
name: setup-matt-pocock-skills
description: 为本仓库配置 engineering skills——设置 issue tracker、triage 标签词汇与领域文档布局。在其他 engineering skills 首次使用前运行一次。
disable-model-invocation: true
---

# Setup Matt Pocock's Skills

脚手架 engineering skills 假设的 per-repo 配置：

- **Issue tracker**——issue 在哪（默认 GitHub；也开箱支持 local markdown）
- **Triage labels**——五个 canonical triage 角色用的字符串
- **Domain docs**——`CONTEXT.md` 和 ADR 在哪，及读取它们的 consumer 规则

这是 prompt 驱动 skill，非确定性脚本。探索、呈现发现、与用户确认、然后写入。

## 流程

### 1. Explore

看当前 repo 理解起始状态。读存在的一切；不要假设：

- `git remote -v` 和 `.git/config`——是 GitHub repo 吗？哪个？
- 根目录 `AGENTS.md` 和 `CLAUDE.md`——是否存在？任一是否已有 `## Agent skills`？
- 根目录 `CONTEXT.md` 和 `CONTEXT-MAP.md`
- `docs/adr/` 及任何 `src/*/docs/adr/`
- `docs/agents/`——本 skill 先前产出是否已存在？
- `.scratch/`——是否已在用 local-markdown issue tracker 惯例
- `triage` skill 是否安装？（与本 skill 并列的 `triage` 文件夹，或可用 skills 中有 `triage`。）决定 Section B 是否运行。
- Monorepo 信号——`pnpm-workspace.yaml`、`package.json` 的 `workspaces`、或 populated `packages/*` 自有 `src/`。仅真大型多包 repo 呈现；缺失即 single-context，几乎是每个 repo。

### 2. 呈现发现并询问

总结有什么、缺什么。按顺序过各 section——一节、一答，再下一节。

每节以推荐答案 lead，用户可一词接受。仅选择真 branch 时给一行 explainer；探索已 settled 的 section 跳过（`triage` 未安装时 Section B，无 monorepo 时 Section C）。

**Section A — Issue tracker。**

> Explainer：「issue tracker」是本 repo issue 所在。`to-tickets`、`triage`、`to-spec` 等 skill 从中读写——需知是调 `gh issue create`、写 `.scratch/` 下 markdown，还是你描述的其他 workflow。选你实际跟踪工作的地方。

默认姿态：这些 skill 为 GitHub 设计。`git remote` 指向 GitHub 则提议它。指向 GitLab（`gitlab.com` 或自托管）则提议 GitLab。否则（或用户偏好）提供：

- **GitHub**——issue 在 repo 的 GitHub Issues（用 `gh` CLI）
- **GitLab**——issue 在 repo 的 GitLab Issues（用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI）
- **Local markdown**——issue 是本 repo `.scratch/<feature>/` 下文件（solo 或无 remote 项目好）
- **Other**（Jira、Linear 等）——请用户一段描述 workflow；skill 记为 freeform prose

选择记入 `docs/agents/issue-tracker.md`。GitHub 和 GitLab 模板带「PRs as request surface」flag，默认**关**——保持关、不提起；要把外部 PR 进 triage 队列的用户可稍后 flip 文件里 flag。

**Section B — Triage label 词汇。**`triage` skill 未安装则整节跳过（探索已告知）——未安装 skill 不需要 label。

若已安装，只问一个问题：

> 要保留默认 triage labels 吗？（推荐：**是**）

默认是五个 canonical 角色，每 label 字符串等于其名：`needs-triage`、`needs-info`、`ready-for-agent`、`ready-for-human`、`wontfix`。**是**则原样写入。仅用户说不——通常 tracker 已用其他名（如 `bug:triage` 代 `needs-triage`）——收集 override，使 `triage` 用现有 label 而非建重复。

**Section C — Domain docs。**默认 **single-context**——根一个 `CONTEXT.md` + `docs/adr/`。fit 几乎每个 repo；不问直接写。

仅探索发现 monorepo 信号时提供 **multi-context**——根 `CONTEXT-MAP.md` 指向 per-context `CONTEXT.md`。然后确认他们要哪种布局。

### 3. 确认并编辑

向用户展示草稿：

- 将加到 `CLAUDE.md` / `AGENTS.md` 的 `## Agent skills` 块（见步骤 4 选择规则）
- `docs/agents/issue-tracker.md`、`docs/agents/domain.md`、`docs/agents/triage-labels.md` 内容（最后仅 `triage` 安装时）

写入前让他们编辑。

### 4. Write

**选要编辑的文件：**

- 若 `CLAUDE.md` 存在，编辑它。
- 否则若 `AGENTS.md` 存在，编辑它。
- 两者都不存在，问用户创建哪个——不要替他们选。

`CLAUDE.md` 已存在时永不创建 `AGENTS.md`（反之亦然）——始终编辑已有的。

所选文件中已有 `## Agent skills` 块则 inplace 更新内容，不 append 重复。不要 overwrite 用户对周围 section 的编辑。

块：

```markdown
## Agent skills

### Issue tracker

[issue 跟踪位置一行摘要]. See `docs/agents/issue-tracker.md`.

### Triage labels

[label 词汇一行摘要]. See `docs/agents/triage-labels.md`.

### Domain docs

[布局一行摘要 — "single-context" 或 "multi-context"]. See `docs/agents/domain.md`.
```

仅 `triage` 安装且 Section B 运行时包含 `### Triage labels` 子块并写 `docs/agents/triage-labels.md`。否则两者都省略。

然后用本 skill 文件夹种子模板写 docs：

- [issue-tracker-github.md](./issue-tracker-github.md) — GitHub issue tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md) — GitLab issue tracker
- [issue-tracker-local.md](./issue-tracker-local.md) — local-markdown issue tracker
- [triage-labels.md](./triage-labels.md) — label 映射（仅 `triage` 安装时）
- [domain.md](./domain.md) — domain doc consumer 规则 + 布局

「other」issue tracker 时，按用户描述从头写 `docs/agents/issue-tracker.md`。

### 5. Done

告知 setup 完成，哪些 engineering skills 现在从这些文件读。说明可稍后直接编辑 `docs/agents/*.md`——仅当要换 issue tracker 或从头 restart 时需重跑本 skill。
