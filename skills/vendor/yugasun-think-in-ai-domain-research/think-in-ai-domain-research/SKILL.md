---
name: think-in-ai-domain-research
description: >
  Turn source materials into a structured domain onboarding pack.
  Processes documents, reports, specs, code, tickets, and notes into a domain model,
  judgment chain, decision boundaries, expert calibration questions,
  and downstream work artifacts (requirements, tests, evals, benchmarks).
  Especially useful for phrases like "学习新领域", "了解业务", "研究方法论",
  "看不懂报告", "帮我快速入门", "先用AI梳理", "业务理解", "领域研究",
  "提炼判断链", "转成需求/测试/Eval".
version: 1.0.0
license: MIT
author: yugasun
---

# Think in AI Domain Research

Use this skill to help a person enter an unfamiliar domain by making AI do the first serious round of research. The goal is not to produce a polished summary. The goal is to build a usable domain model, expose boundaries, and prepare better human questions.

> **AI-first, not AI-only.** Use AI to reach 70-80% structured understanding before consuming expert time. Humans still own final judgment, authority, and accountability.

## When This Skill Applies

- Understanding a new business domain, industry, product workflow, regulation, methodology, technical ecosystem, or report genre
- Reading many documents but not knowing how to use them
- Turning methods, reports, cases, examples, notes, or interviews into usable knowledge
- Preparing to talk with product managers, domain experts, analysts, customers, or stakeholders
- Converting domain understanding into requirements, tests, Eval, Benchmark, Agent Skill, Runbook, or implementation tasks

**Do not use** for simple fact lookup, general brainstorming with no source materials, or purely creative writing.

For detailed operating principles and prompt patterns, read `${CLAUDE_SKILL_DIR}/reference/principles.md`.

## Workflow

Execute these steps in order. Do the work instead of merely explaining the method.

### Step 1: Inventory the Input

Catalog all available materials:

| Source Type | Examples |
|-------------|----------|
| Methodology | Policy, standard, regulation, process doc, framework |
| Evidence | Reports, cases, examples, tickets, meeting notes, screenshots, logs |
| Implementation | Requirements, user stories, API docs, code, schemas, data samples |
| Target task | Requirement design, testing, Eval, feature implementation, onboarding |

If materials are missing, ask for the minimum needed set.

**Output:**

```markdown
## Source Inventory

| Source | Type | What It Can Support | What It Cannot Support |
|--------|------|---------------------|----------------------|
```

### Step 2: Define the Research Goal

State the concrete reason for learning and the immediate downstream artifact.

```markdown
## Research Goal

We are learning this domain in order to ...
The immediate downstream artifact is ...
```

Good downstream artifacts: requirement clarification list, user journey, test plan, Eval/Benchmark case, implementation design, stakeholder interview plan, domain onboarding pack.

### Step 3: Compile the Methodology or Rules

If a methodology, policy, spec, or standard exists, compile it before reading cases. Extract: core problem, key objects, evidence fields, meanings, possible judgments, judgment boundaries, and open questions.

Use the prompt pattern from `${CLAUDE_SKILL_DIR}/reference/principles.md` (Principle 3: Compiling Methodology).

### Step 4: Align Cases, Reports, or Examples

When examples exist, compare them against the compiled rules. Do not summarize separately — align and compare. Output the chain: **evidence → indicators → business meaning → judgment → boundary**.

### Step 5: Build the Domain Model

Produce a compact model that a non-expert can use:

```markdown
## Domain Model

### Concept Map
[5-8 core concepts, not an encyclopedia]

### Core Objects
| Object | Plain Meaning | Key Fields / Evidence | Common Misread |
|--------|--------------|----------------------|----------------|

### Process or Judgment Chain
[Step-by-step decision flow]

### Risk Signals and Edge Cases

### Decision Boundaries
[What can and cannot be concluded]
```

### Step 6: Generate Expert Calibration Questions

Generate narrow, specific questions tied to evidence — not broad questions like "请讲一下这个业务":

```markdown
## Expert Calibration Questions

1. Is this object boundary correct: ...?
2. Which source is authoritative when ... conflicts with ...?
3. Are we allowed to conclude ... from ...?
4. What should the system do when evidence is missing?
5. Which failure would be unacceptable in production?
```

### Step 7: Convert to Work Artifacts

Map domain insights into the requested downstream work:

```markdown
## Artifact Mapping

| Domain Insight | Requirement | Acceptance/Test | Eval/Benchmark | Human Boundary |
|----------------|-------------|-----------------|----------------|----------------|
```

If the user only asked for learning, stop at the onboarding pack and calibration questions.

## Execution Behavior

Start with:

```markdown
我会按 Think in AI Domain Research 处理：先盘点材料，再建立领域模型、判断边界和专家校准问题，最后转成你要的工作产物。
```

Then proceed:

1. Inspect provided files, links, notes, or code before asking broad questions
2. If the research target is unclear, ask one concise question about the downstream artifact
3. Produce a source inventory and research goal
4. Build the domain model and judgment/workflow chain
5. List boundaries and expert calibration questions
6. Map insights into the requested artifact

If no materials provided, request minimum inputs:

```markdown
请至少提供：1 份规则/方法论/说明文档，1-3 个真实案例或样例，以及你最终想产出的工作产物。
```

## Default Output: Domain Onboarding Pack

Unless the user requests another format, produce:

```markdown
# [Domain] 快速入门包

## 1. 研究目标
## 2. Source Inventory
## 3. 业务/领域概念地图
## 4. 核心对象
## 5. 规则、方法论或流程
## 6. 案例对齐与可迁移模式
## 7. 判断链 / 工作流
## 8. 关键指标、字段或术语解释
## 9. 典型风险、失败模式和常见误读
## 10. 当前证据能推出什么
## 11. 当前证据不能推出什么
## 12. 需要专家或权威来源确认的问题
## 13. 可转化的研发产物
```

## Quality Bar

**Good output:**
- Grounded in provided materials or cited primary sources
- Avoids conflating inference with fact
- Makes the domain usable for the user's next task
- Reduces vague expert communication into specific confirmation questions
- Includes at least one reusable asset: model, checklist, artifact mapping, Eval idea, or Runbook step

**Reject or revise outputs that:**
- Only summarize documents one by one
- Overproduce generic dimensions without domain-specific failure modes
- Hide uncertainty
- Jump from limited evidence to final decisions
- Produce expert-sounding language that the user cannot act on

## High-Stakes Domains

For legal, medical, financial, safety, compliance, or regulated domains, read and apply `${CLAUDE_SKILL_DIR}/reference/high-stakes.md`. Key points:

- Prefer authoritative primary sources and user-provided documents
- Cite sources when claims matter
- Mark conclusions as non-authoritative unless a qualified expert confirms them
- Generate calibration questions and decision boundaries explicitly
- Do not present final professional advice

## Examples

For worked examples, see:

- `${CLAUDE_SKILL_DIR}/examples/product-workflow.md` — PRD + tickets + meeting notes
- `${CLAUDE_SKILL_DIR}/examples/tech-ecosystem.md` — Official docs + sample code
- `${CLAUDE_SKILL_DIR}/examples/sample-output.md` — Complete Domain Onboarding Pack output
