# 国内大学各项比赛 PPT 和 HTML skills

做两类东西的 skill：科技风 HTML 动画演示，和国内比赛套路式 PPT。

## 两条轨道

| 轨道 | 用途 | 视觉 |
|---|---|---|
| HTML | 单文件 HTML 动画演示，可录屏成视频 | 科技风：深色底、蓝紫发光节点、青蓝连线、粒子流动、Swarm 多光标 |
| PPT | 原生可编辑 PPTX（16:9） | 比赛风：国内比赛套路式视觉，深蓝底、金色书法大标题、白卡片、2×2 数字卡、章节标签、弧线光带、相交大圆、蜿蜒之路通向奖杯、红字强调关键数字 |

两条轨道不许混。HTML 里不出现金色书法大标题、白卡片；PPT 里不出现流动粒子、雷达、Swarm 光标。

## 目录

```
skill/   # skill 本体
  SKILL.md              # 主说明：视觉母版、双路线、双模式、硬规则
  references/           # 规则与调研：比赛套路提炼、真实案例拆解、风格 token、融合来源
  assets/               # HTML 模板、PPTX 模板
  scripts/              # check.py 自检、make_pptx.py 生成 PPTX
docs/    # 说明站（GitHub Pages）
```

## 用法

- 做 HTML 动画演示：用 `skill/assets/template.html` 作起点，按 `skill/SKILL.md` 的视觉母版改；跑 `skill/scripts/check.py` 自检。
- 做比赛 PPT：先读 `skill/references/competition-style-distilled.md` 的套路清单，再按 `skill/SKILL.md` 的结构做；生成见 `skill/scripts/make_pptx.py`。
- 比赛结构硬约束（页数、章节顺序、标题即结论）优先于视觉套路。

## 许可

MIT。仅覆盖本仓库原创内容；借鉴的第三方来源见 [SOURCES.md](SOURCES.md)。
