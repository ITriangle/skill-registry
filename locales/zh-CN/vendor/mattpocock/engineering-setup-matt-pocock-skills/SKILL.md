---
name: setup-matt-pocock-skills
description: 为当前仓库配置工程技能所需的 issue tracker、分诊标签词汇和领域文档布局。在首次使用其他工程技能前运行一次。
disable-model-invocation: true
---

# 配置 Matt Pocock 技能

搭建工程技能所依赖的仓库级配置：

- **Issue tracker**——issue 存放位置（默认 GitHub；也原生支持本地 Markdown）
- **分诊标签**——五种标准分诊角色所使用的字符串
- **领域文档**——`CONTEXT.md` 和 ADR 的位置，以及读取这些文档的规则

这是一个由提示驱动的技能，而非确定性脚本。先探索并展示发现，获得用户确认后再写入。

## 流程

### 1. 探索

检查当前仓库，了解初始状态。读取实际存在的内容，不要自行假设：

- `git remote -v` 和 `.git/config`——这是 GitHub 仓库吗？具体是哪个？
- 仓库根目录的 `AGENTS.md` 和 `CLAUDE.md`——是否存在其一？其中是否已有 `## Agent skills` 章节？
- 根目录的 `CONTEXT.md` 和 `CONTEXT-MAP.md`
- `docs/adr/` 以及所有 `src/*/docs/adr/` 目录
- `docs/agents/`——本技能之前的输出是否已存在？
- `.scratch/`——是否表明仓库已采用本地 Markdown issue tracker 约定？

### 2. 展示发现并提问

总结已有内容和缺失内容。然后**一次一个**地引导用户完成以下三项决策：展示一个部分，取得用户回答，再进入下一部分。不要一次抛出全部三个问题。

假设用户不了解这些术语。每部分先做简短解释（它是什么、为什么技能需要它、选择不同方案会改变什么），再展示选项和默认值。

**A 部分——Issue tracker。**

> 说明：“issue tracker”是当前仓库保存 issue 的地方。`to-tickets`、`triage`、`to-spec`、`qa` 等技能会读写它——它们必须知道应该调用 `gh issue create`、在 `.scratch/` 下写 Markdown 文件，还是遵循你描述的其他流程。请选择这个仓库实际追踪工作的地方。

默认倾向：这些技能是围绕 GitHub 设计的。如果 `git remote` 指向 GitHub，建议使用 GitHub；如果指向 GitLab（`gitlab.com` 或自托管主机），建议使用 GitLab。其他情况（或用户另有偏好）提供：

- **GitHub**——issue 位于仓库的 GitHub Issues（使用 `gh` CLI）
- **GitLab**——issue 位于仓库的 GitLab Issues（使用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI）
- **本地 Markdown**——issue 是仓库 `.scratch/<feature>/` 下的文件（适合个人项目或无远端仓库）
- **其他**（Jira、Linear 等）——请用户用一段话描述流程；技能将其记录为自由文本

当且仅当用户选择 **GitHub** 或 **GitLab** 时，再问一个后续问题：

> 说明：开源仓库收到的功能请求常以 pull request 而不只是 issue 的形式出现——PR 可以理解为附带代码的 issue。开启后，`/triage` 会将*外部* PR 纳入同一队列，并使用与 issue 相同的标签和状态处理（协作者正在进行的 PR 不受影响）。如果 PR 不是项目的需求入口，请保持关闭。

- **是否把 PR 当作需求入口**——是/否（默认：否）。将答案记录到 `docs/agents/issue-tracker.md`。本地 Markdown 和其他 tracker 没有 PR，跳过此问题。

**B 部分——分诊标签词汇。**

> 说明：`triage` 技能处理新 issue 时，会让它依次进入一套状态机：需要评估、等待报告者补充、可由 AFK agent 领取、需要人工处理或不予修复。为此，它必须应用与你实际配置一致的标签（或 tracker 中的等价状态）。如果仓库已有不同的标签名（例如用 `bug:triage` 而非 `needs-triage`），请在这里映射，防止技能错误创建重复标签。

五种标准角色：

- `needs-triage`——维护者需要评估
- `needs-info`——等待报告者补充信息
- `ready-for-agent`——规格完整，可供 AFK agent 在没有人工上下文时领取
- `ready-for-human`——需要人工实现
- `wontfix`——不会处理

默认值：每种角色使用与角色名相同的字符串。询问用户是否要覆盖任意项。如果 tracker 中还没有标签，默认值即可。

**C 部分——领域文档。**

> 说明：一些技能（`improve-codebase-architecture`、`diagnosing-bugs`、`tdd`）会读取 `CONTEXT.md` 学习项目领域语言，并从 `docs/adr/` 了解过往架构决策。它们需要知道仓库只有一个全局上下文，还是存在多个上下文（例如前后端各自独立的 monorepo），从而到正确位置读取文档。

确认布局：

- **单上下文**——根目录有一个 `CONTEXT.md` 和 `docs/adr/`。大多数仓库采用此布局。
- **多上下文**——根目录的 `CONTEXT-MAP.md` 指向各上下文自己的 `CONTEXT.md`（通常用于 monorepo）。

### 3. 确认并编辑

向用户展示以下草稿：

- 将加入 `CLAUDE.md` 或 `AGENTS.md` 的 `## Agent skills` 区块（选择规则见第 4 步）
- `docs/agents/issue-tracker.md`、`docs/agents/triage-labels.md`、`docs/agents/domain.md` 的内容

允许用户在写入前修改。

### 4. 写入

**选择要编辑的文件：**

- 如果存在 `CLAUDE.md`，编辑它。
- 否则如果存在 `AGENTS.md`，编辑它。
- 如果两者都不存在，询问用户要创建哪一个——不要代替用户选择。

当 `CLAUDE.md` 已存在时，绝不要另建 `AGENTS.md`（反之亦然）——始终编辑已有文件。

如果所选文件已有 `## Agent skills` 区块，就原地更新其内容，不要追加重复区块。不要覆盖周边章节中的用户编辑。

区块内容：

```markdown
## Agent skills

### Issue tracker

[用一行说明 issue 在哪里追踪，以及外部 PR 是否作为分诊入口]。参见 `docs/agents/issue-tracker.md`。

### Triage labels

[用一行总结标签词汇]。参见 `docs/agents/triage-labels.md`。

### Domain docs

[用一行总结布局——“单上下文”或“多上下文”]。参见 `docs/agents/domain.md`。
```

然后以本技能目录中的种子模板为起点写入三个文档：

- [issue-tracker-github.md](./issue-tracker-github.md)——GitHub issue tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md)——GitLab issue tracker
- [issue-tracker-local.md](./issue-tracker-local.md)——本地 Markdown issue tracker
- [triage-labels.md](./triage-labels.md)——标签映射
- [domain.md](./domain.md)——领域文档读取规则和布局

对于“其他”issue tracker，根据用户描述从头编写 `docs/agents/issue-tracker.md`。

### 5. 完成

告诉用户配置已完成，并说明哪些工程技能会读取这些文件。提醒用户之后可以直接编辑 `docs/agents/*.md`；只有切换 issue tracker 或从头重新配置时，才需要再次运行本技能。
