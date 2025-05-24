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

        self.play(Create(axes1),  run_time=2)
        self.play(Create(x_axes1_labels), Create(y_axes1_labels),Write(Text0))
        self.play(Create(part), run_time=2)
        self.add(outer_arc, inner_arc, left_line, right_line)
        self.play(Create(axes2), Write(Text01), run_time=2)
        self.add(part_copy)
        self.play(part1.animate.move_to(RIGHT * 3.05 + DOWN * 0.3), x_axes1_labels_copy.animate.move_to(RIGHT * 5.1 + UP * (-1.5)), y_axes1_labels_copy.animate.move_to(RIGHT * 1.7 + UP * 2), run_time=2)
        self.wait(1)
        self.play(Uncreate(region), Uncreate(angle_alpha), Uncreate(angle_beta), Uncreate(alpha_label_old), Uncreate(beta_label_old), Uncreate(ra), Uncreate(rb), Uncreate(D))
        self.play(Create(line_1), Create(line_2), Create(line_3), run_time=2)
        self.play(Create(big_arc), Create(small_arc), run_time=2)
        


        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
