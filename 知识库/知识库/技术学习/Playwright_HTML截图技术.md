# Playwright HTML转PNG截图技术

> 学习日期：2026-04-26
> 
> **解决的问题**：Auto-RedNote Skill 渲染引擎断链问题
> **可作为什么评估标准**：检查渲染脚本是否正确集成 Playwright 截图能力

---

## 核心模式：同步截图API

```python
from playwright.sync_api import sync_playwright

def html_to_image_sync(html_file_path, output_image_path):
    """同步版本的HTML转图片"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # 设置视口大小（关键参数！）
        page.set_viewport_size({"width": 1080, "height": 1440})
        
        # 读取HTML内容
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # 设置内容并等待加载
        page.set_content(html_content, wait_until="domcontentloaded")
        
        # 等待字体和样式渲染
        page.wait_for_timeout(1000)
        
        # 截图
        page.screenshot(path=output_image_path, full_page=False)
        
        browser.close()
```

---

## 关键参数说明

### 1. sync_playwright() vs async_playwright

| 模式 | 适用场景 | 代码复杂度 |
|------|----------|------------|
| `sync_playwright()` | 简单单次截图 | 低 ✅ |
| `async_playwright()` | 批量处理/并发 | 高 |

**结论**：单张图片渲染用同步API即可。

### 2. page.set_viewport_size()

```python
# 小红书封面：1080x1440（3:4竖版）
page.set_viewport_size({"width": 1080, "height": 1440})

# 小红书正文卡片：1080x1440
page.set_viewport_size({"width": 1080, "height": 1440})
```

**关键**：必须设置正确的视口大小，否则截图会被压缩。

### 3. page.set_content() 参数

```python
# wait_until 选项
page.set_content(html, wait_until="domcontentloaded")  # DOM加载完成 ✅ 推荐
page.set_content(html, wait_until="load")              # 所有资源加载完成
page.set_content(html, wait_until="networkidle")       # 网络空闲
page.set_content(html, wait_until="commit")           # 立即开始截图
```

### 4. page.screenshot() 参数

```python
page.screenshot(
    path="output.png",           # 保存路径
    full_page=False,             # False=只截可视区域，True=截完整页面
    type='png',                  # 'png' 或 'jpeg'
    omit_background=True,        # 透明背景（PNG）
    animations='disabled'        # 禁用动画
)
```

---

## 完整工作流集成

### Markdown → HTML → PNG 完整流程

```python
from playwright.sync_api import sync_playwright
from pathlib import Path
import yaml

def render_markdown_to_image(
    markdown_file: str,
    html_template: str,
    output_image: str,
    theme: str = 'warm-pink-orange',
    **kwargs
) -> dict:
    """
    完整渲染流程：Markdown → HTML模板填充 → Playwright截图
    """
    
    # Step 1: 解析 Markdown
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取 YAML 头部
    yaml_frontmatter = {}
    md_body = content
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml_frontmatter = yaml.safe_load(parts[1]) or {}
            md_body = parts[2].strip()
    
    # Step 2: 填充 HTML 模板
    html_content = html_template
    
    # 替换占位符
    html_content = html_content.replace('{{title}}', yaml_frontmatter.get('title', ''))
    html_content = html_content.replace('{{subtitle}}', yaml_frontmatter.get('subtitle', ''))
    html_content = html_content.replace('{{theme}}', theme)
    
    # 保存 HTML 临时文件
    temp_html = output_image.replace('.png', '.html')
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Step 3: Playwright 截图
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1080, "height": 1440})
        
        page.set_content(html_content, wait_until="domcontentloaded")
        page.wait_for_timeout(1000)  # 等待字体渲染
        
        page.screenshot(path=output_image, full_page=False)
        browser.close()
    
    # Step 4: 清理临时文件
    Path(temp_html).unlink()
    
    return {'output': output_image}
```

---

## 常见问题与解决

### 问题1：字体不渲染

```python
# 方案1：等待更长时间
page.wait_for_timeout(2000)

# 方案2：添加字体加载检测
page.wait_for_selector('body', state='visible')
```

### 问题2：中文显示乱码

```python
# 确保安装中文字体
# Linux: sudo apt install fonts-wqy-microhei fonts-wqy-zenhei
# 或在HTML中使用 web font
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&display=swap" rel="stylesheet">
```

### 问题3：背景图/外部资源加载失败

```python
# 方案1：内联图片为 base64
import base64
def image_to_base64(image_path):
    with open(image_path, 'rb') as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

# 方案2：等待网络空闲
page.set_content(html, wait_until="networkidle")
```

---

## 在 Auto-RedNote Skill 中的集成

### 需要修改的文件

| 文件 | 修改内容 |
|------|----------|
| `render_watercolor.py` | 添加 `html_to_image()` 函数 |
| `SKILL.md` | 更新工作流文档 |

### 集成示例

```python
# 在 render_watercolor.py 末尾添加

def _render_to_image(html_content: str, output_path: str, viewport: dict = None):
    """使用 Playwright 将 HTML 渲染为图片"""
    viewport = viewport or {"width": 1080, "height": 1440}
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size(viewport)
        
        page.set_content(html_content, wait_until="domcontentloaded")
        page.wait_for_timeout(1000)
        
        page.screenshot(path=output_path, full_page=False)
        browser.close()
    
    return output_path
```

---

## 评估标准检查清单

✅ 使用 `sync_playwright()` 同步API  
✅ 设置正确的 `viewport_size`（1080x1440）  
✅ 使用 `set_content()` 而非 `goto()`  
✅ 等待 DOM 加载完成（`wait_until="domcontentloaded"`）  
✅ 添加字体渲染等待时间  
✅ 截图保存到正确路径

---

## 参考资源

- [Playwright Python Screenshots](https://playwright.dev/python/docs/screenshots)
- [HTML to Image with Playwright](https://screenshotone.com/blog/playwright-python-screenshots/)
