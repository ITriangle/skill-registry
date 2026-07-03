# vendor/yugasun/aiops

- Skill name: `aiops`
- Current status: `candidate`
- Description: Flow Conductor for the aiops bundle. One entry — infers task type, shows plain-language steps, tracks journey in flow.state.yaml, dispatches skill + agent per phase.

## Trigger Review

- Review whether the description is narrow enough for implicit invocation.
- Confirm explicit trigger words are front-loaded.

## Dependencies And Risk

- Scripts: scripts/code_graph_query.py, scripts/flow_cli.py, scripts/gates.py, scripts/journey_state.py, scripts/phases.py, scripts/task_dag.py, scripts/test_code_graph.py, scripts/test_router.py
- References: none detected
- Mentions: shell

## Recommendation

- Suggested status: `candidate`
- Approve only after checking license, script behavior, and trigger overlap.
