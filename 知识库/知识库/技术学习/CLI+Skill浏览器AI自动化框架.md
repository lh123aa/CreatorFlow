# CLI + Skill 浏览器AI自动化框架

> 来源：抖音"技术爬爬虾"视频
> 整理时间：2026-04-12
> 视频链接：https://v.douyin.com/Olly6w6XmHg/

---

## 核心观点：CLI是AI的母语

- **GUI为人类设计**：人类不擅长记忆命令，更擅长图形工具
- **CLI为AI设计**：大模型天生学习过大量代码、命令行语料
- **CLI天然优势**：文本输入、结构化输出、报错清晰、易组合、方便自动化
- **趋势**：越来越多公司放弃MCP，拥抱CLI

---

## 两个核心开源项目

### 1. CLI Anything

**功能**：一行命令把任意开源软件CLI化

**工作原理**（7步自动化流程）：
1. 分析软件源代码
2. 分析每个UI操作背后的API逻辑
3. 规划CLI命令分组
4. 设计输入输出
5. 编码实现
6. 编写测试用例
7. 更新文档并发布

**案例：draw.io CLI化**
- 把需要拖拽操作的画板工具变成CLI命令
- AI可以自动绘制流程图、架构图
- 输出drawio格式源文件 + SVG预览图

**已测试软件**：11款开源软件

### 2. OpenCLI

**功能**：把任意网站或Electron桌面应用变成CLI工具

**技术架构**：
- 浏览器插件 + WebSocket通信
- 无需CDP，零指纹检测
- 支持Headless模式和远程浏览器

**案例**：
- `opencli hackernews top --limit 5` —— 获取Hacker News热门
- `opencli grok ask "问题"` —— 自动操作Chrome访问Grok
- `opencli boss search --city 青岛 --job 软件开发` —— 搜索职位

**已接入网站**：Google、Gmail、YouTube、小红书、知乎、Boss直聘等

---

## 关键技术点

### 1. 自解释性（渐进式披露）
- AI可随时调用`--help`学习命令用法
- 不需要一次性学会所有知识
- 大幅减少Token消耗，保证调用准确率

### 2. Browser-CLI架构
```
CLI (client) ── NDJSON/Unix socket ──→ Daemon (server) ── JSON/WebSocket ──→ Extension (browser)
```
- 通过浏览器插件运行，非Headless模式
- 无`navigator.webdriver`指纹
- 共享用户登录状态和Cookie

### 3. Site-Specific Guides
预置热门网站的自动化脚本：
- Google搜索结果提取、分页
- Gmail收件箱、邮件读写
- YouTube视频信息
- 小红书搜索、笔记详情
- 知乎问答

### 4. 结构化输出
- 所有命令支持`--json`输出
- 统一信封格式：`{success, data, error}`
- 方便AI解析和处理

---

## 与定制Skills项目的关系

**本质相同**：把复杂操作封装成可调用的工具

**可借鉴的设计模式**：
1. **原子化命令**：每个命令做一件事
2. **自解释文档**：提供清晰的`--help`
3. **结构化输出**：统一JSON格式
4. **渐进式披露**：不需要一次性传递所有信息

---

## 相关项目链接

- Browser-CLI：https://github.com/six-ddc/browser-cli
- CLI Anything：GitHub搜索"cli-anything"
- OpenCLI：GitHub搜索"opencli"

---

## 后续待学习

- [ ] Browser-CLI的具体安装和使用
- [ ] 如何为特定网站编写Site Guide
- [ ] 如何用AI自动生成CLI工具
- [ ] 视频完整文案内容（待豆包APP提取）
