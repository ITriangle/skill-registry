# Issue tracker: GitLab

本 repo 的 issue 和 spec 是 GitLab issue。所有操作用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI。

## 惯例

- **创建 issue**：`glab issue create --title "..." --description "..."`。多行 description 用 heredoc。`--description -` 打开编辑器。
- **读 issue**：`glab issue view <number> --comments`。机器可读用 `-F json`。
- **列 issue**：`glab issue list -F json`，加适当 `--label` 过滤。
- **评论 issue**：`glab issue note <number> --message "..."`。GitLab 称 comment 为「notes」。
- **加/去 label**：`glab issue update <number> --label "..."` / `--unlabel "..."`。多 label 可逗号分隔或重复 flag。
- **关闭**：`glab issue close <number>`。`glab issue close` 不接受 closing comment，先用 `glab issue note <number> --message "..."` 发帖，再关闭。
- **Merge requests**：GitLab 称 PR 为「merge request」。用 `glab mr create`、`glab mr view`、`glab mr note` 等——与 `gh pr ...` 同形，用 `mr` 代 `pr`，`note`/`--message` 代 `comment`/`--body`。

从 `git remote -v` 推断 repo——在 clone 内运行 `glab` 会自动推断。

## Merge requests 作为 triage 面

**MRs as request surface: no.** _（若本 repo 把外部 merge request 当功能请求，设为 `yes`；`/triage` 读此 flag。）_

设为 `yes` 时，MR 与 issue 走相同 label 和 state，用 `glab mr` 等价：

- **读 MR**：`glab mr view <number> --comments`，diff 用 `glab mr diff <number>`。
- **列 triage 用外部 MR**：`glab mr list -F json`，只保留作者非项目 member/owner 的 MR（贡献者 MR，非维护者 in-flight 工作）。
- **评论 / label / 关闭**：`glab mr note`、`glab mr update --label`/`--unlabel`、`glab mr close`。

与 GitHub 不同，GitLab issue 与 MR 编号分开，知道 maintainer 指哪一面后 `#42` 无歧义。

## 当 skill 说「publish to the issue tracker」

创建 GitLab issue。

## 当 skill 说「fetch the relevant ticket」

运行 `glab issue view <number> --comments`。

## Wayfinding 操作

由 `/wayfinder` 使用。**地图**是单个 issue，**子** issue 为 ticket。

- **Map**：单个 issue，label `wayfinder:map`，body 含 Notes / Decisions-so-far / Fog。`glab issue create --label wayfinder:map`。（有原生 epic 的 GitLab tier，epic 可持地图；labelled issue 处处可用。）
- **子 ticket**：description 顶 `Part of #<map>`，labels `wayfinder:<type>`（`research`/`prototype`/`grilling`/`task`）。claim 后分给 driving dev。
- **Blocking**：GitLab **原生 blocking link**——canonical、UI 可见。用 quick action `/blocked_by #<n>` 作为 note 发布（`glab issue note <child> --message "/blocked_by #<blocker>"`）。原生 blocking link 是 Premium/Ultimate；免费 tier 或不可用时回退 description 顶 `Blocked by: #<n>, #<n>`。每个 blocker 关闭则 unblocked。
- **Frontier query**：`glab issue list -F json` scoped 到地图子项，drop 有 open blocker 的——原生 `blocked_by` 链到 open issue（`glab api projects/:id/issues/:iid/links`），或 `Blocked by` 行中 open issue——或有 assignee 的；地图顺序第一个胜出。
- **Claim**：`glab issue update <n> --assignee @me`——会话首次写入。
- **Resolve**：`glab issue note <n> --message "<answer>"`，然后 `glab issue close <n>`，再把 context pointer（gist + link）追加到地图 Decisions-so-far。
