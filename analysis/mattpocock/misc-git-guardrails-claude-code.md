# vendor/mattpocock/misc-git-guardrails-claude-code

- Skill name: `git-guardrails-claude-code`
- Current status: `candidate`
- Description: Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code.

## Trigger Review

- Review whether the description is narrow enough for implicit invocation.
- Confirm explicit trigger words are front-loaded.

## Dependencies And Risk

- Scripts: scripts/block-dangerous-git.sh
- References: none detected
- Mentions: filesystem, shell

## Recommendation

- Suggested status: `candidate`
- Approve only after checking license, script behavior, and trigger overlap.
