# 幻灯片版式

## 1. 标准内容（卡片网格）
适合 3–4 个要点。
```html
<div class="slide-container" id="slideX">
    <h2 class="animate-in">Slide Title</h2>
    <div class="content-area">
        <div class="grid-tiled">
            <div class="card animate-in delay-1">
                <h3>Point 1</h3>
                <p>Brief description</p>
            </div>
            <div class="card animate-in delay-2">
                <h3>Point 2</h3>
                <p>Brief description</p>
            </div>
            <div class="card animate-in delay-3">
                <h3>Point 3</h3>
                <p>Brief description</p>
            </div>
        </div>
    </div>
</div>
```

## 2. 可滚动内容
适合代码块、长表格或详细日志。
```html
<div class="slide-container compact" id="slideX">
    <h2 class="animate-in">Detailed Content</h2>
    <div class="content-area scrollable">
        <pre class="code-block">
<!-- Long code content here -->
        </pre>
    </div>
</div>
```

## 3. 清单
适合需求项或步骤完成情况。
```html
<div class="slide-container" id="slideX">
    <h2 class="animate-in">Checklist</h2>
    <div class="content-area">
        <ul class="checklist">
            <li><span class="check-icon">✓</span> Item 1</li>
            <li><span class="check-icon">✓</span> Item 2</li>
            <li><span class="check-icon">✓</span> Item 3</li>
        </ul>
    </div>
</div>
```

## 4. 紧凑网格
适合 6–8 个较小条目。
```html
<div class="slide-container compact" id="slideX">
    <h2 class="animate-in">Many Items</h2>
    <div class="content-area">
        <div class="grid-compact">
            <div class="card animate-in delay-1">Content 1</div>
            <div class="card animate-in delay-1">Content 2</div>
            <!-- More cards -->
        </div>
    </div>
</div>
```

## 5. 左右分栏（文字 + 视觉）
适合用图或图形解释一个概念。
```html
<div class="slide-container" id="slideX">
    <h2 class="animate-in">Concept Title</h2>
    <div class="content-area">
        <div class="grid-2">
            <div class="animate-in delay-1">
                <h3>Key Concept</h3>
                <p>Explanation of the concept.</p>
                <ul>
                    <li>Detail 1</li>
                    <li>Detail 2</li>
                </ul>
            </div>
            <div class="animate-in delay-2">
                <!-- Image or Code -->
            </div>
        </div>
    </div>
</div>
```

## 6. 问答（末页）
必须作为最后一页。
```html
<div class="slide-container" id="slide[LAST]">
    <div class="content-area" style="align-items: center; justify-content: center; text-align: center;">
        <h2 class="animate-in" style="font-size: 52px; margin-bottom: 16px;">Q & A</h2>
        <p class="subtitle animate-in delay-1">Thank you for your attention.</p>
        
        <div class="animate-in delay-2" style="margin-top: 40px; display: flex; gap: 16px;">
            <a href="mailto:your@email.com" class="pill">Contact</a>
        </div>
    </div>
</div>
```
