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

        color_db5897 = "#db5897"
        color_03ffff = "#03ffff"
        color_cc00ff = "#cc00ff"
        color_fececa = "#fececa"
        color_e158d0 = "#e158d0"
        color_88bdef = "#88bdef"

        Text_1_scene22 = Tex(
            r"III. ỨNG DỤNG CỦA TÍCH PHÂN KÉP",
            font_size=50
        )
        Text_1_1_scene22 = Tex(
            r"TRONG TỌA ĐỘ CỰC VỚI ĐỜI SỐNG",
         font_size = 50
        )
        
        Text_1_scene22.shift(UP * 1.5)

        Text_1_scene22.set_color_by_gradient(color_03ffff, color_cc00ff)
        Text_1_1_scene22.set_color_by_gradient(color_03ffff, color_cc00ff)

        Text_2_scene22 = Tex(
            r"\textbf{Đồ họa máy tính (Computer Graphics)",
            font_size = 35, 
            color = WHITE
        )
        background_box = SurroundingRectangle(
            Text_2_scene22,
            color=RED_E,            # màu viền
            fill_color=RED_E,    # màu nền
            fill_opacity=0.5,       # độ đậm nền (1 = đặc)
            buff=0.15             # khoảng cách mép khung đến chữ
        )
        Text_2_box_scene22 = VGroup(background_box, Text_2_scene22)
        Text_2_box_scene22.shift(UP * 3)

        Text_2_2_scene22 = Tex(
            r"Tính shading trong mô hình ánh sáng như",
            font_size = 40
        )
        Text_2_3_scene22 = Tex(
            r"Phong Reflection Model",
            r" hoặc",
            r" Radiosity.",
            font_size = 40
        )

        Text_2_2_scene22.shift(UP * 2 + LEFT * 1)
        Text_2_3_scene22.shift(UP * 1.5 + RIGHT * 1.5)

        Phong_Reflection_Model = Text_2_3_scene22[0].copy()
        Radiosity = Text_2_3_scene22[2].copy().shift(DOWN * 4.5 + LEFT * 4.2)
        
        Blinn_Phong = ImageMobject("Blinn_Phong.png")
        Phong = ImageMobject("Phong.png")
        Blinn_Phong_higher_eponent = ImageMobject("Blinn_Phong_higher_exponent.png")
        Radiosity_image = ImageMobject("Radiosity.jpg")

        Blinn_Phong.scale(1.4)
        Blinn_Phong.shift(LEFT * 3.5 + DOWN * 0.8)
        Phong.scale(1.4)
        Phong.shift(DOWN * 0.8)
        Blinn_Phong_higher_eponent.scale(1.4)
        Blinn_Phong_higher_eponent.shift(DOWN * 0.8 + RIGHT * 3.5)
        Radiosity_image.scale(0.35)
        Radiosity_image.shift(DOWN * 2 + UP * 1.3)


        self.play(Write(Text_1_scene22), Write(Text_1_1_scene22), run_time=3)
        self.play(Unwrite(Text_1_1_scene22), Unwrite(Text_1_scene22))
        self.play(LaggedStart(FadeIn(background_box), Write(Text_2_scene22), lag_ratio=0.3), run_time=2)
        self.play(Write(Text_2_2_scene22), run_time=2)
        self.play(Write(Text_2_3_scene22), run_time=2)
        self.play(Phong_Reflection_Model.animate.move_to(DOWN * 3), run_time=1)
        self.play(SpinInFromNothing(Blinn_Phong), run_time=2)
        self.play(SpinInFromNothing(Phong), run_time=2)
        self.play(SpinInFromNothing(Blinn_Phong_higher_eponent), run_time=2)
        self.wait(1)
        self.play(Transform(Phong_Reflection_Model, Radiosity), FadeOut(Phong), FadeOut(Blinn_Phong), FadeOut(Blinn_Phong_higher_eponent), run_time=2)
        self.play(SpinInFromNothing(Radiosity_image), run_time=2)



        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))