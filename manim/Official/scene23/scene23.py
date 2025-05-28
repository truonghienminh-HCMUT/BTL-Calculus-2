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

class SCENE_23(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        color_03ffff = "#03ffff"
        color_cc00ff = "#cc00ff"
        color_4dbbbe0 = "#4dbbe0"
        color_fe7051 = "#fe7051"
        color_7fb663 = "#7fb663"
        color_ff8d28 = "#ff8d28"

        Text_1_scene23 = Tex(
            r"\textbf{4. GIẢI QUYẾT VÍ DỤ THỰC TIỄN}",
            font_size=50
        )
        Text_1_scene23.set_color_by_gradient(color_03ffff, color_cc00ff)
        ViDu_1_scene23 = Tex(r"Áp dụng công thức, ta tính được:", font_size=45).shift(UP * 1)
        ViDu_2_scene23 = Tex(r"$R^2=r^2+d^2=4^2+3^2=5^2$", font_size=45)
        ViDu_3_scene23 = Tex(r"với R là bán kính của hình cầu đáy.", font_size=45).shift(DOWN * 1)
        ViDu_4_scene23 = Tex(r"Vậy R = 5m với R là bán kính của hình cầu đáy.", font_size=40).shift(UP * 0.5)
        ViDu_5_scene23 = Tex(r"$f(x,y)=z=-\sqrt{5^2-x^2-y^2}$", font_size=40).shift(DOWN * 0.5)
        ViDu_6_scene23 = Tex(r"$f(x,y)=z=\sqrt{5^2-x^2-y^2}$", font_size=40).shift(UP * 3)
        ViDu_7_scene23 = Tex(r"Ta có khoảng cách từ mặt đáy đến tâm hình cầu là $d = 3m$. Do hình cầu mô phỏng nằm bên dưới mặt Oz nên mặt đáy phải nằm bên trên mặt $z = -3$ và mặt phẳng $z = -3$ cũng chính là mặt đất thực tế.",
                            font_size=35)
        ViDu_8_scene23 = Tex(r"Tiếp theo là phần đỉnh, từ quan sát anh thấy rằng nó có dạng khá giống hình paraboloid tròn (dạng đặc biệt của elliptic paraboloid) có phương trình:",
                            font_size=35)
        ViDu_9_scene23 = MathTex(r"f(x,y)=z=a(x^2+y^2)+b", font_size=40).shift(DOWN * 0.5)
        ViDu_10_scene23 = Tex(r"Sau khi dùng các số liệu thực tế để tính toán, ta có:", font_size=35).shift(UP * 1)
        ViDu_11_scene23 = MathTex(r"f(x,y)=z=\frac{-3}{8}(x^2+y^2)+9", font_size=40).shift(DOWN * 0.5)

        self.play(Write(Text_1_scene23), run_time=2)
        self.wait(1)
        self.play(FadeOut(Text_1_scene23))
        self.play(Write(ViDu_1_scene23), run_time=1)
        self.play(Write(ViDu_2_scene23), run_time=1)
        self.play(Write(ViDu_3_scene23), run_time=1)
        self.wait(1)
        self.play(ViDu_1_scene23.animate.move_to(UP * 5), ViDu_2_scene23.animate.move_to(UP * 5), ViDu_3_scene23.animate.move_to(UP * 5),
                Write(ViDu_4_scene23), Write(ViDu_5_scene23),
                run_time=2)
        self.remove(ViDu_1_scene23, ViDu_2_scene23, ViDu_3_scene23)
        self.wait(1)
        self.play(ViDu_4_scene23.animate.move_to(UP * 5), ViDu_5_scene23.animate.move_to(UP * 3))
        self.wait(1)
        self.remove(ViDu_4_scene23)
        self.play(Transform(ViDu_5_scene23, ViDu_6_scene23), run_time=1)
        self.wait(1)
        self.remove(ViDu_5_scene23)
        self.play(Write(ViDu_7_scene23), run_time=3)
        self.wait(1)
        self.play(FadeOut(ViDu_7_scene23))
        self.play(Write(ViDu_8_scene23), run_time=2)
        self.play(ViDu_8_scene23.animate.move_to(UP * 0.8))
        self.play(Write(ViDu_9_scene23), run_time=2)
        self.wait(1)
        self.play(Unwrite(ViDu_8_scene23), ViDu_9_scene23.animate.move_to(UP *2 ), run_time=1.5)
        self.wait(1)
        self.play(Write(ViDu_10_scene23), run_time=2)
        self.play(Transform(ViDu_9_scene23, ViDu_11_scene23), run_time=1)
        self.wait(1)
        self.remove(ViDu_9_scene23, ViDu_10_scene23)



        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))