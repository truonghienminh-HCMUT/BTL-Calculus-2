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

class SCENE14_16(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
         
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
        
        

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
