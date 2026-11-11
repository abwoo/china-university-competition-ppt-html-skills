#!/usr/bin/env python3
"""tech-style 最小 PPTX 生成器：按 assets/pptx-template.md 生成 3 页 deck。

只做最小验证（封面 / 内容 / 结尾），复杂 deck 按同一母版另写脚本。
需要 python-pptx，未装时先建 venv 安装：

    python3 -m venv /tmp/techstyle-venv
    /tmp/techstyle-venv/bin/pip install python-pptx
    /tmp/techstyle-venv/bin/python scripts/make_pptx.py --title "示例项目" --out /tmp/test-deck.pptx

用法：
    python3 scripts/make_pptx.py --title "示例项目" --out /tmp/test-deck.pptx
"""
import argparse
import sys

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt, Emu
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN
except ImportError:
    print("缺少 python-pptx：先按文件头说明建 venv 安装后再跑。", file=sys.stderr)
    sys.exit(2)

BG = RGBColor(0x06, 0x07, 0x0A)
CARD = RGBColor(0x12, 0x12, 0x2B)
YELLOW = RGBColor(0xFF, 0xB8, 0x29)
CYAN = RGBColor(0x22, 0xD3, 0xEE)
WHITE = RGBColor(0xED, 0xEF, 0xF7)
MUTED = RGBColor(0x9A, 0xA3, 0xB2)
BORDER = RGBColor(0x3D, 0x3A, 0x6B)


def blank_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.background
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG
    return slide


def set_font(run, name, size=18, color=WHITE, bold=False):
    """同时写 latin 与 east asian 两个 typeface，否则中文在 PowerPoint 里
    可能回退到默认字体。字体名：标题/正文用思源黑体（免费商用，可嵌入），
    备选微软雅黑 / 等线。"""
    from pptx.oxml.ns import qn
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.name = name
    rPr = run._r.get_or_add_rPr()
    ea = rPr.find(qn("a:ea"))
    if ea is None:
        ea = rPr.makeelement(qn("a:ea"), {})
        rPr.append(ea)
    ea.set("typeface", name)


def textbox(slide, left, top, width, height, text, size=18, color=WHITE, bold=False,
            font="思源黑体"):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(text.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        run = p.add_run()
        run.text = line
        set_font(run, font, size=size, color=color, bold=bold)
    return box


def notes(slide, text):
    slide.notes_slide.placeholders[1].text = text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", default="示例项目")
    ap.add_argument("--out", default="/tmp/test-deck.pptx")
    args = ap.parse_args()

    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(5.625)

    # 1 封面
    s = blank_slide(prs)
    textbox(s, 0.6, 0.4, 8.8, 0.4, "INTERNET+  //  2026", size=13, color=CYAN, bold=True)
    textbox(s, 0.6, 1.5, 8.8, 1.2, args.title, size=44, color=YELLOW, bold=True)
    textbox(s, 0.6, 2.8, 8.8, 0.6, "一句话价值主张：睡一觉，200 个客户开发信已发完", size=20, color=WHITE)
    textbox(s, 0.6, 4.9, 8.8, 0.4, "团队名  ·  2026-11-10", size=14, color=MUTED)
    notes(s, "封面讲稿：大家好，我们是示例项目团队，一句话讲清我们解决什么问题。")

    # 2 内容页：痛点
    s = blank_slide(prs)
    textbox(s, 0.6, 0.4, 8.8, 0.6, "痛点：找客户又慢又贵", size=28, color=WHITE, bold=True)
    card = s.shapes.add_shape(1, Inches(0.6), Inches(1.4), Inches(4.2), Inches(2.6))
    card.fill.solid(); card.fill.fore_color.rgb = CARD
    card.line.color.rgb = BORDER
    textbox(s, 0.85, 1.6, 3.7, 2.2, "人工一天找 20 个客户就累瘫了\n获客成本高、重复劳动多", size=18, color=WHITE)
    card2 = s.shapes.add_shape(1, Inches(5.2), Inches(1.4), Inches(4.2), Inches(2.6))
    card2.fill.solid(); card2.fill.fore_color.rgb = CARD
    card2.line.color.rgb = BORDER
    textbox(s, 5.45, 1.6, 3.7, 2.2, "AI 一晚上自动跑 200+ 客户\n人工只需点审批", size=18, color=WHITE)
    textbox(s, 0.6, 4.5, 8.8, 0.4, "数据来源：[待补：真实调研数据]", size=12, color=MUTED)
    textbox(s, 8.9, 5.2, 0.5, 0.3, "2 / 3", size=12, color=MUTED)
    notes(s, "痛点页讲稿：先讲一个真实场景，再给数据，不要堆背景。")

    # 3 结尾
    s = blank_slide(prs)
    textbox(s, 0.6, 2.0, 8.8, 1.0, "谢谢，欢迎提问", size=40, color=YELLOW, bold=True)
    textbox(s, 0.6, 3.2, 8.8, 0.5, "负责人  ·  电话 / 微信  ·  邮箱", size=18, color=MUTED)
    notes(s, "结尾讲稿：收尾一句话，留联系方式。")

    prs.save(args.out)
    print(f"已生成 {args.out}（3 页，16:9）")


if __name__ == "__main__":
    main()
