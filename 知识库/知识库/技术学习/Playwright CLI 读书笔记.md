# Playwright CLI 读书笔记

> 学习日期：2026-04-12
> 学习来源：官方文档 + CSDN 技术博客

## 为什么学这个？

之前做浏览器自动化任务，要么用云手机操作APP，要么用 agent-browser 技能。但云手机有时候卡顿、需要人工验证；agent-browser 技能不够灵活。

Playwright CLI 的优势：
- **纯命令行**：通过 Bash 就能调用，适合云电脑环境
- **快照机制**：Agent 可以通过 snapshot 理解页面结构，不用猜元素在哪
- **会话隔离**：不同任务不干扰，可以跑多个自动化流程

## 核心发现

### 1. 快照机制是最关键的

`playwright-cli snapshot` 返回的不是 HTML，而是**带有元素引用的页面结构**：

```
- e15 [button]: "提交"
- e16 [input]: 搜索框
- e17 [a]: "下一页"
```

这样 Agent 操作页面时，不需要写复杂的 CSS 选择器，直接用 `e15` 这样的引用就行。

**思考**：这个设计太适合 AI Agent 了。传统自动化要维护一堆选择器，页面改了就挂。快照机制让 Agent 每次操作前先"看一眼"页面，理解当前状态再操作。

### 2. 状态持久化解决登录问题

```bash
# 保存登录状态
playwright-cli state-save auth.json

# 加载登录状态
playwright-cli state-load auth.json
```

之前云手机登录抖音要人脸识别，卡住了。如果用 Playwright，登录一次保存状态，后面都能复用。

**思考**：对于需要登录的网站自动化，这个功能是刚需。可以维护一个"已登录状态库"，不同网站保存不同的 auth.json。

### 3. 会话命名让多任务并行

```bash
playwright-cli --session=task1 open https://site1.com
playwright-cli --session=task2 open https://site2.com
```

可以同时跑多个浏览器实例，各自独立。这就意味着可以并行处理多个自动化任务。

## 实践思考：怎么用到日常工作？

### 场景1：数据抓取
- 打开目标网站 → snapshot → 定位数据元素 → eval 提取
- 比用 Python 写爬虫简单，不用处理反爬

### 场景2：表单填写
- 打开表单页 → snapshot → fill 填字段 → click 提交
- 适合批量录入、定期报表提交这类重复工作

### 场景3：网站监控
- 定时打开网站 → snapshot → 检查关键元素是否存在 → 截图保存
- 可以做成定时任务，监控网站变化

## 与其他工具的对比

| 工具 | 优势 | 劣势 |
|------|------|------|
| Playwright CLI | 命令行友好、快照机制、会话隔离 | 需要云电脑环境 |
| agent-browser 技能 | 封装好、开箱即用 | 灵活性不够 |
| 云手机 mobile_use | 可操作APP | 需要人工验证、有时卡顿 |

**结论**：Playwright CLI 更适合"标准化、可重复"的浏览器自动化任务。需要人工判断、APP独有功能的，还是用云手机。

## 学习笔记要点

### 元素定位的两种方式

1. **快照引用**（推荐）
   ```bash
   playwright-cli snapshot
   playwright-cli click e15
   ```

2. **选择器**
   ```bash
   playwright-cli click "#btn-submit"
   playwright-cli click "role=button[name=提交]"
   ```

选择器适合元素固定不变的页面；快照引用适合动态页面。

### 等待策略

不要用 `sleep 5` 这种硬编码等待，用：
```bash
playwright-cli run-code "await page.waitForLoadState('networkidle')"
```

等页面真正加载完再操作。

### 错误处理

写脚本时要加错误处理：
```bash
set -e
trap 'echo "失败于第 $LINENO 行"' ERR
```

自动化任务失败时要能定位问题。

## 后续计划

1. 在云电脑上安装 Playwright CLI 测试一下
2. 尝试做一个简单的数据抓取任务验证流程
3. 考虑封装成 Skill，方便复用

---
*学习心得：Playwright CLI 的设计理念很适合 AI Agent 场景，快照机制是亮点。后续可以深度探索，形成稳定的自动化工作流。*
