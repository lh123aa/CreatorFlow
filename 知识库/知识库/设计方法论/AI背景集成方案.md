# AI生图背景集成方案

> 学习时间：2026-05-03
> 来源：定向学习方案（Day07训练记录）
> 解决什么问题：将AI生成的水彩背景图集成到小红书封面渲染流程
> 可作为什么评估标准：背景质感真实度、AI与卡片的融合度、渲染性能

---

## 一、当前技术状态

### 已有能力
| 模块 | 状态 | 说明 |
|------|------|------|
| 提示词生成 | ✅ 完成 | `get_ai_prompt()`函数，主题+布局组合 |
| CSS背景图类 | ✅ 完成 | `.has-bg-image`类已定义 |
| AI生图工具 | ✅ 可用 | image_generate工具 |
| 背景集成逻辑 | ❌ 缺失 | 需要实现 |

### 技术架构
```
render_watercolor.py
├── get_ai_prompt() → 生成提示词 ✅
├── generate_ai_background() → 只保存提示词，未实际生图 ❌
└── render_watercolor_markdown() → 渲染HTML
    └── HTML模板（cover_watercolor.html）
        └── .has-bg-image → 设置背景图样式 ✅
```

---

## 二、集成方案

### 方案A：两步式工作流（推荐）

```
1. 调用image_generate生成背景图 → 保存到本地
2. 传入render_watercolor.py作为背景图路径
3. 脚本在HTML中设置背景图URL
```

**优点**：
- 灵活控制AI生图时机
- 可预览后确认
- 错误可回退

**缺点**：
- 需要两次调用（生图+渲染）
- 需要额外的文件管理

### 方案B：自动集成（未来优化）

```
1. 脚本内部调用AI生图API
2. 等待生成完成
3. 自动渲染
```

**优点**：
- 一键完成
- 体验流畅

**缺点**：
- 依赖AI API可用性
- 无法预览确认
- 生成失败会导致整体失败

---

## 三、推荐工作流程

### Step 1：生成AI背景图
```python
# 使用image_generate工具
prompt = get_ai_prompt(theme, layout)
# 调用image_generate(prompt=prompt, count=1)
# 保存到: .skills/skill_Auto-RedNote/assets/bg_{theme}_{timestamp}.png
```

### Step 2：渲染时传入背景图
```bash
python render_watercolor.py content.md \
  -t warm-pink-orange \
  -l center \
  --background assets/bg_warm-pink-orange_20260503.png
```

### Step 3：脚本内部处理
```python
# 在render_watercolor.py中添加：
if background_path:
    html_content = html_content.replace(
        'class="cover-container ' + theme,
        'class="cover-container ' + theme + ' has-bg-image'
    )
    # 在CSS中添加背景图URL（通过style属性）
```

---

## 四、HTML模板改造要点

### 1. 添加背景图样式
```css
/* AI生成背景图 */
.cover-container.has-bg-image {
    background: url('{{AI_BG_PATH}}') center/cover no-repeat !important;
}
```

### 2. 脚本注入背景图路径
```python
html_content = html_content.replace('{{AI_BG_PATH}}', background_path)
```

### 3. 保持水彩纹理叠加
```css
.cover-container.has-bg-image::before {
    /* 叠加水彩纹理 */
    mix-blend-mode: soft-light;
    opacity: 0.15;
}
```

---

## 五、测试验证清单

- [ ] warm-pink-orange + center 布局
- [ ] warm-rose + asymmetric 布局
- [ ] warm-vintage + thirds 布局
- [ ] AI背景与卡片的色彩协调性
- [ ] 底部安全区（预留小红书标签区域）
- [ ] 不同设备DPR的清晰度

---

## 六、优化方向

### 短期（1-2天）
1. 实现方案A的两步式工作流
2. 测试3-5个主题×布局组合
3. 验证AI背景与卡片的融合效果

### 中期（3-5天）
1. 增加装饰元素（花枝、叶片、光斑）
2. 优化水彩纹理叠加效果
3. 建立背景图素材库

### 长期
1. 方案B的自动集成
2. 多风格背景图生成
3. 与移动端App的联动

---

## 七、关键参考

- **Day07训练记录**：`./进化引擎/训练记录/Day07_20260502.md`
- **水彩技术知识库**：`./知识库/视觉设计/水彩装饰效果技术.md`
- **AI生图提示词模板**：`./.skills/skill_Auto-RedNote/scripts/render_watercolor.py`
