---
name: grilling
description: 就计划、决定或想法对用户 relentless 拷问。当用户想 stress-test 思考，或使用任何「grill」触发短语时使用。
---

relentless 采访用户直到达成共享理解。将此映射为**设计树**：每个决定分支出挂在其上的后续决定。

按**轮次**遍历树。**frontier** 是每个 prerequisite 已 settled 的决定——现在能问、不必猜尚未听到的答案的问题。一轮问整个 frontier：给每个问题编号并附推荐答案。然后等用户回答再进行下一轮。

每个问题格式如下：

```
❓ **Q1** - **<问题标题>**：<问题正文，可能多段，含多个选项>

➡️ <你的推荐答案>
```

用户每轮回答重塑树——settled 决定把 frontier 外推、解锁依赖它们的 question。重算 frontier 问下一轮。答案依赖本轮仍 open 的另一 question 的，属于* later* 轮，不是本轮。

找*事实*永远是你的工作，从不是用户的。frontier question 需要环境中的事实（文件系统、工具等）时，dispatch sub-agent 去找——不要问用户你能自己查的。不要 block：运行中的探索是 unsettled prerequisite，只有依赖它的 downstream question 等 sub-agent 报告——其余 frontier 现在问。_决定_是用户的——每个都交给他们并等待。

会话完成当 frontier 为空：设计树每条分支都 visited，没有默默 assumed 的。在用户确认已达共享理解前不要行动。
