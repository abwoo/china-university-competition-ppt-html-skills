# 视频融合：HyperFrames 确定性逐帧渲染

来源：heygen-com/hyperframes（Apache License 2.0）。
本文件搬运其 HTML→MP4 确定性逐帧渲染方法，改写成本 skill 的视频导出路线；
未拷入其 CLI 代码。完整出处与许可见 `references/attribution.md`。

## 1. 核心思想（照搬）

"Write HTML. Render video. Built for agents."
无构建步骤：`index.html + data-*` 时间属性即组合。
headless Chrome 逐帧截图 + FFmpeg 编码，同一输入必出同一输出。

## 2. 安装（照搬）

```bash
npx hyperframes skills update          # 安装核心 skill 集（9 个已发布 skill）
claude plugin marketplace add heygen-com/hyperframes
```

另有桌面 Studio 应用（免费，Pro 版付费）；slideshow、remotion-to-hyperframes、
figma 等 skill 按需安装。

## 3. 环境要求（照搬）

Node.js ≥22、FFmpeg、Chrome。输出 MP4（1920×1080 @ 30fps）。

## 4. 本 skill 的视频导出路线（两档）

### A 档：浏览器录屏（MVP 默认，零安装）
1. 用浏览器打开 `assets/template.html`（或做好的单文件 deck）
2. 播放动画，用系统录屏 / OBS 录成 MP4
3. 优点：零依赖；缺点：帧率受录屏影响，不保证逐帧确定

### B 档：HyperFrames 确定性渲染（要精确出片时用）
1. 把 deck 的每一页写成带 `data-*` 时间属性的 HTML
2. `npx hyperframes` 逐帧渲染 → FFmpeg 编码 MP4
3. 优点：逐帧确定、可复现、适合自动化；缺点：需装 Node 22+ 与 FFmpeg

## 5. 确定性渲染的纪律（与 22-hud 的工作法一致）

- 每一帧必须是时间 t 的纯函数；只用种子随机；
- 物理与粒子预计算或用闭式解；不用真实时钟、不用状态触发的 CSS 过渡；
- 渲染前先出 6–10 个关键帧静帧验收，再整片渲染。
