# UI 原型

在单一路由上生成**多个截然不同的 UI 变体**，通过底部浮动栏切换。用户在浏览器中来回切换，选中一个（或从每个方案中取一部分），然后丢弃其余方案。

如果问题涉及逻辑/state，而不是外观——分支选错了。使用 [LOGIC.md](LOGIC.md)。

## 何时适合这种形态

- “这个页面应该长什么样？”
- “我想先看看这个 dashboard 的几种方案，再做决定。”
- “为设置页面尝试一种不同的布局。”
- 任何原本会让用户花一天时间在脑海中三个模糊 mockup 之间抉择的场景。

## 两种子形态——强烈优先选择子形态 A

UI 原型**紧贴应用其余部分**时更容易判断——真实 header、真实 sidebar、真实数据、真实密度。单独存在的抛弃式 route 是真空环境：每个变体独立看来都不错。只要有合理的现有页面可以承载变体，就默认使用子形态 A。只有原型确实没有邻近归属时，才使用子形态 B。

### 子形态 A——调整现有页面（首选）

Route 已经存在。变体在**同一个 route** 渲染，由 `?variant=` URL search param 控制。保留现有 data fetching、param 和 auth——只替换渲染内容。这是默认选择；除非有具体理由，否则使用它。

如果原型内容尚无页面，但*天然应该位于某个页面内部*（dashboard 的新 section、设置页面的新 card、现有流程的新步骤）——仍然属于子形态 A。将变体挂载到宿主页面内。

### 子形态 B——新页面（最后手段）

只有当要验证的事物确实没有现有页面可容纳时才使用——例如全新的顶层表面，或无法合理嵌入任何位置的流程。

遵循项目已有 routing 约定创建**抛弃式 route**——不要发明新的顶层结构。通过命名明确表明它是原型（例如在路径或文件名中加入 `prototype`）。使用相同的 `?variant=` 模式。

决定使用子形态 B 前，再次确认：真的没有可以嵌入的现有页面吗？空 route 会掩盖有内容页面能够暴露的设计问题。

两种子形态使用完全相同的底部浮动栏。

## 流程

### 1. 陈述问题并确定 N

默认为 **3 个变体**。超过 5 个后通常不再是截然不同，而会变成噪声——最多 5 个。

在原型所在位置或文件顶部注释中，用一行写下计划：

> “设置页面的三个变体，通过 `?variant=` 切换，位于现有 `/settings` route。”

无论用户是否在线提出异议，此方式都适用。

### 2. 生成截然不同的变体

起草每个变体。每个方案都应遵守：

- 页面的用途及其可访问的数据。
- 项目的 component library / styling system（TailwindCSS、shadcn、MUI、普通 CSS 等）。
- 清晰的 exported component name，例如 `VariantA`、`VariantB`、`VariantC`。

变体必须在**结构上不同**——布局、信息层级、主要 affordance 都应不同，不能只是颜色变化。三个略有调整的 card grid 不是 UI 原型，而是墙纸。如果两个草案过于相似，使用明确的“不要使用 card grid”指引重新设计其中一个。

### 3. 将它们连接起来

在 route 上创建一个 switcher component：

```tsx
// 伪代码——根据项目 framework 调整
const variant = searchParams.get('variant') ?? 'A';
return (
  <>
    {variant === 'A' && <VariantA {...data} />}
    {variant === 'B' && <VariantB {...data} />}
    {variant === 'C' && <VariantC {...data} />}
    <PrototypeSwitcher variants={['A','B','C']} current={variant} />
  </>
);
```

对于子形态 A（现有页面）：保留 switcher 上方所有现有 data fetching；每个变体只替换渲染的 subtree。

对于子形态 B（新页面）：`/prototype/<name>` 下的抛弃式 route 挂载相同 switcher。

### 4. 构建浮动 Switcher

在屏幕底部中央放置一个小型固定定位栏，包含三部分：

- **左箭头**——切换到上一个变体（循环）。
- **变体标签**——显示当前变体 key；如果变体导出了名称，也同时显示。例如 `B — Sidebar layout`。
- **右箭头**——向前切换（循环）。

行为：

- 点击箭头会更新 URL search param（使用 framework 的 router——Next 使用 `router.replace`，React Router 使用 `navigate` 等），使变体可分享并在重新加载后保持稳定。
- 键盘：`←` 和 `→` 方向键也可切换。当 `<input>`、`<textarea>` 或 `[contenteditable]` 获得焦点时，不要拦截方向键。
- 与页面视觉明显区分（例如高对比度 pill、轻微阴影），清楚表明它不属于被评估的设计。
- 在 production build 中隐藏——通过 `process.env.NODE_ENV !== 'production'` 或等效检查控制，避免原型意外合并后把切换栏发布给用户。

将 switcher 放在一个共享 component 中，让两种子形态复用。将它放在项目存放共享 UI 的位置。

### 5. 交给用户

提供 URL（以及 `?variant=` key）。用户方便时会逐个切换。最有价值的反馈通常是**“我想要 B 的 header 加上 C 的 sidebar”**——这才是他们真正想要的设计。

### 6. 记录答案并清理

一个变体胜出后，记录选中了哪个以及原因（commit message、ADR、issue；如果 AFK 运行且用户尚未回复，则写入原型旁的 `NOTES.md`）。然后：

- **子形态 A**——删除失败变体和 switcher；将胜出方案折叠进现有页面。
- **子形态 B**——将胜出变体提升为正式 route，删除抛弃式 route 和 switcher。

不要留下变体 component 或 switcher。它们会迅速腐化并迷惑下一位读者。

## 反模式

- **变体只有颜色或文案不同。** 那是微调，不是原型。真正的变体在结构上存在分歧。
- **变体之间共享过多代码。** 共享 `<Header>` 没问题；共享 `<Layout>` 会违背目的。每个变体都应能够完全抛弃布局。
- **把变体连接到真实 mutation。** 只读原型没问题。如果变体必须修改内容，将其指向 stub——问题是“它应该长什么样”，而不是“后端是否工作”。
- **把原型直接提升到生产环境。** 变体代码是在原型约束下编写的（无测试、最少错误处理）。折叠进正式实现时要正确重写。
