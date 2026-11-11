# 视觉 Token（复制粘贴用）

本文件是 `tech-style` skill 的全部视觉配方。融合了 5 个高星 MIT/Apache-2.0
仓库与归藏、Anthropic pptx 的做法（见 `references/attribution.md`），
每处都标注来源；模板写法为本 skill 的改编版本。

## 1. 颜色 Token

```css
:root {
  --stage-bg: #06070a;        /* 舞台底色（近黑） */
  --stage-bg-2: #0A0A14;      /* 舞台底色 2（深蓝黑，用于渐变） */
  --panel-bg: rgba(123, 97, 255, 0.06);  /* 卡片底 */
  --panel-border: rgba(167, 139, 250, 0.35);
  --node: #7B61FF;            /* 节点主色 */
  --node-2: #8052FF;          /* 节点副色 */
  --glow: #A78BFA;            /* 辉光 */
  --flow: #22D3EE;            /* 流动连线 */
  --title-yellow: #FFB829;    /* 大标题黄 */
  --title-yellow-2: #FACC15; /* 大标题黄 2 */
  --text: #EDEFF7;            /* 正文 */
  --muted: #9AA3B2;           /* 次要文字 */
  --grid-line: rgba(123, 97, 255, 0.07); /* 网格线 */
}
```

PPTX 里用同一组色（去掉 alpha，网格线用极淡的 `#1A1B2E` 近似）。

## 2. 网格背景

```css
.stage {
  background:
    radial-gradient(1200px 600px at 50% -10%, rgba(123, 97, 255, 0.16), transparent 60%),
    linear-gradient(#06070a, #0A0A14);
}
.grid {
  background-image:
    linear-gradient(var(--grid-line) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid-line) 1px, transparent 1px);
  background-size: 40px 40px;
}
```

40px 是固定值。网格只做背景层，永远不要盖住文字。

## 3. 节点（卡片）

```css
.node {
  background: linear-gradient(180deg, rgba(123, 97, 255, 0.16), rgba(123, 97, 255, 0.05));
  border: 1px solid var(--panel-border);
  border-radius: 14px;
  box-shadow: 0 0 0 1px rgba(123, 97, 255, 0.08);
  padding: 18px 20px;
}
/* 发光核心：每页只允许一个 */
.node.kernel {
  border-color: var(--glow);
  box-shadow: 0 0 24px rgba(167, 139, 250, 0.45), 0 0 64px rgba(123, 97, 255, 0.18);
}
```

节点里放：序号（等宽字体）、动词标题（≤6 字）、一句话说明（≤20 字）、一个结果数字。

## 4. 连线与粒子

```css
/* SVG 连线：虚线流动 */
.connector {
  stroke: var(--flow);
  stroke-width: 2;
  stroke-dasharray: 6 6;
  animation: dashmove 0.8s linear infinite;
  filter: drop-shadow(0 0 6px rgba(34, 211, 238, 0.7));
}
@keyframes dashmove { to { stroke-dashoffset: -12; } }

/* 发光粒子：沿路径跑的光点，用 SVG <circle> + <animateMotion> */
.dot {
  fill: #A5F3FC;
  filter: drop-shadow(0 0 8px #22D3EE);
}
```

连线方向永远与流程方向一致（左→右、上→下），箭头不要刺进节点边框，留 4px 空隙。

## 5. 黄色大标题

```css
.hero-title {
  color: var(--title-yellow);
  font-size: clamp(40px, 6vw, 72px);
  font-weight: 800;
  letter-spacing: 0.02em;
  text-shadow: 0 0 32px rgba(255, 184, 41, 0.35);
}
.hero-sub { color: var(--text); font-size: 18px; }
.hero-kicker {
  color: var(--flow);
  font-family: ui-monospace, "JetBrains Mono", Menlo, Consolas, monospace;
  letter-spacing: 0.35em;
  font-size: 13px;
  text-transform: uppercase;
}
```

每页只允许一个黄色大标题（或一个黄色关键数字），其余标题用白色。

## 6. 字体（国内比赛调研结论，分 HTML 路线 / PPTX 路线）

来源：`references/domestic-competition-style.md`（每条结论带来源链接）；
Anthropic pptx 的字号表与安全字体见 `references/anthropic-pptx-fusion.md`。

### HTML 路线

```css
:root {
  --font-display: system-ui, -apple-system, "PingFang SC", "Source Han Sans SC", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif;
  --font-mono: ui-monospace, "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
}
```

标题粗体，正文常规；数据、标签、序号、HUD 文字用等宽字体。不引入外部字体文件。
HTML 里标题按 `clamp(40px, 6vw, 72px)`，正文 18px，注释 13px。

### PPTX 路线

| 位置 | 字体 | 字号 |
|---|---|---|
| 中文标题 | 思源黑体 Bold / 微软雅黑 Bold / 等线 Bold | 36–44pt |
| 章节头 | 思源黑体 Bold | 20–24pt |
| 中文正文 | 思源黑体 Regular / 微软雅黑 Regular / 等线 | 14–16pt（比赛 PPT ≥18pt） |
| 注释 | 思源黑体 Light | 10–12pt（不小于 14 号是创赛模板文档的要求，PPTX 注释取 10–12pt 时只用于页脚标注） |
| 英文/数字 | Arial / Inter / Montserrat；封面大数字可用 Arial Black | 数字 callout 60–72pt |

**版权**：思源黑体（Source Han Sans / Noto Sans CJK）免费商用（SIL OFL 1.1），
可嵌入 PDF/PPT；微软雅黑**不是免费商用**（版权归方正，仅限 Windows 系统内个人使用）；
系统自带字体（宋体、黑体、楷体、仿宋）为 Windows/macOS 默认免费商用。

**PPTX 字体回退方案**（评委电脑可能缺字体）：
1. 首选思源黑体：Mac 与 Windows 都原生支持，可消除跨平台回退；
2. 交付前在"文件 → 选项 → 保存 → 将字体嵌入文件"勾选，并选"嵌入所有字符"
   （macOS 版 PowerPoint 不支持字体嵌入，改出 PDF）；
3. 导出 PDF 备份随身带（字体自动嵌入），并把 PPTX 在答辩电脑上打开测试过；
4. 没把握时用微软雅黑/等线/黑体等 Windows 自带字体，绝不用特殊字体；
5. 字体不可靠的 QA 预览（LibreOffice 替代渲染）只看版式不看字宽，
   关键标题留约 10% 余量。

**深色底上的字重与行距**：正文字重至少 Medium，禁用 Light/Thin 超细体；
行距 1.3 左右；正文与背景对比度至少翻倍；亮度调到 50% 还能看清才算过关；
所有线条至少 2pt；深色底上字号要比平时大 15%–20%。

**深色底与投影仪**：投影仪 <2000 流明不推荐深色底，2000–3500 流明可用
（对比度 +20%、调暗房间），3500–5000 流明推荐，>5000 流明理想；
务必到现场实测，备一份"投影灾难版"（对比度更高、字号 +2pt、图片提亮 10%）。

### 合规克制版 vs 路演炫技版（字体/风格差异，不只颜色）

| 维度 | 路演炫技版 | 合规克制版（挑战杯/正式评审） |
|---|---|---|
| 底色 | 深色底全程 | 深色只在封面/章节/架构页，内容页浅色高对比 |
| 动效 | 流动、粒子、雷达、扫描线 | 只留入场级联；不用复杂动效、3D、特效字体 |
| 标题字 | 可用大字号 + 辉光 | 36–44pt Bold，无辉光、无特效字体 |
| 正文字 | 思源黑体 Regular | 思源黑体 Regular，≥18pt，行距 1.3 |
| 版式 | 可浓可炫 | 8 部分顺序与页数上限不可调，封面只有项目名+赛道+汇报人 |

### 归藏的补充（杂志/瑞士风）

- 杂志风：内容层级由字号和字体共同定义——最大衬线 = 主标题，中衬线 = 副标，
  大非衬线 = lead，小非衬线 = body，等宽 = 元数据。
- 瑞士风：无衬线只此一家（Inter / Helvetica / Noto Sans SC），任何衬线都是错的；
  主标题与正文比例 ≥ 8:1，KPI 必须是"Data Hero"（屏幕宽度的 18–22%）；
  直角纯色，不允许渐变 / 阴影 / 圆角（rule 横线除外）。
- 两种风格都要求：一份 deck 只用一套主题，不要中途换色、不要混搭。

## 7. HUD 可选模块（每页最多选 1 个）

以下模块全部是可选的，不要全用。完整配方与参数见 `references/hud-recipes.md`
（22-hud 搬运改编：六边形网格、雷达扫描、辉光、扫描线、打字机文字、目标锁定框）：

- **六边形网格**：背景加一层低透明度六边形描边，适合封面。
- **雷达扫描**：`conic-gradient` 旋转扇形 + 中心点，适合"监控/扫描"类页面。
- **扫描线**：一条横向亮线自上而下扫过，适合章节过渡页。
- **打字机文字**：等宽字体逐字出现，适合一句话亮点。
- **目标锁定框**：四个角的折线框 + 收缩动画，适合强调一个节点或数字。
- **数据流小字**：底部一行等宽小字滚动（如 `SYS.OK // 200 OK`），适合页脚装饰。

## 8. 入场动画（级联）

```css
.reveal { opacity: 0; transform: translateY(14px); animation: rise 0.6s ease forwards; }
@keyframes rise { to { opacity: 1; transform: translateY(0); } }
```

节点依次出现（每步间隔 0.35–0.6 秒），连线在源节点出现后再绘制。
持续动画至少一种：节点呼吸辉光（`box-shadow` 脉冲，2.4 秒一轮）或连线流动。

## 9. 合规克制版的替换规则

| 炫技版元素 | 合规版替换 |
|---|---|
| 流动虚线 + 粒子 | 静态实线 + 箭头 |
| 呼吸辉光 | 静态描边，无阴影动画 |
| 雷达 / 扫描线 / 故障 | 全部去掉 |
| 黄色大标题 | 保留，但只在封面/章节页用 |
| 网格背景 | 只在封面/章节/架构页保留，内容页用纯色底 |

## 11. 动画多变配方（v2 新增，细节感与多变性）

来源：`references/attribution.md` 第 8 节新增来源。核心原则照抄
cursorflow 的 motion-graphics-promo：**每帧至少 3 个独立运动、4 层景深、
全部交错（stagger）、静态停留不超过 8 帧**；motion-effects 的确定性规则：
画面只依赖时间 t 与固定种子，循环首尾帧一致，颗粒/闪烁用平滑正弦，
不用每帧随机跳变。

- **背景 4 层**：墙面网格（40px 缓移）+ 点阵网格（呼吸透明度）+
  底部透视网格（向远方滚动）+ canvas 粒子网络（闪烁节点 + 连线 + 彗星脉冲）。
- **连线多光点**：每条连线 3 个光点，大小/速度/延迟各不同
  （大 13px 金黄慢速、标准 10px 青色、中速、6px 紫色快速），带拖尾辉光。
- **节点激活**：扩散环向外扩 1.1 秒 + 角标淡入 + 数字滚动上去再落定
  （animated-chart 做法）+ 迷你进度条按该步占比填充。
- **每步一种微动画**（不要五步全一样）：scan 扫描光带、flip 透视翻转、
  draw 标题下划线描绘、grow 数字弹性生长、burst 金黄爆发闪光。
- **动态排版**：大标题逐字升起（每字延迟 0.06 秒，前两字带辉光脉冲）；
  详情面板每次切换做一次翻转；日志条目滑入；打字机状态行逐字打出当前步骤。
- **HUD 细节**：取景器角标（HUD 与面板四角）、雷达扫描（conic-gradient
  旋转 + 闪烁目标点）、闪烁数据点、LIVE 绿点呼吸。
- **动画强度档**（模板新增，独立于预设与合规开关）：炫技（全部开）、
  标准（关雷达/六边形、大光点关）、静态（只留网格与节点，关粒子/扫描线/
  透视网格）；暂停（`body.paused`）冻结全部 CSS 动画；B 键静态模式停止
  全部装饰动画，只留数据循环。合规克制版仍按第 9 节替换规则走。
- **性能与可读红线**：粒子总数 ≤70、彗星 ≤5；动画不得盖住步骤文字与数字；
  978px 与桌面宽均无横向溢出；移动端竖排时透视网格隐藏。

## 10. 反 AI 味检查（做完逐页打勾）

- [ ] 每页特效 ≤3 种
- [ ] 只有一个发光核心 / 一个黄色标题
- [ ] 内容页文字对比度够高，不会被辉光干扰阅读
- [ ] 没有无意义的装饰粒子盖住文字
- [ ] 标题、数字、结论都是真信息，不是装饰文案

## 12. 评审 / 投资人喜欢的风格（直接抄来的，2026-11-10）

> 个人本地自用，不对外分发。以下全部是公开可下载、可复制的来源，
> 原仓库与 LICENSE 保留在
> `~/workspace/tech-style-skill/reference-downloads/liked-styles-2026-11-10/`，
> 出处总表见 `references/attribution.md` 第 9 节。
> 原则：**抄结构、抄配色、抄字号、抄逻辑链，不抄别人的项目内容、
> 数字、文字**——换上自己的项目再用。个人分享帖与模板库的
> 补充抄法见第 13 节。

### 12.1 投资人到底看什么（有数据支撑的，不是感觉）

- **Sequoia 10 页骨架**（投资人视角的检查清单，顺序本身就是论证）：
  公司宗旨 → 问题 → 解决方案 → 为什么是现在 → 市场规模 →
  竞争 → 产品 → 商业模式 → 团队 → 财务。
  来源：Sequoia《Writing a Business Plan》公开模板；Airbnb 2009 年
  种子轮 deck（14 页，融约 60 万美元）就是按这条链走的，
  每页一个观点、每页一句话能讲清。
- **DocSend 数据**：投资人平均只看 **3 分 44 秒**（2023 年降至约
  2 分 24 秒）；财务页平均 23.2 秒、团队页 22.8 秒，是全 deck
  看得最久的两页；成功 deck 的"为什么是现在"页被多看 65%，
  竞争页多看 88%；只有 58% 的 deck 会被看到最后一页；
  12 页的 deck 平均获得最多浏览（34 次）与最高回访率（68%）。
  结论：**traction 要放前面**（放前 3 页的 deck 多 20% 浏览量），
  团队页和财务页要最下功夫，结尾页大概率没人看，不要把关键
  结论只放在结尾。
- **Guy Kawasaki 10/20/30**：10 页、20 分钟、字号不小于 30pt。
  每页字数（不含标题）目标 **25 字以内**；每页标题必须是
  **一句话陈述结论**，只读标题就能看懂整条逻辑链。
- **Airbnb 式克制**：问题页只列 3 个痛点，解决方案页一句话，
  市场页用 3 个数字收窄（20 亿次出行 → 5.6 亿在线预订 →
  1060 万可服务短租），商业模式页一句话（10% 佣金）。
  抄的是"一个数字只做一个判断"，不是抄它的文案。

### 12.2 直接抄来的配色与字体 token（按来源分）

**A. ppt-agent-skill `dark_tech`（MIT，181★）—— 最贴本 skill 的深色科技风**
```css
/* 背景：#050b1f → #0a1f3d；点阵网格 80px、透明度 0.015；青色光晕 20%/70% 处、模糊 60 */
--bg-primary: #050b1f; --bg-secondary: #0a1f3d;
--accent-1: #22D3EE; --accent-2: #3B82F6; --accent-3: #6366f1; --accent-4: #FDE047;
--card-bg-from: rgba(34,211,238,0.08); --card-bg-to: rgba(99,102,241,0.04);
/* 字体：标题 Inter Tight（字距 -0.045em）、正文 Inter、斜体点缀 Instrument Serif、等宽 JetBrains Mono；
   中文落地：标题思源黑体 Bold（字距收紧）、正文思源黑体、等宽 JetBrains Mono/Consolas */
```
本 skill 的 `assets/template.html` 已新增 `dark-tech` 预设，原样照抄上面这组值
（网格改成 80px 点阵、标题黄改成 #FDE047）。另有 26 套风格可选，
暗色 7 套里 `cyberpunk_neon`（#00ffff/#ff00c8，全 mono）、
`nocturne_violet`（#9b64ff/#c4a8ff）可作备选预设；每套都有
`signature_move`（招牌动作）与 `forbidden`（明确禁用）清单，
抄风格时连禁用清单一起抄，不要只抄颜色。

**B. make-slide `minimal-dark`（MIT，141★）—— 投资人路演最稳的深色底**
```css
/* 底 #0a0a0a，卡片 #1a1a1a，描边 #2a2a2a，正文 #f0f0f0，次要 #888888，强调 #3b82f6（悬停 #60a5fa） */
```
标题 72/52/40px（800/800/700），正文 22px，等宽 JetBrains Mono 15px。
适用：技术路演、创业 pitch、深色会场。抄的要点是"最小装饰、最大清晰"：
深色底去噪音，内容居中，标题一句话。

**C. make-slide `keynote-apple`（MIT，同上）—— 产品发布式路演**
底 #000000 与渐变 #1a1a2e → #16213e → #0f3460 交替，强调 #007AFF；
标题 80px+（900，字距 -2px）、56px+（900，字距 -1px）、44px（800）；
overline 14px、字距 6px。抄的要点是"黑白交替出节奏，每页像一次产品揭晓"，
适合封面、章节、结尾三类页，不适合塞满字的技术页。

**D. make-slide `neon-terminal`（MIT，同上）—— 黑客松 demo 页**
底 #0d1117，卡片 #161b22，描边 #30363d；正文绿 #00ff41、次要 #4ade80、
强调青 #00d4ff；**全部等宽字体**（JetBrains Mono），配扫描线、
闪烁光标、`$`/`>` 提示符、终端窗口三点 chrome。抄的要点只限
黑客松 demo 与终端类产品页，正式评审不要用。

**E. beautiful-html-templates `signal`（MIT，4,965★）—— 评委喜欢的"克制高级感"**
深蓝 #1C2644 + 暖纸 #F0ECE3 双面，**只用一个强调色**：古金 #C8A870
（只用在短横线、斜体强调、数字上）；80px 网格纹理；标题用衬线
Source Serif 4（中文落地：Noto Serif SC）、正文 DM Sans
（中文：Noto Sans SC）、标签 IBM Plex Mono（字距 0.14em，大写）。
抄的要点：深色页与浅色页成对出现、一个强调色走到底、标题衬线+斜体混排。
这是本 skill"三明治"结构的升级版备选。

**F. beautiful-html-templates `8-bit-orbit`（MIT，同上）—— 游戏/黑客松 pitch**
深空 #0A0E27、深蓝 #0F1B3D，霓虹青 #5EDCF4、粉 #F0A6CA、黄 #F4D03F，
像素堆叠阴影（4px/8px 阶梯）。只适合游戏、Web3、黑客松 pitch，
正式评审与投资路演不要用。

**G. beautiful-html-templates `cobalt-grid`（MIT，同上）—— 浅色科技备选**
纸 #F0EBDE、墨蓝 #1F2BE0、网格 rgba(31,43,224,0.10)；标题 Newsreader
衬线大字（clamp 100–200px，行高 0.92）。适合"内容页浅色高对比"的
合规克制版里做章节页。

**H. codex-ppt-skill（MIT，7,778★）—— 风格工作法，不是配色**
12 套内置风格（清爽专业、创意杂志、电子墨水杂志、数据仪表盘、
复古扁平插画、手绘技术解释、手绘白板、温暖手工、**科研答辩风、
麦肯锡风格**、党政红、教学课件）。抄两条工作法：
（1）**先出一样张、用户点头后再做全套**（与本 skill"先出 3 个真实预览"同源，
只做一样张更省）；
（2）一套视觉系统走到底、每页按内容角色换版式，**不要每页长得一样**；
（3）它的 deck 是整页图片式 PPTX——本 skill 不抄这条，
PPTX 路线仍坚持原生可编辑对象。

### 12.3 评审/投资人喜欢的版式（华工官方模板 + SlidesCarnival 免费模板）

- **华南理工大学公开模板**（`scut-internet-plus-roadshow.ppt`，
  学校官网公开下载，3 页，2022 年 WPS 制作）：封面白底居中大标题
  （项目名）+ 右上学校 logo + 下方"项目组别、负责人等信息"；
  正文页只讲一件事：**路演 PPT 是浓缩版商业计划书，是专家评审
  的首要和重要文件**；内容 8 部分：市场调研与痛点、技术优势与壁垒、
  应用案例、团队/组织架构、技术与商业支持、商业营销与财务分析
  （含财务预测）、风险控制与投融资需求、社会效益。
  抄的是结构与"PPT 在前、商业计划书在后"的提交顺序，
  它的视觉本身是白底素版，不抄配色。
- **SlidesCarnival 免费深色科技模板**（免费下载 PPTX/Google Slides，
  未直接下载文件，只抄了风格参数）：`Hexagonal Tech`（深底+亮蓝六边形、
  Montserrat 字体）、`Cyber-Futuristic AI`（蓝黑、Archivo Black、25+ 页）、
  `Techie Contour Lines`（深绿等高线背景、Quantico/Titillium 字体）。
  抄的要点：深底模板要配一个亮色几何母题（六边形/等高线/网格），
  不能只有纯色底。

### 12.4 文字段位：反防御性写作（投资人最反感的写法）

完整规则见 `references/anti-defensive-writing.md`（已抄入本 skill，
来源 Kiterlin/anti-defensive-writing，MIT；中文版 Devilyuu，
MIT）。路演与投资 deck 只记这几条：

- 观点直接前置：每段、每页第一句就是判断，不以局限、退让从句开头。
- 禁止层叠对冲：不写"可能在一定程度上或许"、"maybe potentially suggest"；
  真有不确定就写清来源（"该结论只在已观测的条件下成立"），只出现一次。
- 正向界定范围：写"本研究分析了 X"，不写"我们并不声称 X"、
  "这不是说 X，而是 Y"、"需要注意的是/值得注意的是/总的来说"。
- 禁用自我削弱词："遗憾的是""仅""效果有限""存在严重不足""我们相信/
  我们认为/我们的目标是"——删掉，改写成事实陈述。
- 每页标题必须是**一句话结论**，不写"市场分析""团队介绍"这种
  无判断的栏目名；改写成"市场每年 20 亿次出行，付费意愿已验证"
  这类带数字的判断句（数字必须是真的，有来源占位）。
- 真实的不确定性、反例、证据边界要保留，不编造；只是不让它们
  抢占标题和段首。


## 13. 评审/投资人喜欢的风格（补充：个人分享与模板库直接抄）

> 本节由并行补充任务写入，与第 12 节互补（第 12 节是 GitHub 高星
> skill 与投资人数据，第 13 节是个人分享帖与可下载模板库）。
> 来源：`references/excellent-works.md` 第六节（28 条新条目，L1–L28），
> 以及已下载到本地的开源库
> `~/workspace/tech-style-skill/reference-downloads/copyable-templates/`：
> html-ppt-skill（MIT，9,039★）、competition-ppt-skill（MIT）、
> slide-skill（MIT）、glassmorphism-ppt-skill（MIT）、
> lanshu-html-ppt-templates（新增代码 MIT，原始模板许可未明）、
> editable-ppt-materials（许可 NOASSERTION，未明确）。
> **仅限用户个人本地使用，不对外分发。** 只抄风格和版式，
> 不抄别人的项目内容、数据、文字当成自己的项目内容。

### 13.1 投资人版 10 页骨架（抄 L1、L8、L25）

定位→问题→解决方案→为什么是现在→市场→用户增长数据→商业模式→
竞争→团队→融资需求。10–12 页硬上限，超过 12 页丢注意力；
投资人平均扫 deck 不到 4 分钟，前 5 页决定 80% 印象。

### 13.2 可直接抄的配色（带出处，只抄色值与版式）

```css
/* 路演安全版：白底黑字（L8、L25）——投资人最不会错的选择 */
:root {
  --pitch-bg: #FFFFFF;
  --pitch-text: #111111;
  --pitch-accent: #2563EB; /* 单个高饱和主色，深蓝 */
}
/* Wonderslide Clean Tech（L20）：冷调浅灰底 + 深炭灰字 + 亮青点缀 */
:root {
  --cleantech-bg: #F5F6F8;
  --cleantech-text: #1F242B;
  --cleantech-card: #E3E8EF;
  --cleantech-accent: #00C2FF; /* 只点到为止：编号、流程步骤、照片光线 */
  --cleantech-accent-2: #A6F1FF;
}
/* Wonderslide Nocturne（L20）：沉静午夜藏青，适合文字多的投资人进展汇报 */
:root {
  --nocturne-bg: #0B1220; /* 午夜藏青近似值，按原模板取深蓝黑 */
  --nocturne-card: rgba(255, 255, 255, 0.04);
  --nocturne-highlight: #7B61FF; /* 冷调蓝紫高光，与本 skill 节点色同系 */
}
/* Codia 深色电路（L27）：深海军蓝 + 发光青色电路 + 玻璃质感 */
/* html-ppt-skill tech-sharing（L14）：深色 GitHub 风 #0d1117 + JetBrains Mono */
/* competition-ppt-skill（L13）：封面深蓝渐变 + 金色光晕 */
```

### 13.3 可直接抄的版式规则（带出处）

- **标题即结论**：每页标题必须是完整结论句，禁止"市场分析""团队介绍"
  这类名词标题（G3）；Airbnb 式：每页标题不超过 3 个字 + 一张图，
  4 秒可吸收（L1）。
- **数据页固定写法**：左上角一句话"这一页想证明什么"，右下角
  "所以这意味着什么"；图表用品牌色、重点数字放大、坐标轴灰色（L9）。
- **竞争页**：只列 3 个真正重要的维度，并承认对手在某些地方做得不错
  （L8）；不要 12 维全勾表。
- **每页右下角浅灰小页码 + 左上角 Section 标签**（G3、L13）；
  结尾不要"谢谢"/"Q&A"，写融多少钱、干什么、联系方式/二维码（L8）。
- **每页不超过 20 个词/30 个字**（L25、L1）；一页一个观点；
  截图必须配一句话说明，不要让投资人自己猜（L8）。
- **动效克制度**：简单动画可以用（数据逐条展示、图片渐入），
  不要用花哨的页面切换效果（L25）；整场动画类型不宜超过 3 种（L24）。
- **中国比赛评审版**：先看评分表再排页数——个人成长 30 分、项目创新
  30 分、产业价值 25 分、团队协作 15 分（L13）；融资稿与评分表不能混用（G2）。
