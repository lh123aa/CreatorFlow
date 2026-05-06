# OpenCLI 学习文档

> 让任何网站、Electron应用、本地工具变成AI可调用的命令行

---

## 项目信息

| 项目信息 | 详情 |
|---------|------|
| GitHub | https://github.com/jackwener/opencli |
| npm包 | @jackwener/opencli |
| Star数 | 12,000+ |
| 开源协议 | BSD-3-Clause |
| 开发语言 | TypeScript |
| 运行环境 | Node.js 20+ |

---

## 核心定位

**Make Any Website & Tool Your CLI** —— 让任何网站、Electron应用或本地工具，都变成命令行接口。

---

## 核心特性

### 1. 账号安全
- 复用Chrome已登录状态
- 凭据永不离开浏览器
- 零API Key配置

### 2. AI Agent 就绪
- `explore` 发现API
- `synthesize` 生成适配器
- `cascade` 探测认证策略
- `generate` 一键生成命令

### 3. 双引擎架构
| 引擎 | 适用场景 | 特点 |
|------|----------|------|
| YAML 声明式 | 标准数据抓取 | 简单直观，社区贡献友好 |
| TypeScript 运行时 | 复杂浏览器自动化 | 灵活强大，支持动态交互 |

### 4. 广泛的平台支持
- **网站**：B站、知乎、小红书、Twitter/X、Reddit、YouTube等80+
- **Electron应用**：Cursor、ChatGPT Desktop、Discord、Notion
- **本地CLI工具**：gh、docker、kubectl透传

---

## 技术架构

```
CLI进程 → 本地守护进程(localhost:19825) → WebSocket → Chrome扩展 → 浏览器/应用
```

### Browser Bridge
- **Chrome扩展**：在浏览器中执行JavaScript，与网页交互
- **微守护进程**：后台运行，自动启动，零配置

---

## 安装与配置

### 安装
```bash
npm install -g @jackwener/opencli
```

### 浏览器扩展设置
1. 打开 `chrome://extensions`
2. 启用开发者模式
3. 点击"加载已解压的扩展程序"
4. 选择 `extension/` 文件夹

### 验证安装
```bash
opencli --version      # 查看版本
opencli list           # 查看所有可用命令
opencli doctor         # 诊断扩展和守护进程连接状态
opencli doctor --live  # 诊断+测试实时命令
```

---

## 常用命令

### 基础命令
```bash
# 查看命令列表
opencli list
opencli list -f yaml    # YAML格式输出

# 公开API（无需浏览器）
opencli hackernews top --limit 5

# 浏览器命令（需要已登录）
opencli bilibili hot --limit 5
opencli zhihu hot -f json
opencli xiaohongshu search "关键词"
```

### AI Agent 工作流
```bash
# 探索网站API
opencli explore <URL> --site <name>

# 生成适配器
opencli synthesize <site>

# 探测认证策略
opencli cascade <URL>

# 一键生成（探索→合成→注册）
opencli generate <URL> --goal "获取热门内容"
```

### 输出格式
```bash
opencli bilibili hot -f json      # JSON格式
opencli bilibili hot -f yaml      # YAML格式
opencli bilibili hot -f table     # 表格格式
opencli bilibili hot -f markdown  # Markdown格式
```

---

## 内置适配器（部分）

### 社交媒体
| 平台 | 命令 | 功能 |
|------|------|------|
| Twitter/X | `opencli twitter` | 帖子、用户信息 |
| Reddit | `opencli reddit` | 讨论、评论 |
| LinkedIn | `opencli linkedin` | 职业信息 |

### 内容平台
| 平台 | 命令 | 功能 |
|------|------|------|
| B站 | `opencli bilibili hot/search/me` | 热门、搜索、个人信息 |
| 知乎 | `opencli zhihu hot/search` | 热门、搜索 |
| 小红书 | `opencli xiaohongshu` | 笔记、搜索 |
| YouTube | `opencli youtube` | 视频信息 |

### Electron应用
| 应用 | 命令 | 功能 |
|------|------|------|
| Cursor | `opencli cursor send/read/new` | 发送消息、读取、新建会话 |
| ChatGPT Desktop | `opencli chatgpt` | 对话操作 |
| Notion | `opencli notion` | 文档操作 |

---

## 自定义适配器

### YAML适配器示例
```yaml
name: mysite
description: 我的网站适配器
commands:
  hot:
    description: 获取热门内容
    fetch:
      url: "https://example.com/hot"
    parse:
      selector: ".hot-item"
      fields:
        title: "h3"
        link: "a@href"
```

### 动态加载
- 将 `.ts` 或 `.yaml` 适配器放入 `clis/` 文件夹
- 自动注册，无需手动配置

---

## 与 Playwright CLI 的对比

| 特性 | OpenCLI | Playwright CLI |
|------|---------|----------------|
| 定位 | 网站转CLI工具 | 浏览器自动化框架 |
| 适配器 | 80+内置，开箱即用 | 需自行编写 |
| 登录处理 | 复用Chrome登录 | 需手动处理 |
| AI集成 | 原生支持explore/synthesize | 需二次封装 |
| 适用场景 | 数据采集、内容操作 | 自动化测试、网页操作 |

**结论**：OpenCLI更适合快速获取网站数据，Playwright CLI更适合精细化的浏览器自动化控制。

---

## 与 AI Agent 集成

### AGENT.md 标准协议
AI Agent可以通过标准化接口发现和调用OpenCLI工具：

```markdown
# 在 AGENT.md 或 .cursorrules 中配置
当需要访问网站数据时，先执行 `opencli list` 发现可用工具。
```

### 零 Token 成本
- 适配器是确定性的——相同命令产生相同结构输出
- 不需要LLM解析网页
- 与Browser-Use等方案相比，成本更低

---

## 实际应用场景

### 1. 数据抓取与监控
```bash
# 定时抓取热榜
opencli bilibili hot -f json > bilibili_hot.json
opencli zhihu hot -f json > zhihu_hot.json
```

### 2. 内容创作辅助
```bash
# 下载笔记内容
opencli xiaohongshu note <id> -f markdown
```

### 3. 跨应用工作流
```bash
# 从雪球获取股票数据 → AI分析 → 发送到飞书
opencli xueqi stock <code> | ai-analyze | opencli feishu send
```

### 4. 桌面AI应用控制
```bash
# 控制Cursor写代码
opencli cursor send "帮我写一个Python爬虫"
opencli cursor read  # 读取回复
```

---

## 注意事项

1. **浏览器要求**：必须安装Chrome并登录目标网站
2. **扩展安装**：需要安装Browser Bridge扩展
3. **风控风险**：虽然宣称零风控，但站点策略变化可能影响使用
4. **Electron适配**：需阅读官方适配文档，不同应用版本可能有差异

---

## 相关资源

- GitHub: https://github.com/jackwener/opencli
- npm: https://www.npmjs.com/package/@jackwener/opencli
- 中文文档: https://github.com/jackwener/opencli/blob/main/README.zh-CN.md

---

## 学习心得

OpenCLI的设计理念与之前学的CLI+Skill框架高度契合：

1. **CLI是AI的母语** —— OpenCLI把一切变成CLI，让AI可以轻松调用
2. **自解释性** —— `opencli list` 就能发现所有可用工具
3. **结构化输出** —— JSON/YAML格式，方便AI解析

**与定制Skills项目的关系**：
- OpenCLI可以作为数据采集层的工具
- 通过OpenCLI获取数据 → AI分析 → 封装成Skill
- 可以考虑将常用的OpenCLI命令封装成自定义Skill

---
*学习日期：2026-04-13*
