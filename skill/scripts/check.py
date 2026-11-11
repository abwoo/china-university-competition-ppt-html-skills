#!/usr/bin/env python3
"""tech-style 自检：模板是否自包含、SKILL.md 是否含必备章节。纯标准库，无依赖。

用法：
    python3 scripts/check.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAILURES = []


def check(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAILURES.append(msg)


def main():
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    for word in ["科技感", "流水线", "网格动画", "发光节点", "互联网+ PPT",
                 "挑战杯", "路演", "比赛 PPT", "演示动画", "架构图", "流程图"]:
        check(word in skill, f"SKILL.md 含触发词：{word}")
    for section in ["视觉系统", "动画契约", "比赛 PPT 结构", "内容纪律", "双路线导出", "许可红线"]:
        check(section in skill, f"SKILL.md 含章节：{section}")
    for token in ["#06070a", "#7B61FF", "#A78BFA", "#22D3EE", "#FFB829"]:
        check(token in skill, f"SKILL.md 含 token：{token}")

    tpl = (ROOT / "assets" / "template.html").read_text(encoding="utf-8")
    check("http://" not in tpl and "https://" not in tpl,
          "template.html 无外部链接（自包含）")
    check("@import" not in tpl and "fonts.googleapis" not in tpl,
          "template.html 无外部字体")
    check("compliant" in tpl and "0.5" in tpl,
          "template.html 含合规开关与变速")
    for step in ["数据采集", "智能筛选", "AI 生成", "自动封装", "批量分发"]:
        check(step in tpl, f"template.html 含步骤：{step}")

    for f in ["references/style-tokens.md", "references/competition-outlines.md",
              "references/export-routes.md", "references/attribution.md",
              "references/fireworks-fusion.md", "references/hud-recipes.md",
              "references/html-presets.md", "references/video-fusion.md",
              "references/pptx-fusion.md", "references/guizang-fusion.md",
              "references/anthropic-pptx-fusion.md", "references/award-ppt-cases.md",
              "references/excellent-works.md",
              "references/domestic-competition-style.md",
              "assets/pptx-template.md", "scripts/make_pptx.py"]:
        check((ROOT / f).exists(), f"文件存在：{f}")

    check("low-power" in tpl and "data-preset" in tpl,
          "template.html 含预设切换与 B 键静态模式")
    # v2 动画升级检查：强度档、雷达、打字机、轮次进度、多光点
    check("data-intensity" in tpl and "radar-sweep" in tpl,
          "template.html v2 含动画强度档与雷达")
    check("typewriter" in tpl and "round-bar" in tpl,
          "template.html v2 含打字机状态行与轮次进度条")
    check("dot d2" in tpl and "dot d3" in tpl and "rollCount" in tpl,
          "template.html v2 含多光点与数字滚动")
    check("bg-persp" in tpl and "bg-dots" in tpl and "hex-accent" in tpl,
          "template.html v2 含透视网格、点阵、六边形背景层")
    check("思源黑体" in skill, "SKILL.md 含字体规范（思源黑体）")
    check("仅限用户个人本地使用" in skill, "SKILL.md 含个人自用声明")
    # 反防御性写作：新参考文件存在，SKILL.md 有硬规则
    check((ROOT / "references" / "anti-defensive-writing.md").exists(),
          "文件存在：references/anti-defensive-writing.md")
    check("反防御性写作" in skill and "anti-defensive-writing.md" in skill,
          "SKILL.md 含反防御性写作硬规则")
    anti = (ROOT / "references" / "anti-defensive-writing.md").read_text(encoding="utf-8")
    for phrase in ["需要注意的是", "值得注意的是", "总的来说", "不是 A，而是 B"]:
        check(phrase in anti, f"反防御性写作文件含禁用词表：{phrase}")

    print(f"\n{len(FAILURES)} 项失败" if FAILURES else "\n全部通过")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
