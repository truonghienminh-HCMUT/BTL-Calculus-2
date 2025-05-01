from manim import *

config.media_width = "100%"
VIETNAMESE_TEMPLATE = TexTemplate(
    preamble=r"""
    \usepackage[utf8]{inputenc}
    \usepackage[T5]{fontenc}
    \usepackage{amsmath}
    \usepackage{amssymb}
    \usepackage{lmodern}
    \usepackage{graphicx}
    \usepackage{tikz}
    """
)
# Set the default TeX template
config.tex_template = VIETNAMESE_TEMPLATE

class Slide(Scene):
    def construct(self):
        # GHI TỚI ĐÂU IN TỚI ĐÓ
        color_03ffff = "#03ffff"
        color_cc00ff = "#cc00ff"
        color_fececa = "#fececa"
        color_e158d0 = "#e158d0"
        color_88bdef = "#88bdef"

        title_0 = Tex(r"\textbf{TÍCH PHÂN HAI LỚP}", font_size = 80)
        title_1 = Tex(r"\textbf{TRONG TỌA ĐỘ CỰC}", font_size = 80)
        title = VGroup(title_0, title_1).arrange(DOWN)
        title_0.set_color_by_gradient(color_03ffff, color_cc00ff)
        title_1.set_color_by_gradient(color_03ffff, color_cc00ff)
        self.play(Write(title, run_time = 0.75))
        self.wait(1.5)
        self.play(Unwrite(title), run_time = 0.5)

        # Vào slide
        heading1 = Tex(r"\textbf{1. Định nghĩa}", font_size = 55).to_corner(UL)
        heading1.set_color_by_gradient(color_fececa, color_e158d0, color_88bdef)
        self.play(Write(heading1), run_time = 0.5)
        self.wait(0.5)

        heading2 = Tex(r"1.1. Đặt vấn đề").next_to(heading1, DOWN, aligned_edge=LEFT)
        self.play(Write(heading2), run_time = 0.5)
        self.wait(0.5)

        line1_0 = Tex(r"Cho ").next_to(heading2.get_bottom(), DOWN)
        line1_1 = Tex(r"$z = f(x, y)$").set_color(YELLOW).next_to(line1_0, RIGHT)
        line1_2 = Tex(r" xác định trên \textbf{miền đóng}").next_to(line1_1, RIGHT)
        line1_3 = Tex(r"$D = \{(x, y) \in \mathbb{R}^2 : a \leq x \leq b, c \leq y \leq d\}$.").next_to(line1_2.get_bottom(), DOWN)
        line1 = VGroup(line1_0, line1_1, line1_2, line1_3).next_to(heading2, DOWN, aligned_edge=LEFT)
        self.play(Write(line1), run_time = 0.5)
        self.wait(0.5)

        line2 = Tex(r"$\Omega$", r" là vật thể được giới hạn bởi:", tex_to_color_map={r"$\Omega$": YELLOW}).next_to(line1, DOWN, aligned_edge=LEFT)
        self.play(Write(line2), run_time = 0.5)
        self.wait(0.5)

        line3_omega_part = Tex(r"$\Omega$", tex_to_color_map={r"$\Omega$": YELLOW})
        line3_rest_part = Tex(r" $= \{(x, y, z) \in \mathbb{R}^3 : 0 \leq z \leq f(x, y), (x, y) \in D\}$")
        line3 = VGroup(line3_omega_part, line3_rest_part).arrange(RIGHT)
        line3.next_to(line2, DOWN, aligned_edge=LEFT).shift(RIGHT)

        omega_copy = line2[0].copy()
        omega_target = line3[0]
        rest_of_line3 = line3[1]

        self.add(omega_copy)

        self.play(Transform(omega_copy, omega_target), run_time=1.0)
        self.play(Write(rest_of_line3), run_time=0.5)
        self.wait(0.5)

        line4 = Tex(r"Vậy tính tích phân của \textcolor{yellow}{$\Omega$} như thế nào?", font_size = 50).next_to(line3, DOWN).to_edge(LEFT) # Align relative to the VGroup line3
        self.play(Write(line4), run_time = 0.5)
        self.wait(0.5)
