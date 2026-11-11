# 导出路线与视觉 QA

## 1. HTML 路线（主产物）

起点：`assets/template.html`。改标题、节点文字、配色 token 即可，不要从零手写。

```bash
# 在浏览器里打开预览（任选其一）
open assets/template.html        # macOS
xdg-open assets/template.html    # Linux
# 或用本地静态服务
python3 -m http.server 8000
```

### HTML → 视频 / GIF / PNG

- **录屏（最简单，MVP 推荐）**：浏览器全屏打开模板，点播放，用系统录屏
  （macOS Cmd+Shift+5 / Windows Win+Alt+R）录一轮，剪映加字幕、配音、音效。
- **HyperFrames（HTML → MP4，确定性逐帧渲染）**：上游为 HeyGen 开源框架
  （https://github.com/heygen-com/hyperframes，Apache-2.0），需 Node.js 22+、
  FFmpeg、Chrome。本 skill 不内置它；需要时按其官方文档安装使用。
- **Remotion（备选）**：同样是代码渲染视频，链路较重；只在需要精确时间线时用。
- **GIF**：用 Playwright 逐帧截取 HTML 动画后合成；或录屏后转 GIF。
  注意循环要无缝：每个 CSS 动画周期都应整除总时长。
- **PNG**：浏览器截图，或 Playwright 单帧截图；用于贴进 PPTX。

## 2. PPTX 路线

规格见 `assets/pptx-template.md`。生成工具：

```bash
# 先建 venv 并安装 python-pptx（只需一次）
python3 -m venv /tmp/techstyle-venv
/tmp/techstyle-venv/bin/pip install python-pptx

# 生成最小 3 页 deck（测试用）
/tmp/techstyle-venv/bin/python scripts/make_pptx.py --title "示例项目" --out /tmp/test-deck.pptx

# 用 LibreOffice 转 PDF 检查（如果已安装）
soffice --headless --convert-to pdf /tmp/test-deck.pptx --outdir /tmp
```

规则：

- 16:9，`10 × 5.625 英寸`；标题 36–44pt，正文 ≥18pt。
- 文字、形状、图表尽量用原生对象（可编辑）。
- 发光网格 / 流动管线这类复杂图：用 HTML 模板截图成 PNG 贴入，
  不要试图用 PPTX 形状模拟辉光和粒子。
- 讲稿放进每页的演讲者备注（speaker notes）。

## 3. 视觉 QA 清单（交付前逐项打勾）

### 强制 QA 流程（Anthropic pptx，照搬）

```bash
markitdown output.pptx                                   # 内容 QA：缺内容、错别字、顺序
markitdown output.pptx | grep -iE "\bx{3,}\b|lorem|ipsum|\bTODO|\[insert|this.*(page|slide).*layout"  # 模板残留占位
python scripts/office/validate.py output.pptx [--original src.pptx]  # 文件 QA（模板派生的 deck 一定传 --original）
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
rm -f slide-*.jpg && pdftoppm -jpeg -r 150 output.pdf slide   # 视觉 QA：逐页看图
```

逐页看图检查（重点在前）：文字溢出/被截断 → 重叠 → 引用/页脚与内容碰撞 →
元素间距 <0.3" 或卡片几乎相贴 → 间距不均 → 页边距 <0.5" → 列未对齐 →
低对比文字 → 模板装饰错位 → 低对比图标 → 文本框过窄导致反复换行 → 残留占位内容。
修完只重渲染改过的页；改完重新跑上面四条命令（PDF 必须从改过的 .pptx 重新生成）。
配套脚本在本地副本 `~/workspace/tech-style-skill/reference-downloads/anthropics-skills/skills/pptx/scripts/`。
本地无 LibreOffice 时先用 python-pptx 读回 + 浏览器看 HTML 预览代替，
并在报告里如实说明。

- [ ] HTML：在桌面 Chrome/Edge 打开，播放、暂停、0.5×/1×/2×、合规开关都点过
- [ ] HTML：手机宽度下无横向溢出，流水线自动变竖排
- [ ] HTML：动画一轮完整跑完，节点依次出现、连线后绘制、粒子方向正确
- [ ] PPTX：在 PowerPoint/WPS 打开，文字可选中、可编辑，不是整页图片
- [ ] PPTX：转 PDF/图片逐页检查，无文字溢出、无遮挡、无乱码
- [ ] 页数在上限内（路演 ≤20、挑战杯 ≤20、国赛长版 30–45）
- [ ] 每页一个观点；数字都有来源占位，没有编造的营收/融资/专利数
- [ ] 合规克制版：已去掉复杂动效/3D/特效字体（挑战杯必查）
- [ ] 标题、数字、结论是真信息，不是装饰文案
- [ ] 文件命名：`项目名-路线-模式-日期`，如 `XX项目-路演-炫技版-20261110.pptx`
