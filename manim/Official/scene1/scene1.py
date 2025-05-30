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

class scene1(MovingCameraScene):
    def construct(self):
        color_03ffff = "#03ffff"
        color_cc00ff = "#cc00ff"
        self.camera.frame.save_state()
         
        #SCENE 1: GIỚI THIỆU CHỦ DỀ VÀ TÊN THÀNH VIÊN
        Text_ChuDe_scene1 = Tex(r"\textbf{CHỦ ĐỀ 7}", font_size=45).shift(UP* 1)
        Text_TenChuDe_scene1 = Tex(r"\textbf{TÍCH PHÂN KÉP TRONG TỌA ĐỘ CỰC}", font_size=55)
        Text_TenNhom_scene1= Tex(r"\textbf{NHÓM NM02 - LỚP CN01}", font_size=45).shift(DOWN * 1)

        Text_ChuDe_scene1.set_color_by_gradient(color_03ffff, color_cc00ff)
        Text_TenChuDe_scene1.set_color_by_gradient(color_03ffff, color_cc00ff)
        Text_TenNhom_scene1.set_color_by_gradient(color_03ffff, color_cc00ff)

        self.play(Write(Text_ChuDe_scene1), Write(Text_TenChuDe_scene1), run_time=2)
        self.play(Write(Text_TenNhom_scene1), run_time=2)
        self.wait(2)
        self.play(FadeOut(Text_ChuDe_scene1), FadeOut(Text_TenChuDe_scene1), FadeOut(Text_TenNhom_scene1), run_time=1)

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
