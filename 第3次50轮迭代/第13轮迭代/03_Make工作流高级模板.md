# Make工作流高级模板

## 前言

Make（原Integromat）是更强大的可视化自动化工具，适合复杂工作流设计。本指南提供高级Make工作流模板。

---

## 第一部分：Make基础架构

### 1.1 Make核心概念

**Module（模块）**

- Trigger Modules（触发器）
- Action Modules（执行器）
- Iterator Modules（迭代器）
- Aggregator Modules（聚合器）

**Connection（连接）**

- API连接配置
- 认证授权管理

**Scenario（场景）**

- 自动化工作流
- 定时执行或事件触发

### 1.2 Make vs Zapier对比

| 维度 | Make | Zapier |
|-----|------|--------|
| 复杂度 | 支持复杂逻辑 | 适合简单任务 |
| 价格 | 免费额度更高 | 免费版有限 |
| 调试 | 实时调试 | 有限调试 |
| 自定义 | 高度可定制 | 相对固定 |

---

## 第二部分：高级社媒模板

### 模板1：多平台同步发布系统

```
Modules:
1. RSS Trigger → 监听新内容
2. Router → 分发到多平台
3. YouTube Module → 发布
4. TikTok Module → 格式转换+发布
5. Instagram Module → 格式转换+发布
6. Google Sheets → 记录发布状态
7. Discord → 发送完成通知
```

### 模板2：评论智能回复系统

```
Modules:
1. YouTube Comment Trigger → 新评论
2. ChatGPT Module → AI生成回复
3. Filter → 人工审核判断
4. Router → 分流处理
5. YouTube Reply → 自动回复
6. Notion → 记录待审评论
```

### 模板3：多语言内容自动发布

```
Modules:
1. YouTube Trigger → 新视频
2. YouTube Caption → 获取字幕
3. DeepL Translate → 翻译阿拉伯语
4. YouTube Caption → 添加字幕
5. Google Sheets → 记录状态
```

---

## 第三部分：数据处理模板

### 模板4：跨平台数据汇总分析

```
Modules:
1. YouTube Module → 获取数据
2. TikTok Module → 获取数据
3. Instagram Module → 获取数据
4. Array Aggregator → 合并数据
5. Google Sheets → 写入汇总
6. ChatGPT → 生成分析报告
7. Gmail → 发送报告
```

### 模板5：粉丝行为自动分析

```
Modules:
1. YouTube Trigger → 新订阅
2. YouTube Analytics → 获取观看历史
3. Router → 分类处理
4. Array → 数据聚合
5. ChatGPT → 生成粉丝画像
6. Notion → 更新粉丝数据库
```

### 模板6：内容效果对比分析

```
Modules:
1. Schedule Trigger → 每周
2. YouTube → 获取视频列表
3. Iterator → 遍历每个视频
4. YouTube → 获取详细数据
5. Array → 汇总数据
6. Google Sheets → 生成对比表
7. ChatGPT → 生成建议
```

---

## 第四部分：变现自动化模板

### 模板7：多渠道收款汇总

```
Modules:
1. PayPal Trigger → 新收款
2. Payoneer Trigger → 新收款
3. Stripe Trigger → 新收款
4. Gumroad Trigger → 新收款
5. Array Aggregator → 合并记录
6. Google Sheets → 分类记录
7. Calculator → 计算总计
8. Gmail → 发送日结报告
```

### 模板8：会员订阅管理系统

```
Modules:
1. Stripe Trigger → 订阅事件
2. Router → 分流处理
3. 路径1：新订阅 → 发送欢迎 → 添加群组
4. 路径2：续费 → 更新记录 → 发送感谢
5. 路径3：取消 → 更新记录 → 发送挽留
6. Notion → 更新会员数据库
```

### 模板9：课程自动交付系统

```
Modules:
1. Teachable Trigger → 新注册
2. Gmail → 发送登录信息
3. Discord → 发送欢迎消息
4. Notion → 创建学员档案
5. Google Sheets → 更新学员表
6. Calendar → 创建学习提醒
```

### 模板10：联盟佣金自动追踪

```
Modules:
1. Amazon Trigger → 新订单
2. Parser → 提取订单详情
3. Calculator → 计算佣金
4. Google Sheets → 记录佣金
5. Calculator → 更新月度目标
6. Discord → 发送佣金通知
```

---

## 第五部分：高级逻辑模板

### 模板11：条件分支处理

```
Modules:
1. YouTube Trigger → 新视频
2. Filter → 判断视频类型
3. Router → 多条件分支
4. 路径A：教程 → 执行教程流程
5. 路径B：Vlog → 执行Vlog流程
6. 路径C：合作 → 执行合作流程
7. Aggregate → 汇总处理结果
```

### 模板12：批量数据处理

```
Modules:
1. Google Sheets Trigger → 新数据
2. Iterator → 遍历每行数据
3. ChatGPT → 处理每条数据
4. Google Sheets → 写入结果
5. Aggregator → 批量写入
```

### 模板13：错误自动重试

```
Modules:
1. HTTP Request → API调用
2. Error Handler → 错误处理
3. Retry → 自动重试3次
4. Router → 分流成功/失败
5. 成功路径 → 继续流程
6. 失败路径 → 发送警报
```

---

## 总结

Make适合复杂工作流设计，可以实现Zapier难以完成的自动化任务。学习Make的高级功能，解锁更强大的自动化能力。
