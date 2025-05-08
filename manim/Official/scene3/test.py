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
        x_labels = VGroup(
            Tex("a").next_to(ax.c2p(1, 0), DOWN, buff=0.4),
            Tex("b").next_to(ax.c2p(9, 0), DOWN, buff=0.3),
        )

        x_labels1 = VGroup(
            MathTex("x_{1}").next_to(ax.c2p(2, 0), DOWN, buff=0.4),
            MathTex("x_{i-1}").next_to(ax.c2p(5, 0), DOWN, buff=0.3),
            MathTex("x_{i}").next_to(ax.c2p(6, 0), DOWN, buff=0.3),
        )

        y_labels = VGroup(
            Tex("c").next_to(ax.c2p(0, 1), LEFT, buff=0.3),
            Tex("d").next_to(ax.c2p(0, 9), LEFT, buff=0.3),
        )

        y_labels1 = VGroup(
            MathTex("y_{1}").next_to(ax.c2p(0, 2), LEFT, buff=0.3),
            MathTex("y_{j-1}").next_to(ax.c2p(0, 5), LEFT, buff=0.3),
            MathTex("y_{j}").next_to(ax.c2p(0, 6), LEFT, buff=0.3),
        )

        left_bar_x = Line(UP * (-1.9), DOWN * 2.2).shift(LEFT * (3.82))
        right_bar_x = Line(UP * (-1.9), DOWN * 2.2).shift(LEFT * (2.73))

        arrow_x = DoubleArrow(
            start=LEFT * 3.75,
            end=LEFT  * 2.6,
            buff=0.05,
            stroke_width=1,
            max_tip_length_to_length_ratio=0.1  # làm đầu mũi tên nhỏ lại
        )
        arrow_x.move_to([-3.28, -2.05, 0])

        top_bar_y = Line(LEFT * 4.6, LEFT * 4.3).shift(UP * 2.45)
        bottom_bar_y = Line(LEFT * 4.6, LEFT * 4.3).shift(UP * 1.91)

        arrow_y = DoubleArrow(
            start=UP * 0.5,
            end=UP  * 1.5,
            buff=0.05,
            stroke_width=1,
            max_tip_length_to_length_ratio=0.1  # làm đầu mũi tên nhỏ lại
        )
        arrow_y.move_to([-4.45, 2, 0])


        verticalline1 = Line(start=[-3.82, -2.45, 0], end=[-3.83, 2.44, 0], color=RED, stroke_width=2)#tạo đường thẳng, số 1 tính từ trái qua
        verticalline2 = Line(start=[-2.73, -2.45, 0], end=[-2.73, 2.44, 0], color=RED, stroke_width=2)
        verticalline3 = Line(start=[-1.63, -2.45, 0], end=[-1.63, 2.44, 0], color=RED, stroke_width=2)
        verticalline4 = Line(start=[-0.54, -2.45, 0], end=[-0.54, 2.44, 0], color=RED, stroke_width=2)
        verticalline5 = Line(start=[0.55, -2.45, 0], end=[0.55, 2.44, 0], color=RED, stroke_width=2)
        verticalline6 = Line(start=[1.63, -2.45, 0], end=[1.63, 2.44, 0], color=RED, stroke_width=2)
        verticalline7 = Line(start=[2.73, -2.45, 0], end=[2.73, 2.44, 0], color=RED, stroke_width=2)
        verticalline8 = Line(start=[3.82, -2.45, 0], end=[3.82, 2.44, 0], color=RED, stroke_width=2)
        verticalline9 = Line(start=[4.91, -2.45, 0], end=[4.91, 2.44, 0], color=RED, stroke_width=2)

        horizontalline1 = Line(start=[-4.9, -1.91, 0], end=[4.91, -1.91, 0], color=RED, stroke_width=2)#tạo đường thẳng nằm ngang, số 1 tính từ dưới lên
        horizontalline2 = Line(start=[-4.9, -1.36, 0], end=[4.91, -1.36, 0], color=RED, stroke_width=2)
        horizontalline3 = Line(start=[-4.9, -0.82, 0], end=[4.91, -0.82, 0], color=RED, stroke_width=2)
        horizontalline4 = Line(start=[-4.9, -0.27, 0], end=[4.91, -0.27, 0], color=RED, stroke_width=2)
        horizontalline5 = Line(start=[-4.9, 0.27, 0], end=[4.91, 0.27, 0], color=RED, stroke_width=2)
        horizontalline6 = Line(start=[-4.9, 0.82, 0], end=[4.91, 0.82, 0], color=RED, stroke_width=2)
        horizontalline7 = Line(start=[-4.9, 1.36, 0], end=[4.91, 1.36, 0], color=RED, stroke_width=2)
        horizontalline8 = Line(start=[-4.9, 1.91, 0], end=[4.91, 1.91, 0], color=RED, stroke_width=2)
        horizontalline9 = Line(start=[-4.9, 2.45, 0], end=[4.91, 2.45, 0], color=RED, stroke_width=2)
        
        verticalline11 = Line(start=[-3.82, -1.93, 0], end=[-3.83, 2.44, 0], color=RED, stroke_width=2)#tạo đường thẳng, số 1 tính từ trái qua(ngắn hơn)
        verticalline22 = Line(start=[-2.73, -1.93, 0], end=[-2.73, 2.44, 0], color=RED, stroke_width=2)
        verticalline33 = Line(start=[-1.63, -1.93, 0], end=[-1.63, 2.44, 0], color=RED, stroke_width=2)
        verticalline44 = Line(start=[-0.54, -1.93, 0], end=[-0.54, 2.44, 0], color=RED, stroke_width=2)
        verticalline55 = Line(start=[0.55, -1.93, 0], end=[0.55, 2.44, 0], color=RED, stroke_width=2)
        verticalline66 = Line(start=[1.63, -1.93, 0], end=[1.63, 2.44, 0], color=RED, stroke_width=2)
        verticalline77 = Line(start=[2.73, -1.93, 0], end=[2.73, 2.44, 0], color=RED, stroke_width=2)
        verticalline88 = Line(start=[3.82, -1.93, 0], end=[3.82, 2.44, 0], color=RED, stroke_width=2)
        verticalline99 = Line(start=[4.91, -1.93, 0], end=[4.91, 2.44, 0], color=RED, stroke_width=2)

        horizontalline11 = Line(start=[-3.84, -1.91, 0], end=[4.91, -1.91, 0], color=RED, stroke_width=2)#tạo đường thẳng nằm ngang, số 1 tính từ dưới lên
        horizontalline22 = Line(start=[-3.84, -1.36, 0], end=[4.91, -1.36, 0], color=RED, stroke_width=2)
        horizontalline33 = Line(start=[-3.84, -0.82, 0], end=[4.91, -0.82, 0], color=RED, stroke_width=2)
        horizontalline44 = Line(start=[-3.84, -0.27, 0], end=[4.91, -0.27, 0], color=RED, stroke_width=2)
        horizontalline55 = Line(start=[-3.84, 0.27, 0], end=[4.91, 0.27, 0], color=RED, stroke_width=2)
        horizontalline66 = Line(start=[-3.84, 0.82, 0], end=[4.91, 0.82, 0], color=RED, stroke_width=2)
        horizontalline77 = Line(start=[-3.84, 1.36, 0], end=[4.91, 1.36, 0], color=RED, stroke_width=2)
        horizontalline88 = Line(start=[-3.84, 1.91, 0], end=[4.91, 1.91, 0], color=RED, stroke_width=2)
        horizontalline99 = Line(start=[-3.84, 2.45, 0], end=[4.91, 2.45, 0], color=RED, stroke_width=2)

        dot1 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)#đếm dot từ trái qua phải, từ trên xuống dưới
        dot1.move_to([-2.9, 2.2, 0])
        dot2 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot2.move_to([-2.3, 2.2, 0])
        dot3 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot3.move_to([-0.7, 2.3, 0])
        dot4 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot4.move_to([0.2, 2.25, 0])
        dot5 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot5.move_to([0.8, 2.1, 0])
        dot6 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot6.move_to([1.8, 2.2, 0])
        dot7 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot7.move_to([3.6, 2.2, 0])
        dot8 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot8.move_to([4.3, 2.1, 0])
        dot9 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot9.move_to([-3.5, 1.6, 0])
        dot10 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot10.move_to([-2.5, 1.8, 0])
        dot11 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot11.move_to([-1.5, 1.65, 0])
        dot12 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot12.move_to([-0.03, 1.5, 0])
        dot13 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot13.move_to([1.3, 1.7, 0])
        dot14 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot14.move_to([2.17, 1.6, 0])
        dot15 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot15.move_to([3.5, 1.7, 0])
        dot16 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot16.move_to([4.5, 1.6, 0])
        dot17 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot17.move_to([-3.38, 1.16, 0])
        dot18 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot18.move_to([-2.14, 1.2, 0])
        dot19 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot19.move_to([-0.8, 1.1, 0])
        dot20 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot20.move_to([0.3, 1.25, 0])
        dot21 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot21.move_to([1, 1.13, 0])
        dot22 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot22.move_to([2, 1, 0])
        dot23 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot23.move_to([3.2, 1.01, 0])
        dot24 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot24.move_to([4., 1.13, 0])
        dot25 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot25.move_to([-3.38, 0.7, 0])
        dot26 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot26.move_to([-2, 0.6, 0]) 
        dot27 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot27.move_to([-0.7, 0.7, 0])
        dot28 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot28.move_to([-0.2, 0.4, 0])

        dot29 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot29.move_to([1.08, 0.55, 0])
        
        dot30 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)   
        dot30.move_to([2, 0.4, 0])
        dot31 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot31.move_to([3.3, 0.7, 0])
        dot32 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot32.move_to([4.5, 0.4, 0])
        dot33 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot33.move_to([-3, 0, 0])
        dot34 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot34.move_to([-1.9, 0.06, 0])
        dot35 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot35.move_to([-0.9, 0, 0])
        dot36 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot36.move_to([-0.2, -0.1, 0])
        dot37 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot37.move_to([1.2, 0.16, 0])
        dot38 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot38.move_to([1.9, 0.1, 0])
        dot39 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot39.move_to([3.4, -0.1, 0])
        dot40 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot40.move_to([4.5, 0, 0])

        dot41 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot41.move_to([-3.4, -0.65, 0])
        dot42 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot42.move_to([-2.22, -0.44, 0])
        dot43 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot43.move_to([-1.16, -0.66, 0])
        dot44 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot44.move_to([0.12, -0.44, 0])
        dot45 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot45.move_to([1.15, -0.49, 0])
        dot46 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot46.move_to([2.19, -0.41, 0])
        dot47 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot47.move_to([3.16, -0.39, 0])
        dot48 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot48.move_to([4.42, -0.65, 0])
        dot49 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot49.move_to([-3.21, -1.19, 0])
        dot50 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot50.move_to([-2, -1.23, 0])
        dot51 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot51.move_to([-1.2, -1.2, 0])
        dot52 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot52.move_to([-0.1, -1, 0])
        dot53 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot53.move_to([1.5, -1.2, 0])
        dot54 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot54.move_to([2.2, -1.17, 0])
        dot55 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot55.move_to([3.3, -1.07, 0])
        dot56 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot56.move_to([4.29, -1.13, 0])

        dot57 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot57.move_to([-3.2, -1.6, 0])
        dot58 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot58.move_to([-2.3, -1.5, 0])
        dot59 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot59.move_to([-1.03, -1.55, 0])
        dot60 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot60.move_to([-0.09, -1.69, 0])
        dot61 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot61.move_to([1.13, -1.55, 0])
        dot62 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot62.move_to([2.23, -1.5, 0])
        dot63 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot63.move_to([3.35, -1.49, 0])
        dot64 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot64.move_to([4.29, -1.6, 0])

        dot65 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot65.move_to([-3.28, -2.2, 0])
        dot66 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot66.move_to([-2.19, -2.2, 0])
        dot67 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot67.move_to([-1.1, -2.2, 0])
        dot68 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot68.move_to([-0.07, -2.26, 0])
        dot69 = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        dot69.move_to([1.23, -2.34, 0])

        rect = Rectangle(
            width=1.1, 
            height=0.5,
            fill_color=BLUE,
            fill_opacity=0.5,  # Độ trong suốt phần tô màu
            stroke_opacity=1.0  # Độ trong suốt đường viền (1.0 = không trong suốt)
        )
        rect.shift(RIGHT*(1.1) + UP*0.55)#hình chữ nhật nằm ngang màu xanh lấy từ miền D ra 
        rect1 = Rectangle(
            width=1.1, 
            height=0.5,
            fill_color=BLUE,
            fill_opacity=0.5,  # Độ trong suốt phần tô màu
            stroke_opacity=1.0  # Độ trong suốt đường viền (1.0 = không trong suốt)
        )
        rect1.shift(RIGHT*(1.1) + UP*0.55)
        dotxiyi = Circle(radius=0.01, color=BLUE, fill_opacity=1)
        dotxiyi.move_to([1.65, 0.8, 0])
        dotxiyi1 = Circle(radius=0.1, color=BLUE, fill_opacity=1)
        dotxiyi1.move_to([1.65, 0.8, 0])

        tex1 = MathTex(r"D_{ij}", color=WHITE)
        tex1.scale(0.8)
        tex1.move_to([-1, 3, 0])

        text2 = MathTex(r"(x_{i}, y_{j})", color=WHITE)
        text2.scale(0.8)
        text2.move_to([1.6, 3, 0])

        text3 = MathTex(r"(x_{ij}*, y_{ij}*)", color=WHITE)    
        text3.scale(0.8)
        text3.move_to([4, 3, 0])

        text11 = MathTex(r"\Delta x = \frac{b-a}{m}", color=BLUE) 
        text11.scale(0.8)
        text11.move_to([-3.2, -1.2, 0])

        text22 = MathTex(r"\Delta y = \frac{d-c}{n}", color=BLUE)
        text22.scale(0.8)
        text22.move_to([-2.8, 2.2, 0])
        
        self.play(Create(ax), run_time=2)
        self.play(Create(labels), run_time=1)
        self.play(Create(left_bar_x), Create(right_bar_x), Create(arrow_x), run_time=1)
        self.play(FadeIn(text11), run_time=1)
        self.wait(0.5)
        self.play(Create(top_bar_y), Create(bottom_bar_y), Create(arrow_y), run_time=1)
        self.play(FadeIn(text22), run_time=1)
        self.wait(0.5)
        self.play(Uncreate(left_bar_x), Uncreate(right_bar_x), Uncreate(arrow_x), Uncreate(text11),Uncreate(top_bar_y), Uncreate(bottom_bar_y), Uncreate(arrow_y), Uncreate(text22), run_time=1)
        self.wait(0.5)

        self.play(Create(x_labels), Create(y_labels), run_time=1)
        self.wait(0.5)
        self.play(Create(x_labels1), run_time=1)
        self.play(Create(verticalline1), Create(verticalline2), Create(verticalline3), Create(verticalline4), Create(verticalline5), Create(verticalline6), Create(verticalline7), Create(verticalline8), Create(verticalline9),run_time=2)
        self.wait(0.5)
        self.play(Create(y_labels1), run_time=1)
        self.play(Create(horizontalline1), Create(horizontalline2), Create(horizontalline3), Create(horizontalline4), Create(horizontalline5), Create(horizontalline6), Create(horizontalline7), Create(horizontalline8), Create(horizontalline9), run_time=2)
        self.play(Create(verticalline11), Create(verticalline22), Create(verticalline33), Create(verticalline44), Create(verticalline55), Create(verticalline66), Create(verticalline77), Create(verticalline88), Create(verticalline99),run_time=0.5)
        self.play(Create(horizontalline11), Create(horizontalline22), Create(horizontalline33), Create(horizontalline44), Create(horizontalline55), Create(horizontalline66), Create(horizontalline77), Create(horizontalline88), Create(horizontalline99), run_time=0.5)
        self.play(Uncreate(verticalline1), Uncreate(verticalline2), Uncreate(verticalline3), Uncreate(verticalline4), Uncreate(verticalline5), Uncreate(verticalline6), Uncreate(verticalline7), Uncreate(verticalline8), Uncreate(verticalline9), 
                  Uncreate(horizontalline1), Uncreate(horizontalline2), Uncreate(horizontalline3), Uncreate(horizontalline4), Uncreate(horizontalline5), Uncreate(horizontalline6), Uncreate(horizontalline7), Uncreate(horizontalline8), Uncreate(horizontalline9),
                  run_time=0.5)
        self.wait(0.5)
        self.play(Create(dot1), run_time=0.2)
        self.play(Create(dot2), Create(dot9), run_time=0.2)
        self.play(Create(dot3), Create(dot10), Create(dot17), run_time=0.2)
        self.play(Create(dot4), Create(dot11), Create(dot18), Create(dot25), run_time=0.2)           
        self.play(Create(dot5), Create(dot12), Create(dot19), Create(dot26), Create(dot33), run_time=0.2)
        self.play(Create(dot6), Create(dot13), Create(dot20), Create(dot27), Create(dot34), Create(dot41), run_time=0.2)
        self.play(Create(dot7), Create(dot14), Create(dot21), Create(dot28), Create(dot35), Create(dot42), Create(dot49), run_time=0.2)       
        self.play(Create(dot8), Create(dot15), Create(dot22), Create(dot29), Create(dot36), Create(dot43), Create(dot50), Create(dot57), run_time=0.2)
        self.play(Create(dot9), Create(dot16), Create(dot23), Create(dot30), Create(dot37), Create(dot44), Create(dot51), Create(dot58), run_time=0.2)
        self.play(Create(dot24), Create(dot31), Create(dot38), Create(dot45), Create(dot52), Create(dot59), run_time=0.2)
        self.play(Create(dot32), Create(dot39), Create(dot46), Create(dot53), Create(dot60), run_time=0.2)
        self.play(Create(dot40), Create(dot47), Create(dot54), Create(dot61), run_time=0.2)
        self.play(Create(dot48), Create(dot55), Create(dot62), run_time=0.2)
        self.play(Create(dot56), Create(dot63), run_time=0.2)
        self.play(Create(dot64), run_time=0.2)
        self.play(Create(rect), Create(rect1), Create(dotxiyi), run_time=2)
        self.wait(0.5)
        self.play(rect.animate.move_to(UP*3), run_time=2)
        self.play(FadeIn(tex1), run_time=2)
        self.wait(0.5)
        self.play(Transform(dotxiyi, dotxiyi1), run_time=2)
        self.play(dotxiyi1.animate.move_to(UP*3 + RIGHT*2.5), run_time=2)
        self.play(FadeIn(text2), run_time=2)
        self.wait(0.5)
        self.play(dot29.animate.move_to(UP*3 + RIGHT*5.2), run_time=2)
        self.play(FadeIn(text3), run_time=2)
        self.wait(0.5)


        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))