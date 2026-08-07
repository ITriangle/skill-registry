# Issue tracker: GitHub

本 repo 的 issue 和 spec 是 GitHub issue。所有操作用 `gh` CLI。

## 惯例

- **创建 issue**：`gh issue create --title "..." --body "..."`。多行 body 用 heredoc。
- **读 issue**：`gh issue view <number> --comments`，用 `jq` 过滤 comment，并取 labels。
- **列 issue**：`gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'`，加适当 `--label` 和 `--state` 过滤。
- **评论 issue**：`gh issue comment <number> --body "..."`
- **加/去 label**：`gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **关闭**：`gh issue close <number> --comment "..."`

从 `git remote -v` 推断 repo——在 clone 内运行 `gh` 会自动推断。

## Pull requests 作为 triage 面

**PRs as request surface: no.** _（若本 repo 把外部 PR 当功能请求，设为 `yes`；`/triage` 读此 flag。）_

设为 `yes` 时，PR 与 issue 走相同 label 和 state，用 `gh pr` 等价：

- **读 PR**：`gh pr view <number> --comments`，diff 用 `gh pr diff <number>`。
- **列 triage 用外部 PR**：`gh pr list --state open --json number,title,body,labels,author,authorAssociation,comments`，只保留 `authorAssociation` 为 `CONTRIBUTOR`、`FIRST_TIME_CONTRIBUTOR` 或 `NONE`（drop `OWNER`/`MEMBER`/`COLLABORATOR`）。
- **评论 / label / 关闭**：`gh pr comment`、`gh pr edit --add-label`/`--remove-label`、`gh pr close`。

GitHub issue 与 PR 共享编号空间，裸 `#42` 可能是任一——用 `gh pr view 42`，失败则 `gh issue view 42`。

## 当 skill 说「publish to the issue tracker」

创建 GitHub issue。

## 当 skill 说「fetch the relevant ticket」

运行 `gh issue view <number> --comments`。

## Wayfinding 操作

由 `/wayfinder` 使用。**地图**是单个 issue，**子** issue 为 ticket。

- **Map**：单个 issue，label `wayfinder:map`，body 含 Notes / Decisions-so-far / Fog。`gh issue create --label wayfinder:map`。
- **子 ticket**：通过 GitHub sub-issue 链到地图的 issue（sub-issues endpoint 上 `gh api`）。未启用 sub-issue 时，把子项加入地图 body 的 task list，子 body 顶加 `Part of #<map>`。Labels：`wayfinder:<type>`（`research`/`prototype`/`grilling`/`task`）。claim 后 ticket 分给 driving dev。
- **Blocking**：GitHub **原生 issue 依赖**——canonical、UI 可见表示。用 `gh api --method POST repos/<owner>/<repo>/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-db-id>` 加边，`<blocker-db-id>` 是 blocker 的数值**数据库 id**（`gh api repos/<owner>/<repo>/issues/<n> --jq .id`，*不是* `#number` 或 `node_id`）。GitHub 报告 `issue_dependencies_summary.blocked_by`（仅 open blocker——live gate）。依赖不可用时，回退子 body 顶 `Blocked by: #<n>, #<n>`。每个 blocker 关闭则 unblocked。
- **Frontier query**：列地图 open 子项（`gh issue list --state open`，scoped 到地图 sub-issue / task list），drop 有 open blocker 的（`issue_dependencies_summary.blocked_by > 0`，或 `Blocked by` 行中 open issue）或有 assignee 的；地图顺序第一个胜出。
- **Claim**：`gh issue edit <n> --add-assignee @me`——会话首次写入。
- **Resolve**：`gh issue comment <n> --body "<answer>"`，然后 `gh issue close <n>`，再把 context pointer（gist + link）追加到地图 Decisions-so-far。
