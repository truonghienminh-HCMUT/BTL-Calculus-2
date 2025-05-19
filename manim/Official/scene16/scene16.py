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

        axes1_labels = axes1.get_axis_labels(x_label="x", y_label="y")
        axes2_labels = axes2.get_axis_labels(x_label="x", y_label="y")
        Text0 = Tex("O").to_edge(UP * 7,  buff=0.5).scale(1)
        Text0.shift((DOWN * 2.5), LEFT * 5.2)
        Text01 = Tex("O").to_edge(UP * 7,  buff=0.5).scale(1)
        Text01.shift((DOWN * 2.5), RIGHT * 0.9)
        rb = Tex("r = b").scale(1).next_to(axes1.c2p(a, 0), UP)
        rb.move_to([-1.6, 0.8, 0])
        ra = Tex("r = a").scale(0.7).next_to(axes2.c2p(b, 0), UP)
        ra.move_to([-3.9, -1, 0])

        outer_arc = Arc(radius=b, start_angle=alpha, angle=beta - alpha, arc_center=origin)
        inner_arc = Arc(radius=a, start_angle=beta, angle=-(beta - alpha), arc_center=origin)

        # Tính điểm đầu dựa trên góc alpha
        left_point = origin + b * np.array([np.cos(alpha), np.sin(alpha), 0])
        right_point = origin + b * np.array([np.cos(beta), np.sin(beta), 0])

        # Tạo các đoạn thẳng từ origin
        left_line = Line(origin, left_point)
        right_line = Line(origin, right_point)

        outer_points = [b * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(alpha, beta, 30)]
        inner_points = [a * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(beta, alpha, 30)]

        region_points = outer_points + inner_points
        region = VMobject()
        region.set_points_as_corners(region_points)
        region.set_fill(RED, opacity=0.5)
        region.set_stroke(BLUE)

        # Tạo vùng D tô màu
        region = VGroup(outer_arc, right_line, inner_arc, left_line).set_fill(RED, opacity=0.5).set_stroke(BLUE)

        x_axis_point = axes1.c2p(1, 0)
        x_axis_line_1 = Line(origin, x_axis_point, color=RED)
        angle = Angle(
            x_axis_line_1, left_line,
            radius=0.9,
            color=BLUE,
            quadrant=(1,-1),  # Chọn phần tư
            other_angle=False,  # Vẽ góc lớn hơn 180°
            fill_opacity=0.5   # Độ trong suốt
        )

        part = VGroup(outer_arc, inner_arc, left_line, right_line, region, x_axis_line_1, angle)
        part.shift(LEFT * 0)
        self.play(Create(axes1), Create(axes2))
        self.play(Create(axes1_labels), Create(axes2_labels), 
                  Write(Text0), Write(Text01))
        self.play(Create(part), run_time=2)
        self.play(Write(rb), Write(ra), run_time=1)

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
