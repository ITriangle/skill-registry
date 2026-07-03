# vendor/mattpocock/deprecated-qa

- Skill name: `qa`
- Current status: `analysis-only`
- Description: Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues. Explores the codebase in the background for context and domain language. Use when user wants to report bugs, do QA, file issues conversationally, or mentions "QA session".

## Trigger Review

- Review whether the description is narrow enough for implicit invocation.
- Confirm explicit trigger words are front-loaded.

## Dependencies And Risk

- Scripts: none detected
- References: none detected
- Mentions: filesystem

## Recommendation

- Suggested status: `candidate`
- Approve only after checking license, script behavior, and trigger overlap.
