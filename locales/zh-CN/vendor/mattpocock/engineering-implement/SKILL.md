---
name: implement
description: 当用户已有 PRD、issue 或明确工作项，需要按规格实现代码改动时使用。 当需求尚未澄清、需要先研究或只做代码评审时不要用。
---

# 中文导读

- 使用场景：当用户已有 PRD、issue 或明确工作项，需要按规格实现代码改动时使用。
- 不适用：当需求尚未澄清、需要先研究或只做代码评审时不要用。

# 上游说明原文

Implement the work described by the user in the spec or tickets.

Use /tdd where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, use /code-review to review the work.

Commit your work to the current branch.
