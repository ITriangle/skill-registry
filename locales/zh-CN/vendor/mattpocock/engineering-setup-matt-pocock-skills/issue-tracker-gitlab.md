# Issue tracker：GitLab

当前仓库的 issue 和 PRD 以 GitLab issue 保存。所有操作都使用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI。

## 约定

- **创建 issue**：`glab issue create --title "..." --description "..."`。多行描述使用 heredoc。传入 `--description -` 可打开编辑器。
- **读取 issue**：`glab issue view <number> --comments`。使用 `-F json` 获取机器可读输出。
- **列出 issue**：`glab issue list -F json`，并添加适当的 `--label` 筛选器。
- **评论 issue**：`glab issue note <number> --message "..."`。GitLab 将评论称为 note。
- **添加/移除标签**：`glab issue update <number> --label "..."` / `--unlabel "..."`。多个标签可以逗号分隔，也可以重复传入参数。
- **关闭**：`glab issue close <number>`。`glab issue close` 不接受关闭评论，因此先用 `glab issue note <number> --message "..."` 发布说明，再关闭。
- **Merge request**：GitLab 将 PR 称为 merge request。使用 `glab mr create`、`glab mr view`、`glab mr note` 等命令——整体形态与 `gh pr ...` 相同，只需用 `mr` 代替 `pr`，并以 `note`/`--message` 代替 `comment`/`--body`。

从 `git remote -v` 推断仓库——在 clone 内运行时，`glab` 会自动完成此操作。

## 将 merge request 作为分诊入口

**是否把 MR 当作需求入口：否。**（如果当前仓库把外部 merge request 视为功能请求，设为 `yes`；`/triage` 会读取此标志。）

设为 `yes` 后，MR 使用与 issue 相同的标签和状态，并通过对应的 `glab mr` 命令进入同一流程：

- **读取 MR**：`glab mr view <number> --comments`，并用 `glab mr diff <number>` 获取 diff。
- **列出待分诊的外部 MR**：`glab mr list -F json`，只保留作者不是项目成员/所有者的 MR（贡献者的 MR，而非维护者正在进行的工作）。
- **评论/标签/关闭**：`glab mr note`、`glab mr update --label`/`--unlabel`、`glab mr close`。

与 GitHub 不同，GitLab 分别为 issue 和 MR 编号；一旦知道维护者所指的入口，`#42` 就没有歧义。

## 当技能要求“发布到 issue tracker”时

创建一个 GitLab issue。

## 当技能要求“获取相关 ticket”时

运行 `glab issue view <number> --comments`。

## 寻路操作

由 `/wayfinder` 使用。**地图**是一个 issue，**child** ticket 是它的子 issue。

- **地图**：带 `wayfinder:map` 标签的单个 issue，正文包含 Notes / Decisions-so-far / Fog。使用 `glab issue create --label wayfinder:map` 创建。（在支持原生 epic 的 GitLab 套餐中，也可以由 epic 承载地图；带标签的 issue 在所有套餐中都可用。）
- **子 ticket**：正文顶部带 `Part of #<map>` 的 issue，标签为 `wayfinder:<type>`（`research`/`prototype`/`grilling`/`task`）。领取后，将 ticket 分配给负责推进的开发者。
- **阻塞关系**：使用 GitLab **原生 blocking link**，它是标准且在 UI 可见的表示。以 note 形式发布 `/blocked_by #<n>` quick action：`glab issue note <child> --message "/blocked_by #<blocker>"`。原生阻塞链接属于 Premium/Ultimate 功能；免费套餐（或功能不可用时）回退为描述顶部的 `Blocked by: #<n>, #<n>` 行。所有阻塞项关闭后，ticket 才解除阻塞。
- **前沿查询**：使用 `glab issue list -F json` 列出地图的子项，移除存在开放阻塞项——指向开放 issue 的原生 `blocked_by` 链接（`glab api projects/:id/issues/:iid/links`），或 `Blocked by` 行中的开放 issue——以及已有 assignee 的项；按地图顺序取第一个。
- **领取**：`glab issue update <n> --assignee @me`——这是会话中的首次写操作。
- **解决**：运行 `glab issue note <n> --message "<answer>"`，再运行 `glab issue close <n>`，然后把上下文指针（摘要 + 链接）追加到地图的 Decisions-so-far。
