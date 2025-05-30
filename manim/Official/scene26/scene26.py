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
        DeViDu = Tex(r"\textbf{Anh A mô phỏng được tòa nhà bằng một hình cầu}", font_size=30).shift(UP * 2 + RIGHT * 3).set_color(YELLOW)
        DeViDu_2 = Tex(r"\textbf{và một hình paraboloid tròn}", font_size=30).shift(UP * 1.5 + RIGHT * 2.5).set_color(YELLOW)
        ChieuDai = Tex(r"12m chiều cao (h)", font_size=30).shift(UP * 0.6 + RIGHT * 2.7)
        BanKinh = Tex(r"4m bán kính của đường tròn đáy (r)", font_size=30).shift( RIGHT * 2.7 + DOWN * 0.2)
        KhoangCach = Tex(r"3m khoảng cách từ mặt đất đến tâm hình cầu (d)", font_size=30).shift(DOWN * 1 + RIGHT * 2.7)

        Text_1_scene23.set_color_by_gradient(color_03ffff, color_cc00ff)
        


        self.play(Write(Text_1_scene23), run_time=2)
        self.wait(1)
        self.play(FadeOut(Text_1_scene23))
        self.play(Write(DeViDu), Write(DeViDu_2), Write(ChieuDai), Write(BanKinh), Write(KhoangCach), run_time=2)
        self.wait(1)
        

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))