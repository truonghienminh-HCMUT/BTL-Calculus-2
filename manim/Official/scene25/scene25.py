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
         
        TEXT_scene25 = Tex(r"\textbf{CẢM ƠN MỌI NGƯỜI ĐÃ XEM}", font_size=40).shift(UP * 0.5)

        self.play(Write(TEXT_scene25), run_time=2)
        self.play(FadeOut(TEXT_scene25))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))