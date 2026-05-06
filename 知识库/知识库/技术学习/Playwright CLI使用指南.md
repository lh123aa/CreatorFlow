# Playwright CLI 使用指南

> Microsoft 开发的浏览器自动化命令行工具，支持录制操作、生成测试代码、元素定位、截图等功能

## 一、安装

```bash
# 推荐方式（已整合到主包）
npm install -g @playwright/cli@latest
playwright-cli install --skills

# 或通过 npx 直接使用
npx playwright --help
```

**注意**：旧版 `playwright-cli` 已迁移至 `playwright` 核心包，推荐使用 `npx playwright` 命令

## 二、核心命令速查

### 页面操作
| 操作 | 命令 |
|------|------|
| 打开页面 | `playwright-cli open https://example.com` |
| 导航 | `playwright-cli goto <url>` |
| 获取快照 | `playwright-cli snapshot` |
| 点击元素 | `playwright-cli click e15` 或 `playwright-cli click "#btn"` |
| 输入文本 | `playwright-cli type "hello world"` |
| 填充表单 | `playwright-cli fill e15 "text"` |
| 按键 | `playwright-cli press Enter` |
| 截图 | `playwright-cli screenshot --filename=shot.png` |
| 关闭页面 | `playwright-cli close` |

### 元素定位
```bash
# 使用快照返回的元素引用
playwright-cli snapshot    # 获取页面快照，返回元素引用如 e15
playwright-cli click e15   # 点击元素

# 使用 CSS 选择器
playwright-cli click "#main > button.submit"

# 使用 role 选择器
playwright-cli click "role=button[name=Submit]"
```

### 标签页管理
```bash
playwright-cli tab-list              # 列出所有标签页
playwright-cli tab-new [url]         # 新建标签页
playwright-cli tab-select <index>    # 切换标签页
playwright-cli tab-close [index]     # 关闭标签页
```

### 存储与Cookie
```bash
# 保存登录状态
playwright-cli state-save auth.json
# 加载登录状态
playwright-cli state-load auth.json

# Cookie 操作
playwright-cli cookie-list           # 列出所有 cookie
playwright-cli cookie-get <name>     # 获取指定 cookie
playwright-cli cookie-set <name> <value>
playwright-cli cookie-delete <name>
```

### 网络请求
```bash
playwright-cli network               # 列出网络请求
playwright-cli route <pattern>       # 模拟网络请求
```

## 三、会话管理

### 多会话隔离
```bash
# 为不同项目创建命名会话
playwright-cli --session=dev open https://dev.example.com
playwright-cli --session=prod open https://example.com

# 列出所有活动会话
playwright-cli list

# 关闭所有浏览器
playwright-cli close-all
```

### 可视化监控
```bash
# 打开可视化仪表盘，查看和控制所有浏览器会话
playwright-cli show
```

## 四、配置选项

### 浏览器选择
```bash
playwright-cli open --browser=chrome https://example.com
playwright-cli open --browser=firefox
playwright-cli open --browser=webkit
playwright-cli open --browser=msedge
```

### 显示模式
```bash
# 有头模式（显示浏览器窗口）
playwright-cli open https://example.com --headed

# 无头模式（默认，不显示窗口）
playwright-cli open https://example.com
```

### 设备模拟
```bash
# 模拟移动设备
playwright-cli open --device="iPhone 13" https://example.com
playwright-cli resize 375 667  # iPhone SE 尺寸
```

## 五、高级功能

### 代码生成（录制）
```bash
# 启动录制模式，操作自动生成代码
npx playwright codegen

# 指定网站录制
npx playwright codegen https://example.com

# 生成 Python 代码
npx playwright codegen --target=python -o test.py
```

### 执行 JavaScript
```bash
# 在页面执行 JavaScript
playwright-cli eval "document.querySelector('.title').textContent"

# 执行 Playwright 代码片段
playwright-cli run-code "await page.waitForSelector('.dynamic-content')"
```

### 视频录制
```bash
playwright-cli video-start
playwright-cli video-chapter "测试步骤1"
playwright-cli video-stop --filename=test.mp4
```

### 追踪调试
```bash
playwright-cli tracing-start
# ... 执行操作 ...
playwright-cli tracing-stop
```

## 六、最佳实践

### 1. 快照策略
```bash
# ❌ 不好：不重新获取快照
playwright-cli open example.com
playwright-cli click e5
playwright-cli click e10  # DOM 可能已改变，e10 可能失效

# ✅ 好：重大操作后重新快照
playwright-cli open example.com
playwright-cli snapshot
playwright-cli click e5
playwright-cli snapshot  # 页面改变后重新获取
playwright-cli click e10
```

### 2. 等待策略
```bash
# ❌ 硬编码等待时间
playwright-cli click e5
sleep 5  # 不知道需要等多久

# ✅ 使用等待命令
playwright-cli click e5
playwright-cli run-code "await page.waitForLoadState('networkidle')"
```

### 3. 错误处理
```bash
#!/bin/bash
set -e  # 错误时退出

trap 'echo "测试失败于第 $LINENO 行"' ERR

playwright-cli open example.com || {
  echo "无法打开页面"
  exit 1
}
```

### 4. 登录状态复用
```bash
# 首次登录并保存状态
playwright-cli --session=auth open https://app.example.com --persistent
# ... 手动登录 ...
playwright-cli state-save auth.json

# 后续使用已保存的登录状态
playwright-cli open --load-storage=auth.json https://app.example.com
```

## 七、与 AI Agent 配合

Playwright CLI 特别适合 AI Agent 进行浏览器自动化：

1. **快照机制**：通过 snapshot 获取页面结构，Agent 可理解页面内容
2. **元素引用**：使用 e15 这样的引用而非复杂选择器，降低出错率
3. **会话隔离**：不同任务使用不同会话，互不干扰
4. **状态保存**：登录状态可持久化，避免重复登录

### 典型工作流
```bash
# 1. 打开页面
playwright-cli open https://example.com --headed

# 2. 获取页面快照，理解页面结构
playwright-cli snapshot

# 3. 执行操作
playwright-cli click e5
playwright-cli fill e8 "search text"
playwright-cli press Enter

# 4. 等待结果
playwright-cli run-code "await page.waitForLoadState('networkidle')"

# 5. 提取数据
playwright-cli eval "document.querySelector('.result').textContent"
```

## 八、常用场景示例

### 数据抓取
```bash
playwright-cli open https://github.com/microsoft/playwright
playwright-cli snapshot
STARS=$(playwright-cli eval "document.querySelector('.Counter').textContent")
echo "Playwright Stars: $STARS"
```

### 多页面数据对比
```bash
# 打开第一个页面
playwright-cli open https://github.com/microsoft/playwright
playwright-cli snapshot
STARS_1=$(playwright-cli eval "document.querySelector('.Counter').textContent")

# 打开新标签页
playwright-cli tab-new https://github.com/puppeteer/puppeteer
playwright-cli tab-select 1
playwright-cli snapshot
STARS_2=$(playwright-cli eval "document.querySelector('.Counter').textContent")

echo "Playwright: $STARS_1 vs Puppeteer: $STARS_2"
```

### 文件上传
```bash
playwright-cli open https://example.com/upload
playwright-cli snapshot
playwright-cli upload /tmp/test-file.txt
playwright-cli click e9  # 提交按钮
```

## 九、官方资源

- 官方文档：https://playwright.dev/docs/getting-started-cli
- GitHub：https://github.com/microsoft/playwright

---
*学习日期：2026-04-12*
