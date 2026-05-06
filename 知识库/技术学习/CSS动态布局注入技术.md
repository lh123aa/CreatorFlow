# CSS 动态布局注入技术

## 学习日期
2026-04-27

## 背景问题

Auto-RedNote 技能的 HTML 渲染系统存在布局功能失效问题：
- CSS 中定义了 5 种布局类（.layout-centered, .layout-left-text, .layout-top-image, .layout-diagonal, .layout-whitespace）
- 但 HTML 模板硬编码了 `layout-centered`，无法动态切换
- JavaScript 切换时也只更新主题类，不更新布局类

## 核心知识点

### 1. HTML 模板变量注入模式

**错误模式（硬编码）**：
```html
<div class="cover-container watercolor-card theme-sunrise layout-centered">
```

**正确模式（变量注入）**：
```html
<div class="cover-container watercolor-card {{THEME_CLASS}} {{LAYOUT_CLASS}}">
```

### 2. CSS 类名切换机制

```javascript
// Python 端注入
html_content = html_content.replace('{{LAYOUT_CLASS}}', f'layout-{layout_name}')

// 动态切换
element.classList.remove('layout-centered', 'layout-diagonal')
element.classList.add(`layout-${newLayout}`)
```

### 3. 布局类与样式对应关系

| 布局名 | CSS 类 | 视觉效果 |
|--------|--------|----------|
| 居中对称 | .layout-centered | 中心聚焦，文字居中 |
| 左文右图 | .layout-left-text | 55%文字 + 45%图片 |
| 上图下文 | .layout-top-image | 60%图片 + 40%文字 |
| 对角构图 | .layout-diagonal | 旋转5度，动感 |
| 环绕留白 | .layout-whitespace | 200px内边距，呼吸感 |

### 4. 装饰元素随布局移动

**当前问题**：装饰元素（watercolor-blob）位置固定，不随布局变化

**解决方案**：装饰元素也需要根据布局注入不同的定位样式

```javascript
const DECOR_POSITIONS = {
  'centered': { top: '50%', left: '50%', transform: 'translate(-50%,-50%)' },
  'diagonal': { top: '20%', right: '10%' },
  'whitespace': { display: 'none' }  // 留白布局不需要装饰
}
```

## 修复方案

### Step 1: 修改 HTML 模板
```html
<div class="cover-container watercolor-card {{THEME_CLASS}} {{LAYOUT_CLASS}}">
  <div class="decorations {{LAYOUT_DECOR_CLASS}}">
    <!-- 装饰元素 -->
  </div>
</div>
```

### Step 2: 修改 Python 渲染函数
```python
def render_watercolor_markdown(markdown_file, theme, layout):
    # 读取 HTML 模板
    html_content = read_template('cover_watercolor.html')
    
    # 注入主题和布局类
    html_content = html_content.replace('{{THEME_CLASS}}', f'theme-{theme}')
    html_content = html_content.replace('{{LAYOUT_CLASS}}', f'layout-{layout}')
    
    # 注入装饰配置
    decor_class = LAYOUTS[layout].get('decor_class', 'decor-centered')
    html_content = html_content.replace('{{LAYOUT_DECOR_CLASS}}', decor_class)
```

### Step 3: 扩展 LAYOUTS 配置
```python
LAYOUTS = {
    "diagonal": {
        "name": "对角构图",
        "description": "动感活泼，吸引眼球",
        "decor_class": "decor-diagonal",
        "decor_style": "position: absolute; top: 15%; right: 8%;"
    }
}
```

## 评估标准

| 检查项 | 标准 |
|--------|------|
| 布局切换 | 5种布局应有明显视觉差异 |
| 装饰位置 | 装饰元素随布局合理定位 |
| 主题一致性 | 不同主题下布局保持一致 |
| 响应式 | 截图比例正确（1728x2304） |

## 相关文件

- `.skills/skill_Auto-RedNote/scripts/render_watercolor.py`
- `.skills/skill_Auto-RedNote/templates/cover_watercolor.html`
- `.skills/skill_Auto-RedNote/styles/styles_watercolor.css`
