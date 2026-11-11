# Swarm 融合来源 · swarm-fusion.md

PipeCompare 演示 `pipecompare-demo.html` 里“🐝 Swarm 重建”模式的两处来源。
仅个人本地使用，不对外分发。

## 1. DhvanilPatel/swarm-cursors（Swarm Rebuild）

- 仓库：https://github.com/DhvanilPatel/swarm-cursors
- 星数：**2,665★**（GitHub API，2026-11-10 查询）
- License：**无 license 文件（API 返回 `license: null`）**——视为保留所有权利
- 本地：`~/workspace/tech-style-skill/reference-downloads/swarm/swarm-cursors/`（clone 约 41M，含 demo/media）
- 它是什么：一个 Chrome 扩展，把任意网页先抹成空白画布，再由一群多人光标
  现场把它重建回来：十字准星画框、打字、钢笔工具画线、标尺参考线、
  ⌥-拖拽复制，直到页面恢复原样。它自述是向 Joel Califa 的 Swarm 网站致敬，
  动作设计（光标集、群聚物理、搭建编排、标尺、外观）源自该网站。
- **借了什么：只有想法，不抄代码**
  - 清空页面后光标重建的整体构思
  - 光标画矩形/条形、打字出值、拖拽排组件三种重建动作
  - 开场光标聚拢再散开、收尾光标聚拢的群聚感
- **没抄什么**：它的 `swarm-rebuild/swarm.js` 快照/蓝图引擎、扩展代码、
  音效合成，一行都没复制。无 license，只能借想法，这是硬边界。
- 演示里的对应：Swarm 重建先清空证据板，五只光标再按角色把它画回来；
  画柱、打值、排 5 个管线节点、一起打结论，都是这个构思的落地。

## 2. ruvnet/mouse-swarm（Mouse Swarm Reveal）

- 仓库：https://github.com/ruvnet/mouse-swarm
- 星数：**24★**（GitHub API，2026-11-10 查询）
- License：**MIT**（`LICENSE`，Copyright (c) 2026 ruvnet）——代码与想法均可改编，需保留 attribution
- 描述：“Turn a landing page into a visual build sequence. Elements appear in
  order while a swarm of colored cursors and agent markers moves around them.”
- 本地：`~/workspace/tech-style-skill/reference-downloads/swarm/mouse-swarm/`
- 关键文档：`skills/mouse-swarm-reveal/SKILL.md`（已读，全文照此改编）
- **借了什么（规则与机制，内联改编）**
  - 多只彩色虚拟光标，数量可配（演示里 `SWARM_CURSOR_COUNT = 5`）
  - 光标协同揭示内容：按顺序出现文字、卡片、组件
  - 暂停 / 继续 / 重播 / 跳过四件套，控件全程可见、键盘可达
  - 进度回调（演示里状态行“重建中 3/8 · …”即 `onStep` 的等价物）
  - 出错与静态时恢复终态；尊重 reduced motion；光标只是模拟演示，
    明确标注不是真实输入，也绝不挡点击（`pointer-events: none`）
  - 控件放在被揭示内容之外，不遮挡可交互元素
- **改编方式**：没有直接引入它捆绑的 `assets/mouse-swarm.js` ES 模块，
  因为演示要求单文件自包含、零外部引用；按 SKILL.md 的规则在页内
  用原生 JS 重写了一个小步骤机（`runSwarm` / `swSleep` / `swMove` /
  `swType` / `swDrawBar`）。行为对齐，代码是自己的。
- **没借什么**：Ruflo 观测桥、录制/回放、MP4 导出、Playwright 验证——
  演示不需要，也没接。

## 3. 演示里的融合点（本质关联，不是装饰）

每只光标对应 PipeCompare 故事里的一个真实角色，颜色与任务写死对应：

| 光标 | 颜色 | 真实角色 | 画什么 / 打什么 |
|---|---|---|---|
| ① | 青 `#22D3EE` | 开发组10人 | MSE 对比柱（Standard 0.483 / 最简 2.352 / ICA 1.173），逐人点图并圈出 S004 |
| ② | 金 `#FFB829` | 换人复测11-20号 | 全平双柱（都是 1.182348），打“10/10 全平” |
| ③ | 紫 `#A78BFA` | 校准检查 | 校准条：开发组 1.17 / 换人复测 1.54，合格门 [0.8, 1.2] |
| ④ | 绿 `#34D399` | 短故障检查 | 检出率：1 秒 0% / 5 秒 0% / 10 秒 100% / 20 秒 100% |
| ⑤ | 粉红 `#FB7185` | ERP CORE下一轮 | 时间线：2026-11 冻结 → P3b 20 人 300 秒 → 先跑 1 号冒烟 |

五只光标最后一起打结论（已按 PR51 事实核过）：
“开发组赢了最简方法，没赢常用 ICA；换人复测全平，校准更糟——下一轮走真实数据。”

逐人点图数字来源：`~/workspace/audits/pr51-review/raw/docs__WITHIN_VARIANCE_TRIAL_RESULTS.md`
（S001–S010 原版/候选版 MSE）与 `docs__PUBLIC_PILOT_RESULTS.md`；
换人复测见 `HELDOUT_SCORING_RESULTS.md`（1.182348、校准比 1.537936）。

## 4. Attribution（保留出处）

- `pipecompare-demo.html` 文件头注释已写明两处来源、星数与 license 状态。
- ruvnet/mouse-swarm：MIT，Copyright (c) 2026 ruvnet。
- DhvanilPatel/swarm-cursors：无 license，仅借想法，未复制代码；
  其致敬对象 Joel Califa 的 Swarm（https://califa.github.io/swarm-site/）
  在此一并注明。
- 本文件与演示均仅限个人本地使用，不对外分发。
