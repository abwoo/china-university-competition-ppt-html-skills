# Anthropic pptx 融合：PptxGenJS 路线与强制视觉 QA

来源：anthropics/skills 仓库中的 `skills/pptx`，
https://github.com/anthropics/skills
本地副本：`~/workspace/tech-style-skill/reference-downloads/anthropics-skills/skills/pptx/`。
许可：**Apache License 2.0**（以该 skill 自带的 `LICENSE.txt` 为准；
SKILL.md 的 frontmatter 写明 "license: Complete terms in LICENSE.txt"）。
完整出处与许可见 `references/attribution.md`。

> 许可核实说明：此前报告曾写该 skill 为"source-available、禁复制/衍生/分发"，
> 下载后核实是错的。实际读到的 `skills/pptx/LICENSE.txt` 是 Apache License 2.0 全文，
> 仓库根目录没有 LICENSE 文件（GitHub license 端点返回 404）。
> 因此按 Apache-2.0 处理：允许复制、修改、自用，保留版权说明即可。
> 本 skill 只融合方法与做法，未整段拷入其 SKILL.md。

## 1. 总路线（照搬）

`.pptx` 本质是 ZIP 包里的 XML 文件，按任务选做法：

| 任务 | 做法 |
|---|---|
| 新建 deck | 写 PptxGenJS 脚本 |
| 改现有 deck / 从模板建 | 解压 → 改 `ppt/slides/slideN.xml` → 重新打包 |
| 读内容 | `markitdown deck.pptx`（每页一个块，`<!-- Slide number: N -->` 标记）；视觉网格：`python scripts/thumbnail.py deck.pptx` |

## 2. 配套脚本（照搬，本地副本里有）

| 脚本 | 作用 |
|---|---|
| `scripts/thumbnail.py deck.pptx [prefix]` | 输出每页的标注网格图，供挑选模板版式；prefix 务必传 deck 名，否则默认 `thumbnails` 会覆盖同目录下其他 deck 的网格 |
| `scripts/add_slide.py unpacked/ slide2.xml [--after slideN.xml]` | 复制一页（含全部包内登记）；也可直接对 `.pptx` 用 `-o out.pptx`（不传 `-o` 会原地改写输入文件） |
| `scripts/clean.py unpacked/` | 删掉 `<p:sldIdLst>` 定稿后不再引用的 slide、媒体、rels |
| `scripts/office/validate.py deck.pptx [--original src.pptx]` | 模式、关系、内容类型、图表与 slide 检查，每个失败都写明修复方法；模板派生的 deck 一定传 `--original`，以模板为基线，模板自带的 XSD 错误不算你的 |
| `scripts/office/soffice.py --headless --convert-to pdf deck.pptx` | LibreOffice 包装（裸 `soffice` 在沙箱里会挂起） |

## 3. PptxGenJS 避坑清单（照搬）

- 先设 `pres.layout` 再加 slide；默认画布 `LAYOUT_16x9` = 10" × 5.625"，
  不是 13.3" 宽；超出边界的坐标会被写进去、不被截断，形状直接不在页上。
- 十六进制颜色不要 `#`、不要 8 位：`color: "FF0000"`；
  `"#FF0000"` 与 8 位 alpha（`"00000020"`）都会**损坏文件**；
  半透明用 fills/images 的 `transparency: 0-100`，shadows 用 `opacity: 0.0-1.0`，
  两者不可互换（用错会被静默忽略）。
- pptxgenjs 会原地改写 option 对象（首次使用时把值转成 EMU）：
  不要在两次 `add*` 之间共用同一个 shadow/options 对象，每次新建。
- 阴影 `offset` 必须 ≥ 0（负值损坏文件）；要向上投阴影用 `angle: 270` + 正 offset。
- `letterSpacing` 会被静默忽略，正确选项是 `charSpacing`。
- 列表：每项设 `bullet: true`，不要写字面 `•`（会双重项目符号）；
  除最后一项外每项设 `breakLine: true`；项目符号间距用 `paraSpaceAfter`，
  不要用 `lineSpacing`（间距会巨大）。
- 一个输出文件只用一个 `new pptxgen()`，不要复用实例。
- `rectRadius` 只对 `ROUNDED_RECTANGLE` 有效，对 `RECTANGLE` 无效。
- 渐变填充不支持——用渐变图片做背景代替。
- 文本框自带内边距：文字必须与形状/线/图标在同一 x 对齐时设 `margin: 0`。
- 演讲者备注用 `slide.addNotes("...")`（纯文本，每页一次），不要写进页上的文本框。
- 图表保持原生：`addChart()`；PowerPoint 没有原生形态的图型
  （Sankey、network、chord）才贴图片；趋势线、误差线等库未暴露的功能
  自己算额外 series 或后处理 OOXML，不要退回渲染图。
- 默认图表很素：设 `showTitle` + `title`、`showValue: true` + `dataLabelPosition`、
  `chartColors: [...]` 用你的配色、安静化坐标轴
  （`catAxisLabelColor`/`valAxisLabelColor`、`valGridLine`、单 series 时
  `showLegend: false`）。
- 堆叠条形/柱形图的 `dataLabelPosition` 必须是 `ctr`、`inEnd` 或 `inBase`，
  `outEnd` 会**损坏文件**。
- 用 `secondaryValAxis`/`secondaryCatAxis` 的组合图必须同时给 `valAxes` 与
  `catAxes`（各两条）；只给 `valAxes` 时 pptxgenjs 会写出未声明的 axis id，
  PowerPoint 会丢弃该图表并报文件损坏。
- `writeFile()` 之后跑 `python scripts/office/validate.py deck.pptx`；
  在生成器里修问题，不要手改打包后的 XML。
- 不要重排 `<p:presentation>` 的子元素顺序（pptxgenjs 把
  `<p:notesMasterIdLst>` 写在 `<p:sldIdLst>` 紧后并共用 theme；
  移动它会让同一份 deck 打不开）。
- 图标：`react-icons` 渲染成 SVG（`ReactDOMServer.renderToStaticMarkup`），
  用 `sharp` 以 ≥256px 光栅化，再用
  `addImage({ data: "image/png;base64," + buf.toString("base64") })`
  插入——`image/png;base64,` 前缀是必需的。

## 4. 改现有 deck / 模板（照搬）

```bash
python3 -c "import sys,zipfile; zipfile.ZipFile(sys.argv[1]).extractall('unpacked')" deck.pptx
python scripts/add_slide.py unpacked/ slide2.xml --after slide2.xml
# 增删改顺序 = 改 ppt/presentation.xml 里的 <p:sldIdLst>
python scripts/clean.py unpacked/
# 改 ppt/slides/slideN.xml 里的内容
(cd unpacked && rm -f ../out.pptx && zip -Xr ../out.pptx .)
python scripts/office/validate.py out.pptx --original deck.pptx
```

- 先做结构工作（增、删、重排），再改每页内容：`add_slide.py` 是逐字复制，
  改完再复制会克隆已改内容；`clean.py` 会删掉不在 `<p:sldIdLst>` 里的页。
- 不要手拷 slide 文件——`add_slide.py` 做全部登记并报告做了什么。
- 复制的 slide 仍引用源 slide 的图表/SmartArt/嵌入对象，改一页的图表会改另一页。
- 用 `python-pptx` 时注意它做不到的三件事：复制 slide（只能 `add_slide(layout)`）、
  `text_frame.text = "..."` 会丢格式（改 `run.text`）、读模板常用的 SVG/EMF
  （`add_picture` 会报 `UnidentifiedImageError`）。
- 旧 `.ppt` 先转：`python scripts/office/soffice.py --headless --convert-to pptx file.ppt`；
  `.potx` 模板解压打包方式相同，输出保持 `.potx` 后缀。
- 填模板时：模板槽位 ≠ 你的内容项——模板有 4 个团队成员、你只有 3 个时，
  删掉第 4 人的整个组（图片 + 文本框），不只删文字；QA 时检查残留视觉元素。
- 一个 `<a:p>` 放一个列表项，不要把多项拼进一段；复制相邻的 `<a:pPr>` 保间距；
  标题、章节头、行内标签（`Status:`、`Owner:`）的 `<a:rPr>` 加 `b="1"`。
- XML 转换脚本用 `defusedxml.minidom` 解析——用 `xml.etree.ElementTree`
  回写会重写命名空间前缀、损坏 deck。
- 首尾有空格的文本要在 `<a:t>` 上加 `xml:space="preserve"`。

## 5. 设计思路（照搬）

- **不要做无聊的 slide**：白底 + 纯项目符号打动不了任何人，每页都要想视觉元素。
- 配色要为**这个主题**定制：主色占 60–70% 视觉权重，1–2 个支撑色 + 1 个锐利 accent；
  不要所有颜色平分权重；不要默认用蓝色。
- **"三明治"结构**：深色底做标题页 + 结尾页，浅色底做内容页；
  或者全程深色走高级感（二选一，定下来就贯彻到底）。
- 一个视觉母题重复全 deck（圆角图片框、彩色圆圈里的图标等）；
  **不要用色条/强调线做母题**。
- 每页必须有视觉元素（图片、图表、图标或形状），纯文字页会被忘掉。
- 版式：两栏（左文右图）、图标 + 文字行、2×2/2×3 网格、半出血大图。
- 数据展示：大数字 callout（60–72pt 大数字 + 下方小标签）、对比栏、
  时间线/流程（编号步骤 + 箭头）。
- 字号：标题 36–44pt bold、章节头 20–24pt bold、正文 14–16pt、注释 10–12pt muted。
- 间距：页边距最小 0.5"、内容块之间 0.3–0.5"、留呼吸空间。
- 字体（QA 可靠性）：正文用 QA 能真实渲染的字体——Arial、Calibri、Cambria、
  Times New Roman、Courier New、Bookman Old Style、Century Schoolbook；
  标题可配安全列表里的衬线（Cambria、Bookman Old Style、Century Schoolbook）+
  安全列表里的无衬线正文；不要默认用 Aptos（新版 Office 默认字体，
  旧版 Office 没有，且无等宽替代）；Georgia、Trebuchet MS、Impact、
  Arial Black、Garamond、Consolas、Palatino Linotype 的 QA 预览宽度不可靠，
  只用在标题/强调处并留约 10% 余量。

### 避坑清单（照搬）
- 不要重复同一个版式；不要居中正文（只居中标题）；
  标题与正文要有尺寸对比（标题 36pt+ 对正文 14–16pt）；
  不要随机混用间距（选 0.3" 或 0.5"，全 deck 一致）；
  不要只精修一页、其余页留白；不要纯文字页；
  不要忘文本框内边距（对齐时设 `margin: 0` 或给形状留偏移）；
  图标与文字都要与背景高对比。
- **绝不要在标题下加强调线**——这是 AI 生成 slide 的标志；用留白或背景色代替。
- **绝不要加装饰性色条/强调条**——包括通栏页眉/页脚条、一侧竖条、
  卡片边缘细条、矩形的"单边边框"；要区分卡片用浅底色、阴影或图标，不要用边缘条。
- 不要默认用奶油/米色底（`F5F5DC`、`FAF0E6`、`FAEBD7`、`FFF8E1`）；
  没指定背景时用白色 `FFFFFF` 或用户品牌色。
- 不要交付溢出形状的文字——放不下就减字号、分两页或放大容器。

## 6. 强制视觉 QA（照搬）

```bash
markitdown output.pptx                                   # 内容 QA：缺内容、错别字、顺序
markitdown output.pptx | grep -iE "\bx{3,}\b|lorem|ipsum|\bTODO|\[insert|this.*(page|slide).*layout"  # 模板残留占位
python scripts/office/validate.py output.pptx [--original src.pptx]  # 文件 QA
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
rm -f slide-*.jpg && pdftoppm -jpeg -r 150 output.pdf slide   # 视觉 QA
```

逐页看图检查（重点在前）：文字溢出/被截断 → 重叠 → 引用/页脚与内容碰撞 →
元素间距 <0.3" 或卡片几乎相贴 → 间距不均 → 页边距 <0.5" → 列未对齐 →
低对比文字 → 模板装饰错位 → 低对比图标 → 文本框过窄导致反复换行 → 残留占位内容。
修完只重渲染改过的页；改完重新跑上面四条命令（PDF 必须从改过的 .pptx 重新生成）。

## 7. 在 tech-style 里怎么用

- 本 skill 的 PPTX 路线默认用 `scripts/make_pptx.py`（python-pptx）做 MVP；
  需要 PptxGenJS 的原生图表/逐元素入场动画/模板编辑时，按本文件第 2–4 节走，
  脚本在本地副本 `reference-downloads/anthropics-skills/skills/pptx/scripts/`。
- 标题 36–44pt、正文 14–16pt 的字号表与"三明治"结构并入
  `assets/pptx-template.md` 与 `references/style-tokens.md`。
- 避坑清单（标题下不加线、不用装饰色条、不用奶油底、不重复版式）
  并入 SKILL.md 的负向约束。
- 强制视觉 QA（markitdown 内容 → validate.py 文件 → soffice 转 PDF →
  pdftoppm 逐页看图）并入 `references/export-routes.md` 的 QA 清单；
  本地无 LibreOffice 时先用 python-pptx 读回 + 浏览器看 HTML 预览代替，
  并在报告里如实说明。
