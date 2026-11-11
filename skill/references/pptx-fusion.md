# PPTX 融合：PPT Master 的原生路线

来源：hugohe3/ppt-master（MIT，Copyright (c) 2025-2026 Hugo He）。
本文件搬运其 SVG→DrawingML 管线与七步流程，改写成本 skill 的 PPTX 导出指南；
未拷入其仓库代码。完整出处与许可见 `references/attribution.md`。

## 1. 核心思想（照搬）

AI 手写 SVG，确定性脚本把 SVG 翻译成 PowerPoint 原生 DrawingML。
两者都用绝对坐标描述形状，所以矩形、路径、渐变、阴影几乎一对一映射。
AI 做它擅长的事（用文本友好的格式画图），脚本做精确翻译。

结果不是"可编辑"而已，而是真正的 PowerPoint：每个形状、文本框、图表、
表格都是原生对象，点开就能改颜色、字体、数据；支持母版/版式继承
（`p:sldMaster` / `p:sldLayout`）、页面切换、逐元素入场动画、
演讲者备注转语音旁白。

## 2. 目录结构（照搬）

| 目录 | 内容 |
|---|---|
| `svg_output/` | AI 手写的原始 SVG（作者源文件，唯一可手工编辑的目录） |
| `svg_final/` | 由此派生的自包含 SVG，供预览用 |
| `exports/` | 最终交付物：原生可编辑 `.pptx`（带时间戳命名） |
| `backup/` | 原始 SVG 备份，可不调 AI 重新导出 |

## 3. 七步串行流程（照搬）

1. 来源处理：读 PDF / DOCX / PPTX / EPUB / HTML / LaTeX / Markdown / 纯文本 / URL
2. 项目初始化：建目录、定画布格式
3. 模板选择：用现成模板或新建品牌模板
4. 策略：八项确认（叙事、结构、风格、页数等）
5. 图片生成：按需生成配图
6. SVG 执行：一页一页串行画 SVG（串行保风格一致）
7. 后处理与 PPTX 导出：SVG→DrawingML，写出 `exports/`，加切换/入场动画与备注

## 4. 画布格式（照搬）

不只 16:9。PPT 16:9、PPT 4:3、小红书、微信朋友圈等 10 余种画布可直接在
提示词里指定。本 skill 默认 16:9（`10 × 5.625 英寸`），学术答辩可用 4:3。

## 5. 本 skill 的 MVP 落地（最小改动）

- 完整管线需按 PPT Master 仓库安装使用（Python 3.10–3.14 + AI 编辑器）；
  耗时预期：10–15 页约 10–20 分钟。
- MVP 用 `scripts/make_pptx.py`（python-pptx）做最小实现：封面/内容/结尾
  三页，原生文本框与形状、演讲者备注；复杂 deck 按同一母版另写脚本生成。
- 发光网格/流动管线这类复杂图：用 HTML 模板截图成 PNG 贴入，
  不要试图用 PPTX 形状模拟辉光和粒子（PPTX 原生对象做不到动画辉光）。
- SmartArt 是 PPT Master 有意不做的，不用；流程图用原生形状+连接线手排，
  或贴 HTML 截图。

## 6. 模板复现路线（照搬）

PPT Master 可以从参考文件反推品牌/风格/版式模板，也可以往现成 `.pptx`
里填新内容并保留原设计。tech-style 的用法：先用本 skill 的母版规格
（`assets/pptx-template.md`）定好一套深色科技母版，之后所有 deck 都复用它，
不要每份 deck 重新发明配色与版式。
