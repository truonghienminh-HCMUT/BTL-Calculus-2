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
        ).shift(LEFT * 3.5 + DOWN * 1)
        
        axes2 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": RED}
        ).shift(RIGHT * 3.5 + DOWN * 1)

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
        
        text = Tex(
            r"Giả sử ta tính tích phân ",#0
            r"$\iint_D f(x, y)\,dxdy$",  #1
            r".",#2
            r" Trong trường hợp",#3
            r" miền $D$",#4
            r" là",#5
            r" hình tròn",#6
            r" hoặc",#7
            r" vành khăn",#8
            r", việc mô tả",#9
            r" miền $D$", #10
            r" trong hệ trục tọa độ",#11
            r" Descartes",#12
            r" khá phức tạp ",#13
            r"nhưng mô tả trong ",#14
            r" hệ tọa độ cực",#15
            r" thì sẽ dễ dàng hơn.",#16
            font_size=36
        ).shift(UP * 3)

        text_6_copy = text[6].copy()
        text_8_copy = text[8].copy()

        # Đổi màu các phần mong muốn
        text[1].set_color(YELLOW)  # Đổi màu công thức tích phân
        text[4].set_color(YELLOW)    # Đổi màu chữ D
        text[10].set_color(YELLOW)
        text[12].set_color(BLUE)
        text[15].set_color(BLUE)  # Đổi màu chữ D

        text_cuoi = VGroup(text[9], text[10], text[11], text[12], text[13], text[14], text[15], text[16])


        circle = ParametricFunction(
            lambda t: axes1.coords_to_point(np.cos(t), np.sin(t)),
            t_range=[0, 2*PI],
            color=[BLUE_E, TEAL_B, GREEN],
            fill_color=[BLUE_E, TEAL_B, GREEN],     # Màu tô bên trong
            fill_opacity=0.5,   # Độ trong suốt (0-1)
            stroke_width=4
        )
        equation = MathTex("x^2 + y^2 = 1").to_edge(UP * 5.6,  buff=0.5).scale(0.8)
        equation.shift(RIGHT * (-1.8) + DOWN * 1)

        half_circle = Annulus(
            inner_radius=0.83,
            outer_radius=1.69,
            fill_opacity=0.8,
            stroke_width=0
        ).set_color([BLUE_E, TEAL_B, GREEN]).move_to(axes2.c2p(0, 0))
        half_circle_equation1 = MathTex("x^2 + y^2 = 4").to_edge(UP * 4,  buff=0.5).scale(0.8)
        half_circle_equation1.shift(RIGHT * (5.3) + DOWN * 1)
        half_circle_equation2 = MathTex("x^2 + y^2 = 1").to_edge(UP * (0),  buff=0.5).scale(0.5)
        half_circle_equation2.shift(RIGHT * (3.6) + DOWN * 0.7)


        # Hiển thị tất cả cùng lúc
        self.play(Write(text[0]), run_time=2)
        self.play(FadeIn(text[1]), Write(text[2]), run_time=1)
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
        self.play(Write(text[3]), Write(text[4]), Write(text[5]), Write(text[6]), run_time=2)
        self.wait(0.5)
        self.play(Write(text_6_copy), Transform(text[6], circle), Write(equation), run_time=2)
        self.wait(0.5)
        self.play(Write(text[7]), Write(text[8]), run_time=2)
        self.play(Write(text_8_copy), Transform(text[8],half_circle), Write(half_circle_equation1), Write(half_circle_equation2), run_time=2)
        self.play(Write(text_cuoi),  run_time=2)
        self.wait(0.5)

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
