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

        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], 
                y_range=[-1, 10],
                 x_axis_config={"include_numbers": False},  # Tắt số mặc định
                 y_axis_config={"include_numbers": False})#tạo trục tọa độ
        labels = ax.get_axis_labels(
            x_label=Tex(r"$x$"), y_label=Tex(r"$y$")#tạo nhãn cho các trục
        )
        TextO = Tex(r"$O$", color=WHITE).move_to(ax.c2p(0, 0))
        TextO.move_to(LEFT * 5.4 + DOWN * 2.8)

        a = 9  # bán kính trong
        b = 10    # bán kính ngoài
        alpha = 0.3  # góc alpha (rad)
        beta = 0.5   # góc beta (rad)
        origin = ax.c2p(0, 0)

        outer_arc = Arc(radius=b, start_angle=alpha, angle=beta - alpha, arc_center=origin)
        inner_arc = Arc(radius=a, start_angle=beta, angle=-(beta - alpha), arc_center=origin)

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

        part = VGroup(outer_arc, inner_arc, left_line, right_line, region)
        self.play(Create(ax), run_time=2)
        self.play(Create(labels), Create(TextO), run_time=1)
        self.play(Create(part), run_time=2)


        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))