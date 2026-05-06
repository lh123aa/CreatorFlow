# Huashu Design 使用指南

> 安装日期：2026-04-28
> 安装路径：`~/.agents/skills/huashu-design`

---

## 是什么

**花叔Design** —— 用HTML做高保真设计的Skill，4400+ stars的爆款开源项目。

核心能力：
- **打字回车就出设计** —— 一句话生成精美作品
- **HTML原生** —— 不是图片生成器，是真正可编辑的设计
- **多格式导出** —— HTML → PPTX / PDF / MP4 / GIF

---

## 七大能力

| 能力 | 交付物 | 耗时 |
|------|--------|------|
| **交互原型** | 单文件HTML，iPhone真机边框，可点击 | 10-15分钟 |
| **幻灯片** | HTML演示 + 可编辑PPTX | 15-25分钟 |
| **动画视频** | MP4(25fps/60fps) + GIF + BGM | 8-12分钟 |
| **设计变体** | 3+并排对比，Tweaks实时调参 | 10分钟 |
| **信息图** | 印刷级排版，PDF/PNG/SVG导出 | 10分钟 |
| **品牌动画** | Logo reveal、产品发布动画 | 15分钟 |
| **设计评审** | 5维度雷达图 + 改进清单 | 即时 |

---

## 触发词

直接说这些话就能触发：

**中文**：
- 做个原型、设计Demo、交互原型、HTML演示
- 动画Demo、导出MP4、导出GIF
- 设计变体、hi-fi设计、UI mockup
- app原型、iOS原型、移动应用mockup
- 设计风格、设计方向、配色方案、视觉风格
- 评审、好不好看

**英文**：
- prototype、design demo、interactive mockup
- export MP4、export GIF、60fps video
- design variations、hi-fi design
- app prototype、iOS mockup
- design style、design philosophy、review this design

---

## 核心工作流

### 1. Junior Designer模式

**不要闷头做大招**，先展示假设：

```
1. 写下assumptions + reasoning + placeholders
2. 用户确认方向
3. 写React组件填placeholder
4. 再show一次看进度
5. 迭代细节
```

### 2. 品牌资产协议（涉及品牌时必走）

**资产 > 规范**，识别度靠的是：
1. **Logo**（必需）
2. **产品图/渲染图**（实体产品必需）
3. **UI截图**（数字产品必需）
4. 色值、字体（辅助）

**5步流程**：
```
Step 1 → 问用户要资产清单
Step 2 → 搜官方渠道（官网/press kit/社媒）
Step 3 → 下载资产（5轮搜索，找10个，选2个好的，每个8分以上）
Step 4 → 验证+提取
Step 5 → 固化为 brand-spec.md
```

### 3. 设计方向顾问模式

**触发条件**：需求模糊、没有design context

**流程**：
```
Phase 1 → 深度理解需求
Phase 2 → 顾问式重述
Phase 3 → 推荐3套设计哲学（必须差异化）
Phase 4 → 展示预制Showcase画廊
Phase 5 → 生成3个视觉Demo
Phase 6 → 用户选择
Phase 7 → 生成AI提示词
Phase 8 → 进入主干流程
```

**20种设计哲学**（5流派 × 4种）：

| 流派 | 风格示例 |
|------|----------|
| 信息建筑派 | Pentagram、IBM Design |
| 运动诗学派 | Field.io、AKQA |
| 极简主义派 | Kenya Hara、Muji |
| 实验先锋派 | Sagmeister、Bibliothèque |
| 东方哲学派 | 无印良品、原研哉 |

---

## 反AI Slop清单

**什么是AI Slop？**
AI训练语料里最常见的"视觉最大公约数"——不携带品牌信息。

**要规避的**：

| 元素 | 为什么是slop |
|------|-------------|
| 激进紫色渐变 | "科技感"万能公式，烂大街 |
| Emoji作图标 | 不够专业就用emoji凑 |
| 圆角卡片+左彩色border | Material/Tailwind时期烂大街 |
| SVG画人脸/场景 | 五官错位，比例诡异 |
| CSS剪影代替产品图 | 任何产品都长一样，识别度归零 |
| Inter/Roboto作display | 太常见，看不出是"有设计" |
| 赛博霓虹/深蓝底#0D1117 | GitHub dark mode烂大街复制 |

**正确做法**：
- ✅ 用真实Logo/产品图（走品牌资产协议）
- ✅ 配图优先AI生成，不要SVG手画
- ✅ 一个细节做到120%，其他80%
- ✅ 宁可留诚实placeholder，不要烂实现

---

## 技术架构

### 单文件Inline React（默认）

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
</head>
<body>
  <div id="root"></div>
  <script type="text/babel">
    // 所有JSX/data/styles写在这里
    function App() {
      return <div>...</div>;
    }
    ReactDOM.render(<App />, document.getElementById('root'));
  </script>
</body>
</html>
```

### 可用组件（assets/）

| 组件 | 用途 |
|------|------|
| `ios_frame.jsx` | iPhone 15 Pro边框 + 灵动岛 |
| `android_frame.jsx` | Android设备边框 |
| `browser_window.jsx` | 浏览器预览窗口 |
| `macos_window.jsx` | 桌面应用窗口 |
| `animations.jsx` | 动画引擎 + Easing |
| `deck_stage.js` | HTML幻灯片引擎 |
| `design_canvas.jsx` | 并排变体展示 |

### 背景音乐（6首场景化BGM）

| 文件 | 场景 |
|------|------|
| `bgm-ad.mp3` | 广告/产品发布 |
| `bgm-tech.mp3` | 科技/技术展示 |
| `bgm-educational.mp3` | 教育/教程 |
| `bgm-tutorial.mp3` | 教程/演示 |

### 音效库（37个，8类）

路径：`assets/sfx/`
类别：whoosh、click、pop、chime、swoosh、transition、notification、success

---

## 导出能力

### HTML → PPTX
```bash
node scripts/export_deck_pptx.mjs input.html output.pptx
```

### HTML → PDF
```bash
node scripts/export_deck_pdf.mjs input.html output.pdf
```

### HTML → MP4/GIF
```bash
node scripts/render-video.js input.html output.mp4 --fps 60
node scripts/convert-formats.sh output.mp4  # 生成60fps + GIF
```

### 添加BGM
```bash
bash scripts/add-music.sh video.mp4 bgm-tech.mp3 output.mp4
```

---

## 使用示例

### 示例1：做个产品发布幻灯片

```
用户：帮我做一个AI心理学的产品发布PPT，给我3个风格方向选

Huashu Design：
1. 推荐3个设计哲学（信息建筑/运动诗学/东方极简）
2. 展示预制Showcase
3. 生成3个视觉Demo
4. 用户选择后生成完整HTML
5. 导出PPTX可编辑版本
```

### 示例2：做个iOS App原型

```
用户：做个番茄钟App原型，4个页面，要能点击交互

Huashu Design：
1. 生成单文件HTML（iPhone 15 Pro边框）
2. 4个页面可切换
3. Playwright验证点击流程
4. 双击打开即可演示
```

### 示例3：做个品牌动画

```
用户：给大疆Pocket 4做个发布动画

Huashu Design：
1. WebSearch确认产品已发布
2. 走品牌资产协议：下载DJI Logo + Pocket 4产品图
3. 生成动画HTML
4. 导出MP4 + BGM
```

---

## 文件结构

```
huashu-design/
├── SKILL.md              # 主文档（801行）
├── README.md             # 中文说明
├── README.en.md          # 英文说明
├── assets/               # 组件和资源
│   ├── ios_frame.jsx     # iPhone边框
│   ├── animations.jsx    # 动画引擎
│   ├── deck_stage.js     # 幻灯片引擎
│   ├── bgm-*.mp3         # 6首BGM
│   └── sfx/              # 37个音效
├── references/           # 20个参考文档
│   ├── design-styles.md  # 20种设计哲学详解
│   ├── slide-decks.md    # 幻灯片架构
│   ├── video-export.md   # 视频导出流程
│   └── ...
├── scripts/              # 导出脚本
│   ├── render-video.js   # HTML→MP4
│   ├── export_deck_pptx.mjs  # HTML→PPTX
│   └── ...
└── demos/                # 9个演示案例
```

---

## 与Forge项目的关联

两个项目可以配合使用：

| 场景 | Forge | Huashu Design |
|------|-------|---------------|
| 代码生成 | ✅ 45+技能 | ❌ |
| 产品原型 | ❌ | ✅ 交互原型 |
| 发布PPT | ❌ | ✅ 幻灯片+PPTX |
| 产品动画 | ❌ | ✅ MP4+GIF+BGM |
| 设计评审 | ❌ | ✅ 5维度打分 |

**组合场景**：
1. 用Forge写代码 → 用Huashu Design做产品原型
2. 用Forge开发功能 → 用Huashu Design做发布PPT
3. 用Forge迭代产品 → 用Huashu Design做演示动画

---

## 注意事项

1. **涉及品牌必须走资产协议** —— 找真实Logo和产品图
2. **需求模糊时进入顾问模式** —— 推荐3个方向让用户选
3. **反AI Slop** —— 不要紫色渐变、emoji图标、圆角卡片+左border
4. **单文件优先** —— 双击就能开，不要要求用户起server
5. **宁缺毋滥** —— 诚实的placeholder比烂实现好10倍

---

## 参考链接

- GitHub: https://github.com/alchaincyf/huashu-design
- 安装命令: `npx skills add alchaincyf/huashu-design --yes --global`
- 详细文档: `~/.agents/skills/huashu-design/SKILL.md`

---

## 关联知识
- **所属知识域**: 技术工具
- **相关迭代**: 第5期(1-10轮)、第6期(11-20轮)
- **关联知识库文件**: 
  - [方法论/AI时代个人创业机会方向_深度版2](./方法论/AI时代个人创业机会方向_深度版2.md)
  - [方法论/Harness_Engineering_AI驾驭工程学](./方法论/Harness_Engineering_AI驾驭工程学.md)
  - [运营体系/自媒体运营自动化与效率工具链指南](./运营体系/自媒体运营自动化与效率工具链指南.md)
- **实操应用**: AI设计工具的核心使用指南；可提升内容创作效率
