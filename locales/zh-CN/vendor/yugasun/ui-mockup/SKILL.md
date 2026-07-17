---
name: ui-mockup
description: >
  为 UI 设计生成 HTML/CSS 模型。产出可在浏览器预览、使用占位数据的模型文件。
  当用户提到 ui-mockup、mockup、设计 UI、wireframe，或某项功能需要视觉参考时使用。
---

# UI 模型

生成静态 HTML 模型，作为 Builder 实现时的视觉参考。

## 输出结构

```
.scratch/<feature>/mockups/
├── index.html              # 链接到所有模型的入口页面
├── <page-name>.html        # 每个页面/状态一个 HTML
└── design-notes.md         # 设计决策和交互
```

## 模型规则

### HTML

- 自包含：无需构建步骤，可直接在浏览器中打开
- 通过 `<style>` 使用内联 CSS，或使用 CDN 框架（优先 Tailwind CDN）
- 使用语义化 HTML 结构
- 占位数据用 `[placeholder]` 标记

### CSS

- 使用 8px 网格间距系统
- 使用 CSS 变量定义颜色和间距
- 响应式：桌面端（>1024px）、平板端（768–1024px）、移动端（<768px）
- 使用媒体查询设置响应式断点

### 状态

用单独文件或 CSS 类展示关键状态：

- 默认
- 悬停/激活
- 错误/验证
- 加载/空状态
- 成功

### 不使用 JavaScript 逻辑

- 不添加事件处理器
- 不动态获取数据
- 在 `design-notes.md` 中描述交互
- 可用 CSS `:hover`、`:active`、`:focus` 展示视觉状态

## 模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Page Name] — Mockup</title>
  <style>
    :root {
      --color-primary: #1a73e8;
      --color-error: #d93025;
      --color-success: #188038;
      --spacing-unit: 8px;
      --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: var(--font-family); padding: calc(var(--spacing-unit) * 3); }
    /* 页面专用样式 */
  </style>
</head>
<body>
  <!-- 模型内容 -->
</body>
</html>
```

## index.html

链接到所有模型文件的入口页面：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>模型 — [功能名称]</title>
  <style>
    body { font-family: sans-serif; padding: 32px; max-width: 600px; }
    h1 { margin-bottom: 16px; }
    ul { list-style: none; }
    li { margin: 8px 0; }
    a { color: #1a73e8; text-decoration: none; }
    a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <h1>[功能名称]模型</h1>
  <ul>
    <li><a href="page-name.html">页面名称</a> — 描述</li>
  </ul>
</body>
</html>
```

## 设计说明格式

编写包含以下内容的 `design-notes.md`：

1. **页面**——列出所有模型文件及其用途的表格
2. **设计决策**——颜色、字体、间距的选择理由
3. **交互**——用文字描述悬停、点击和过渡
4. **响应式**——每个页面在各断点下的行为
5. **组件**——所用 UI 组件及其变体的表格

## 流程

1. 阅读 `.scratch/<feature>/NOTES.md` 和 `tech-spec.md` 了解上下文
2. 识别所需页面和状态
3. 先生成 `index.html`
4. 为每个页面生成 HTML
5. 编写 `design-notes.md`
6. 汇报：生成的文件列表 + 打开浏览器的命令

## 与设计系统集成

如果目标项目已有设计系统：

- 将其颜色 token 用作 CSS 变量
- 遵循其组件模式
- 在 `design-notes.md` 中引用其组件名称
