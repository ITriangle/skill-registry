---
name: review
description: >
  以三种模式审查——代码（diff 对照标准/规格）、设计（规划前审查 NOTES + tech-spec）、
  漂移（发布前对照 tech-spec 审查实现）。根据 Flow Conductor 阶段或用户意图选择模式；
  不要混合不同产物类型。
---

# 审查

共有三种模式。每种模式都有自己的输入、审查维度和输出产物。**不要在一个文件中混用模式。**

## 模式选择

| 模式 | 触发条件 | 代理 | 输出 |
| --- | --- | --- | --- |
| **code** | `delivery` 子阶段；用户要求审查 diff/PR | code-reviewer | `.scratch/<slug>/REVIEW.md` |
| **design** | `design_review` 阶段；用户要求审查设计 | design-reviewer | `.scratch/<slug>/DESIGN_REVIEW.md` |
| **drift** | `drift_check` 阶段（交付后、发布前） | design-reviewer | `.scratch/<slug>/DRIFT_REPORT.md` |

不确定时，以 Flow Conductor 阶段名称为准。直接调用时默认使用 **code**，除非用户明确指定 design 或 drift。

---

## Code 模式

审查 `git diff <fixed-point>...HEAD`：

- **标准**——是否符合仓库编码标准？
- **规格**——是否符合来源 issue/PRD？
- **宪法**（可选）——仓库根目录存在 `CONSTITUTION.md` 时，是否违反任何不可妥协的原则？

如果缺少 `docs/agents/issue-tracker.md`，运行 `/aiops-setup`。

### 流程

1. **固定基准点**——commit、branch、tag 或 `main`。确认 ref 可解析且 diff 非空。
2. **查找规格**——commit 中的 issue 引用（`docs/agents/issue-tracker.md`）、用户给出的路径，或 `docs/`/`.scratch/` 中的 PRD。没有规格 → 跳过规格维度。
3. **查找标准**——`CODING_STANDARDS.md`、`CONTRIBUTING.md` 等。
4. **查找宪法**——仓库根目录的 `CONSTITUTION.md`。缺失 → 跳过宪法维度。
5. **并行子代理**——每个启用的维度一个代理。每个结果不超过 400 词，并引用来源。
6. **汇总**——每个维度原样保留为独立章节。每个维度写一行摘要；不要合并维度。

一项变更可能通过一个维度，却未通过另一个——务必保持维度独立。

### 输出：REVIEW.md

```markdown
# 代码审查：<feature-slug>

## 摘要
<总体评估>

## 设计一致性
- [ ] 实现符合 NOTES.md 设计决策
- [ ] 接口符合 tech-spec.md 规格
- [ ] 无超出 scope 的变更

## 发现

### 阻塞项（必须修复）
#### B1: <file:line> — <title>
- **问题**: …
- **建议**: …

### 非阻塞项（建议改进）
#### N1: <file:line> — <title>
- **问题**: …
- **建议**: …

## 结论
**APPROVE** | **REQUEST_CHANGES**
```

门禁：`review_approve` 要求 `REVIEW.md` 包含 `APPROVE`。

---

## Design 模式

在规划或实现**之前**审查设计产物。不看代码 diff——只审查 `NOTES.md` + `tech-spec.md`。

深度/seam/deletion-test 检查所用词汇见：[design-vocabulary.md](../architect-design/design-vocabulary.md)。

### 输入

- `.scratch/<slug>/NOTES.md`
- `.scratch/<slug>/tech-spec.md`
- `CONTEXT.md`（项目根目录或各区域目录）
- `docs/adr/`
- `.scratch/<slug>/mockups/`（如果存在 UI 模型）

### 流程

1. 阅读 NOTES.md 中的决策——每项决策必须列出至少一个被否决的替代方案。
2. 阅读 tech-spec.md 的模块清单——依据 [design-vocabulary.md](../architect-design/design-vocabulary.md) 对每个模块应用 deletion test 并评估深度。
3. 交叉检查 CONTEXT.md 的词汇和现有 ADR——除非有明确理由，否则标记冲突。
4. 如果存在 `CONSTITUTION.md`，检查设计是否遵守不可妥协的原则。
5. 提供独立的第二视角——不要照单全收架构师的推理。

不要审查实现细节（那属于 code 模式）。

### 输出：DESIGN_REVIEW.md

```markdown
# 设计审查：<feature-slug>

## 摘要
<一段话>

## 设计健全性
- [ ] 每个设计决策列出了至少一个被否决的替代方案及原因
- [ ] 模块通过 deletion test（非 pass-through）
- [ ] 接口设计遵循 depth 原则：小接口 + 深实现
- [ ] 依赖分类正确，seam 位置合理（≥2 adapters 才有真实 seam）
- [ ] 接口定义与 CONTEXT.md 领域模型一致
- [ ] 无与现有 ADR 的冲突（或冲突已记录并有充分理由）
- [ ] Open Questions 全部解决或明确标记为非阻塞
- [ ] 无过早优化或过度设计
- [ ] Scope 边界清晰，out-of-scope 明确排除

## 发现

### 阻塞项（必须修正才能进入规划）
#### D1: <title>
- **问题**: …
- **建议**: …
- **关联**: NOTES.md Decision X / tech-spec.md §Y

### 非阻塞项（建议改进）
#### N1: <title>
- **建议**: …

## 结论
**APPROVE** | **REQUEST_CHANGES**
```

门禁：`design_review_approve` 要求 `DESIGN_REVIEW.md` 包含 `APPROVE`。阻塞项会阻止 planner，直至问题解决。

---

## Drift 模式

交付后、发布前：**实现**是否符合**已批准的设计**？

### 输入

- `.scratch/<slug>/tech-spec.md`
- `.scratch/<slug>/NOTES.md`（范围和决策）
- 从工作历程起点或用户指定基准点开始的 `git diff`

### 流程

1. 固定 diff 基准点（与 code 模式相同）。
2. 对 tech-spec 的每项要求逐一检查：已实现？部分实现？缺失？
3. 对 diff 中的每项行为逐一检查：规格内？超出范围？
4. 分别标记范围蔓延和规格缺口。

### 输出：DRIFT_REPORT.md

```markdown
# 漂移报告：<feature-slug>

## 摘要
<总体漂移评估>

## 规格覆盖情况
| 要求（tech-spec） | 状态 | 证据 |
| --- | --- | --- |
| … | 已实现 / 部分实现 / 缺失 | file:line 或“未找到” |

## 未记录的行为
| diff 中的变更 | 在规格中？ | 说明 |
| --- | --- | --- |
| … | 是 / 否 / 部分 | … |

## 发现

### 阻塞项（发布前必须修复或更新规格）
#### F1: …

### 非阻塞项
#### N1: …

## 结论
**PASS** | **DRIFT_FOUND**
```

门禁：`drift_check_pass` 要求存在 `DRIFT_REPORT.md`。没有阻塞性漂移时，结论使用 `PASS`。
