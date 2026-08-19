---
name: github-code-review
description: Perform a read-only, gated review of a GitHub pull request or local Git changes. Use for PR URLs or numbers, branches, commit ranges, staged or unstaged changes, pre-push reviews, and requests such as code review, review this PR, 审 PR, 代码审查, or 检查提交前改动. Do not use to implement fixes or publish a GitHub review.
---

# GitHub Code Review

Review changes without changing the repository or GitHub. Apply the repository's own rules first, then use the personal baseline in [references/review-rubric.md](references/review-rubric.md).

Use two strict stages:

1. Gate on code standards, naming, and file length.
2. Only after the gate passes, review behavior and broader quality.

If stage 1 fails or cannot be completed reliably, stop. Do not perform stage 2.

## Preserve Read-Only Operation

- Do not post comments, submit reviews, approve, request changes, label, merge, close, or otherwise mutate GitHub.
- Do not edit files, run fix-mode formatters, update snapshots, push, fetch, checkout, create or delete branches, or change repository state.
- Permit tests and check-mode tooling only when they are expected not to modify tracked files. Note any transient cache or build output.
- Check repository status before and after validation. If a command changes tracked files, stop and report it; do not revert user work.
- Do not inspect token values, credential files, or authentication environment variables. Use a host-provided read-only GitHub connector when available; otherwise use authenticated `gh` read commands. Use `gh auth status` only to diagnose authentication.
- If PR context cannot be read safely, ask for a patch or review a locally available diff. State the missing context instead of claiming a complete PR review.

## Resolve the Review Target

Identify one mode and keep its comparison fixed throughout the review.

### GitHub pull request

For a PR URL or number, collect read-only metadata: title, body, author, base and head refs, head SHA, draft state, changed files, diff, and check results. Read existing discussion when it affects intent or prevents duplicate findings.

Use the PR base ref as the comparison base. Do not check out or fetch the PR. If full files are already available in the local repository, use them for context; otherwise rely on the PR diff and read-only GitHub content and disclose the limitation.

### Local changes

Use the user's stated scope exactly:

- Staged changes: `git diff --cached`.
- Unstaged changes: `git diff`.
- All tracked worktree changes against `HEAD`: `git diff HEAD`.
- Branch, tag, or commit baseline: validate it with `git rev-parse --verify`, then use `git diff <base>...HEAD` and `git log <base>..HEAD --oneline`.

When a branch review has no explicit base, prefer the repository's resolved remote default branch, then an existing `main`, then an existing `master`. Ask for the base if none resolves or more than one interpretation remains plausible. Do not silently assume `main`.

Fail early on an invalid ref or empty diff. Record the exact target, base, head, and changed-file list in the final coverage section.

## Gather Governing Context

Before judging the diff, inspect the rules that govern each changed file:

1. The nearest applicable `AGENTS.md` or equivalent agent instructions.
2. `CONTRIBUTING.md`, coding standards, architecture rules, and repository documentation.
3. Formatter, linter, type-checker, test, and file-length configuration.
4. The PR body, linked issue, specification, or commit messages describing intent.
5. Established conventions in adjacent code when no explicit rule exists.

An explicit repository rule overrides the personal baseline. Treat tool-enforced rules as tool results rather than restating every possible violation manually.

## Stage 1: Basic Quality Gate

Check these categories in order. Collect all reliable findings within stage 1, then stop the review if any exist.

### 1. Code standards

Run the repository's configured formatter, linter, type-checker, or policy checks in check-only mode when safe. Prefer commands scoped to changed files. Never invent a command or run a formatter that may rewrite files.

Report only violations supported by an applicable rule, configuration, check result, or clear established convention. Separate environment/tooling failures from code violations.

### 2. Naming

Check changed identifiers, files, modules, tests, configuration keys, and public API names. Require evidence from repository rules, language conventions, or consistent adjacent code. Do not fail the gate for subjective taste, unfamiliar vocabulary, or an abbreviation that is already established in the domain.

### 3. File length

Use a repository-configured maximum when one exists. Otherwise, set the maximum to **500 physical lines**.

Fail the gate when any changed, non-deleted code file is currently over the applicable maximum, even if it was already over the limit before this change. Include tests as code. Exclude only files demonstrably belonging to one of these classes:

- generated code;
- vendored or third-party code;
- lockfiles;
- migrations;
- snapshots;
- pure data files;
- binary files.

Do not infer that a file is generated merely because it is long. Use a generated marker, repository configuration, documented path, or established project convention.

### Gate decision

- **PASS:** all three checks completed and no reliable findings exist. Continue to stage 2.
- **FAIL:** at least one reliable finding exists. Report stage 1 findings and stop.
- **INCONCLUSIVE:** missing context or an unavailable check prevents a reliable gate decision. Report what is missing and stop.

## Stage 2: Deep Review

Read [references/review-rubric.md](references/review-rubric.md) in full only after stage 1 passes.

For each suspected issue:

1. Read enough surrounding code, callers, contracts, and tests to trace the affected behavior.
2. Confirm that the change introduces, exposes, or materially worsens the issue. Do not report unrelated pre-existing problems.
3. Run the narrowest safe test or check that can validate the claim when practical.
4. Discard speculative findings that lack a concrete trigger, impact, or violated requirement.

Prefer a small set of well-supported findings over a long checklist of possibilities.

## Severity

- **P0:** stop-ship issue with immediate, widespread impact such as destructive data loss or critical compromise.
- **P1:** high-impact correctness, security, availability, or compatibility defect likely to affect users or production.
- **P2:** actionable defect or substantial quality risk that should be fixed, but is not an emergency.
- **P3:** non-blocking improvement to tests, design, maintainability, naming, or documentation.

Stage 1 fails on any supported finding regardless of its P-level. Severity communicates impact; it does not override the gate.

## Report Findings First

Write in the user's language; default to Chinese when no preference is visible. Preserve code identifiers and commands verbatim.

For every finding, provide:

- `[P0-P3]` plus a concise, specific title;
- file and tight line location when available;
- the rule or evidence;
- the concrete impact or failure scenario;
- a bounded repair direction, without implementing it.

Then report:

- `基础门禁`: PASS, FAIL, or INCONCLUSIVE;
- `深度审查`: completed, not run because the gate failed, or not run because the gate was inconclusive;
- the reviewed target, base/head, files, and commands/checks used;
- residual risk and anything not verified.

If stage 2 completes with no reliable findings, say `未发现可靠问题`; do not claim the change is proven correct. Do not add praise merely to fill the report.
