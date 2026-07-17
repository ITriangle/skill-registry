---
name: resolving-merge-conflicts
description: 当仓库正在 merge 或 rebase 且存在冲突，需要解决冲突并保持双方意图时使用。 当没有进行中的冲突，或用户只是要普通变更、评审、提交时不要用。
---

# 中文导读

- 使用场景：当仓库正在 merge 或 rebase 且存在冲突，需要解决冲突并保持双方意图时使用。
- 不适用：当没有进行中的冲突，或用户只是要普通变更、评审、提交时不要用。

# 上游说明原文

1. **See the current state** of the merge/rebase. Check git history, and the conflicting files.

2. **Find the primary sources** for each conflict. Understand deeply why each change was made, and what the original intent was. Read the commit messages, check the PRs, check original issues/tickets.

3. **Resolve each hunk.** Preserve both intents where possible. Where incompatible, pick the one matching the merge's stated goal and note the trade-off. Do **not** invent new behaviour. Always resolve; never `--abort`.

4. Discover the project's **automated checks** and run them — typically typecheck, then tests, then format. Fix anything the merge broke.

5. **Finish the merge/rebase.** Stage everything and commit. If rebasing, continue the rebase process until all commits are rebased.
