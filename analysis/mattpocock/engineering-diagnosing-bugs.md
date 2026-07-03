# vendor/mattpocock/engineering-diagnosing-bugs

- Skill name: `diagnosing-bugs`
- Current status: `candidate`
- Description: Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow.

## Trigger Review

- Review whether the description is narrow enough for implicit invocation.
- Confirm explicit trigger words are front-loaded.

## Dependencies And Risk

- Scripts: scripts/hitl-loop.template.sh
- References: none detected
- Mentions: network, filesystem, shell

## Recommendation

- Suggested status: `candidate`
- Approve only after checking license, script behavior, and trigger overlap.
