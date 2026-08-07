---
name: diagnosing-bugs
description: 针对难 bug 和性能回归的诊断循环。当用户说「diagnose」/「debug this」，或报告损坏/抛错/失败/变慢时使用。
---

# Diagnosing Bugs

针对难 bug 的 discipline。仅在有明确理由时跳过 phase。

探索代码库时，读 `CONTEXT.md`（若存在）建立相关 module 的心智模型，并检查触及区域的 ADR。

## Redact

本 skill 会让你展示命令、输出和捕获的 artifact。**先脱敏每个秘密**——用 `<REDACTED>` 替代。针对 env var 建 loop，使凭据留在环境而非你展示的内容。捕获的 artifact 带 auth header：只引用承载 signal 的行。

若脱敏后输出不足以诊断 bug，说明并请用户协助。

## Phase 1 — 构建 feedback loop

**这就是 skill。**其余都是机械。若你有 bug 的 **tight** pass/fail signal——在此 bug 上会变红——你会找到原因；二分、假设检验、instrumentation 都只是消费它。若没有，盯代码救不了你。

在此 disproportionate 投入。**要激进。要创造性。拒绝放弃。**

### 构建方式——大致按此顺序尝试

1. **失败测试**，在能触及 bug 的 seam——unit、integration、e2e。
2. **Curl / HTTP 脚本**，针对运行中的 dev server。
3. **CLI 调用**，fixture 输入，stdout diff 已知好 snapshot。
4. **Headless 浏览器脚本**（Playwright / Puppeteer）——驱动 UI，断言 DOM/console/network。
5. **重放捕获 trace。**把真实网络请求 / payload / event log 存盘；在隔离中重放代码路径。
6. **Throwaway harness。**拉起系统最小子集（一服务、mock deps），单函数调用 exercises bug 路径。
7. **Property / fuzz loop。**若 bug 是「有时输出错」，跑 1000 随机输入找 failure mode。
8. **Bisection harness。**若 bug 出现在两个已知状态之间（commit、dataset、version），自动化「boot at state X, check, repeat」以便 `git bisect run`。
9. **Differential loop。**同一输入跑旧版 vs 新版（或两配置），diff 输出。
10. **HITL bash 脚本。**最后手段。若人类必须点击，用 `scripts/hitl-loop.template.sh` 驱动*他们*，使 loop 仍结构化。捕获输出反馈给你。

建好 feedback loop，bug 就 90% 修了。

### Tighten the loop

把 loop 当产品。一旦有了*一个* loop，**tighten** 它：

- 能更快吗？（缓存 setup、跳过无关 init、缩小测试范围。）
- signal 能更 sharp 吗？（断言具体症状，非「没 crash」。）
- 能更 deterministic 吗？（pin 时间、seed RNG、隔离文件系统、freeze 网络。）

30 秒 flaky loop 几乎不比没有好；2 秒 deterministic 的是 tight——调试超能力。

### 非确定性 bug

目标不是干净 repro，而是**更高复现率**。loop 触发 100×、并行、加压、缩小 timing window、注入 sleep。50% flake bug 可调试；1% 不行——持续提高直到可调试。

### 当真建不了 loop 时

停下并明确说明。列出试过什么。向用户要：(a) 能 repro 的环境访问，(b) 脱敏捕获 artifact（HAR、log dump、core dump、带时间戳录屏），或 (c) 添加临时生产 instrumentation 的许可。没有 loop **不要**进入假设。

### 完成标准——tight 且可红的 loop

Phase 1 完成当 loop **tight** 且 **red-capable**：你能命名**一条命令**——脚本路径、测试调用、curl——且你**至少已运行一次**（展示调用与输出，脱敏），且：

- [ ] **Red-capable**——驱动实际 bug 代码路径，断言**用户确切症状**，能在此 bug 上变红、修好后变绿。不是「运行不报错」——必须能*抓住此具体 bug*。
- [ ] **Deterministic**——每次运行同一 verdict（flaky bug：按上文 pinned、高复现率）。
- [ ] **Fast**——秒级，非分钟。
- [ ] **Agent-runnable**——你可 unattended 运行；人类在 loop 仅通过 `scripts/hitl-loop.template.sh`。

若在命令存在前读代码建理论，**停下——直接跳假设正是本 skill 要防止的失败。**无 red-capable 命令，无 Phase 2。

## Phase 2 — 复现 + 最小化

跑 loop。看它变红——bug 出现。

确认：

- [ ] loop 产生**用户**描述的 failure mode——不是碰巧附近的另一种失败。错 bug = 错修复。
- [ ] 多次运行可复现（或非确定性 bug 有足够高复现率可调试）。
- [ ] 已捕获确切症状（错误消息、错输出、慢 timing），后续 phase 可验证修复真针对它。

### 最小化

变红后，把 repro shrink 到**仍变红的最小场景**。一次 cut 输入、调用者、配置、数据、步骤，每次 cut 后重跑 loop——只留 failure load-bearing 的。

为何 bother：minimal repro 缩小 Phase 3 假设空间（更少 moving parts 可怀疑），并成为 Phase 5 干净回归测试。

完成当**每个剩余元素都 load-bearing**——去掉任一都会让 loop 变绿。

复现**且**最小化前不要继续。

## Phase 3 — 假设

测试任何假设**之前**生成 **3–5 个 ranked 假设**。单假设生成锚定第一个 plausible 想法。

每个假设必须**可证伪**：陈述它做出的预测。

> 格式：「若 <X> 是原因，则 <改 Y> 会使 bug 消失 / <改 Z> 会使其更糟。」

若说不出预测，假设是 vibe——丢弃或 sharpen。

**测试前把 ranked 列表展示给用户。**他们常有领域知识 instant re-rank（「我们刚 deploy 了 #3 的变更」），或知道已排除的假设。便宜 checkpoint，大时间节省。用户 AFK 则不 block——按你的 ranking 继续。

## Phase 4 — Instrument

每个 probe 必须映射 Phase 3 的具体预测。**一次只改一个变量。**

工具偏好：

1. **Debugger / REPL inspection**，若环境支持。一个 breakpoint 胜十条 log。
2. **Targeted logs**，在区分假设的边界。
3. 永不「log everything and grep」。

**给每条 debug log 打唯一前缀 tag**，如 `[DEBUG-a4f2]`。结束时 cleanup 成一次 grep。无 tag log 存活；有 tag 死。

**Perf 分支。**性能回归，log 通常错。改为：建立 baseline 测量（timing harness、`performance.now()`、profiler、query plan），然后二分。先测量，后修复。

## Phase 5 — 修复 + 回归测试

在修复**之前**写回归测试——但仅当有**正确 seam**。

正确 seam 是测试在调用点 exercises **真实 bug 模式**的 seam。若唯一可用 seam 太浅（单调用者测试而 bug 需多调用者，unit test 无法复制触发链），那里的回归测试给 false confidence。

**若无正确 seam，这本身就是发现。**记下。代码库架构阻止锁 bug。为下一 phase flag。

若有正确 seam：

1. 把最小 repro 变成该 seam 上的失败测试。
2. 看它失败。
3. 应用修复。
4. 看它通过。
5. 对原始（未最小化）场景重跑 Phase 1 feedback loop。

## Phase 6 — Cleanup + 事后分析

宣布完成前必须：

- [ ] 原始 repro 不再 repro（重跑 Phase 1 loop）
- [ ] 回归测试通过（或 seam 缺失已记录）
- [ ] 所有 `[DEBUG-...]` instrumentation 已移除（`grep` 前缀）
- [ ] Throwaway 原型已删（或移到明确标记的 debug 位置）
- [ ] 最终正确的假设写在 commit / PR message——下一位 debugger 可学

**然后问：什么能预防此 bug？**若答案涉及架构变更（无好测试 seam、tangled 调用者、隐藏 coupling），hand off 到 `/improve-codebase-architecture` skill 并给 specifics。在修复**之后**做建议，非之前——你现在比开始时信息更多。
