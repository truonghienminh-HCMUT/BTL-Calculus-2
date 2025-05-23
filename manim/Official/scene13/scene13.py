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

        color_00ffff = "#00ffff"
        color_7cfc00 = "#cc00ff"


        Text1 = Tex("Tọa độ Descartes").to_edge(UP * 7,  buff=0.5).scale(1)
        Text1.shift((UP * 3), LEFT * 3)
        Text1.shift(LEFT * 2)
        Text2 = Tex("Tọa độ cực").to_edge(UP * 7,  buff=0.5).scale(1)
        Text2.shift((UP * 3), RIGHT * 3)
        Text2.shift(LEFT * 3)
        Text1.set_color_by_gradient(color_00ffff, color_7cfc00)
        Text2.set_color_by_gradient(RED, ORANGE, YELLOW)
        axes = Axes(
            x_range=[-5, 5, 1],  # [min, max, step]
            y_range=[-5, 5, 1],
            x_length=7.3,  # Giảm chiều dài trục x
            y_length=7.3,
            axis_config={"color": WHITE},
        ).shift(LEFT * 2.5)

        axes1 = Axes(
            x_range=[-5, 5, 1],  # [min, max, step]
            y_range=[-5, 5, 1],
            x_length=7.3,  # Giảm chiều dài trục x
            y_length=7.3,
            axis_config={"color": WHITE},
        ).shift(LEFT * 2.5)
        
        x_numbers = axes.get_x_axis().add_numbers(font_size=24)
        y_numbers = axes.get_y_axis().add_numbers(font_size=24)

        # Thêm nhãn cho các trục
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        dashed_line_x = DashedLine(start=LEFT*3, end=RIGHT*3, dash_length=0.2)
        dashed_line_x = DashedLine(start=[2.197,1.46,0], end=[0,1.46,0])
        dashed_line_x.set_color(RED)
        dashed_line_x.shift(LEFT * 2.5)

        dashed_line_x1 = DashedLine(start=LEFT*3, end=RIGHT*3, dash_length=0.2)
        dashed_line_x1 = DashedLine(start=[1.46,1.46,0], end=[0,1.46,0])
        dashed_line_x1.set_color(RED)

        dashed_line_y = DashedLine(start=LEFT*3, end=RIGHT*3, dash_length=0.2)
        dashed_line_y = DashedLine(start=[2.197,1.46,0], end=[2.197,-0,0])
        dashed_line_y.set_color(RED)
        dashed_line_y.shift(LEFT * 2.5)

        dashed_line_y1 = DashedLine(start=LEFT*3, end=RIGHT*3, dash_length=0.2)
        dashed_line_y1 = DashedLine(start=[1.46,1.46,0], end=[1.46,-0,0])
        dashed_line_y1.set_color(RED)

        pi4 = Line(start=[0, 0, 0], end=[2.08, 2.08, 0], color=WHITE, stroke_width=5).shift(LEFT * 2.5)
        pi34 = Line(start=[0, 0, 0], end=[-2.08, 2.08, 0], color=WHITE, stroke_width=5).shift(LEFT * 2.5)
        pi54 = Line(start=[0, 0, 0], end=[-2.08, -2.08, 0], color=WHITE, stroke_width=5).shift(LEFT * 2.5)
        pi74 = Line(start=[0, 0, 0], end=[2.08, -2.08, 0], color=WHITE, stroke_width=5).shift(LEFT * 2.5)

        textpi4 = MathTex(r"\frac{\pi}{4}").scale(0.7).set_color_by_gradient(WHITE)
        textpi4.move_to([2.35, 2.35, 0]).shift(LEFT * 2.5)
        textpi34 = MathTex(r"\frac{3\pi}{4}").scale(0.7).set_color_by_gradient(WHITE)
        textpi34.move_to([-2.35, 2.35, 0]).shift(LEFT * 2.5)
        textpi54 = MathTex(r"\frac{5\pi}{4}").scale(0.7).set_color_by_gradient(WHITE)
        textpi54.move_to([-2.35, -2.35, 0]).shift(LEFT * 2.5)
        textpi74 = MathTex(r"\frac{7\pi}{4}").scale(0.7).set_color_by_gradient(WHITE)
        textpi74.move_to([2.35, -2.35, 0]).shift(LEFT * 2.5)
        textpi2 = MathTex(r"\frac{\pi}{2}").scale(0.7).set_color_by_gradient(WHITE)
        textpi2.move_to([-0.5, 3.3, 0]).shift(LEFT * 2.5)
        textpi = MathTex(r"\pi").scale(0.7).set_color_by_gradient(WHITE)
        textpi.move_to([-3.17, 0.3, 0]).shift(LEFT * 2.5)
        textpi32 = MathTex(r"\frac{3\pi}{2}").scale(0.7).set_color_by_gradient(WHITE)
        textpi32.move_to([-0.5, -3.3, 0]).shift(LEFT * 2.5)
        text0 = MathTex(r"0").scale(0.7).set_color_by_gradient(WHITE)
        text0.move_to([3.17, 0.3, 0]).shift(LEFT * 2.5)
        x_1 = MathTex(r"x_1").scale(0.7).set_color_by_gradient(YELLOW)
        x_1.move_to(axes.c2p(3, 0)).shift(DOWN * 0.5)
        y_1 = MathTex(r"y_1").scale(0.7).set_color_by_gradient(YELLOW)
        y_1.move_to(axes.c2p(0, 2)).shift(LEFT * 0.5)




        x_line = Line(start=[0, 0, 0], end=[5, 0, 0], color=RED, stroke_width=5)


        #toado = Tex("(3, 2)").scale(0.6).set_color_by_gradient(YELLOW)
        #toado.move_to([2.197, 1.06, 0])
        #toado.shift(DOWN * (-0.5))

        dot = Circle(radius=0.1, color=RED, fill_opacity=1)
        dot.move_to([2.197, 1.46, 0]).shift(LEFT * 2.5)
        dot1 = Circle(radius=0.1, color=RED, fill_opacity=1)
        dot1.move_to([1.96, 1, 0])
        dot1.shift(LEFT * 2.5)

        Px1y1 = MathTex(r"P(x_1, y_1)").scale(0.7).set_color_by_gradient(YELLOW)
        Px1y1.move_to([2.5, 1.9, 0])
        Px1y1.shift(LEFT * 2.5)
        Px1y1_copy = Px1y1.copy()
        Px1y1_copy.shift(LEFT * 1)

        line1 = Line(start=[2.197, 1.46, 0], end=[0, 0, 0], color=YELLOW, stroke_width=5).shift(LEFT * 2.5)
        line11 = Line(start=[1.96, 1, 0], end=[0, 0, 0], color=YELLOW, stroke_width=5).shift(LEFT * 2.5)
        line2 = Line(start=[2.197, 0, 0], end=[0, 0, 0], color=YELLOW, stroke_width=5).shift(LEFT * 2.5)
        r = Tex(r"r").scale(0.7).set_color_by_gradient(YELLOW)
        r.move_to([1.2, 1.2, 0])
        r.shift(LEFT * 2.5)
        r1 = r.copy()
        r2 = r.copy()

        dotxoay = Dot(line2.get_start(), color=RED)  # Đánh dấu điểm cần xoay
        
        # Nhóm đường thẳng và dấu chấm để cùng di chuyển
        moving_part = VGroup(line2.copy(), dot)


        angle = Angle(
            x_line, line1,
            radius=0.9,
            color=BLUE,
            quadrant=(1,-1),  # Chọn phần tư
            other_angle=False,  # Vẽ góc lớn hơn 180°
            fill_opacity=0.5   # Độ trong suốt
        )
           
        angle_label = MathTex(r"\theta").scale(0.7).set_color_by_gradient(BLUE)
        angle_label.move_to([1.2, 0.3, 0])
        angle_label.shift(LEFT * 2.5)
        angle_label1 = angle_label.copy()
        angle_label2 = angle_label.copy()
        angle1 = Angle(
            x_line, line11,
            radius=0.9,
            color=BLUE,
            quadrant=(1,-1),  # Chọn phần tư
            other_angle=False,  # Vẽ góc lớn hơn 180°
            fill_opacity=0.5   # Độ trong suốt
        )

        sin = MathTex(r"\sin").scale(0.7).set_color_by_gradient(RED)
        sin.move_to([2.8, 0.73, 0])
        sin.shift(LEFT * 2.5)
        cos = MathTex(r"\cos").scale(0.7).set_color_by_gradient(RED)
        cos.move_to([1.12, -0.3, 0])
        cos.shift(LEFT * 2.5)

        circle1 = Circle(radius=0.74, color=WHITE).shift(LEFT * 2.5)
        circle2 = Circle(radius=1.47, color=WHITE).shift(LEFT * 2.5)
        circle3 = Circle(radius=2.2, color=WHITE).shift(LEFT * 2.5)
        circle4 = Circle(radius=2.93, color=WHITE).shift(LEFT * 2.5)

        Text_1_scene13 = Tex(
            r"Trong bài toán tích phân kép thông thường,",#0
            r" ta thường sử dụng",#1
            r" tọa độ",#2
            r" Descartes",#3
            r" để xử lí",#4
            r" và tính toán.",#5
            font_size=30
        )

        Text_1_scene13[2].set_color(color_00ffff)
        Text_1_scene13[3].set_color(color_00ffff)


        Text_1_scene13[0].shift(RIGHT * 5.6 + UP * 2)
        Text_1_scene13[1].shift(LEFT * 0.5 + UP * 1.6)
        Text_1_scene13[2].shift(RIGHT * -0.5 + UP * 1.6)
        Text_1_scene13[3].shift(RIGHT * 6.5 + UP * 1.97)
        Text_1_scene13[4].shift(RIGHT * 6.5 + UP * 1.97)
        Text_1_scene13[5].shift(RIGHT * 2.5 + UP * 1.6)

        Text_2_scene13 = Tex(
            r"Thế nhưng do đặc thù của bài toán tính",#0
            r" tích phân kép của",#1
            r" tọa độ cực,",#2
            r" ta sẽ",#3
            r" chuyển từ",#4
            r" tọa độ Descartes",#5
            r" sang",#6
            r" tọa độ cực",#7
            r" để dễ dàng tính toán.",#8
            font_size=30
        )

        Text_2_scene13[2].set_color(RED)
        Text_2_scene13[5].set_color(color_00ffff)
        Text_2_scene13[7].set_color(RED)

        Text_2_scene13[0].shift(RIGHT * 6.5 + UP * 2)
        Text_2_scene13[1].shift(RIGHT * 1.2 + UP * 1.62)
        Text_2_scene13[2].shift(RIGHT * 1.2 + UP * 1.62)
        Text_2_scene13[3].shift(RIGHT * 1.2 + UP * 1.62)
        Text_2_scene13[4].shift(RIGHT * 6.2 + UP * 1.58)
        Text_2_scene13[5].shift(RIGHT * 6.2 + UP * 1.58)
        Text_2_scene13[6].shift(RIGHT * 6.2 + UP * 1.58)
        Text_2_scene13[7].shift(RIGHT * 1.7 + UP * 1.18)
        Text_2_scene13[8].shift(RIGHT * 1.7 + UP * 1.18)

        Text_3_scene13 = Tex(
            r"Hệ toạ độ cực",#0
            r" $(r,\varphi)$",#1
            r" xác định một điểm",#2
            r" có toạ độ",#3
            r" $P(x_1, y_1)$",#4
            r"như",#5
            r" sau:",#6
            r"$r^2=x^2+y^2$",
            font_size=30
        )

        Text_3_scene13[1].set_color(YELLOW)
        Text_3_scene13[4].set_color(YELLOW)


        Text_3_scene13[0].shift(RIGHT * 4.5 + UP * 2)
        Text_3_scene13[1].shift(RIGHT * 4.5 + UP * 2)
        Text_3_scene13[2].shift(RIGHT * 4.5 + UP * 2)
        Text_3_scene13[3].shift(RIGHT * 4.5 + UP * 2)
        Text_3_scene13[4].shift(RIGHT * -0.3 + UP * 1.64)
        Text_3_scene13[5].shift(RIGHT * -0.25 + UP * 1.64)
        Text_3_scene13[6].shift(RIGHT * 5.3 + UP * 2.02)

        Text_4_scene13 = MathTex(r"r^2=x_1^2+y_1^2").scale(1)
        Text_4_scene13.shift(RIGHT * 3.5 + UP * 1)
        Text_4_scene13.set_color(BLUE)
        Text_5_scene13 = MathTex(r"x_1=rcos\varphi").scale(1)
        Text_5_scene13.shift(RIGHT * 3.5 + UP * 0.4)
        Text_5_scene13.set_color(BLUE)
        Text_6_scene13 = MathTex(r"y_1=rsin\varphi").scale(1)
        Text_6_scene13.shift(RIGHT * 3.5 + UP * -0.1)
        Text_6_scene13.set_color(BLUE)
        Text_7_scene13 = MathTex(r"tan\varphi =\frac{y_1}{x_1}")
        Text_7_scene13.shift(RIGHT * 3.5 + UP * -0.9)
        Text_7_scene13.set_color(BLUE)
        
        self.play(Write(Text_1_scene13[0]), Write(Text_1_scene13[1]), run_time=2)
        self.play(Write(Text_1_scene13[2]), Write(Text_1_scene13[3]), Write(Text1), run_time=2)
        self.play(Write(Text_1_scene13[4]), Write(Text_1_scene13[5]))
        self.wait(1)
        self.play(Create(axes), Write(axes_labels))
        self.wait(1)
        self.play(Create(dot))
        #self.play(Create(toado))
        self.play(Create(dashed_line_y), Create(dashed_line_x), Create(Px1y1))
        self.wait(1)
        self.play(Unwrite(Text_1_scene13[0]), Unwrite(Text_1_scene13[1]), Unwrite(Text_1_scene13[2]), Unwrite(Text_1_scene13[3]), Unwrite(Text_1_scene13[4]), Unwrite(Text_1_scene13[5]) )
        self.play(Write(Text_2_scene13[0]), Write(Text_2_scene13[1]), Write(Text_2_scene13[2]), Write(Text_2_scene13[3]), Write(Text_2_scene13[4]), 
                Write(Text_2_scene13[5]), Write(Text_2_scene13[6]), Write(Text_2_scene13[7]), Write(Text_2_scene13[8]),
                 run_time=2)
        self.play(Create(line1), Create(r), FadeOut(x_numbers), FadeOut(y_numbers), Create(axes1), Create(x_1), Create(y_1) )
        self.play(Unwrite(Text_2_scene13[0]), Unwrite(Text_2_scene13[1]), Unwrite(Text_2_scene13[2]), Unwrite(Text_2_scene13[3]), Unwrite(Text_2_scene13[4]), 
                Unwrite(Text_2_scene13[5]), Unwrite(Text_2_scene13[6]), Unwrite(Text_2_scene13[7]), Unwrite(Text_2_scene13[8]),
                run_time=2)
        self.play(Write(Text_3_scene13[0]), Write(Text_3_scene13[1]), Write(Text_3_scene13[2]), Write(Text_3_scene13[3]), Create(Px1y1_copy),
                Transform(Px1y1, Text_3_scene13[4]), Write(Text_3_scene13[5]), Write(Text_3_scene13[6]),
                run_time=2)
        self.play(Unwrite(Text_3_scene13[0]), Unwrite(Text_3_scene13[1]), Unwrite(Text_3_scene13[2]), Unwrite(Text_3_scene13[3]), Uncreate(Px1y1),
                Unwrite(Text_3_scene13[4]), Unwrite(Text_3_scene13[5]), Unwrite(Text_3_scene13[6]))
        self.play(Write(Text_4_scene13), Write(Text_5_scene13), Write(Text_6_scene13), Write(Text_7_scene13), run_time=1)
        self.play(dashed_line_x.animate.shift(DOWN * 1.46), Unwrite(Px1y1_copy), Unwrite(x_1), Unwrite(y_1))
        self.play(Create(angle))
        self.play(Write(angle_label))
        self.wait(1)
        self.play(r1.animate.move_to([0, 0.7, 0]), r2.animate.move_to([-1.7, -0.3, 0]), Write(sin), Write(cos), angle_label1.animate.move_to([0.6, 0.73, 0]), angle_label2.animate.move_to([-1.05, -0.27, 0]))
        self.wait(1)
        self.play(Unwrite(sin), Unwrite(cos), Uncreate(angle_label1), Uncreate(angle_label2), Unwrite(r1), Unwrite(r2))
        self.play(Transform(dot, dot1), Uncreate(dashed_line_x), Uncreate(dashed_line_y), Transform(line1, line11), angle_label.animate.move_to([-1.4, 0.3, 0]), r.animate.move_to([-1.4, 0.8, 0]), Transform(angle, angle1))
        self.play(Create(circle1), Create(circle2), Create(circle3), Create(circle4), Transform(Text1, Text2), Create(dot1))
        self.play(Create(pi4), Create(pi34), Create(pi54), Create(pi74))
        self.play(Write(textpi4), Write(textpi34), Write(textpi54), Write(textpi74), Write(textpi2), Write(textpi), Write(textpi32), Write(text0))
        self.wait(1)
        self.play(dot.animate.move_to([2.197, 0, 0]).shift(LEFT * 2.5), dot1.animate.move_to([2.197, 0, 0]).shift(LEFT * 2.5), Transform(line1, line2))
        self.add(moving_part)
        self.play( Uncreate(line1), Uncreate(angle_label), Uncreate(r), Uncreate(angle))
        self.play(Uncreate(dot1))

        diem_quay = ORIGIN + LEFT * 2.5

        # Phase 1: Xoay nhanh (0 → PI, 2 giây)
        self.play(
            Rotating(
                moving_part,
                radians=PI,
                about_point=diem_quay,
                run_time=2,
                rate_func=rush_into,  # Nhanh dần
            )
       )

        # Phase 2: Xoay chậm (PI → 1.5PI, 2 giây)
        self.play(
            Rotating(
                moving_part,
                radians=0.5 * PI,
                about_point=diem_quay,
                run_time=2,
                rate_func=slow_into,  # Chậm dần
            )
       )

        # Phase 3: Xoay nhanh tiếp (1.5PI → 2PI, 1 giây)
        self.play(
            Rotating(
                moving_part,
                radians=0.5 * PI,
                about_point=diem_quay,
                run_time=1,
                rate_func=rush_from,  # Nhanh dần về cuối
           )
       )




        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
