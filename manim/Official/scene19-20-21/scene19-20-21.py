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

config.frame_rate = 60

class ChiaNho(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        Text_1 = Tex(
            r"Khi đổi biến trong \textbf{tích phân đôi} (ví dụ như",
            r" $\iint_R f(x, y) \, dxdy$)",
            r", nếu chuyển sang",
            r" tọa độ cực",
            r", ta phải nhân thêm hệ số",
            r"\textbf{ r}",
            r":",
            font_size=40
        )
        ToaDoCuc = Text_1[3].copy()
        ToaDoCuc.set_color(BLUE)

        Text_1[3].set_color(BLUE)
        Text_1[5].set_color(YELLOW)

        Text_2 = Tex(
            r"Công thức đổi biến sang hệ",
            r" toạ độ cực:",
            font_size=40
        ).shift(UP * 3)
        Text_2[1].set_color(BLUE)

        Text_3 = MathTex(
            r"x=",
            r"r",
            r"\cos\varphi",
            font_size=80
        )
        r1 = Text_3[1].copy()
        Text_4 = MathTex(
            r"y=",
            r"r",
            r"\sin\varphi", 
            font_size=80
        )
        r2 = Text_4[1].copy()
        Text_5 = MathTex(
            r"r",
            r" \ge 0",
            font_size=80
        )
        Text_5[1].shift(RIGHT * 1 + DOWN * 1)

        CongThucToaDoCuc = VGroup(Text_4, Text_3)

        Text_6 = Tex(
            r"Khi đó, định thức Jacobian khi chuyển sang hệ toạ độ cực là:",
            font_size=40
        ).shift(UP * 3)

        Jacobian = MathTex(
            r"J = \frac{\partial (x, y)}{\partial (r, \varphi)} = ",
            r"\begin{vmatrix}"
            r"\frac{\partial x}{\partial r} & \frac{\partial x}{\partial \varphi} \\"
            r"\frac{\partial y}{\partial r} & \frac{\partial y}{\partial \varphi}"
            r"\end{vmatrix}",
            r"=",
            r"\begin{vmatrix}"
            r"\cos \varphi & -r \sin \varphi \\"
            r"\sin \varphi & r \cos \varphi"
            r"\end{vmatrix}",
            r"= r",
            font_size=55
        )
        HeToaDoCuc_scene19 = VGroup(Text_3, Text_4, Text_5)


        self.play(Write(Text_1), run_time=3)
        self.wait(1)
        self.play(Unwrite(Text_1), Transform(ToaDoCuc, Text_2[1]), Write(Text_2[0]), run_time=2)
        self.play(Write(Text_3), run_time=2)
        self.play(Text_3.animate.move_to(UP * 1), Write(Text_4))
        self.play(r1.animate.move_to(DOWN * 1), r2.animate.move_to(DOWN * 1), run_time=2)
        self.play(Write(Text_5[1]))
        self.play(Circumscribe(HeToaDoCuc_scene19))
        self.wait(1)
        self.play(Unwrite(r1), Unwrite(r2), Unwrite(Text_5[1]))
        self.remove(ToaDoCuc)
        self.play(Transform(Text_2, Text_6), run_time=1)
        self.play(Transform(CongThucToaDoCuc, Jacobian), run_time=2)
        self.play(Circumscribe(CongThucToaDoCuc))
        self.wait(1)
        self.remove(CongThucToaDoCuc, Text_2)

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))