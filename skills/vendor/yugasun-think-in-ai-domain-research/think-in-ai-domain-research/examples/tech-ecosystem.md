# Example: Technical Ecosystem / 技术生态

## Input

- Official documentation for a framework/library (e.g., a state management library)
- 3-5 sample code snippets from official tutorials
- Current project codebase that needs to integrate with this library

## Process

### Step 1: Source Inventory

| Source | Type | What It Can Support | What It Cannot Support |
|--------|------|---------------------|----------------------|
| Official Docs | Methodology | API surface, concepts, best practices, constraints | How it fits YOUR project |
| Sample Code | Evidence | Working patterns, idiomatic usage | Scalability, edge cases in production |
| Current Codebase | Evidence | Existing patterns, constraints, tech debt | What the new library can do |

### Step 2: Compile Rules from Documentation

Key concepts:
- **Store**: centralized state container
- **Action**: description of a state change event
- **Reducer**: pure function that computes new state from current state + action
- **Middleware**: interceptor for side effects (async, logging, etc.)
- **Selector**: derived/computed state query

Core runtime model:
```
Dispatch(action) → Middleware chain → Reducer(currentState, action) → NewState → Notify subscribers
```

Constraints discovered:
- Reducers must be pure functions (no side effects)
- State is immutable (must return new objects, not mutate)
- Middleware order matters (logging before async, etc.)
- Selectors should be memoized for performance

### Step 3: Align Samples and Current Codebase

| Concept | Official Example | Current Codebase | Transferable? |
|---------|-----------------|-----------------|---------------|
| State shape | Flat, normalized | Nested, denormalized | Partially — need refactoring |
| Async handling | Middleware-based | Direct API calls in components | Yes — adopt middleware pattern |
| Testing | Reducer unit tests | No state tests | Yes — add reducer tests |
| DevTools | Built-in support | None | Yes — zero cost to add |

### Step 4: Domain Model Output

**Integration Points:**
- Replace current nested state with normalized structure
- Extract API calls from components into middleware
- Add reducer unit tests for critical state transitions

**Constraints:**
- Cannot adopt incrementally per-component (library requires global store)
- Must refactor existing state shape before migration
- Middleware must be ordered: validation → logging → async → error handling

**What Transfers vs. What Doesn't:**
- ✅ Reducer pattern, action creators, middleware pattern
- ✅ DevTools integration, time-travel debugging
- ❌ Sample's flat state shape (need to adapt to our domain model)
- ❌ Sample's simple sync actions (our use case needs complex async chains)

### Step 5: Expert Calibration Questions

1. Should we normalize all state upfront, or migrate module by module?
2. Is the middleware ordering documented or convention-based?
3. What's the team's experience level with functional programming / immutable patterns?
4. Are there performance benchmarks for our expected state size (~10K items)?

### Step 6: Downstream Artifacts

| Domain Insight | Requirement | Acceptance Criteria | Test Matrix |
|----------------|-------------|-------------------|-------------|
| Need normalized state | Refactor state shape | All selectors pass with new shape | Test each domain module |
| Async in middleware | Extract API calls from components | No direct fetch() in components | Grep codebase for violations |
| Immutable updates | Use spread/immer for all updates | No Object.assign to state | Lint rule: no state mutation |

## Output Focus

- Core concepts and runtime model
- Integration points and constraints
- Examples that transfer to this project vs. examples that do not
- Downstream artifacts: implementation plan, API contract, test matrix
