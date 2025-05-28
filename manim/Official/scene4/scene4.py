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
         
        #SCENE 2: TABLE OF CONTENTS
        TEXT_scene4 = Tex(r"\textbf{NỘI DUNG}", font_size=70)
        NoiDung1 = Tex(r"1. TÍCH PHÂN KÉP", font_size=40).shift(UP * 2 + LEFT * 2.28+ DOWN * 0.5)
        NoiDung2 = Tex(r"2. TÍCH PHÂN KÉP TRONG TỌA ĐỘ CỰC", font_size=40).shift(UP * 1 + DOWN * 0.5)
        NoiDung3 = Tex(r"3. ỨNG DỤNG CỦA TÍCH PHÂN KÉP", font_size=40).shift(LEFT * 0.5 + DOWN * 0.5)
        NoiDung3_1 = Tex( r"TRONG TỌA ĐỘ CỰC VỚI ĐỜI SỐNG", font_size=40).shift(DOWN * 0.5 + RIGHT * 0.08 + DOWN * 0.5)
        NoiDung4 = Tex(r"4. GIẢI QUYẾT VÍ DỤ THỰC TIỄN", font_size=40).shift(DOWN * 1.5 + LEFT * 0.7 + DOWN * 0.5)

        self.play(Write(TEXT_scene4), run_time=2)
        self.play(TEXT_scene4.animate.move_to(UP * 3), run_time=1)
        self.play(Write(NoiDung1), run_time=2)
        self.play(Write(NoiDung2), run_time=2)
        self.play(Write(NoiDung3), Write(NoiDung3_1), run_time=2)
        self.play(Write(NoiDung4), run_time=2)


        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
