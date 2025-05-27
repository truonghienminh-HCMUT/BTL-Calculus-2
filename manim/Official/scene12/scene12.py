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

class SCENE12(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        
        #SCENE12
        #TRỤC TỌA ĐỘ BÊN TRÁI
        axes1_scene12 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": BLUE}
        ).shift(LEFT * 3.5 + DOWN * 1)
        
        #TRỤC TỌA ĐỘ BÊN PHẢI
        axes2_scene12 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": RED}
        ).shift(RIGHT * 3.5 + DOWN * 1)

        # Thêm nhãn trục X và Y cho hệ trục 1
        axes1_labels_scene12 = axes1_scene12.get_axis_labels(
            Tex("$x$").scale(0.8),  # Nhãn trục x
            Tex("$y$").scale(0.8)   # Nhãn trục y
        )
        
        # Thêm nhãn trục X và Y cho hệ trục 2
        axes2_labels_scene12 = axes2_scene12.get_axis_labels(
            Tex("$x$").scale(0.8),  # Nhãn trục x
            Tex("$y$").scale(0.8)   # Nhãn trục y
        )
        
        #LÝ THUYẾT 
        text_scene12 = Tex(
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

        text_scene12[0].shift(DOWN * 3)
        text_scene12[1].shift(DOWN * 3)

        text_6_copy_scene12 = text_scene12[6].copy()
        text_8_copy_scene12 = text_scene12[8].copy()

        #ĐỔI MÀU CÁC PHẦN MONG MUỐN
        text_scene12[1].set_color(YELLOW)  # Đổi màu công thức tích phân
        text_scene12[4].set_color(YELLOW)    # Đổi màu chữ D
        text_scene12[10].set_color(YELLOW)
        text_scene12[12].set_color(BLUE)
        text_scene12[15].set_color(BLUE)  # Đổi màu chữ D

        text_cuoi_scene12 = VGroup(text_scene12[9], text_scene12[10], text_scene12[11], text_scene12[12], text_scene12[13], text_scene12[14], text_scene12[15], text_scene12[16])

        #HÌNH TRÒN TRỤC 1
        circle_scene12 = ParametricFunction(
            lambda t: axes1_scene12.coords_to_point(np.cos(t), np.sin(t)),
            t_range=[0, 2*PI],
            color=[BLUE_E, TEAL_B, GREEN],
            fill_color=[BLUE_E, TEAL_B, GREEN],     # Màu tô bên trong
            fill_opacity=0.5,   # Độ trong suốt (0-1)
            stroke_width=4
        )
        equation_scene12 = MathTex("x^2 + y^2 = 1").to_edge(UP * 5.6,  buff=0.5).scale(0.8)
        equation_scene12.shift(RIGHT * (-1.8) + DOWN * 1)
        
        #HÌNH VÀNH KHĂN TRỤC 2
        half_circle_scene12 = Annulus(
            inner_radius=0.83,
            outer_radius=1.69,
            fill_opacity=0.8,
            stroke_width=0
        ).set_color([BLUE_E, TEAL_B, GREEN]).move_to(axes2_scene12.c2p(0, 0))
        half_circle_equation1_scene12 = MathTex("x^2 + y^2 = 4").to_edge(UP * 4,  buff=0.5).scale(0.8)
        half_circle_equation1_scene12.shift(RIGHT * (5.3) + DOWN * 1)
        half_circle_equation2_scene12 = MathTex("x^2 + y^2 = 1").to_edge(UP * (0),  buff=0.5).scale(0.5)
        half_circle_equation2_scene12.shift(RIGHT * (3.6) + DOWN * 0.7)


        #CHẠY SCENE12
        self.play(Write(text_scene12[0]), Write(text_scene12[1]), run_time=2)
        self.play(Write(text_scene12[2]), run_time=0.5)
        self.play(text_scene12[0].animate.shift(UP * 3), text_scene12[1].animate.shift(UP * 3), run_time=1)
        self.play(
            LaggedStart(
                Create(axes1_scene12),
                Create(axes2_scene12),
                lag_ratio=0.5
            ),
            run_time=2
        )
        self.play(
            Write(axes1_labels_scene12),
            Write(axes2_labels_scene12)
        )
        self.wait(0.5)
        self.play(Write(text_scene12[3]), Write(text_scene12[4]), Write(text_scene12[5]), Write(text_scene12[6]), run_time=1.5)
        self.wait(0.5)
        self.play(Write(text_6_copy_scene12), Transform(text_scene12[6], circle_scene12), Write(equation_scene12), run_time=1)
        self.play(Write(text_scene12[7]), Write(text_scene12[8]), run_time=2)
        self.play(Write(text_8_copy_scene12), Transform(text_scene12[8], half_circle_scene12), Write(half_circle_equation1_scene12), Write(half_circle_equation2_scene12), run_time=1)
        self.play(Write(text_cuoi_scene12),  run_time=2.5)
        self.wait(0.5)
        self.remove(text_6_copy_scene12, text_8_copy_scene12, text_scene12, text_cuoi_scene12, 
                axes1_labels_scene12, axes2_labels_scene12, axes1_scene12, axes2_scene12, 
                equation_scene12, half_circle_equation1_scene12, half_circle_equation2_scene12, text_scene12[0], text_scene12[1], text_scene12[2], text_scene12[7], text_scene12[8], text_scene12[6],
                text_scene12[3], text_scene12[4], text_scene12[5])

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
