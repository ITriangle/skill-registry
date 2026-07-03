# vendor/mattpocock/engineering-code-review

- Skill name: `code-review`
- Current status: `candidate`
- Description: Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/PRD asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to "review since X".

## Trigger Review

- Review whether the description is narrow enough for implicit invocation.
- Confirm explicit trigger words are front-loaded.

## Dependencies And Risk

- Scripts: none detected
- References: none detected
- Mentions: filesystem, shell

## Recommendation

- Suggested status: `candidate`
- Approve only after checking license, script behavior, and trigger overlap.
