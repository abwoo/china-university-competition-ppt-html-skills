# HTML 预设：Frontend Slides 融合

来源：zarazhangrui/frontend-slides（MIT，Copyright (c) 2025 Zara Zhang）。
本文件搬运其 12 预设名单与三预览机制，改写成本 skill 的 HTML 路线预设流程；
未拷入其 bold-template-pack 全文。完整出处与许可见 `references/attribution.md`。

## 1. 12 个安全预设（名单照搬）

| 预设 | 气质 | 适合 |
|---|---|---|
| Bold Signal | 大胆信号 | 路演、产品发布、战略声明 |
| Electric Studio | 电气工作室 | 科技演示 |
| Creative Voltage | 创意电压 | 科技 / AI 产品 Demo |
| Dark Botanical | 深色植物 | 高端品牌 |
| Notebook Tabs | 笔记本标签 | 企业级合作提案 |
| Pastel Geometry | 粉彩几何 | 叙事、思想领导力 |
| Split Pastel | 分割粉彩 | 创意演示 |
| Vintage Editorial | 复古编辑 | 品牌、编辑类 |
| Neon Cyber | 霓虹赛博 | 开发工具、AI、黑客松 |
| Terminal Green | 终端绿 | 开发者大会 |
| Swiss Modern | 瑞士现代 | 企业级合作提案 |
| Paper & Ink | 纸墨 | 正式、文气场合 |

本 skill 加一个专属预设：**tech-style**（蓝紫节点 + 黄标题 + 40px 网格，
见 `references/style-tokens.md`），作为默认主预设。

## 2. 三预览机制（照搬）

默认出 3 个真实预览，角色固定、缺一不可：

1. **1 个安全预设**：从上面 12 个里选；
2. **至少 1 个 bold 模板**：从 bold-template-pack（34 个设计系统）里选；
3. **1 个 wildcard**：第二个 bold 模板，或 agent 针对本次 brief 自设计的风格。

每个预览都是用**真实第一页内容**做的单页 HTML（约 50–100 行），
不是占位诊断卡。NON-NEGOTIABLE 规则：预览必须像真实第一页，
不许把模板名、文件名、需求笔记写进画面。

本 skill 的改编：三预览改为"tech-style 主预设 + 1 个深色备选
（Neon Cyber 或 Terminal Green）+ 1 个 wildcard"，用户点选后再做全 deck。

## 3. 心情映射（照搬）

| 心情 | 候选预设 |
|---|---|
| impressed（震撼/自信） | Bold Signal、Electric Studio、Dark Botanical |
| energized（兴奋/有活力） | Creative Voltage、Neon Cyber、Split Pastel |
| focused（专注/冷静） | Notebook Tabs、Paper & Ink、Swiss Modern |
| inspired（受启发/感动） | Dark Botanical、Vintage Editorial、Pastel Geometry |

不知道选哪个时问心情（四个选项），不要让用户从 12 个名字里挑。

## 4. 零依赖与转换（照搬）

- 单文件 HTML，内联 CSS/JS，零依赖，无 npm、无构建工具；
- PPTX→HTML 转换：`scripts/extract-pptx.py`，保留图片与内容；
- 固定 16:9；反 AI 味：禁通用紫渐变白底等陈词滥调
  （本 skill 的紫是深底上的蓝紫发光，不在禁令内）。

## 5. 在模板里的落地

`assets/template.html` 顶部控制条有预设切换：
`tech-style`（默认）/ `Neon Cyber` / `Terminal Green`，
切换只换 CSS 变量（底色、节点色、辉光色、标题色），结构与动画不变。
