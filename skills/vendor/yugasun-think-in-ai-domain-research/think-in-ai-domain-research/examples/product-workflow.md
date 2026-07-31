# Example: New Product Workflow / 新产品工作流

## Input

- PRD (Product Requirements Document) for a new feature
- 15-20 support tickets from similar existing features
- 3 meeting notes from cross-functional syncs

## Process

### Step 1: Source Inventory

| Source | Type | What It Can Support | What It Cannot Support |
|--------|------|---------------------|----------------------|
| PRD | Methodology | Intended workflow, user stories, acceptance criteria | Real-world edge cases |
| Support Tickets | Evidence | Actual failures, user confusion, workarounds | Intended design rationale |
| Meeting Notes | Evidence | Stakeholder disagreements, unresolved decisions | Final decisions (may be outdated) |

### Step 2: Compile Rules from PRD

Key objects:
- **Actor**: end user, admin, approver, system
- **State**: draft → submitted → under review → approved/rejected → completed
- **Transition**: trigger, guard condition, side effect
- **Exception**: timeout, escalation, rollback

Intended workflow:
```
User creates → Submits for review → Auto-route to approver → Approver decides → System executes → User notified
```

### Step 3: Align Tickets and Meeting Notes Against PRD

| Finding Type | Evidence | PRD Says | Tickets Show | Meeting Notes Confirm |
|--------------|----------|----------|-------------|---------------------|
| Conflict | Tickets #12, #15 | Auto-route based on amount | Manual routing required for amounts >$10K | Finance team insisted on manual review |
| Gap | Tickets #8, #19 | No mention of timeout | Users abandoned after 3-day wait | PM acknowledged: "we need a timeout rule" |
| Ambiguity | Meeting note 2 | "Approver" role defined | Unclear if team lead or director | Unresolved: "let's discuss next sprint" |

### Step 4: Domain Model Output

**Process Model:**

```
User creates request
    ├─ Amount ≤ $10K → Auto-route to team lead
    └─ Amount > $10K → Manual routing (finance review first)
        └─ [GAP: no timeout rule defined]
Team lead reviews
    ├─ Approve → Execute
    ├─ Reject → Notify user with reason
    └─ [GAP: no escalation if team lead is unavailable]
```

**Risk Signals:**
- Approval bottleneck: 40% of tickets show >2 day wait
- Missing timeout: users abandon requests silently
- Role ambiguity: "approver" not consistently defined

### Step 5: Expert Calibration Questions

1. Is the $10K threshold for manual routing a finance policy or a system limitation?
2. What should happen when the team lead is unavailable for >24 hours?
3. Should rejected requests be editable and resubmittable, or require a new request?
4. Who owns the timeout escalation: the system or a designated backup approver?

### Step 6: Downstream Artifacts

| Domain Insight | Requirement | Acceptance Criteria | Test Case |
|----------------|-------------|-------------------|-----------|
| Manual routing for large amounts | Route requests >$10K to finance first | Finance receives notification within 1 min | Submit $15K request, verify routing |
| No timeout rule exists | Implement 48-hour escalation | Auto-escalate if no action in 48h | Simulate 48h idle, verify escalation |
| Role ambiguity | Define approver hierarchy | System resolves to specific person | Check routing for each org chart scenario |

## Output Focus

- Actors, states, transitions, exceptions
- Conflicts between stated process and real tickets
- Unclear ownership or approval boundaries
- Downstream artifacts: requirement questions, acceptance criteria, edge-case tests
