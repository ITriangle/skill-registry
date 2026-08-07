# Issue tracker: Local Markdown

本 repo 的 issue 和 spec 是 `.scratch/` 中的 markdown 文件。

## 惯例

- 每功能一目录：`.scratch/<feature-slug>/`
- spec 是 `.scratch/<feature-slug>/spec.md`
- 实现 issue 是每个 ticket 一个文件：`.scratch/<feature-slug>/issues/<NN>-<slug>.md`，从 `01` 编号——从不是单个合并 tickets 文件
- triage 状态记录为每个 issue 文件顶部附近的 `Status:` 行（role 字符串见 `triage-labels.md`）
- 评论与对话历史追加到文件底 `## Comments` 下

## 当 skill 说「publish to the issue tracker」

在 `.scratch/<feature-slug>/` 下建新文件（必要时建目录）。

## 当 skill 说「fetch the relevant ticket」

读引用路径的文件。用户通常直接传路径或 issue 编号。

## Wayfinding 操作

由 `/wayfinder` 使用。**地图**是一个文件，每个 ticket 一个**子**文件。

- **Map**：`.scratch/<effort>/map.md`——Notes / Decisions-so-far / Fog body。
- **子 ticket**：`.scratch/<effort>/issues/NN-<slug>.md`，从 `01` 编号，body 含问题。`Type:` 行记 ticket 类型（`research`/`prototype`/`grilling`/`task`）；`Status:` 行记 `claimed`/`resolved`。
- **Blocking**：顶部附近 `Blocked by: NN, NN`。所列每个文件 `resolved` 则 unblocked。
- **Frontier**：扫描 `.scratch/<effort>/issues/` 找 open、unblocked、unclaimed 文件；按编号第一个胜出。
- **Claim**：设 `Status: claimed` 并在任何工作前保存。
- **Resolve**：在 `## Answer` 下追加答案，设 `Status: resolved`，再把 context pointer（gist + link）追加到 `map.md` 的 Decisions-so-far。
