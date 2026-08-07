# Logic Prototype

单个自包含 HTML 文件——**可分享 demo**——让人通过点击按钮驱动状态模型。用于**业务逻辑、状态转换或数据形状**的问题——纸上合理、推过真实 case 才 feel wrong 的那种。

因单文件无需安装，可交给非开发者——设计师、PM、领域专家——自己感受模型。因此用他们的语言，不是代码的语言。

## 何时是正确形状

- 「我不确定这状态机在 X 然后 Y 的 edge case 怎么处理。」
- 「这数据模型真能表示……的情况吗？」
- 「写 API 之前想感受接口应什么样。」
- 任何人想**按按钮看状态变**的任何事。

若问题是「应该长什么样」——错分支。用 [UI.md](UI.md)。

## 流程

### 1. 陈述问题

写代码前，写下正在原型什么状态模型、什么问题。一段，在 demo 顶部可见 intro（不只是 comment）。答错问题的 logic prototype 纯浪费——把问题 explicit，便于用户在场或 AFK 回来检查。

### 2. 在可移植 module 中隔离逻辑

把真正答问题的逻辑——放在单个 `<script>`，写成小纯 module，日后可 lift 进真实代码库。周围页面是 throwaway；此 module 不是。

形状取决于问题：

- **纯 reducer**——`(state, action) => state`。action 是离散事件、state 是单值时好。
- **状态机**——显式状态与转换。「此刻哪些 action 合法」是问题一部分时好。
- **小集纯函数** over plain data type。无隐式当前 state，只有变换时好。
- **类或 module 带清晰 method surface**，当逻辑真拥有 ongoing internal state。

选*最 fit 问题*的形状，非最易接页面的。保持纯：无 DOM、无 `document`、无 button handler 伸进内部。页面调用它；无反向流。这使原型超出自身寿命有用：问题答完后，validated reducer / machine / 函数集可独自 lift 进真实 module。

### 3. 构建可分享 HTML 文件

单文件，plain HTML/CSS/JS——无 framework、无 bundler、无 server，全 inline，双击打开、可邮件传。任何人应能打开运行。

为非开发者写。每个 label 是**领域语言**，非代码——按钮和 state 读像业务，非 reducer。plain words 解释发生什么。

自上而下清晰层次：

1. **标题与一行说明**——此 demo 让你探索什么（步骤 1 的问题）。
2. **当前 state**——完整相关 state，可读 panel（label 字段，非 raw JSON dump），每次点击后 re-render 使变化可见。有助非开发者跟随时，标出刚变什么。
3. **自由玩按钮**——每 action 一按钮，始终可用，任意顺序 poke。每点击 dispatch action 并 re-render state。
4. **引导 walkthrough**——一组 **scenario**，每 tab 一个。每 tab 短 plain-language 场景描述——设置的情境与要 watch 什么——其下是该 scenario 的**有序要按的按钮**。每步是真按钮：点击执行 action 并到下一步。开始 walkthrough 重置到已知初始 state，scenario 每次相同。

选 scenario 演示别扭 case——happy path、tricky edge、应非法的尝试——纸上难推理的。

美观但克制：干净 typography、宽裕 spacing、一 accent 色。无动画、无 gimmick——不与 state 和按钮竞争。

### 4. 交付

发文件或为他们打开。他们会点 walkthrough 和自由玩；有趣时刻是「wait, that shouldn't be possible」或「huh, I assumed X would be different」——那是*想法*里的 bug，正是要点。若要新 action 或 scenario，加它们。原型会演化。

### 5. Capture 答案与原型

原型答完问题后，按 [SKILL](SKILL.md) 描述 capture 答案，再 capture 原型。logic 特有映射：validated reducer / machine / 函数集 lift 进真实 module（决定，吸收）；HTML shell 跟到 throwaway branch 把原型作 primary source——单文件，那里仍 trivial 重跑。

## Anti-patterns

- **不要加测试。**需要测试的不再是原型。
- **不要接真实数据库。**用内存 state，除非问题 specifically 关于持久化。
- **不要泛化。**无「以后若要支持 X」。原型只答一个问题。
- **不要把 logic 和 page 糊在一起。**纯 module 引用 DOM、`document` 或 button handler，就不再 liftable。页面作薄 shell over 纯 module。
- **不要伸手 framework、bundler、server。**收件人双击的单文件；React app 或 dev server  defeat「可分享」。
- **不要把 HTML shell  ship 进生产。**页面为手点优化。背后 logic module 才是值得留的。
