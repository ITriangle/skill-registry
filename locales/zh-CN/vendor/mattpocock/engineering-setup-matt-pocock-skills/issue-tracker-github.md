# Issue tracker：GitHub

当前仓库的 issue 和 PRD 以 GitHub issue 保存。所有操作都使用 `gh` CLI。

## 约定

- **创建 issue**：`gh issue create --title "..." --body "..."`。多行正文使用 heredoc。
- **读取 issue**：`gh issue view <number> --comments`，用 `jq` 筛选评论，并同时获取标签。
- **列出 issue**：`gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'`，并使用适当的 `--label` 和 `--state` 筛选器。
- **评论 issue**：`gh issue comment <number> --body "..."`
- **添加/移除标签**：`gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **关闭**：`gh issue close <number> --comment "..."`

从 `git remote -v` 推断仓库——在 clone 内运行时，`gh` 会自动完成此操作。

## 将 pull request 作为分诊入口

**是否把 PR 当作需求入口：否。**（如果当前仓库把外部 PR 视为功能请求，设为 `yes`；`/triage` 会读取此标志。）

设为 `yes` 后，PR 使用与 issue 相同的标签和状态，并通过对应的 `gh pr` 命令进入同一流程：

- **读取 PR**：`gh pr view <number> --comments`，并用 `gh pr diff <number>` 获取 diff。
- **列出待分诊的外部 PR**：`gh pr list --state open --json number,title,body,labels,author,authorAssociation,comments`，只保留 `authorAssociation` 为 `CONTRIBUTOR`、`FIRST_TIME_CONTRIBUTOR` 或 `NONE` 的项（排除 `OWNER`/`MEMBER`/`COLLABORATOR`）。
- **评论/标签/关闭**：`gh pr comment`、`gh pr edit --add-label`/`--remove-label`、`gh pr close`。

GitHub 的 issue 和 PR 共用同一编号空间，因此单独的 `#42` 可能指向任意一种对象——先用 `gh pr view 42` 解析，失败后再尝试 `gh issue view 42`。

## 当技能要求“发布到 issue tracker”时

创建一个 GitHub issue。

## 当技能要求“获取相关 ticket”时

运行 `gh issue view <number> --comments`。

## 寻路操作

由 `/wayfinder` 使用。**地图**是一个 issue，**child** ticket 是它的子 issue。

- **地图**：带 `wayfinder:map` 标签的单个 issue，正文包含 Notes / Decisions-so-far / Fog。使用 `gh issue create --label wayfinder:map` 创建。
- **子 ticket**：作为 GitHub sub-issue 链接到地图的 issue（通过 sub-issues endpoint 调用 `gh api`）。如果未启用 sub-issues，就把子项加入地图正文的任务列表，并在子 issue 正文顶部写 `Part of #<map>`。标签为 `wayfinder:<type>`（`research`/`prototype`/`grilling`/`task`）。领取后，把 ticket 分配给负责推进的开发者。
- **阻塞关系**：使用 GitHub **原生 issue dependencies**，它是标准且在 UI 可见的表示。调用 `gh api --method POST repos/<owner>/<repo>/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-db-id>` 添加边；其中 `<blocker-db-id>` 是阻塞 issue 的数字 **database id**（通过 `gh api repos/<owner>/<repo>/issues/<n> --jq .id` 获取，*不是* `#number` 或 `node_id`）。GitHub 的 `issue_dependencies_summary.blocked_by` 只报告仍开放的阻塞项，是实时门禁。依赖功能不可用时，回退为子 issue 正文顶部的 `Blocked by: #<n>, #<n>` 行。所有阻塞项关闭后，ticket 才解除阻塞。
- **前沿查询**：列出地图下开放的子项（`gh issue list --state open`，限定在地图的 sub-issues/任务列表范围），移除存在开放阻塞项（`issue_dependencies_summary.blocked_by > 0`，或 `Blocked by` 行指向开放 issue）或已有 assignee 的项；按地图顺序取第一个。
- **领取**：`gh issue edit <n> --add-assignee @me`——这是会话中的首次写操作。
- **解决**：运行 `gh issue comment <n> --body "<answer>"`，再运行 `gh issue close <n>`，然后把上下文指针（摘要 + 链接）追加到地图的 Decisions-so-far。
