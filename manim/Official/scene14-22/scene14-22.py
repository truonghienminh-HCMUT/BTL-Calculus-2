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

        color_03ffff = "#03ffff"
        color_cc00ff = "#cc00ff"
        color_4dbbbe0 = "#4dbbe0"
        color_fe7051 = "#fe7051"
        color_7fb663 = "#7fb663"
        color_ff8d28 = "#ff8d28"
         
        #SCENE14_16
        axes1 = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=4,
            y_length=4,
            axis_config={"include_tip": True},
        ).move_to(LEFT * 3)

        axes2 = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=4,
            y_length=4,
            axis_config={"include_tip": True},
        ).move_to(RIGHT * 3)
        
        a = 2  # bán kính trong
        b = 3.5    # bán kính ngoài
        alpha = 0.3  # góc alpha (rad)
        beta = 1.2   # góc beta (rad)
        origin = axes1.c2p(0, 0)
        origin2 = axes2.c2p(0, 0)

        x_axes1_labels = axes1.get_x_axis_label("x")
        y_axes1_labels = axes1.get_y_axis_label("y")
        x_axes1_labels_copy = x_axes1_labels.copy()
        y_axes1_labels_copy = y_axes1_labels.copy()
        Text0 = Tex("O").to_edge(UP * 7,  buff=0.5).scale(1)
        Text0.shift((DOWN * 2.5), LEFT * 5.2)
        Text01 = Tex("O").to_edge(UP * 7,  buff=0.5).scale(1)
        Text01.shift((DOWN * 2.5), RIGHT * 0.9)
        rb = Tex("r = b").scale(1).next_to(axes1.c2p(a, 0), UP)
        rb.move_to([-1.6, 0.8, 0])
        ra = Tex("r = a").scale(0.7).next_to(axes2.c2p(b, 0), UP)
        ra.move_to([-3.9, -0.9, 0])
        r_a_sau = Tex("r = a").scale(1).next_to(axes2.c2p(b, 0), UP)
        r_a_sau.scale(1)
        r_a_sau.move_to([0.45, -0.75, 0])
        Textphi = Tex(r"$\varphi$").scale(0.85).next_to(axes1.c2p(a, 0), UP)
        Textphi.move_to([5.4, -1.5, 0])
        D = MathTex(r"D").scale(2).next_to(axes1.c2p(a, 0), UP).set_color(YELLOW)
        D.move_to([-2.9, 0, 0])
        alpha_label = MathTex(r"\alpha").scale(1).next_to(axes1.c2p(a, 0), UP)
        alpha_label.move_to([2.2, -2.2, 0])
        alpha_label.set_color(RED)
        alpha_label_old = MathTex(r"\alpha").scale(0.9).next_to(axes1.c2p(a, 0), UP)
        alpha_label_old.move_to([-3.3, -1.65, 0])
        alpha_label_old.set_color(RED)
        beta_label_old = MathTex(r"\beta").scale(1).next_to(axes1.c2p(a, 0), UP)
        beta_label_old.move_to([-3.8, -1.3, 0])
        beta_label_old.set_color(GREEN)
        beta_label = MathTex(r"\beta").scale(1).next_to(axes1.c2p(a, 0), UP)
        beta_label.move_to([3.7, -2.2, 0])
        beta_label.set_color(GREEN)

        outer_arc = Arc(radius=b, start_angle=alpha, angle=beta - alpha, arc_center=origin)
        inner_arc = Arc(radius=a, start_angle=beta, angle=-(beta - alpha), arc_center=origin)

        big_arc = Arc(radius=3, start_angle=alpha, angle=beta - alpha, arc_center=origin2)
        big_arc.set_color(RED)
        small_arc = Arc(radius=2.5, start_angle=beta, angle=-(beta - alpha), arc_center=origin2)
        small_arc.set_color(RED)

        # Tính điểm đầu dựa trên góc alpha
        left_point = origin + b * np.array([np.cos(alpha), np.sin(alpha), 0])
        right_point = origin + b * np.array([np.cos(beta), np.sin(beta), 0])

        # Tạo các đoạn thẳng từ origin
        left_line = Line(origin, left_point)
        right_line = Line(origin, right_point)

        outer_points = [origin + b * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(alpha, beta, 30)]
        inner_points = [origin + a * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(beta, alpha, 30)]

        region_points = outer_points + inner_points
        region = VMobject()
        region.set_points_as_corners(region_points)
        region.set_fill(RED, opacity=0.5)
        left_line.set_color(BLUE)
        right_line.set_color(BLUE)
        outer_arc.set_color(RED)
        inner_arc.set_color(RED)

        # Tạo vùng D tô màu

        x_axis_point = axes1.c2p(1, 0)
        x_axis_line_1 = Line(origin, x_axis_point, color=RED)
        angle_alpha = Angle(
            left_line, x_axis_line_1,
            radius=1.3,
            color=RED,
            other_angle=True,  # Hoặc True nếu muốn góc > 180°
            fill_opacity=0.5
        )
        angle_beta = Angle(
            right_line, x_axis_line_1,
            radius=0.9,
            color=GREEN,
            other_angle=True,  # Hoặc True nếu muốn góc > 180°
            fill_opacity=0.5
        )
        angle_beta.set_fill(opacity=0)


        part = VGroup(outer_arc, inner_arc, left_line, right_line, region, angle_alpha, angle_beta, alpha_label_old, beta_label_old, D, ra, rb)
        part1 = VGroup(region, outer_arc, inner_arc, left_line, right_line, angle_alpha, angle_beta, alpha_label_old, beta_label_old, D, ra, rb)#đưa region lên để đưa sang bên phải
        part.shift(LEFT * 0)
        part_copy = part1.copy()

        line_1 = Line(start= axes2.c2p(0, 0), end=axes2.c2p(2.5, 3.6), color=BLUE, stroke_width=4)
        line_2 = Line(start= axes2.c2p(0, 0), end=axes2.c2p(3.3, 2.9), color=BLUE, stroke_width=4)
        line_3 = Line(start= axes2.c2p(0, 0), end=axes2.c2p(3.9, 2), color=BLUE, stroke_width=4)

        Text_1_scene15 = Tex(
            r"Như vậy, miền D được mô tả trong hệ toạ độ cực:",
            font_size=40
        )
        NhuVayMienD = MathTex(
            r"D \;=\; \{(r, \varphi) \colon a \leq r \leq b, \alpha \leq \varphi \leq \beta\}",
            font_size=40
        )
        Text_2_scene15 = Tex(
            r"Miền nhỏ bất kỳ trong hệ toạ độ cực xác định như sau:",
            font_size=40
        ).shift(UP * 3)
 
        Text_1_scene16 = Tex(
            r"Tâm của phần tử con trong hệ toạ độ cực:",
            font_size=35
        ).shift(LEFT * 3 + UP * 1)
        TamCuaPhanTuCon = MathTex(
            r"D_{ij} = \{ (r,\varphi) \colon r_{i-1} \le r \le r_i, \varphi_{j-1} \le \varphi \le \varphi_j \}",
            font_size=35
        ).shift(LEFT * 3)

        Text_2_scene16 = Tex(
            r"Lấy một điểm bất kỳ trong $D_{ij}$ có toạ độ:", 
            font_size=35
        ).shift(LEFT * 3 + UP * 1)
        LayMotDiem = MathTex(
            r"r_i^* = \tfrac{1}{2}\Big(r_i + r_{i-1}\Big), \,",
            r"\varphi_j^* = \tfrac{1}{2}\Big(\varphi_j + \varphi_{j-1}\Big)",
            font_size=35
        ).shift(LEFT * 3)

        Text_3_scene16 = Tex(
            r"Diện tích của miền $D_{ij}$ được tính bằng:",
            font_size=35
        ).shift(LEFT * 3 + UP * 2)
        DienTichCuaMienD_1 = MathTex(
            r"S_{D_{ij}} = \frac{1}{2} r_i^2 \Delta \varphi - \frac{1}{2} r_{i-1}^2 \Delta \varphi ",
            font_size=35
        ).shift(LEFT * 3 + UP * 1)
        DienTichCuaMienD_2 = MathTex(
            r"= \frac{1}{2} \Big( r_i + r_{i-1} \Big) \Big( r_i - r_{i-1} \Big) \cdot \Delta \varphi ",
            r"= r_i^* \Delta r \cdot \Delta \varphi",
            font_size=35
        ).shift(LEFT * 3)

        Text_4_scene16 = Tex(
            r"Khi đó, tổng Riemann tương ứng sẽ là:",
            font_size=35
        ).shift(LEFT * 3 + UP * 2)
        TongRiemann_1 = MathTex(
            r"\sum_{i=1}^m \sum_{j=1}^n f \left( r_i^* \cos \varphi_j, r_j^* \sin \varphi_j \right) S_{D_{ij}}",
            font_size=35
        ).shift(LEFT * 3 + UP * 1)
        TongRiemann_2 = MathTex(
            r"=",
            r"\sum_{i=1}^m \sum_{j=1}^n f \left( r_i^* \cos \varphi_j, r_j^* \sin \varphi_j \right) r_i^* \cdot \Delta r \cdot \Delta \varphi",
            font_size=35
        ).shift(LEFT * 3 + DOWN  * 0.2)

        Text_5_scene16 = Tex(
            r"Nếu ta đặt $g(r, \varphi) =rf(rcos\varphi,rsin\varphi)$",
            font_size=35
        ).shift(LEFT * 3 + UP * 2)
        Text_5_scene16_2 = Tex(
            r"thì tổng Riemann ở trên có dạng:",
            font_size=35
        ).shift(LEFT * 3 + UP * 1)
        NeuTaDat = MathTex(
            r"\left| \sum_{i=1}^m \sum_{j=1}^n g\left(r_i^*, \varphi_j^*\right) \cdot \Delta r \cdot \Delta \varphi \right|",
            font_size=35
        ).shift(LEFT * 3)



        self.play(Write(Text_1_scene15), run_time=2)
        self.play(Text_1_scene15.animate.move_to(UP * 1.5), run_time=1)
        self.play(Write(NhuVayMienD), run_time=2)
        self.wait(1)
        self.play(FadeOut(NhuVayMienD), run_time=1)
        self.play(Transform(Text_1_scene15, Text_2_scene15))
        self.play(Create(axes1),  run_time=2)
        self.play(Create(x_axes1_labels), Create(y_axes1_labels),Write(Text0), run_time=2)
        self.play(Create(part), run_time=3)
        self.add(outer_arc, inner_arc, left_line, right_line)
        self.play(Create(axes2), Write(Text01), run_time=2)
        self.add(part_copy)
        self.play(part1.animate.move_to(RIGHT * 3.05 + DOWN * 0.3), x_axes1_labels_copy.animate.move_to(RIGHT * 5.1 + UP * (-1.5)), y_axes1_labels_copy.animate.move_to(RIGHT * 1.7 + UP * 2), run_time=2)
        self.wait(1)
        self.play(Uncreate(region), Uncreate(angle_alpha), Uncreate(angle_beta), Unwrite(alpha_label_old), Unwrite(beta_label_old), Unwrite(ra), Unwrite(rb), Unwrite(D))
        self.play(Create(line_1), Create(line_2), Create(line_3), run_time=2)
        self.play(Create(big_arc), Create(small_arc), run_time=2)
        self.remove(part_copy, axes1, x_axes1_labels, y_axes1_labels, Text0)
        self.play(
                  part1.animate.move_to(DOWN * 0.3 + RIGHT * 4), axes2.animate.move_to(RIGHT * 4), line_1.animate.move_to(RIGHT * 4), line_2.animate.move_to(RIGHT * 4),
                  line_3.animate.move_to(RIGHT * 4), big_arc.animate.move_to(RIGHT * 4), small_arc.animate.move_to(RIGHT * 4), x_axes1_labels_copy.animate.move_to(RIGHT * 4), y_axes1_labels_copy.animate.move_to(RIGHT * 4), Text01.animate.move_to(RIGHT * 4), Unwrite(Text_1_scene15),
                  Write(Text_1_scene16), Write(TamCuaPhanTuCon),
                  run_time=3   
        )
        self.wait(1.5)
        self.play(Transform(Text_1_scene16, Text_2_scene16), Transform(TamCuaPhanTuCon, LayMotDiem), run_time=1)
        self.wait(1.5)
        self.play(Transform(Text_1_scene16, Text_3_scene16), Transform(TamCuaPhanTuCon, DienTichCuaMienD_1), Write(DienTichCuaMienD_2), run_time=1)
        self.wait(1.5)
        self.play(Transform(Text_1_scene16, Text_4_scene16), Transform(TamCuaPhanTuCon, TongRiemann_1), Transform(DienTichCuaMienD_2, TongRiemann_2), run_time=1)
        self.wait(1.5)
        self.play(Transform(Text_1_scene16, Text_5_scene16), Transform(TamCuaPhanTuCon, Text_5_scene16_2), Transform(DienTichCuaMienD_2, NeuTaDat), run_time=1)
        self.play(Uncreate(part1),  Uncreate(axes2), Uncreate(line_1), Uncreate(line_2),
                  Uncreate(line_3), Uncreate(big_arc), Uncreate(small_arc), Uncreate(x_axes1_labels_copy), Uncreate(y_axes1_labels_copy), Unwrite(Text01),
                  Unwrite(DienTichCuaMienD_2), Unwrite(Text_1_scene16), Unwrite(TamCuaPhanTuCon),
                  run_time=1   )
         

        #SCENE17
        axes1_scene17 = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=4,
            y_length=4,
            axis_config={"include_tip": True},
        ).move_to(LEFT * 3)

        axes2_scene17 = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=4,
            y_length=4,
            axis_config={"include_tip": True},
        ).move_to(RIGHT * 3)
        
        a_scene17 = 2  # bán kính trong
        b_scene17 = 3.5    # bán kính ngoài
        alpha_scene17 = 0.3  # góc alpha (rad)
        beta_scene17 = 1.2   # góc beta (rad)
        origin_scene17 = axes1_scene17.c2p(0, 0)

        x_axes1_labels_scene17 = axes1_scene17.get_x_axis_label("x")
        y_axes1_labels_scene17 = axes1_scene17.get_y_axis_label("y")
        x_axes1_labels_copy_scene17 = x_axes1_labels_scene17.copy()
        y_axes1_labels_copy_scene17 = y_axes1_labels_scene17.copy()
        yaxes2_label_scene17 = axes2_scene17.get_y_axis_label("r")
        Text0_scene17 = Tex("O").to_edge(UP * 7,  buff=0.5).scale(1)
        Text0_scene17.shift((DOWN * 2.5), LEFT * 5.2)
        Text01_scene17 = Tex("O").to_edge(UP * 7,  buff=0.5).scale(1)
        Text01_scene17.shift((DOWN * 2.5), RIGHT * 0.9)
        rb_scene17 = Tex("r = b").scale(1).next_to(axes1_scene17.c2p(a_scene17, 0), UP)
        rb_scene17.move_to([-1.6, 0.8, 0])
        ra_scene17 = Tex("r = a").scale(0.7).next_to(axes2_scene17.c2p(b_scene17, 0), UP)
        ra_scene17.move_to([-3.9, -0.9, 0])
        r_a_sau_scene17 = Tex("r = a").scale(1).next_to(axes2_scene17.c2p(b_scene17, 0), UP)
        r_a_sau_scene17.scale(1)
        r_a_sau_scene17.move_to([0.45, -0.75, 0])
        Textphi_scene17 = Tex(r"$\varphi$").scale(0.85).next_to(axes1_scene17.c2p(a_scene17, 0), UP)
        Textphi_scene17.move_to([5.4, -1.5, 0])
        D_scene17 = MathTex(r"D").scale(2).next_to(axes1_scene17.c2p(a_scene17, 0), UP).set_color(YELLOW)
        D_scene17.move_to([-2.9, 0, 0])
        alpha_label_scene17 = MathTex(r"\alpha").scale(1).next_to(axes1_scene17.c2p(a_scene17, 0), UP)
        alpha_label_scene17.move_to([2.2, -2.2, 0])
        alpha_label_scene17.set_color(RED)
        alpha_label_old_scene17 = MathTex(r"\alpha").scale(0.9).next_to(axes1_scene17.c2p(a_scene17, 0), UP)
        alpha_label_old_scene17.move_to([-3.3, -1.65, 0])
        alpha_label_old_scene17.set_color(RED)
        beta_label_old_scene17 = MathTex(r"\beta").scale(1).next_to(axes1_scene17.c2p(a_scene17, 0), UP)
        beta_label_old_scene17.move_to([-3.8, -1.3, 0])
        beta_label_old_scene17.set_color(GREEN)
        beta_label_scene17 = MathTex(r"\beta").scale(1).next_to(axes1_scene17.c2p(a_scene17, 0), UP)
        beta_label_scene17.move_to([3.7, -2.2, 0])
        beta_label_scene17.set_color(GREEN)
        fxy_scene17 = MathTex(r"f(x,y)").scale(1.5).next_to(axes1_scene17.c2p(a_scene17, 0), UP)
        fxy_scene17.move_to([-2.9, 3, 0])
        fxy_scene17.set_color(RED)
        fxy_copy_scene17 = fxy_scene17.copy()
        frphi_scene17 = MathTex(r"f(r(cos(\varphi)),rsin(\varphi)).r").scale(1).next_to(axes2_scene17.c2p(a_scene17, 0), UP)
        frphi_scene17.move_to([3, 3, 0])
        frphi_scene17.set_color(BLUE)

        outer_arc_scene17 = Arc(radius=b_scene17, start_angle=alpha_scene17, angle=beta_scene17 - alpha_scene17, arc_center=origin_scene17)
        inner_arc_scene17 = Arc(radius=a_scene17, start_angle=beta_scene17, angle=-(beta_scene17 - alpha_scene17), arc_center=origin_scene17)

        # Tính điểm đầu dựa trên góc alpha
        left_point_scene17 = origin_scene17 + b_scene17 * np.array([np.cos(alpha_scene17), np.sin(alpha_scene17), 0])
        right_point_scene17 = origin_scene17 + b_scene17 * np.array([np.cos(beta_scene17), np.sin(beta_scene17), 0])

        # Tạo các đoạn thẳng từ origin
        left_line_scene17 = Line(origin_scene17, left_point_scene17)
        right_line_scene17 = Line(origin_scene17, right_point_scene17)

        outer_points_scene17 = [origin_scene17 + b_scene17 * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(alpha_scene17, beta_scene17, 30)]
        inner_points_scene17 = [origin_scene17 + a_scene17 * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(beta_scene17, alpha_scene17, 30)]

        region_points_scene17 = outer_points_scene17 + inner_points_scene17
        region_scene17 = VMobject()
        region_scene17.set_points_as_corners(region_points_scene17)
        region_scene17.set_fill(RED, opacity=0.5)
        left_line_scene17.set_color(BLUE)
        right_line_scene17.set_color(BLUE)
        outer_arc_scene17.set_color(RED)
        inner_arc_scene17.set_color(RED)

        x_axis_point_scene17 = axes1_scene17.c2p(1, 0)
        x_axis_line_1_scene17 = Line(origin_scene17, x_axis_point_scene17, color=RED)
        angle_alpha_scene17 = Angle(
            left_line_scene17, x_axis_line_1_scene17,
            radius=1.3,
            color=RED,
            other_angle=True,  # Hoặc True nếu muốn góc > 180°
            fill_opacity=0.5
        )
        angle_beta_scene17 = Angle(
            right_line_scene17, x_axis_line_1_scene17,
            radius=0.9,
            color=GREEN,
            other_angle=True,  # Hoặc True nếu muốn góc > 180°
            fill_opacity=0.5
        )
        angle_beta_scene17.set_fill(opacity=0)


        part_scene17 = VGroup(outer_arc_scene17, inner_arc_scene17, left_line_scene17, right_line_scene17, region_scene17, angle_alpha_scene17, angle_beta_scene17, alpha_label_old_scene17, beta_label_old_scene17, D_scene17, ra_scene17, rb_scene17)
        part1_scene17 = VGroup(region_scene17, outer_arc_scene17, inner_arc_scene17, left_line_scene17, right_line_scene17, angle_alpha_scene17, angle_beta_scene17,alpha_label_old_scene17, beta_label_old_scene17, D_scene17, ra_scene17, rb_scene17)#đưa region lên để đưa sang bên phải
        part_scene17.shift(LEFT * 0)
        part_copy_scene17 = part1_scene17.copy()

        line_r_a_scene17 = Line(start= axes2_scene17.c2p(-1, 3), end= axes2_scene17.c2p(5, 3), color=RED, stroke_width=4)
        line_r_b_scene17 = Line(start= axes2_scene17.c2p(-1, 1), end= axes2_scene17.c2p(5, 1), color=RED, stroke_width=4)
        line_alpha_scene17 = Line(start= axes2_scene17.c2p(1, -1), end= axes2_scene17.c2p(1, 5), color=BLUE, stroke_width=4)
        line_beta_scene17 = Line(start= axes2_scene17.c2p(3, -1), end= axes2_scene17.c2p(3, 5), color=BLUE, stroke_width=4)

        p1_scene17 = axes2_scene17.c2p(1, 3)  # Giao alpha và r_a
        p2_scene17 = axes2_scene17.c2p(3, 3)  # Giao beta và r_a
        p3_scene17 = axes2_scene17.c2p(3, 1)  # Giao beta và r_b
        p4_scene17 = axes2_scene17.c2p(1, 1)  # Giao alpha và r_b

        region_new_D_scene17 = Polygon(p1_scene17, p2_scene17, p3_scene17, p4_scene17, fill_color=RED, fill_opacity=0.5, stroke_width=0)

        Text_1_scene17 = Tex(
            r"Đây chính là tổng Riemann của tích phân kép $\int_{\alpha}^{\beta} \int_{a}^{b} g(r, \varphi)\, dr\, d\varphi$ . Do đó, ta có:", 
            font_size=35
        )
        TongRiemannCuaTichPhanKep_dai = MathTex(
            r"\iint_D",
            r"f(x, y)",
            r"\,dx\,dy &= \sum_{i=1}^m \sum_{j=1}^n f\left(r_i^* \cos\varphi_j^*,\, r_i^* \sin\varphi_j^*\right)\cdot S_{D_{ij}} \\",
            r"&= \sum_{i=1}^m \sum_{j=1}^n g\left(r_i^*,\, \varphi_j^*\right)\cdot \Delta r \cdot \Delta \varphi \\",
            r"&= \int_{\alpha}^{\beta} \int_{a}^{b} g(r, \varphi)\, dr\, d\varphi = \int_{\alpha}^{\beta} \int_{a}^{b}",
            r" f(rcos\varphi, rsin\varphi)",
            r"\cdot r\, dr\, d\varphi",
            font_size=35
        )
        TongRiemannCuaTichPhanKep_ngan = MathTex(
            r"\iint_D",#0
            r" f(x, y)",#1
            r"\,dx\,dy",#2
            r" = \int_{\alpha}^{\beta} \int_{a}^{b}",#2
            r" f(rcos\varphi, rsin\varphi)",#3
            r"\cdot r\,",#4
            r" dr\, d\varphi",#5
            font_size=35
        )

        self.play(Write(Text_1_scene17), run_time=2)
        self.play(Text_1_scene17.animate.move_to(UP * 2.5))
        self.wait(1)
        self.play(Write(TongRiemannCuaTichPhanKep_dai), run_time=2)
        self.wait(1.5)
        self.play(Transform(TongRiemannCuaTichPhanKep_dai, TongRiemannCuaTichPhanKep_ngan), run_time=1)
        self.play(Circumscribe(TongRiemannCuaTichPhanKep_ngan))
        self.wait(1)
        self.play(Unwrite(Text_1_scene17))
        self.play(Transform(TongRiemannCuaTichPhanKep_ngan[1], fxy_scene17), TongRiemannCuaTichPhanKep_dai.animate.move_to(DOWN * 3), run_time=2)
        self.play(Create(axes1_scene17), run_time=2)
        self.play(Create(x_axes1_labels_scene17), Create(y_axes1_labels_scene17),Write(Text0_scene17))
        self.play(Create(part_scene17), run_time=2)
        self.add(outer_arc_scene17, inner_arc_scene17, left_line_scene17, right_line_scene17)
        self.wait(1)
        self.play(Create(axes2_scene17), Write(Text01_scene17), run_time=2)
        self.add(part_copy_scene17)
        self.play(fxy_copy_scene17.animate.move_to(RIGHT * 3 + UP *3), part1_scene17.animate.move_to(RIGHT * 3.05 + DOWN * 0.3), x_axes1_labels_copy_scene17.animate.move_to(RIGHT * 5.1 + UP * (-1.5)), y_axes1_labels_copy_scene17.animate.move_to(RIGHT * 1.7 + UP * 2), run_time=2)
        self.wait(1)
        self.play(Transform(fxy_copy_scene17, frphi_scene17), Transform(x_axes1_labels_copy_scene17, Textphi_scene17), Transform(y_axes1_labels_copy_scene17, yaxes2_label_scene17), Transform(left_line_scene17, line_r_a_scene17), Transform(right_line_scene17, line_r_b_scene17), Transform(angle_alpha_scene17, line_alpha_scene17), Transform(angle_beta_scene17, line_beta_scene17), Transform(region_scene17, region_new_D_scene17),
                D_scene17.animate.move_to(DOWN * 0.2 + RIGHT * 2.7), Uncreate(outer_arc_scene17), Uncreate(inner_arc_scene17), Uncreate(alpha_label_old_scene17), Uncreate(beta_label_old_scene17), rb_scene17.animate.move_to(LEFT * (-0.4) +  UP * 0.8), Transform(ra_scene17, r_a_sau_scene17), Create(alpha_label_scene17), Create(beta_label_scene17),
                run_time=2)
        self.play(Wiggle(TongRiemannCuaTichPhanKep_dai[4]), Wiggle(TongRiemannCuaTichPhanKep_dai[5]))
        self.remove(TongRiemannCuaTichPhanKep_dai, fxy_copy_scene17, x_axes1_labels_copy_scene17, y_axes1_labels_copy_scene17, left_line_scene17, right_line_scene17, angle_alpha_scene17, angle_beta_scene17,region_scene17,
                D_scene17, rb_scene17, ra_scene17, alpha_label_scene17, beta_label_scene17, part1_scene17,
                axes1_scene17, axes2_scene17, x_axes1_labels_scene17, y_axes1_labels_scene17, x_axes1_labels_copy_scene17, y_axes1_labels_copy_scene17, part_copy_scene17, TongRiemannCuaTichPhanKep_ngan[1], Text01_scene17, Text0_scene17
                ) 
        


        #SCENE 18
        # create the axes and the curve
        ax_scene18 = Axes(x_range=[-1, 10], 
                y_range=[-1, 10],
                x_length=6,  # Độ dài trục x (đơn vị màn hình, không phải giá trị)
                y_length=4,  # Độ dài trục y
                 x_axis_config={
                    "include_numbers": False,
                    "tip_width": 0.25,     # rộng mũi tên trục x
                    "tip_height": 0.25     # cao mũi tên trục x
                },  # Tắt số mặc định
                 y_axis_config={
                    "include_numbers": False,
                    "tip_width": 0.25,     # rộng mũi tên trục x
                    "tip_height": 0.25     # cao mũi tên trục x
                })#tạo trục tọa độ
        labels_scene18 = ax_scene18.get_axis_labels(
            x_label=Tex(r"$x$"), y_label=Tex(r"$y$")#tạo nhãn cho các trục
        )
        labels_scene18.shift(DOWN * 1)
        ax_scene18.shift(DOWN * 1)

        a_scene18 = 5  # bán kính trong
        b_scene18 = 6    # bán kính ngoài
        alpha_scene18 = 0.3  # góc alpha (rad)
        beta_scene18 = 0.5   # góc beta (rad)
        origin_scene18 = ax_scene18.c2p(0, 0)

        outer_arc_scene18 = Arc(radius=b_scene18, start_angle=alpha_scene18, angle=beta_scene18 - alpha_scene18, arc_center=origin_scene18)
        inner_arc_scene18 = Arc(radius=a_scene18, start_angle=beta_scene18, angle=-(beta_scene18 - alpha_scene18), arc_center=origin_scene18)


        # Tính điểm đầu dựa trên góc alpha
        left_point_scene18 = origin_scene18 + b_scene18 * np.array([np.cos(alpha_scene18), np.sin(alpha_scene18), 0])
        right_point_scene18 = origin_scene18 + b_scene18 * np.array([np.cos(beta_scene18), np.sin(beta_scene18), 0])

        # Tạo các đoạn thẳng từ origin
        left_line_scene18 = Line(origin_scene18, left_point_scene18)
        right_line_scene18 = Line(origin_scene18, right_point_scene18)

        angle_scene18 = Angle(
            left_line_scene18, right_line_scene18,
            radius=4,
            other_angle=False,      # Lấy góc nhỏ
            quadrant=(1, 1),        # Đặt góc phía trên phải
            color=YELLOW
        )

        outer_points_scene18 = [origin_scene18 + b_scene18 * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(alpha_scene18, beta_scene18, 30)]
        inner_points_scene18 = [origin_scene18 + a_scene18 * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(beta_scene18, alpha_scene18, 30)]

        region_points_scene18 = outer_points_scene18 + inner_points_scene18
        region_scene18 = VMobject()
        region_scene18.set_points_as_corners(region_points_scene18)
        region_scene18.set_fill(RED, opacity=0.5)
        left_line_scene18.set_color(BLUE)
        right_line_scene18.set_color(BLUE)
        outer_arc_scene18.set_color(RED)
        inner_arc_scene18.set_color(RED)

        Text_1_scene18 = Tex(
            r"Khi chuyển từ hệ toạ độ Descartes sang hệ toạ độ cực bằng cách đổi \textbf{$x=rcos\varphi$}, \textbf{$y=rsin\varphi$} sử dụng tính gần đúng của giới hạn khi tính tích phân đối với \textbf{$r$} và \textbf{$\varphi$}, ta có thể viết lại ",
            r"\textbf{$dA = rdrd\varphi$}.",
            font_size=35
        ).shift(UP * 3)



        d_phi_scene18 = CurvedArrow(start_point=[1.2, -1 , 0],  end_point=[1, 0, 0], angle=PI/2, color=WHITE,  stroke_width=2)
        d_phi_scene18.tip.scale(0.5)
        d_A_scene18 = Arrow(start=[4, -0.5, 0], end=[2.6, -0.5, 0], buff=0, stroke_width=2, color=WHITE)
        d_A_scene18.tip.scale(0.5)
        d_r_scene18 = CurvedArrow(start_point=[2.04, -0.5, 0], end_point=[2, 1, 0], angle=PI/2, color=WHITE,  stroke_width=2)
        d_r_scene18.tip.scale(0.5)
        r_d_phi_scene18 = Arrow(start=[2, -2, 0], end=[3, -0.9, 0], buff=0, stroke_width=2, color=WHITE)
        r_d_phi_scene18.tip.scale(0.5)

        d_phi_text_scene18 = Tex(
            r"$d\varphi$",
            font_size=30
        ).move_to([[1, 0, 0]]).shift(UP * 0.1)
        d_A_text_scene18 = Tex(
            r"$dA$",
            font_size=30
        ).move_to([4, -0.5, 0]).shift(RIGHT * 0.3)
        d_r_text_scene18 = Tex(
            r"$dr$",
            font_size=30
        ).move_to([2, 1, 0]).shift(UP * 0.1)
        r_d_phi_text_scene18 = Tex(
            r"$rd\varphi$",
            font_size=30
        ).move_to([2, -2, 0]).shift(LEFT * 0.2 + DOWN * 0.2)

        Text_2_scene18 = Tex(
            r"\textbf{Định lý.}",
            r" Nếu $f(x, y)$ là hàm liên tục trên miền $D = \{(r, \varphi): 0 \leq a \leq r \leq b, \alpha \leq \varphi \leq \beta\}$, với $0 \leq \beta - \alpha \leq 2\pi$, thì:",
            font_size=40
        ).shift(UP * 2)

        Text_3_scene18 = MathTex(
            r"\iint_D f(x, y) \,dx\,dy = \int_{\alpha}^{\beta} \int_{a}^{b} f(r\cos\varphi, r\sin\varphi) \cdot r \,dr\,d\varphi",
            font_size=40
        )

        part_scene18 = VGroup(outer_arc_scene18, inner_arc_scene18, left_line_scene18, right_line_scene18, region_scene18)
        self.play(Create(ax_scene18), run_time=2)
        self.play(Create(labels_scene18), run_time=1)
        self.play(Write(Text_1_scene18), run_time=4)
        self.play(Create(part_scene18), Create(angle_scene18), run_time=4)
        self.play(Create(d_phi_scene18), Create(d_A_scene18), Create(d_r_scene18), Create(r_d_phi_scene18), Write(d_r_text_scene18), Write(d_phi_text_scene18), Write(d_A_text_scene18), Write(r_d_phi_text_scene18), Wiggle(Text_1_scene18[1]), run_time=2)
        self.wait(2)
        self.play(Uncreate(d_phi_scene18), Uncreate(d_A_scene18), Uncreate(r_d_phi_scene18), Uncreate(d_r_text_scene18), Unwrite(r_d_phi_text_scene18), Unwrite(d_A_text_scene18), Unwrite(r_d_phi_text_scene18), Unwrite(d_r_scene18), Uncreate(part_scene18), Unwrite(labels_scene18), Uncreate(ax_scene18), Transform(Text_1_scene18, Text_2_scene18[0]), 
                  Uncreate(angle_scene18), Unwrite(d_phi_text_scene18), run_time=1)
        self.play(Write(Text_2_scene18[1]), run_time=2)
        self.play(Write(Text_3_scene18), run_time=2)
        self.play(Circumscribe(Text_3_scene18))
        self.wait(2)
        self.play(Unwrite(Text_2_scene18[1]), Unwrite(Text_3_scene18), Unwrite(Text_1_scene18), run_time=2)  



        #SCENE19

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

        #SCENE22

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
        background_box_dohoamaytinh = SurroundingRectangle(
            Text_2_scene22,
            color=RED_E,            # màu viền
            fill_color=RED_E,    # màu nền
            fill_opacity=0.5,       # độ đậm nền (1 = đặc)
            buff=0.15             # khoảng cách mép khung đến chữ
        )
        Text_2_box_scene22 = VGroup(background_box_dohoamaytinh, Text_2_scene22)

        Text_2_2_scene22 = Tex(
            r"Tính shading trong mô hình ánh sáng như",
            font_size = 40
        )
        Text_2_3_scene22 = Tex(
            r"Phong Reflection Model",
            r" hoặc",
            r" Radiosity",
            r".",
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

        Text_3_scene22 = Tex(
            r"\textbf{Thị giác máy tính (Computer Vision)}",
            font_size = 35,
            color = WHITE
        )
        background_box_thigiacmaytinh = SurroundingRectangle(
            Text_3_scene22,
            color=BLUE,            # màu viền
            fill_color= color_4dbbbe0,    # màu nền
            fill_opacity=0.5,       # độ đậm nền (1 = đặc)
            buff=0.15             # khoảng cách mép khung đến chữ
        )
        Text_3_box_scene22 = VGroup(background_box_thigiacmaytinh, Text_3_scene22)
        Text_3_box_scene22.shift(UP * 3 + RIGHT * 7)

        Text_4_scene22 = Tex(
            r"Trong quá trình trích xuất đặc trưng hoặc tính toán các đặc trưng dạng hình tròn,",
            r" việc tích phân trong tọa độ cực giúp chuẩn hóa và tính toán chính xác hơn các thuộc tính hình học",
            r" như",
            r" diện tích",
            r",",
            r" mật độ điểm ảnh",
            r", ...",
            font_size=35
        ).shift(UP * 1.9)

        DienTich = Text_4_scene22[3].copy()
        MatDoDiemAnh = Text_4_scene22[5].copy()

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=3,
            y_length=3,
            axis_config={"include_tip": True},
        ).move_to(LEFT * 3.5 + DOWN * 1)

        Text0 = Tex("O").to_edge(UP * 7,  buff=0.5).scale(1)
        Text0.shift(LEFT * 5.1 + DOWN * 3)

        x_axes_labels = axes.get_x_axis_label("x")
        y_axes_labels = axes.get_y_axis_label("y")

        a = 2  # bán kính trong
        b = 3.5    # bán kính ngoài
        alpha = 0.3  # góc alpha (rad)
        beta = 1.2   # góc beta (rad)
        origin = axes.c2p(0, 0)

        outer_arc = Arc(radius=b, start_angle=alpha, angle=beta - alpha, arc_center=origin)
        inner_arc = Arc(radius=a, start_angle=beta, angle=-(beta - alpha), arc_center=origin)

        left_point = origin + b * np.array([np.cos(alpha), np.sin(alpha), 0])
        right_point = origin + b * np.array([np.cos(beta), np.sin(beta), 0])

        # Tạo các đoạn thẳng từ origin
        left_line = Line(origin, left_point)
        right_line = Line(origin, right_point)

        outer_points = [origin + b * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(alpha, beta, 30)]
        inner_points = [origin + a * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(beta, alpha, 30)]

        region_points = outer_points + inner_points
        region = VMobject()
        region.set_points_as_corners(region_points)
        region.set_fill(RED, opacity=0.5)
        left_line.set_color(BLUE)
        right_line.set_color(BLUE)
        outer_arc.set_color(RED)
        inner_arc.set_color(RED)

        TrucDienTich = VGroup(axes, x_axes_labels, y_axes_labels, Text0, outer_arc, inner_arc, left_line, right_line, region)

        MatDoDiemAnh_Image = ImageMobject("MatDoDiemAnh.jpg")
        MatDoDiemAnh_Image.scale(1).shift(RIGHT * 3 + DOWN * 1)


        Text_5_scene22 = Tex(
            r"\textbf{Xử lý tín hiệu số (Digital Signal Processing - DSP)}",
            font_size=35
        )
        background_box_xulytinhieuso = SurroundingRectangle(
            Text_5_scene22,
            color=GREEN,            # màu viền
            fill_color= color_7fb663,    # màu nền
            fill_opacity=0.5,       # độ đậm nền (1 = đặc)
            buff=0.15             # khoảng cách mép khung đến chữ
        )
        Text_5_box_scene22 = VGroup(background_box_xulytinhieuso, Text_5_scene22)
        Text_5_box_scene22.shift(UP * 3)

        Text_6_scene22 = Tex(
            r"Tích phân trong tọa độ cực giúp tối ưu hóa và đánh giá hiệu suất của các bộ lọc không gian hình tròn trong việc làm mịn ảnh, phát hiện biên hình tròn, ...", 
            font_size=35
        )
        axes2_scene12 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4,
            y_length=4,
            axis_config={"color": RED}
        ).shift(LEFT * 3 )
        half_circle_scene22 = Annulus(
            inner_radius=0.6,
            outer_radius=1.2,
            fill_opacity=0.8,
            stroke_width=0
        ).set_color([BLUE_E, TEAL_B, GREEN]).move_to(axes2_scene12.c2p(0, 0))
        half_circle_after_scene22 = half_circle_scene22.copy()

        LamMinAnh_before_Image = ImageMobject("LamMinAnh_before.png")
        LamMinAnh_before_Image.scale(1).shift(LEFT  * 3.8 + UP * 0.8)
        LamMinAnh_after_Image = ImageMobject("LamMinAnh_after.png")
        LamMinAnh_after_Image.scale(1).shift(RIGHT  * 3 + DOWN * 2.4)


        Text_7_scene22 = Tex(
            r"\textbf{Robot học và điều khiển}"
        )
        background_box_robothocvadieukhien = SurroundingRectangle(
            Text_7_scene22,
            color=ORANGE,            # màu viền
            fill_color= color_ff8d28,    # màu nền
            fill_opacity=0.5,       # độ đậm nền (1 = đặc)
            buff=0.15             # khoảng cách mép khung đến chữ
        ).shift(UP * 3)
        Text_7_box_scene22 = VGroup(background_box_robothocvadieukhien, Text_7_scene22)

        # Tạo robot với thiết kế đẹp hơn
        body = RoundedRectangle(
            width=1.2, height=1.8, 
            corner_radius=0.2,
            fill_color=BLUE_E, fill_opacity=1,
            stroke_color=BLUE_A, stroke_width=3
        )
        
        head = Circle(
            radius=0.4,
            fill_color=BLUE_C, fill_opacity=1,
            stroke_color=BLUE_A, stroke_width=3
        ).shift(UP*1.2)
        
        eyes = VGroup(
            Dot(color=WHITE).shift(UP*1.3 + LEFT*0.15),
            Dot(color=WHITE).shift(UP*1.3 + RIGHT*0.15)
        )
        
        # Chân và tay sẽ được animate
        left_arm = Line(ORIGIN, LEFT*0.5 + DOWN*0.5, stroke_width=8)
        right_arm = Line(ORIGIN, RIGHT*0.5 + DOWN*0.5, stroke_width=8)
        arms = VGroup(left_arm, right_arm).shift(UP*0.5)
        
        left_leg = Line(ORIGIN, LEFT*0.3 + DOWN*0.7, stroke_width=8)
        right_leg = Line(ORIGIN, RIGHT*0.3 + DOWN*0.7, stroke_width=8)
        legs = VGroup(left_leg, right_leg).shift(DOWN*0.9)
        
        robot = VGroup(body, head, eyes, arms, legs)
        robot.scale(0.8).shift(LEFT*5 + DOWN*0.5)
        
        # Thêm bóng đổ
        shadow = Circle(radius=0.8, fill_color=BLACK, fill_opacity=0.2, stroke_width=0)
        shadow.scale(0.5).shift(DOWN*2.2)
        
        # Tạo hiệu ứng chạy
        start_pos = robot.get_center()
        end_pos = start_pos + RIGHT*10
        
        
        Text_7_scene22.next_to(robot, UP)  # đặt trên đầu robot

        Text_8_scene22 = Tex(
            r"Tích phân trong tọa độ cực dùng để tính diện tích quét, phân bố năng lượng, hoặc tối ưu hóa đường đi của robot khi hoạt động trong không gian có tính đối xứng tròn.",
            font_size=35
        ).shift(UP * 1.8)
        self.play(Write(Text_1_scene22), Write(Text_1_1_scene22), run_time=3)
        self.play(FadeOut(Text_1_1_scene22), FadeOut(Text_1_scene22))
        self.play(LaggedStart(FadeIn(background_box_dohoamaytinh), Write(Text_2_scene22), lag_ratio=0.3), run_time=2)
        self.play(background_box_dohoamaytinh.animate.move_to(UP * 3), Text_2_scene22.animate.move_to(UP * 3))
        self.play(Write(Text_2_2_scene22), run_time=2)
        self.play(Write(Text_2_3_scene22), run_time=2)
        self.play(Phong_Reflection_Model.animate.move_to(DOWN * 3), run_time=1)
        self.play(SpinInFromNothing(Blinn_Phong), SpinInFromNothing(Phong), SpinInFromNothing(Blinn_Phong_higher_eponent), run_time=2)
        self.wait(1)
        self.play(Blinn_Phong.animate.move_to( DOWN * 0.8), Blinn_Phong_higher_eponent.animate.move_to(DOWN * 0.8))
        self.play(FadeOut(Phong), FadeOut(Blinn_Phong), FadeOut(Blinn_Phong_higher_eponent), run_time=2)
        self.play(Transform(Phong_Reflection_Model, Radiosity), SpinInFromNothing(Radiosity_image), run_time=2)
        self.wait(1)
        self.play(FadeOut(Radiosity_image), Unwrite(Radiosity), Unwrite(Text_2_2_scene22), Unwrite(Text_2_3_scene22), Unwrite(Phong_Reflection_Model))
        self.play(Text_2_box_scene22.animate.move_to(LEFT * 13 + UP *3), run_time=2)
        self.play(Text_3_box_scene22.animate.move_to( UP * 3), run_time=2)
        self.play(Uncreate(Text_2_box_scene22))
        self.play(Write(Text_4_scene22), run_time = 2)
        self.play(DienTich.animate.move_to(DOWN * 1 + LEFT * 3.5), MatDoDiemAnh.animate.move_to(DOWN * 1 + RIGHT * 3.5), run_time=1)
        self.play(Transform(DienTich, TrucDienTich), run_time=2)
        self.play(FadeOut(MatDoDiemAnh), FadeIn(MatDoDiemAnh_Image), run_time=2)
        self.play(Transform(Text_3_scene22, Text_5_box_scene22), Write(Text_5_scene22), Transform(background_box_dohoamaytinh, background_box_xulytinhieuso), Uncreate(Text_3_box_scene22), Unwrite(Text_4_scene22), Uncreate(TrucDienTich), FadeOut(MatDoDiemAnh_Image), Unwrite(DienTich), run_time=1)
        self.play(Write(Text_6_scene22), run_time=2)
        self.play(Text_6_scene22.animate.move_to(UP * 1.9), run_time=1)
        self.play(Create(half_circle_scene22), run_time=2)
        self.play(SpinInFromNothing(LamMinAnh_before_Image), run_time=2)
        self.play(LamMinAnh_before_Image.animate.move_to(DOWN * 2.5 + LEFT * 3), run_time=1)
        self.play(half_circle_after_scene22.animate.move_to(RIGHT * 3), SpinInFromNothing(LamMinAnh_after_Image), run_time=2)
        self.play(Uncreate(half_circle_after_scene22), Uncreate(half_circle_scene22), FadeOut(LamMinAnh_after_Image), FadeOut(LamMinAnh_before_Image), Uncreate(background_box_dohoamaytinh), Unwrite(Text_5_scene22), Unwrite(Text_6_scene22), FadeOut(Text_5_box_scene22), Uncreate(background_box_xulytinhieuso))
        self.add(shadow, robot)
        # Animation di chuyển
        run_time = 3
        frames_per_step = 5
        
        for i in range(frames_per_step):
            alpha = i / frames_per_step
            new_pos = interpolate(start_pos, end_pos, alpha)

            leg_angle = 20 * np.sin(2 * PI * alpha * 4)
            arm_angle = 30 * np.sin(2 * PI * alpha * 4 + PI / 2)

            # Tính delta từ vị trí hiện tại đến vị trí mới
            delta = new_pos - robot.get_center()

            # Di chuyển toàn bộ robot cũ sang vị trí mới
            new_robot = robot.copy().shift(delta)

            # Tạo tay/chân mới (gắn đúng vị trí theo new_pos)
            leg_origin = new_pos + DOWN * 0.9
            new_left_leg = Line(leg_origin, leg_origin + LEFT*0.3 + DOWN*0.7).rotate(leg_angle * DEGREES, about_point=leg_origin)
            new_right_leg = Line(leg_origin, leg_origin + RIGHT*0.3 + DOWN*0.7).rotate(-leg_angle * DEGREES, about_point=leg_origin)

            arm_origin = new_pos + UP * 0.5
            new_left_arm = Line(arm_origin, arm_origin + LEFT*0.5 + DOWN*0.5).rotate(arm_angle * DEGREES, about_point=arm_origin)
            new_right_arm = Line(arm_origin, arm_origin + RIGHT*0.5 + DOWN*0.5).rotate(-arm_angle * DEGREES, about_point=arm_origin)

            # Gắn lại tay và chân mới vào robot
            new_robot.submobjects[3] = VGroup(new_left_arm, new_right_arm)
            new_robot.submobjects[4] = VGroup(new_left_leg, new_right_leg)

            # Cập nhật bóng
            new_shadow = shadow.copy().shift(delta)
            new_shadow.stretch_to_fit_width(1.2 - 0.3 * abs(np.sin(2 * PI * alpha * 4)))

            # Cập nhật màn hình
            self.remove(robot, shadow)
            robot = new_robot
            shadow = new_shadow
            self.add(shadow, robot)
            self.wait(run_time / frames_per_step)
            self.add(Text_7_scene22)
            Text_7_scene22.shift(delta)
        self.play(Text_7_scene22.animate.move_to(UP * 3), Create(background_box_robothocvadieukhien), run_time=1)
        self.play(Uncreate(robot), Uncreate(shadow))
        self.add(Text_7_box_scene22)
        self.play(Write(Text_8_scene22), run_time=2)
        circle1_scene22 = Circle(radius=2, color=WHITE).shift(DOWN * 1)
        circle2_scene22 = Circle(radius=1.5, color=WHITE).shift(DOWN * 1)
        line2_scene13 = Line(start=[2.5, 0, 0], end=[0, 0, 0], color=YELLOW, stroke_width=5).shift(LEFT * 2.5 + DOWN * 1)
        diem_quay_scene13 = ORIGIN + DOWN * 1
        self.add(circle1_scene22)
        angle_tracker = ValueTracker(0)
        center = ORIGIN + DOWN * 1

        # Đường tròn nền
        circle = Circle(radius=2, color=WHITE).move_to(center)
        self.add(circle)
        circle1 = Circle(radius=1.5, color=WHITE).move_to(center)
        self.add(circle1)
        circle2 = Circle(radius=1, color=WHITE).move_to(center)
        self.add(circle2)
        circle3 = Circle(radius=0.5, color=WHITE).move_to(center)
        self.add(circle3)

        dot_scene22 = Circle(radius=0.1, color=RED, fill_opacity=1)
        dot_scene22.move_to(center)
        dot_scene22.shift(DOWN * 0.5 + LEFT * 0.5)
        self.add(dot_scene22)

        # Bộ theo dõi góc quay
        angle_tracker = ValueTracker(0)

        # Đoạn thẳng quay, cập nhật theo góc
        rotating_line = always_redraw(lambda: Line(
            start=center,
            end=center + rotate_vector(RIGHT * 2, angle_tracker.get_value()),
            color=YELLOW,
            stroke_width=5
        ))

        # Vùng tô động theo góc
        dynamic_sector = always_redraw(lambda: Sector(
            arc_center=center,
            radius=2,
            angle=angle_tracker.get_value(),
            start_angle=0,
            color=BLUE,
            fill_opacity=0.3,
            stroke_width=0,
        ))

        self.add(dynamic_sector, rotating_line)

        # Animation: tăng góc từ 0 đến 2π
        self.play(
            angle_tracker.animate.set_value(2 * PI),
            run_time=4,
            rate_func=rush_into
        )
        
        self.wait(1)
        self.remove(dynamic_sector, rotating_line, circle, circle1_scene22, Text_7_box_scene22, Text_8_scene22, dot_scene22, circle, circle1, circle2, circle3)

        #SCENE23
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
        ViDu_37_scene23 = Tex(r"Anh cho biết anh sẽ dùng kính để làm tòa nhà, vậy diện tích kính cần sử dụng là:", font_size=35).shift(UP * 1.5)
        ViDu_38_scene23 = MathTex("\\frac{32\\pi}{27}(10\\sqrt{10} - 1) + 60\\pi\\,(m^2)", font_size=40)
        ViDu_39_scene23 = Tex(r"Anh sử dụng kính cường lực $10 mm$ Việt Nhật $480.000$ VNĐ$/m^2$, vậy số tiền cần sử dụng là:", font_size=35).shift(UP * 0.8)
        ViDu_40_scene23 = MathTex(
            "\\left[ \\frac{32\\pi}{27}(10\\sqrt{10} - 1) + 60\\pi \\right]"
            " \\times 480\\,000 \\approx 145\\,154\\,000 \\ (\\text{VNĐ})", font_size=40
        ).shift(DOWN * 0.7)


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
