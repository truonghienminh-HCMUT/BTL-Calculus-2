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
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": BLUE}
        ).shift(LEFT * 3.5)
        
        axes2 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": RED}
        ).shift(RIGHT * 3.5)

        # Thêm nhãn trục X và Y cho hệ trục 1
        axes1_labels = axes1.get_axis_labels(
            Tex("$x$").scale(0.8),  # Nhãn trục x
            Tex("$y$").scale(0.8)   # Nhãn trục y
        )
        
        # Thêm nhãn trục X và Y cho hệ trục 2
        axes2_labels = axes2.get_axis_labels(
            Tex("$x$").scale(0.8),  # Nhãn trục x
            Tex("$y$").scale(0.8)   # Nhãn trục y
        )

        circle = ParametricFunction(
            lambda t: axes1.coords_to_point(np.cos(t), np.sin(t)),
            t_range=[0, 2*PI],
            color=[BLUE_E, TEAL_B, GREEN],
            fill_color=[BLUE_E, TEAL_B, GREEN],     # Màu tô bên trong
            fill_opacity=0.5,   # Độ trong suốt (0-1)
            stroke_width=4
        )
        equation = MathTex("x^2 + y^2 = 1").to_edge(UP * 5.6,  buff=0.5).scale(0.8)
        equation.shift(RIGHT * (-1.8))

        half_circle = Annulus(
            inner_radius=0.83,
            outer_radius=1.69,
            fill_opacity=0.8,
            stroke_width=0
        ).set_color([BLUE_E, TEAL_B, GREEN]).move_to(axes2.c2p(0, 0))
        half_circle_equation1 = MathTex("x^2 + y^2 = 4").to_edge(UP * 4,  buff=0.5).scale(0.8)
        half_circle_equation1.shift(RIGHT * (5.3))
        half_circle_equation2 = MathTex("x^2 + y^2 = 1").to_edge(UP * (0),  buff=0.5).scale(0.5)
        half_circle_equation2.shift(RIGHT * (3.6))

        # Hiển thị tất cả cùng lúc
        self.play(
            LaggedStart(
                Create(axes1),
                Create(axes2),
                lag_ratio=0.5
            ),
            run_time=2
        )
        self.play(
            Write(axes1_labels),
            Write(axes2_labels)
        )
        self.wait(0.5)
        self.play(Create(circle), Write(equation))
        self.wait(0.5)
        self.play(Create(half_circle), Write(half_circle_equation1), Write(half_circle_equation2))
        self.wait(0.5)

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
