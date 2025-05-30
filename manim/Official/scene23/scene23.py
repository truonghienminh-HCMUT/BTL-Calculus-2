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
        Atiso = ImageMobject("Atiso.jpg")
        Atiso.scale(1).shift(LEFT  * 3.8)
        DeViDu = Tex(r"\textbf{Anh A mô phỏng được tòa nhà bằng một hình cầu}", font_size=30).shift(UP * 2 + RIGHT * 3).set_color(YELLOW)
        DeViDu_2 = Tex(r"\textbf{và một hình paraboloid tròn}", font_size=30).shift(UP * 1.5 + RIGHT * 2.5).set_color(YELLOW)
        ChieuDai = Tex(r"12m chiều cao (h)", font_size=30).shift(UP * 0.6 + RIGHT * 2.7)
        BanKinh = Tex(r"4m bán kính của đường tròn đáy (r)", font_size=30).shift( RIGHT * 2.7 + DOWN * 0.2)
        KhoangCach = Tex(r"3m khoảng cách từ mặt đất đến tâm hình cầu (d)", font_size=30).shift(DOWN * 1 + RIGHT * 2.7)

        Text_1_scene23.set_color_by_gradient(color_03ffff, color_cc00ff)
        ViDu_1_scene23 = Tex(r"Áp dụng công thức, ta tính được:", font_size=45).shift(UP * 1)
        ViDu_2_scene23 = Tex(r"$R^2=r^2+d^2=4^2+3^2=5^2$", font_size=45)
        ViDu_3_scene23 = Tex(r"với R là bán kính của hình cầu đáy.", font_size=45).shift(DOWN * 1)
        ViDu_4_scene23 = Tex(r"Vậy R = 5m với R là bán kính của hình cầu đáy.", font_size=40).shift(UP * 0.5)
        ViDu_5_scene23 = Tex(r"$f(x,y)=z=-\sqrt{5^2-x^2-y^2}$", font_size=40).shift(DOWN * 0.5)
        ViDu_6_scene23 = Tex(r"$f(x,y)=z=\sqrt{5^2-x^2-y^2}$", font_size=40).shift(UP * 3)
        ViDu_7_scene23 = Tex(r"Ta có khoảng cách từ mặt đáy đến tâm hình cầu là $d = 3m$. Do hình cầu mô phỏng nằm bên dưới mặt Oz nên mặt đáy phải nằm bên trên mặt $z = -3$ và mặt phẳng $z = -3$ cũng chính là mặt đất thực tế.",
                            font_size=35)
        ViDu_8_scene23 = Tex(r"Tiếp theo là phần đỉnh, từ quan sát ta thấy rằng nó có dạng khá giống hình paraboloid tròn (dạng đặc biệt của elliptic paraboloid) có phương trình:",
                            font_size=35)
        ViDu_9_scene23 = MathTex(r"f(x,y)=z=a(x^2+y^2)+b", font_size=40).shift(DOWN * 0.5)
        ViDu_10_scene23 = Tex(r"Sau khi dùng các số liệu thực tế để tính toán, ta có:", font_size=35).shift(UP * 1)
        ViDu_11_scene23 = MathTex(r"f(x,y)=z=\frac{-3}{8}(x^2+y^2)+9", font_size=40).shift(DOWN * 0.5)
        ViDu_12_scene23 = Tex(r"TÍNH TOÁN", font_size=50).set_color(YELLOW)
        ViDu_13_scen23 = Tex(r"TÍNH TOÁN", font_size=40).shift(UP * 3).set_color(YELLOW)
        ViDu_14_scen23 = Tex(r"Diện tích khối cầu có phương trình $f(x, y)=\sqrt{5^2-x^2-y^2}$, giới hạn bởi mặt phẳng $z = 3$:", font_size=35).shift(UP*2)
        ViDu_15_scen23 = MathTex(r"S_c = \iint\limits_D \sqrt{1^2 + f_x^2 + f_y^2}\, dA", font_size=40).shift(UP * 0.8)
        ViDu_16_scene23 = MathTex(r" = \iint\limits_D \sqrt{\frac{25}{5^2-x^2-y^2}}\, dA", font_size=40).shift(DOWN * 0.5)
        ViDu_17_scene23 = Tex(r"Thay vào tọa độ cực: $x=rcos\varphi,y=rsin\varphi,dA=rdrd\varphi$", font_size=35).shift(DOWN * 1.5)
        ViDu_18_scene23 = MathTex(r"S_c = \iint\limits_D \sqrt{\frac{25}{25 - r^2}} \, r \, dr \, d\varphi", font_size=40).shift(DOWN * 3)
        ViDu_19_scene23 = Tex(r"Do đồ thị khối cầu phần trên bị giới hạn bởi đường $z=3$ do khoảng cách tới tâm từ đáy là 3 và không có điều kiện về góc nên ta có", font_size=35).shift(UP * 0.8)
        ViDu_20_scene23 = MathTex(
            r"\left\{ \begin{array}{l}"
            r"4 \leq r \leq 5 \\"
            r"0 \leq \varphi \leq 2"
            r"\end{array} \right.", 
            font_size=40
        ).shift(DOWN * 0.3)
        ViDu_21_scene23 = MathTex(r"S_c = \int_0^{2\pi} d\varphi \int_4^5 r\,dr\, \sqrt{\frac{25}{25 - r^2}}", font_size=40).shift(UP * 0.8)
        ViDu_23_scene23 = MathTex(r"= 5 \int_0^{2\pi} d\varphi \int_4^5 r\,dr\, \sqrt{\frac{1}{25 - r^2}}", font_size=40).shift(DOWN * 0.5)
        ViDu_24_scene23 = Tex(r"Đặt $u = 25-r^2$ $\Rightarrow$ $du = -2rdr$", font_size=35).shift(UP * 0)
        ViDu_25_scen23 = MathTex( r"S_c = \frac{5}{2} \int_0^{2\pi} d\varphi \int_0^9 du\, \sqrt{\frac{1}{u}}", font_size=40).shift(DOWN * 1)
        ViDu_26_scene23 = MathTex(r"= \frac{5}{2} \int_0^{2\pi} 6\, d\varphi =",r"30\pi", font_size=40).shift(DOWN * 2.2)
        ViDu_27_scene23 = Tex(r"Lấy đối xứng lên trên.", font_size=35).shift(UP*1.2)
        ViDu_28_scene23 = Tex(r"$\Rightarrow$ Diện tích khối cầu ở đáy là", r" $60\pi$", font_size=40)
        ViDu_29_scene23 = Tex(r"Tiếp theo là phần đỉnh. Ta có phần đỉnh là một paraboloid tròn tiếp xúc với hình cầu đáy. Phần tiếp xúc là một đường tròn có bán kính là $4 m$. Ứng với:", font_size=35).shift(UP*2)
        ViDu_30_scene23 = MathTex(
            r"\left\{ \begin{array}{l}"
            r"0 \leq r \leq 4 \\"
            r"0 \leq \varphi \leq 2"
            r"\end{array} \right.", 
            font_size=40
        ).shift(UP * 1)
        ViDu_31_scene23 = Tex(r"Thay phương trình của paraboloid vào công thức, ta có:", font_size=35)
        ViDu_32_scene23 = MathTex(
            "S_p = \\int_0^{2\\pi} d\\varphi \\int_0^4 r \\sqrt{1 + \\frac{9}{16} r^2} \\, dr", font_size=40).shift(DOWN * 1)
        ViDu_33_scene23 = MathTex(
            "\\text{- Đặt } u = 1 + \\frac{9}{16}r^2 \\Rightarrow du = \\frac{9}{8}r\\,dr "
            "\\Rightarrow r\\,dr = \\frac{8}{9}du", font_size=35
        ).shift(UP * 0.7)
        ViDu_34_scene23 = MathTex(
            "\\Rightarrow S_p = \\int_0^{2\\pi} d\\varphi \\int_1^{10} "
            "\\frac{8}{9} \\sqrt{u} \\, du", font_size=40).shift(DOWN * 0.5)
        ViDu_35_scene23 = MathTex(
            "= \\int_0^{2\\pi} d\\varphi \\, \\frac{16}{27} \\left( 10\\sqrt{10} - 1 \\right)", font_size=40
        ).shift(DOWN * 1.6)
        ViDu_36_scene23 = MathTex(
            "=", "\\frac{32\\pi}{27} \\left( 10\\sqrt{10} - 1 \\right)", font_size=40
        ).shift(DOWN * 2.7)
        ViDu_37_scene23 = Tex(r"Anh A cho biết anh sẽ dùng kính để làm tòa nhà, vậy diện tích kính cần sử dụng là:", font_size=35).shift(UP * 1.5)
        ViDu_38_scene23 = MathTex("\\frac{32\\pi}{27}(10\\sqrt{10} - 1) + 60\\pi\\,(m^2)", font_size=40)
        ViDu_39_scene23 = Tex(r"Anh A sử dụng kính cường lực $10 mm$ Việt Nhật $480.000$ VNĐ$/m^2$, vậy số tiền cần sử dụng là:", font_size=35).shift(UP * 0.8)
        ViDu_40_scene23 = MathTex(
            "\\left[ \\frac{32\\pi}{27}(10\\sqrt{10} - 1) + 60\\pi \\right]"
            " \\times 480\\,000 \\approx 145\\,207\\,000 \\ (\\text{VNĐ})", font_size=40
        ).shift(DOWN * 0.7)


        self.play(Write(Text_1_scene23), run_time=2)
        self.wait(1)
        self.play(FadeOut(Text_1_scene23))
        self.play(SpinInFromNothing(Atiso), run_time=2)
        self.play(Write(DeViDu), Write(DeViDu_2), Write(ChieuDai), Write(BanKinh), Write(KhoangCach), run_time=2)
        self.wait(1)
        self.remove(DeViDu, DeViDu_2, ChieuDai, BanKinh, KhoangCach, Atiso)
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
        self.wait(3)
        self.remove(ViDu_4_scene23)
        self.play(Transform(ViDu_5_scene23, ViDu_6_scene23), run_time=1)
        self.wait(3)
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
        self.play(ViDu_19_scene23.animate.move_to(UP * 3), run_time=2)
        self.wait(3)
        self.remove(ViDu_9_scene23, ViDu_10_scene23)
        self.wait(1)
        self.play(Write(ViDu_12_scene23), run_time=2)
        self.play(Transform(ViDu_12_scene23, ViDu_13_scen23), run_time=1)
        self.play(Write(ViDu_14_scen23), run_time=2)
        self.play(Write(ViDu_15_scen23), run_time=2)
        self.play(Write(ViDu_16_scene23), run_time=2)
        self.wait(1)
        self.play(Write(ViDu_17_scene23), run_time=2)
        self.play(Transform(ViDu_16_scene23, ViDu_18_scene23), run_time=1)
        self.wait(1)
        self.play(FadeOut(ViDu_14_scen23), FadeOut(ViDu_15_scen23), FadeOut(ViDu_17_scene23), ViDu_16_scene23.animate.move_to(UP * 2), run_time=2)
        self.play(Write(ViDu_19_scene23), run_time=2)
        self.play(Write(ViDu_20_scene23), run_time=2)
        self.play(FadeOut(ViDu_19_scene23), Transform(ViDu_20_scene23, ViDu_21_scene23), run_time=2)
        self.play(Write(ViDu_23_scene23), run_time=2)
        self.play(FadeOut(ViDu_16_scene23), ViDu_20_scene23.animate.move_to(UP* 2), ViDu_23_scene23.animate.move_to(UP * 0.8))
        self.play(Write(ViDu_24_scene23), run_time=2)
        self.play(Write(ViDu_25_scen23), run_time=2)
        self.play(Write(ViDu_26_scene23), run_time=2)
        self.play(Circumscribe(ViDu_26_scene23[1]))
        self.play(FadeOut(ViDu_26_scene23), FadeOut(ViDu_25_scen23), FadeOut(ViDu_24_scene23), FadeOut(ViDu_20_scene23), FadeOut(ViDu_23_scene23))
        self.play(Write(ViDu_27_scene23), run_time=2)
        self.play(Write(ViDu_28_scene23), run_time=2)
        self.play(Circumscribe(ViDu_28_scene23[1]))
        self.wait(1)
        self.play(FadeOut(ViDu_27_scene23), FadeOut(ViDu_28_scene23))
        self.play(Write(ViDu_29_scene23), run_time=2)
        self.play(Write(ViDu_30_scene23), run_time=2)
        self.play(Write(ViDu_31_scene23), run_time=2)
        self.play(Write(ViDu_32_scene23), run_time=2)
        self.play(FadeOut(ViDu_29_scene23), FadeOut(ViDu_30_scene23), FadeOut(ViDu_31_scene23), ViDu_32_scene23.animate.move_to(UP * 2), run_time=2)
        self.play(Write(ViDu_33_scene23), run_time=2)
        self.play(Write(ViDu_34_scene23), run_time=2)
        self.play(Write(ViDu_35_scene23), run_time=2)
        self.play(Write(ViDu_36_scene23), run_time=2)
        self.play(FadeOut(ViDu_32_scene23), FadeOut(ViDu_33_scene23), FadeOut(ViDu_34_scene23), FadeOut(ViDu_35_scene23))
        self.play(ViDu_36_scene23.animate.move_to(UP * 1), Write(ViDu_37_scene23), Transform(ViDu_36_scene23, ViDu_38_scene23), run_time=2)
        self.play(Circumscribe(ViDu_36_scene23))
        self.wait(1)
        self.play(FadeOut(ViDu_36_scene23), FadeOut(ViDu_37_scene23))
        self.play(Write(ViDu_39_scene23), run_time=2)
        self.play(Write(ViDu_40_scene23), run_time=2)
        self.play(Circumscribe(ViDu_40_scene23))
        self.wait(1)
        self.play(FadeOut(ViDu_39_scene23), FadeOut(ViDu_40_scene23))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))