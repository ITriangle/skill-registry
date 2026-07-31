# High-Stakes Domain Guardrails / 高风险领域规则

This document defines additional guardrails for legal, medical, financial, safety, compliance, or regulated domains. The agent should apply these rules when the domain involves professional judgment, regulatory requirements, or irreversible decisions.

## When These Guardrails Apply

These guardrails apply when the domain involves:

- **Legal**: contracts, regulations, compliance, liability, intellectual property
- **Medical**: diagnosis, treatment, drug interactions, clinical decisions, patient safety
- **Financial**: credit ratings, investment decisions, risk assessment, regulatory filings
- **Safety**: engineering tolerances, safety-critical systems, hazard analysis
- **Compliance**: regulatory requirements, audit trails, governance frameworks
- **Any regulated domain**: where incorrect conclusions could cause material harm

## Required Practices

### 1. Prefer Primary Sources

- Use authoritative primary sources and user-provided documents
- Do not rely on secondary summaries, blog posts, or community interpretations
- When web research is needed, cite the original source, not aggregators

**Prompt pattern:**

```text
这是一个高风险领域。请优先使用用户提供的原始材料和权威来源。
如需网络调研，请引用原始出处，并标注 [来源: URL]。
```

### 2. Cite Sources When Claims Matter

- Every factual claim that affects a decision should have a source reference
- Use inline citations: `[Source: document name, page/section]`
- If the source is ambiguous, flag it as uncertain

### 3. Mark Conclusions as Non-Authoritative

- Default stance: AI-generated conclusions in high-stakes domains are non-authoritative
- Add explicit disclaimers to outputs:

```markdown
> ⚠️ **Disclaimer**: This analysis is AI-generated and non-authoritative.
> All conclusions must be reviewed and confirmed by a qualified domain expert
> before being used for professional, legal, medical, or financial decisions.
```

### 4. Generate Explicit Calibration Questions

For high-stakes domains, calibration questions should be more rigorous:

```markdown
## Expert Calibration Questions (High-Stakes)

1. **Regulatory authority**: Which regulatory body has jurisdiction over ...?
2. **Liability boundary**: Who bears liability if ... is incorrect?
3. **Source hierarchy**: When the methodology document says X but the case shows Y, which takes precedence?
4. **Threshold validation**: Is the threshold of ... derived from regulation, industry practice, or internal policy?
5. **Failure consequence**: What is the worst-case outcome if this judgment is wrong?
6. **Audit trail**: What evidence must be preserved to support this conclusion?
```

### 5. Do Not Present Final Professional Advice

- Never present AI output as final legal, medical, or financial advice
- Always frame output as "preliminary analysis for expert review"
- Include explicit human-in-the-loop checkpoints

## Output Template Additions

For high-stakes domains, add these sections to the Domain Onboarding Pack:

```markdown
## ⚠️ High-Stakes Considerations

### Regulatory Framework
- Applicable regulations/standards:
- Regulatory body:
- Compliance requirements:

### Source Authority Hierarchy
1. [Primary source - highest authority]
2. [Secondary source]
3. [AI inference - lowest authority, requires expert validation]

### Liability and Risk Boundaries
- Decisions that require human expert approval:
- Consequences of incorrect judgment:
- Required audit trail elements:

### Disclaimer
> This analysis is preliminary and AI-generated. It must be reviewed by
> a qualified [domain] professional before any professional decisions are made.
```
