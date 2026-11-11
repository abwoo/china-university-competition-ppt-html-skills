# 出处与许可（Attribution）

本 skill 为用户**个人自用**，不对外分发、不商用。
以下 5 个高星仓库均为 MIT 或 Apache-2.0 许可，允许复制、修改、自用，
条件是保留原版权说明。本文件即履行该条件：每处借鉴都标注来源仓库、链接、原许可，
并说明搬了什么、改了什么。

> 融合情况已核实（2026-11-10 下载后核对原文）：
> Guizang PPT Skill（AGPL-3.0）与 Anthropic pptx skill（Apache-2.0，
> 见第 7 节许可核实说明）**都已融合进本 skill**，只搬规则、方法与参数，
> 不整段拷入模板 HTML/JS 与脚本代码。归藏来源的内容仅限用户个人本地使用，
> 不得对外分发、分享或商用；以后要分享 skill，须先把归藏来源的内容去掉
> 或重新取得许可。旧版"仍排除在外"的说法已被第 6、7 节的核实推翻，以本段为准。

## 1. fireworks-tech-graph

- 仓库：https://github.com/yizhiyanhua-ai/fireworks-tech-graph
- 许可：MIT License — Copyright (c) 2025 fireworks-tech-graph contributors
- 搬了什么（见 `references/fireworks-fusion.md`）：
  - 构图质量契约：零交叉、每条边最多 2 个拐点、全图最多 8 个拐点、
    节点间距 ≥40px、容器边距 ≥20px、标签避让节点/连线/标题；
  - 12 种视觉风格清单（含 Dark Terminal `#0f0f1a`、Blueprint `#0a1628`、Dark Luxury）；
  - 语义形状词表（LLM=双边框矩形、Agent=六边形、向量库=带环圆柱体）与
    语义箭头系统（颜色+虚线样式编码写/读/异步/循环）；
  - 14 种图型（含全部 UML）与 AI/Agent 领域模式；
  - 5.75 秒 settled-flow 动效时间线（先画线，后 2 秒数据流动）；
  - 验证回路：提示词 → 图契约 → 语义 IR → 路由规划 → SVG 构建 →
    结构验证 → PNG 回读检查 → 定向修订。
- 改了什么：只取了契约、词表、风格清单与时间线，改写成 tech-style 的
  检查清单与模板参数；未拷入其生成器代码（`scripts/fireworks.py` 等），
  也未拷入其 SVG 样张。配色按本 skill 的蓝紫+黄母版覆盖。

## 2. mg-styles-15（22-hud）

- 仓库：https://github.com/Vincentwei1021/mg-styles-15
- 许可：MIT License — Copyright (c) 2026 Vincentwei1021
- 搬了什么（见 `references/hud-recipes.md`）：
  - `prompts/22-hud.md` 的全部配方：深青黑底、青色 `#00E5FF` 线框 +
    橙/红 `#FF6A00` 告警、六边形网格、同心旋转环+刻度、雷达扫描
    （conic-gradient）+ 闪烁目标点、等宽小字数据流、打字机文字、
    Three.js 线框全息图、辉光+扫描线+轻微色差、目标锁定框（1.4→1.0 收缩）；
  - 关键技法：线框生长（stroke-dasharray/dashoffset）、数字滚动
    （随机数跳变 3–5 帧后落定）、锁定框快出缓入；
  - 工作法：先定一句话创意与节拍表、先出关键帧静帧验收、再做动效、
    声音与画面按节拍对齐、确定性渲染（时间 t 的纯函数、种子随机）。
- 改了什么：把 10 秒短片的配方改写成可复用的 HUD 模块清单与 CSS/SVG
  参数，接入本 skill 的蓝紫+黄配色（青色线框保留为可选模块）；
  Three.js 全息图改为可选（单文件模板默认不用，以保轻量）；
  未拷入其 demo 工程与音频素材。

## 3. PPT Master

- 仓库：https://github.com/hugohe3/ppt-master
- 许可：MIT License — Copyright (c) 2025-2026 Hugo He
- 搬了什么（见 `references/pptx-fusion.md`）：
  - SVG→DrawingML 管线：AI 手写 SVG（`svg_output/`）→ 自包含 SVG
    （`svg_final/`）→ 原生 PPTX（`exports/`），两者都用绝对坐标描述形状，
    矩形/路径/渐变/阴影几乎一对一映射；
  - 七步串行流程：来源处理 → 项目初始化 → 模板选择 → 策略（八项确认）→
    图片生成 → SVG 执行 → 后处理与 PPTX 导出；
  - 原生对象原则：形状、文本框、图表、表格均为原生 DrawingML 对象，
    可在 PowerPoint 里继续改；支持母版/版式继承（`p:sldMaster`/`p:sldLayout`）、
    页面切换与逐元素入场动画、演讲者备注转语音旁白；
  - 输入：PDF/DOCX/PPTX/EPUB/HTML/LaTeX/Markdown/纯文本/URL；
    多画布格式（16:9、4:3、小红书、朋友圈等）。
- 改了什么：只搬了方法与流程，未拷入其仓库代码；
  本 skill 的 MVP 用 `scripts/make_pptx.py`（python-pptx）做最小实现，
  完整 SVG→DrawingML 转换仍需按其仓库安装使用；
  耗时预期照搬：10–15 页约 10–20 分钟，串行生成保风格一致。

## 4. Frontend Slides

- 仓库：https://github.com/zarazhangrui/frontend-slides
- 许可：MIT License — Copyright (c) 2025 Zara Zhang
- 搬了什么（见 `references/html-presets.md`）：
  - 12 个安全预设：Bold Signal、Electric Studio、Creative Voltage、
    Dark Botanical、Notebook Tabs、Pastel Geometry、Split Pastel、
    Vintage Editorial、Neon Cyber、Terminal Green、Swiss Modern、Paper & Ink；
  - 三预览机制：默认出 3 个真实预览——1 个安全预设 + 至少 1 个 bold 模板 +
    1 个 wildcard（第二个 bold 模板或 agent 自设计），用真实第一页内容做预览，
    不许用占位诊断卡；NON-NEGOTIABLE 规则：预览必须像真实第一页，
    不许把模板名、文件名、需求笔记写进画面；
  - 心情映射：impressed→Bold Signal/Electric Studio/Dark Botanical；
    energized→Creative Voltage/Neon Cyber/Split Pastel；
    focused→Notebook Tabs/Paper & Ink/Swiss Modern；
    inspired→Dark Botanical/Vintage Editorial/Pastel Geometry；
  - 零依赖单文件 HTML（内联 CSS/JS）、PPTX→HTML 转换（`scripts/extract-pptx.py`）、
    固定 16:9、反 AI 味（禁通用紫渐变白底等陈词滥调）。
- 改了什么：预设名单与三预览机制原样搬入本 skill；
  本 skill 在此基础上加了一个专属预设 `tech-style`（蓝紫+黄母版），
  并把三预览改成"tech-style 主预设 + 1 个深色备选 + 1 个 wildcard"；
  未拷入其 bold-template-pack（34 个设计系统）全文，只保留选用方法。

## 5. HyperFrames

- 仓库：https://github.com/heygen-com/hyperframes
- 许可：Apache License 2.0 — Copyright HeyGen（以仓库 LICENSE 为准）
- 搬了什么（见 `references/video-fusion.md`）：
  - 口号与方法："Write HTML. Render video. Built for agents."；
    无构建步骤，`index.html + data-*` 时间属性即组合；
  - 确定性逐帧渲染：headless Chrome 逐帧截图 + FFmpeg 编码，
    同一输入同一输出；MP4（1920×1080@30fps）；
  - 安装：`npx hyperframes skills update`（核心 skill 集）或
    `claude plugin marketplace add heygen-com/hyperframes`；
    需 Node.js ≥22、FFmpeg、Chrome；Studio 桌面应用免费，Pro 版付费；
  - 9 个已发布 skill（以仓库为准），另有 slideshow / remotion-to-hyperframes / figma 按需安装。
- 改了什么：只搬了方法与命令，未拷入其 CLI 代码；
  本 skill 的 MVP 默认用浏览器录屏出视频，HyperFrames 作为"要精确逐帧出 MP4 时"的升级路线。

## 6. Guizang PPT Skill（归藏）

- 仓库：https://github.com/op7418/guizang-ppt-skill
- 许可：**GNU Affero General Public License v3.0（AGPL-3.0）**，
  本地副本：`~/workspace/tech-style-skill/reference-downloads/guizang-ppt-skill/LICENSE`，
  原文件未动。
- 许可要点（已读原文）：允许复制、修改、私人使用；对外分发或通过网络
  向公众提供修改版时，必须同样以 AGPL-3.0 开源并提供源码。
  因此本 skill 的这份融合版**仅限用户个人本地使用**，不得对外分发、分享或商用；
  以后要分享 skill，须先把归藏来源的内容去掉或重新取得许可。
- 搬了什么（见 `references/guizang-fusion.md`）：
  - 负向约束：只用一套主题不混搭、不用用户给的 hex 直接写页面、
    不直接改模板颜色、底色走命名纸色 token、模板是唯一类名来源、
    不从零写 slide（用登记布局骨架）、SVG 只画几何不写字、图片只裁底部、
    文字压图先做 quiet-zone 判断、内容放不下先删文案/拆页/换版式不压字号、
    溢出先量后改；
  - 杂志风 6 条与瑞士风 7 条核心原则（克制优于炫技、结构优于装饰、
    单一锚点色、主标题与正文比例 ≥8:1、直角纯色、12-col 网格、1px hairline 等）；
  - 主题系统：5 套预设（墨水经典/靛蓝瓷/森林墨/牛皮纸/沙丘），
    换主题只改 `<html>` 的 `data-theme` 一处；
  - WebGL 流体背景参数（只在 hero 页透出，dark hero 遮罩 12–15%、
    light hero 16–20%）与 `B` 键低功耗模式；
  - 工作流：7 问澄清 → 拷贝模板 → 填占位符 → 同步演讲备注
    （`data-slide-id` 稳定键）→ 对照清单自检 → 本地预览 → 迭代。
- 改了什么：只搬了规则与参数，改写成本 skill 的条目；未整段拷入其
  `template.html` / `template-swiss.html` 与 `motion.min.js`；
  WebGL 流体背景在 `assets/template.html` 里是可选模块（默认 CSS 网格+辉光），
  `B` 键静态模式已接入模板。

## 7. Anthropic skills 仓库中的 pptx skill

- 仓库：https://github.com/anthropics/skills（`skills/pptx/`）
- 许可：**Apache License 2.0**（以该 skill 自带的 `LICENSE.txt` 为准；
  SKILL.md 的 frontmatter 写明 "license: Complete terms in LICENSE.txt"）。
  本地副本：`~/workspace/tech-style-skill/reference-downloads/anthropics-skills/skills/pptx/`。
- 许可核实说明：此前报告曾写该 skill 为"source-available、禁复制/衍生/分发"，
  下载后核实是**错的**。实际读到的 `skills/pptx/LICENSE.txt` 是 Apache License 2.0 全文；
  仓库根目录没有 LICENSE 文件（GitHub license 端点返回 404）。
  因此按 Apache-2.0 处理：允许复制、修改、自用，保留版权说明即可。
  本 skill 只融合方法与做法，未整段拷入其 SKILL.md。
- 搬了什么（见 `references/anthropic-pptx-fusion.md`）：
  - 总路线：新建用 PptxGenJS、改现有 deck 用解压改 XML 再打包、
    读内容用 markitdown、视觉网格用 thumbnail.py；
  - 配套脚本清单：thumbnail.py、add_slide.py、clean.py、
    office/validate.py、office/soffice.py（本地副本里有，可直接用）；
  - PptxGenJS 避坑清单：先设 layout、颜色不要 `#` 与 8 位、不要共用 option 对象、
    阴影 offset ≥0、`charSpacing` 不是 `letterSpacing`、bullet/breakLine、
    一个文件一个 pptxgen 实例、渐变填充不支持、图表保持原生、
    堆叠图 dataLabelPosition、组合图双轴、writeFile 后跑 validate.py 等；
  - 模板编辑法：先做结构再改内容、不要手拷 slide、defusedxml 解析、
    模板槽位 ≠ 内容项、一个 `<a:p>` 一个列表项、标题加 `b="1"`；
  - 设计思路："三明治"结构（深色标题/结尾 + 浅色内容）、主色占 60–70%、
    一个视觉母题、每页必须有视觉元素、大数字 callout 60–72pt、
    标题 36–44pt / 章节头 20–24pt / 正文 14–16pt / 注释 10–12pt、
    页边距 0.5"、内容块间距 0.3–0.5"、安全字体表；
  - 避坑：标题下不加强调线、不加装饰色条、不用奶油/米色底、不重复版式、
    不交付溢出文字；
  - 强制视觉 QA：markitdown 内容 → validate.py 文件 → soffice 转 PDF →
    pdftoppm 逐页看图，逐页检查清单。
- 改了什么：只搬方法与清单，未拷入其 SKILL.md 全文与脚本代码；
  本 skill 的 MVP 仍用 python-pptx，需要 PptxGenJS/模板编辑时按本文件走。

## 严格借鉴清单（总表）

| 来源 | 搬了什么 | 放在 skill 的哪里 | 改动 |
|---|---|---|---|
| fireworks-tech-graph（MIT） | 构图契约、12 风格、语义词表/箭头、14 图型、5.75s 动效时间线、验证回路 | `references/fireworks-fusion.md`；SKILL.md 动画契约与原型 | 只取契约与清单，未拷生成器代码；配色覆盖为蓝紫+黄 |
| mg-styles-15 22-hud（MIT） | HUD 全套配方与关键技法、工作法 | `references/hud-recipes.md`；`assets/template.html` 的 HUD 模块 | 改写成模块清单+CSS/SVG 参数；Three.js 全息图改为可选 |
| PPT Master（MIT） | SVG→DrawingML 管线、七步流程、原生对象原则、母版/动画/备注转语音 | `references/pptx-fusion.md`；`assets/pptx-template.md`；`scripts/make_pptx.py` | 只搬方法，未拷仓库代码；MVP 用 python-pptx 最小实现 |
| Frontend Slides（MIT） | 12 预设、三预览机制、心情映射、零依赖单文件 | `references/html-presets.md`；SKILL.md 接单流程；模板预设切换 | 加专属 `tech-style` 预设；未拷 bold-template-pack 全文 |
| HyperFrames（Apache-2.0） | 确定性逐帧渲染、HTML+data-* 时间属性、安装命令 | `references/video-fusion.md`；`references/export-routes.md` | 只搬方法，未拷 CLI 代码；MVP 默认录屏 |
| Guizang PPT Skill（AGPL-3.0） | 负向约束、杂志/瑞士 13 条原则、5 套主题、WebGL 流体背景参数、B 键低功耗、工作流 | `references/guizang-fusion.md`；SKILL.md 负向约束；`assets/template.html` 的 B 键静态模式 | 只搬规则与参数，未拷模板 HTML/JS；WebGL 为可选模块；**仅限个人本地使用，不得分发** |
| Anthropic pptx skill（Apache-2.0） | PptxGenJS 避坑清单、模板编辑法、"三明治"结构、字号表、安全字体、强制视觉 QA、配套脚本清单 | `references/anthropic-pptx-fusion.md`；`assets/pptx-template.md`；`references/export-routes.md` | 只搬方法与清单，未拷 SKILL.md 全文与脚本代码；MVP 仍用 python-pptx |

## 8. v2 新增借鉴（HTML 模板动画升级，2026-11-10）

以下来源均为个人本地自用融合，星数为当日 GitHub API 实测（2026-11-10）：

| 来源 | 星数 / 许可 | 搬了什么 | 放在哪里 | 改动 |
|---|---|---|---|---|
| sueun-dev/motion-effects | 0★（2026-10-27 新建，API 实测 0）/ MIT | 325 个效果库的配方：#020 Sci-fi HUD（反向旋转环+刻度、雷达扫过点亮目标点、条形/波形面板）、粒子（073–083）、确定性时间 t 纯函数、5 秒无缝循环、无闪烁规则（颗粒用固定纹理、平滑运动） | `assets/template.html` 的雷达、粒子、彗星脉冲；`references/style-tokens.md` 第 11 节 | 只搬配方与规则，未拷效果代码文件；配色覆盖为蓝紫+黄 |
| charlie947/motion-graphics-skills | 625★ / MIT | 15 个 skill 的做法：animated-chart（数字滚动上去再落定、图表自我描绘）、milestone-reveal（星点汇聚成真实数字）、motion-effects（16 种高级效果 8 秒循环）、house 规则（事实先行、首 3 秒钩子、每镜头中部抽帧检查） | `assets/template.html` 的数字滚动、扩散环、详情翻转；`references/style-tokens.md` 第 11 节 | 改写成模板内的 CSS/JS，未拷其 skill 文本 |
| lovisdotio/motion2code | 348★ / MIT | 单条 GSAP 时间线是唯一时钟、`window.anim.seek(t)` 可寻址、循环首尾帧一致（frame(duration)=frame(0)） | `assets/template.html` 的单时钟时序（`body.paused` 冻结全部 CSS 动画） | 未引入 GSAP（模板保持零依赖），只搬了"单时钟+可寻址"思想，用原生 JS/CSS 实现 |
| 2boysfromtown/hyperframes-motion | 9★ / MIT | AE 风格 HTML+GSAP：3D 镜头推拉、动态排版、粒子与胶片质感、4 个 1080×1920 模板 | `assets/template.html` 的标题逐字升起、节点透视翻转 | 未拷其模板文件，未引入 GSAP/CDN |
| Vincentwei1021/video-shotcraft | 18,292★ / Apache-2.0 | 124 张镜头配方卡、节拍同步、逐帧检查、Motion Workbench 可视化编辑 | `assets/template.html` 的节拍化步骤时序与逐帧可查的日志 | 只搬方法，未拷其 Remotion 工程 |
| onstonboy/cursorflow（motion-graphics-promo） | 许可未标注（API 返回 None）/ 仅借方法 | 每帧至少 3 个独立运动、4 层景深、全部交错、静态停留 ≤8 帧、取景器角标、雷达网格、HUD 仪表盘 | `assets/template.html` 的 4 层背景、角标、雷达、HUD | **只借方法，未拷任何代码/文本**（许可未标注） |
| PHANTOMTONYT/motion-design-skills | 23★ / MIT | system-diagram-animation（架构图逐节点搭建、数据包沿边旅行）、data-story-charts（线条描绘、计数器跳动、轴线重缩放） | `assets/template.html` 的逐节点点亮、多光点沿连线、数字滚动 | 改写成模板内的 CSS/JS，未拷其 skill 文本 |
| iart-ai/motion-skills | 1,321★ / MIT | 50 个动效 skill 合集（动效字体、数据图表动画、解释视频、WebGL/Three.js、Manim、Remotion、GSAP 等） | 作为选型索引，未直接搬入模板 | 仅作候选清单，不作主底座 |

## 9. 反防御性写作（2026-11-10，用户要求"搜反防御性写作的说明或 skill 并 copy 进来"）

专门讲"反防御性写作"的 skill 真实存在，已按 MIT 许可抄入本 skill，
原文副本在 `~/workspace/tech-style-skill/reference-downloads/anti-defensive-writing/`（LICENSE 已存）：

| 来源 | 星数 / 许可 | 搬了什么 | 放在哪里 |
|---|---|---|---|
| Kiterlin/anti-defensive-writing — https://github.com/Kiterlin/anti-defensive-writing | 1815★ / MIT | 四大原则、五阶段重写管线、正向界定范围、精准校准不确定性、篇章结构解耦、中文技术写作与 SOP 节、对比矩阵与重构示例 | `references/anti-defensive-writing.md` 第 3、5.6、7 节 |
| Adkid-Zephyr/anti-defensive-writing-Skill — https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill | 5654★ / MIT | "论文是一场学术发布会，不是项目总结"的一句话原则；只围绕优势组织叙事；不说输；交稿前自查六问 | 同上文件第 2、5.7、6 节 |
| Devilyuu/anti-defensive-writing-zh — https://github.com/Devilyuu/anti-defensive-writing-zh | 1★ / MIT | 中文六步法、强信号清单、"不增事实、不丢不变"守则、"不是 X，而是 Y"翻案句处理、"这句删掉后读者少知道了什么"检验 | 同上文件第 4、6 节 |
| Boom5426/Nature-Paper-Skills 中的 anti-defensive-writing | 663★ / MIT | "Rule zero: do not add it"；除非删掉会让句子字面不成立，否则不加限定、免责与出处注 | 未单独下载，源自 Kiterlin（MIT），只取规则 |

另参考去 AI 味来源（只取词表与句式禁则）：taxueseek/plainspoken-writing、
say-it-human、ninehills/public-skills deslop-zh、Rexray117/De-AI-Writing-Skill。
Smoothsailing0/anti-defensive-writing-skill（19★，许可未标注）只作存在记录，未搬内容。
用户本人在 2026-11-03 至 11-04 对公众号草稿的逐句纠正（不要自我设限、事实出处只说一次、
禁"需要注意的是"等套话、禁定义式免责表述、禁冒号逻辑）与上述 skill 方向一致，
一并收录为本 skill 的用户定稿规则，见同上文件第 1、4 节。
**仅限用户个人本地使用，不对外分发。**

## 9. 直接抄升级（2026-11-10，评审/投资人喜欢的风格）

用户 2026-11-10 16:12 明确：能复制/直接 copy 的就下载下来直接抄，
只自己一个人用；HTML 与 PPT 风格一定要严格借鉴评审评委和投资人
喜欢的风格。以下来源均为公开可下载，星数为当日 GitHub API 实测，
本地副本在 `~/workspace/tech-style-skill/reference-downloads/liked-styles-2026-11-10/`，
各仓库 LICENSE 原文件未动。抄的是配色、字体、字号、版式、逻辑链，
**不抄别人的项目内容、数字、文字**。

| 来源 | 星数 / 许可 | 抄了什么 | 放在 skill 的哪里 |
|---|---|---|---|
| Akxan/ppt-agent-skill | 181★ / MIT | dark_tech 全套 token：底 #050b1f→#0a1f3d、80px 点阵、强调 #22D3EE/#3B82F6/#6366f1/#FDE047、Inter Tight 字距 -0.045em；26 风格的 signature_move/forbidden 做法 | `assets/template.html` 新增 dark-tech 预设；`references/style-tokens.md` §12.2A；`assets/pptx-template.md` 投资人版式 |
| Kuneosu/make-slide | 141★ / MIT | minimal-dark（底 #0a0a0a、强调 #3b82f6、标题 72/52/40px）、keynote-apple（黑底+渐变、标题 80px+ 900、字距 -2px）、neon-terminal（底 #0d1117、全等宽、扫描线/闪烁光标/`$` 提示符） | `references/style-tokens.md` §12.2B/C/D |
| zarazhangrui/beautiful-html-templates | 4,965★ / MIT | signal（深蓝 #1C2644+暖纸 #F0ECE3、单强调色古金 #C8A870、80px 网格、衬线标题+等宽标签）、8-bit-orbit（#0A0E27/#0F1B3D、霓虹青粉黄、像素堆叠阴影）、cobalt-grid（纸 #F0EBDE、墨蓝 #1F2BE0） | `references/style-tokens.md` §12.2E/F/G |
| ningzimu/codex-ppt-skill | 7,778★ / MIT | 12 套内置风格（科研答辩风、麦肯锡风格、数据仪表盘风等）；工作法：先出一样张再做全套、一套视觉系统走到底、每页按角色换版式；**未抄**其整页图片式 PPTX 做法，本 skill PPTX 仍坚持原生可编辑对象 | `references/style-tokens.md` §12.2H；`assets/pptx-template.md` 投资人版式 |
| tristan-mcinnis/pptx-from-layouts-skill | 42★ / MIT | 模板保真做法：从现有 .pptx 模板取版式再填内容（与 Anthropic 模板编辑法同源） | 仅作方法索引，未单独成节；做法已在 `references/anthropic-pptx-fusion.md` |
| Kiterlin/anti-defensive-writing | MIT（星数未单独核实，见下） | 反防御性写作规则：观点直接前置、正向界定范围、禁层叠对冲与自我削弱词 | `references/style-tokens.md` §12.4；完整规则见 `references/anti-defensive-writing.md`（并行任务已抄入，含中文版 Devilyuu） |
| Devilyuu/anti-defensive-writing-zh | MIT | 中文反防御性写作："发布会原则"、禁"遗憾的是/仅/效果有限" | 同上 |
| 华南理工大学公开模板 | 学校官网公开下载，无许可声明 | 3 页路演指导模板：封面结构 + 内容 8 部分 + "PPT 在前、商业计划书在后" | `references/style-tokens.md` §12.3；`assets/pptx-template.md` 投资人版式；原文件 `liked-styles-2026-11-10/scut-internet-plus-roadshow.ppt`（已转 PDF 核实 3 页、16:9） |
| Sequoia 模板 / Airbnb 2009 deck / DocSend / Guy Kawasaki | 公开资料，无代码许可问题 | Sequoia 10 页骨架；Airbnb 一页一观点；DocSend 观看时长数据；10/20/30 纪律 | `references/style-tokens.md` §12.1；`assets/pptx-template.md` 投资人版式 |
| SlidesCarnival 免费模板 | 免费下载，未直接下载文件 | Hexagonal Tech / Cyber-Futuristic AI / Techie Contour Lines 的风格参数（深底+亮色几何母题） | `references/style-tokens.md` §12.3 |

**未抄 / 未核实说明：**
- slidevjs/slidev（49,415★ MIT）与 hakimel/reveal.js（72,549★ MIT）只作
  选型参考，未下载整库（框架太重，单文件模板不需要）。
- officecli/officecli 经 API 核实只有 114★（MIT），与某聚合站声称的
  6,999★ 不符，未采用该数字，未下载。
- andyh102/deck-craft（API 实测 0★、许可 NOASSERTION）与
  xinhan2000/skillmill（0★、无许可）未抄。
- Kiterlin/anti-defensive-writing 的星数本轮未用 API 单独核实；
  并行任务记录为 1,815★，以其记录为准，本处不重复断言。
- SlidesCarnival 模板未直接下载 .pptx 文件（需经 Canva/Google
  Slides 流程），只抄了公开页面上的风格参数。
- 华工 .ppt 原文件无许可声明，仅作结构参考、不商用、不分发；
  与并行任务下载的 `copyable-templates/scut-internet-plus-template.ppt`
  为同一份公开文件（52KB），两处各存一份，未去重。
- 本地副本总计约 179MB（beautiful-html-templates 66M、
  codex-ppt-skill 86M 为大头）；与并行任务的
  `copyable-templates/`（185M，html-ppt-skill 等另一批仓库）无重复仓库，
  互补。

## 未搬的东西（排除清单）

- Guizang 与 Anthropic pptx 的模板 HTML/JS 与脚本代码未整段拷入；
  归藏来源的内容仅限个人本地使用，见上文第 6 节。
- 本 skill 不对外分发。含有 AGPL 来源内容是原因之一；
  若以后要分享 skill，须先把归藏来源的内容去掉或重新取得许可。
