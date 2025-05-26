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
            r"\iint_D",
            r" f(x, y)",
            r"\,dx\,dy",
            r" = \int_{\alpha}^{\beta} \int_{a}^{b}",
            r" f(rcos\varphi, rsin\varphi)",
            r"\cdot r\, dr\, d\varphi",
            font_size=35
        )

        self.play(Write(Text_1_scene17), run_time=2)
        self.play(Text_1_scene17.animate.move_to(UP * 2.5))
        self.wait(1)
        self.play(Write(TongRiemannCuaTichPhanKep_dai), run_time=2)
        self.play(Transform(TongRiemannCuaTichPhanKep_dai, TongRiemannCuaTichPhanKep_ngan), run_time=1)
        self.wait(1)
        self.play(Unwrite(Text_1_scene17))
        self.play(Transform(TongRiemannCuaTichPhanKep_ngan[1], fxy_scene17), TongRiemannCuaTichPhanKep_dai.animate.move_to(DOWN * 3), run_time=2)
        self.play(Create(axes1_scene17), run_time=2)
        self.play(Create(x_axes1_labels_scene17), Create(y_axes1_labels_scene17),Write(Text0_scene17))
        self.play(Create(part_scene17), run_time=2)
        self.add(outer_arc_scene17, inner_arc_scene17, left_line_scene17, right_line_scene17)
        self.play(Create(axes2_scene17), Write(Text01_scene17), run_time=2)
        self.add(part_copy_scene17)
        self.play(fxy_copy_scene17.animate.move_to(RIGHT * 3 + UP *3), part1_scene17.animate.move_to(RIGHT * 3.05 + DOWN * 0.3), x_axes1_labels_copy_scene17.animate.move_to(RIGHT * 5.1 + UP * (-1.5)), y_axes1_labels_copy_scene17.animate.move_to(RIGHT * 1.7 + UP * 2), run_time=2)
        self.wait(1)
        self.play(Transform(fxy_copy_scene17, frphi_scene17), Transform(x_axes1_labels_copy_scene17, Textphi_scene17), Transform(y_axes1_labels_copy_scene17, yaxes2_label_scene17), Transform(left_line_scene17, line_r_a_scene17), Transform(right_line_scene17, line_r_b_scene17), Transform(angle_alpha_scene17, line_alpha_scene17), Transform(angle_beta_scene17, line_beta_scene17), Transform(region_scene17, region_new_D_scene17),
                D_scene17.animate.move_to(DOWN * 0.2 + RIGHT * 2.7), Uncreate(outer_arc_scene17), Uncreate(inner_arc_scene17), Uncreate(alpha_label_old_scene17), Uncreate(beta_label_old_scene17), rb_scene17.animate.move_to(LEFT * (-0.4) +  UP * 0.8), Transform(ra_scene17, r_a_sau_scene17), Create(alpha_label_scene17), Create(beta_label_scene17),
                run_time=2)

        

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
