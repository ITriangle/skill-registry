# 交互式 HTML 幻灯片生成器

生成高质量、单文件的 HTML 交互式演示文稿。需要做 presentation、slide deck 或 PPT 时使用本技能。

## 概览

本技能扮演前端开发 + 演示设计专家，生成接近 Keynote 品质的 HTML 演示。支持 **两条工作流**：

1. **Beautiful HTML Templates**（推荐）：来自 [beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates) 的 32 套专业模板。Agent 会问场合和气质，给出 3 个候选，再按真实模板的 HTML/CSS 制作。
2. **内置 CSS 主题**：4 套自包含主题（Cyberpunk、Corporate、Minimal、Nature），适合要快、要轻的输出。

## 能力

- **单文件输出**：CSS、JS、HTML 打进一个文件
- **可交互**：键盘/点击翻页，带进度条
- **响应式**：手机纵向滚动，桌面单页展示
- **32 套精美模板**：专业设计，视觉辨识度高
- **4 套内置主题**：Cyberpunk、Corporate、Minimal、Nature

## 用法

请 Agent 做幻灯片时，说明 **场合** 和 **气质/vibe**。Agent 会：

1. **问清口味**：问场合和想要的气质
2. **给出候选**：展示 3 套匹配模板，并提供可打开的预览
3. **制作**：按选定模板做出精致 HTML 文稿
4. **交付**：在浏览器里打开成稿

也可以直接点名主题（Cyberpunk/Corporate/Minimal/Nature），走更快的自包含输出。

## 模板库

`beautiful-html-templates/` 目录里有 32 套精选 HTML 幻灯片模板。完整元数据（mood、tone、formality、density、best_for）见 `beautiful-html-templates/index.json`。

重点模板：
- **Soft Editorial**：Cormorant Garamond 衬线配暖色纸面
- **8-Bit Orbit**：像素风霓虹街机美学
- **Studio**：黑画布配电光黄字体
- **Grove**：森林绿配古典 Playfair 衬线
- **Signal**：深海军蓝配哑光金点缀
- **Daisy Days**：明快粉彩，带手绘元素

## 目录结构

- `SKILL.md`：主技能定义与操作说明
- `examples/`：示例输出
- `templates/`：基础模板 + 脚本 + 版式（工作流 B）
- `themes/`：CSS 主题文件（工作流 B）
- `beautiful-html-templates/`：32 套 HTML 幻灯片模板库
  - `index.json`：模板元数据与匹配指南
  - `AGENTS.md`：完整 agent 操作手册
  - `templates/<slug>/template.html`：模板 HTML 文件
