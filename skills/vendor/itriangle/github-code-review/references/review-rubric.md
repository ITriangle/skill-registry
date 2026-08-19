# Deep Review Rubric

Read this reference only after the basic quality gate in `SKILL.md` passes. Apply the repository's documented behavior and constraints before this baseline.

## Correctness and Requirements

- Compare behavior with the PR description, linked issue, specification, public contract, and existing tests.
- Trace changed conditions, state transitions, data transformations, boundary values, empty inputs, nullability, partial failures, retries, and cleanup paths.
- Check whether success and error results reach callers with the promised meaning.
- Look for off-by-one errors, inverted conditions, stale state, unreachable branches, accidental fallthrough, and incorrect default behavior.
- Confirm that a fix addresses the actual failure path rather than only the demonstrated example.

## Security and Privacy

- Check authentication and authorization at the operation and object level.
- Trace untrusted input through queries, templates, shell commands, paths, redirects, parsers, and deserialization.
- Check secret handling, sensitive logging, data exposure, insecure defaults, and privilege expansion.
- Verify that validation occurs at a trusted boundary and cannot be bypassed through an alternate path.
- Report a security finding only with a concrete source, sink, missing control, or violated policy.

## Data Integrity, State, and Concurrency

- Check transaction boundaries, atomicity, idempotency, duplicate delivery, ordering, lost updates, and retry behavior.
- Verify that partial failure cannot leave externally visible state inconsistent.
- Examine caches, background jobs, event handlers, async tasks, locks, and shared mutable state for races or stale reads.
- Check schema, serialization, and persistence changes for forward/backward readability and safe defaults.

## Compatibility and Interfaces

- Check public APIs, CLI flags, configuration, events, schemas, stored data, and exported types for breaking changes.
- Verify callers and consumers, including cases outside the changed file.
- Check migration, rollout, downgrade, and mixed-version behavior when the change crosses a deployment boundary.
- Distinguish intentional contract changes from accidental incompatibility.

## Performance and Resource Use

- Look for unbounded work, N+1 access, repeated parsing or allocation, full scans, excessive network calls, and blocking operations in asynchronous paths.
- Check memory, file descriptors, connections, goroutines/threads/tasks, and cleanup on both success and failure.
- Require a realistic input size or execution path before reporting a performance problem.
- Treat optimization ideas without demonstrated risk as P3 at most.

## Tests and Verification

- Map each changed behavior and failure path to existing or added tests.
- Check boundary, negative, permission, concurrency, retry, and regression coverage where relevant.
- Ensure tests exercise the public behavior rather than merely mirroring implementation details.
- Look for assertions that can pass without proving the intended result, flaky timing assumptions, and mocks that bypass the changed integration.
- Do not require tests for comments, mechanical metadata, or behavior already proven at the appropriate lower layer.

## Design and Maintainability

- Check whether responsibilities remain cohesive and whether the change creates avoidable coupling, duplication, hidden global state, or divergent sources of truth.
- Examine abstractions only when they obscure behavior, duplicate an existing seam, or add scope not required by the change.
- Check that control flow, error ownership, and lifecycle are understandable from the relevant module interface.
- Keep subjective refactoring preferences non-blocking unless they create a concrete defect or violate a repository rule.

## Error Handling and Observability

- Verify that errors are preserved, classified, retried, surfaced, or translated at the correct boundary.
- Check timeouts, cancellation, fallback behavior, and cleanup.
- Ensure logs, metrics, traces, and alerts provide useful signals without exposing secrets or creating excessive noise.
- Check that operators can distinguish expected user errors from system failures when operational behavior changes.

## Documentation and Delivery

- Check user-facing, API, configuration, migration, and operational documentation when the change alters those contracts.
- Verify comments explain non-obvious reasons rather than restating code.
- Check feature flags, environment variables, deployment order, and rollback assumptions when applicable.
- Report missing documentation only when a concrete consumer or operator would otherwise be misled.

## Finding Quality Filter

Keep a finding only when all applicable answers are clear:

1. What changed behavior or rule is involved?
2. Where is the tightest useful location?
3. Under what concrete input, state, or call path does it matter?
4. What observable impact follows?
5. Is the issue introduced, exposed, or materially worsened by this change?
6. What bounded repair direction would address it?

If the answer depends on unknown external behavior, inspect the owning code or authoritative contract. If it remains unknown, record it as residual risk rather than a finding.
