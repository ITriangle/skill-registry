# Think in AI Domain Research

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-open_standard-green.svg)](https://agentskills.io)

[中文文档](README_zh.md)

> Turn source materials into structured domain knowledge. AI does the first serious round of research so you can have better conversations with experts.

## When to Use

Use this skill when you need to:

- **Learn a new domain** — business, industry, regulation, methodology, or technical ecosystem
- **Understand documents** — reports, specs, policies, code, tickets, or meeting notes
- **Prepare for expert conversations** — with product managers, analysts, stakeholders, or customers
- **Convert understanding into work** — requirements, tests, evals, benchmarks, or implementation plans

**Not for:** simple fact lookup, brainstorming without source materials, or purely creative writing.

## Installation

**Natural language** (in Claude Code, Cursor, Codex, etc.):

```
Install the think-in-ai-domain-research skill from https://github.com/yugasun/think-in-ai-domain-research
```

**CLI:**

```bash
npx skills add yugasun/think-in-ai-domain-research
```

**Manual:**

```bash
# Clone into your skills directory
git clone https://github.com/yugasun/think-in-ai-domain-research ~/.claude/skills/think-in-ai-domain-research
```

## Features

- 🔍 **Domain Model Building** — concept maps, core objects, process chains, decision boundaries
- 📊 **Multi-source Alignment** — compares materials instead of summarizing independently
- 🎯 **Fact/Inference Separation** — labels every conclusion as fact, rule, inference, or boundary
- ❓ **Expert Calibration Questions** — narrow, specific, evidence-tied questions for domain experts
- 🔧 **Work Artifact Conversion** — maps insights to requirements, tests, evals, and benchmarks
- ⚠️ **High-Stakes Guardrails** — extra rigor for legal, medical, financial, and compliance domains

## Usage Examples

```text
我拿到一份评级方法论和三份评级报告，请帮我建立业务认知。
```

```text
Here's a PRD, support tickets, and meeting notes. Help me understand this domain and convert it to test cases.
```

```text
我要学习一个新的技术生态，手里有官方文档和示例代码。请帮我快速入门。
```

## How It Works

The skill follows a 7-step workflow:

| Step | Action | Output |
|------|--------|--------|
| 1. Inventory | Catalog all source materials | Source table |
| 2. Goal | Define research purpose and downstream artifact | Research goal statement |
| 3. Rules | Compile methodology, policy, or specs | Rules model |
| 4. Alignment | Compare cases against compiled rules | Evidence → Judgment chain |
| 5. Domain Model | Build concept map, objects, process, boundaries | Domain model |
| 6. Expert Questions | Generate narrow calibration questions | Question list |
| 7. Artifacts | Map insights to requirements, tests, evals | Work artifact mapping |

## Default Output: Domain Onboarding Pack

Unless you request another format, the skill produces a 13-section onboarding pack:

1. Research Goal
2. Source Inventory
3. Concept Map
4. Core Objects
5. Rules / Methodology
6. Case Alignment
7. Judgment Chain / Workflow
8. Key Metrics & Terminology
9. Risk Signals & Failure Modes
10. What Evidence Supports
11. What Evidence Does Not Support
12. Expert Calibration Questions
13. Convertible Work Artifacts

## Project Structure

```
think-in-ai-domain-research/
├── SKILL.md              # Core skill definition
├── reference/
│   ├── principles.md     # Operating principles & prompt patterns
│   └── high-stakes.md    # High-stakes domain guardrails
├── examples/
│   ├── credit-rating.md  # Credit rating case study
│   ├── product-workflow.md # Product workflow case study
│   ├── tech-ecosystem.md # Technical ecosystem case study
│   └── sample-output.md  # Complete output example
└── evals/
    └── evals.json        # Evaluation test cases
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on reporting issues, adding examples, and writing evals.

## License

[MIT](LICENSE) © [yugasun](https://github.com/yugasun)
