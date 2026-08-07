# Phase boundaries

**phase** 是会话内的一块工作——grilling、实现、QA。定义故意模糊：phase 在你觉得*「好，那部分做完了」*时结束。

**phase boundary** 是两个 phase 之间的间隙，此决定只应在此处做出。phase 中途没有决定要做——继续，或把剩余工作拆成 subagent。phase 中途 compact 会让 agent 丢线。

## 五个选项

| 选项       | 作用                                                    |
| ---------- | ------------------------------------------------------- |
| **Continue** | 留在会话中。完全没有上下文切换。                        |
| **`/clear`** | 清空上下文窗口，从零开始。                              |
| **`/handoff`** | 写可移植 markdown 文件，在任何处用其 seed 会话。        |
| **Subagent** | 把任务发到自己的上下文窗口，收回报告。                  |
| **`/compact`** | 压缩此上下文，用摘要 seed 新会话。                      |

## 决策树

在边界处自上而下工作。第一个**是**胜出。

**1. 能否在此会话继续？**两件事使答案为是：下一阶段需要此 phase 作为**primary source**，或你还有足够 [smart zone](https://www.aihero.dev/ai-coding-dictionary/smart-zone)（约 150k token）容纳下一阶段。Grilling → 实现是标准「是」：实现要 verbatim 推理，而非摘要。Continue 不花成本、不丢东西，因此在其他任何事之前先排除它。

**2. 上下文对后续是否无关？**此会话中的一切——探索、决定、死胡同——是否都可丢弃？若是，**`/clear`**。它是棋盘上最便宜的走法：不花时间，归还整个窗口。`/clear` 也非终点——旧会话仍可 resume。

弄错的成本是单向的。Clear *相关*上下文，你失去构建背后的**why**，读 diff 回来也换不回来。

**3. 是否需要 hand off？**`/handoff` 范围窄。仅当你：

- 换到**新 harness**（Claude → Codex），
- 移到**新目录**或仓库，
- 把工作发给**同事**，
- 或在**phase 中途** fork 旁路任务而不 derail 当前工作时，

才需要它。列表就是全部条款。`/handoff` 换来的是**可移植性**——可携带的文件。若无东西在携带，你不需要它。

**4. 任务能否 AFK 完成？**范围足够紧，可在你离开键盘、无需 steering 时运行？发给 **subagent**，此会话不动。自动评审是标准情形：agent 读 diff 并报告，你做的时候不需要你。

**5. 否则，`/compact`。**相关上下文、同一 harness、同一目录、你需要留在 loop 中——树落在此处，且常落在此处。传指令（`/compact we're going to QA this area`），使摘要保留下一阶段所需。

`/compact` 是**默认，而非首选**。它在底部，因为上面四个问题都更便宜或更精确。人们从这里开始的失败模式，是摘要压扁了决定、对新会话 confidently wrong 的 fresh session。

## Primary 与 secondary sources

除 **Continue** 外，每个动作都把 **primary source** 变成 **secondary source**——发生的会话，被其摘要取代。交易总是同一形状：

| Source                            | 信息 | 噪声 | 活动空间 |
| --------------------------------- | ---- | ---- | -------- |
| Primary (Continue)                | 完整 | 多   | 小       |
| Secondary (`/compact`, `/handoff`) | 有损 | 少   | 大       |

因此问题 1 排第一。仅当 staying 比 saving 更贵时才付有损性。

## 这些是判断调用

问题并非客观——每个都有品味，同一边界两天可能两种走向。价值在于**按顺序**在边界而非工作中途问它们。
