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
        Text2 = Tex("Tọa độ cực").to_edge(UP * 7,  buff=0.5).scale(1)
        Text2.shift((UP * 3), RIGHT * 3)
        Text1.set_color_by_gradient(color_00ffff, color_7cfc00)
        Text2.set_color_by_gradient(RED, ORANGE, YELLOW)
        axes = Axes(
            x_range=[-5, 5, 1],  # [min, max, step]
            y_range=[-5, 5, 1],
            x_length=7.3,  # Giảm chiều dài trục x
            y_length=7.3,
            axis_config={"color": WHITE},
        )

        axes1 = Axes(
            x_range=[-5, 5, 1],  # [min, max, step]
            y_range=[-5, 5, 1],
            x_length=7.3,  # Giảm chiều dài trục x
            y_length=7.3,
            axis_config={"color": WHITE},
        )
        
        x_numbers = axes.get_x_axis().add_numbers(font_size=24)
        y_numbers = axes.get_y_axis().add_numbers(font_size=24)

        # Thêm nhãn cho các trục
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        dashed_line_x = DashedLine(start=LEFT*3, end=RIGHT*3, dash_length=0.2)
        dashed_line_x = DashedLine(start=[2.197,1.46,0], end=[0,1.46,0])
        dashed_line_x.set_color(RED)

        dashed_line_x1 = DashedLine(start=LEFT*3, end=RIGHT*3, dash_length=0.2)
        dashed_line_x1 = DashedLine(start=[1.46,1.46,0], end=[0,1.46,0])
        dashed_line_x1.set_color(RED)

        dashed_line_y = DashedLine(start=LEFT*3, end=RIGHT*3, dash_length=0.2)
        dashed_line_y = DashedLine(start=[2.197,1.46,0], end=[2.197,-0,0])
        dashed_line_y.set_color(RED)

        dashed_line_y1 = DashedLine(start=LEFT*3, end=RIGHT*3, dash_length=0.2)
        dashed_line_y1 = DashedLine(start=[1.46,1.46,0], end=[1.46,-0,0])
        dashed_line_y1.set_color(RED)

        pi4 = Line(start=[0, 0, 0], end=[2.08, 2.08, 0], color=WHITE, stroke_width=5)
        pi34 = Line(start=[0, 0, 0], end=[-2.08, 2.08, 0], color=WHITE, stroke_width=5)
        pi54 = Line(start=[0, 0, 0], end=[-2.08, -2.08, 0], color=WHITE, stroke_width=5)
        pi74 = Line(start=[0, 0, 0], end=[2.08, -2.08, 0], color=WHITE, stroke_width=5)

        textpi4 = MathTex(r"\frac{\pi}{4}").scale(0.7).set_color_by_gradient(WHITE)
        textpi4.move_to([2.35, 2.35, 0])
        textpi34 = MathTex(r"\frac{3\pi}{4}").scale(0.7).set_color_by_gradient(WHITE)
        textpi34.move_to([-2.35, 2.35, 0])
        textpi54 = MathTex(r"\frac{5\pi}{4}").scale(0.7).set_color_by_gradient(WHITE)
        textpi54.move_to([-2.35, -2.35, 0])
        textpi74 = MathTex(r"\frac{7\pi}{4}").scale(0.7).set_color_by_gradient(WHITE)
        textpi74.move_to([2.35, -2.35, 0])
        textpi2 = MathTex(r"\frac{\pi}{2}").scale(0.7).set_color_by_gradient(WHITE)
        textpi2.move_to([-0.5, 3.3, 0])
        textpi = MathTex(r"\pi").scale(0.7).set_color_by_gradient(WHITE)
        textpi.move_to([-3.17, 0.3, 0])
        textpi32 = MathTex(r"\frac{3\pi}{2}").scale(0.7).set_color_by_gradient(WHITE)
        textpi32.move_to([-0.5, -3.3, 0])
        text0 = MathTex(r"0").scale(0.7).set_color_by_gradient(WHITE)
        text0.move_to([3.17, 0.3, 0])

        x_line = Line(start=[0, 0, 0], end=[5, 0, 0], color=RED, stroke_width=5)


        #toado = Tex("(3, 2)").scale(0.6).set_color_by_gradient(YELLOW)
        #toado.move_to([2.197, 1.06, 0])
        #toado.shift(DOWN * (-0.5))

        dot = Circle(radius=0.1, color=RED, fill_opacity=1)
        dot.move_to([2.197, 1.46, 0])
        dot1 = Circle(radius=0.1, color=RED, fill_opacity=1)
        dot1.move_to([1.96, 1, 0])

        Toado = MathTex(r"(3,2)").scale(0.7).set_color_by_gradient(YELLOW)
        Toado.move_to([2.7, 1.9, 0])

        line1 = Line(start=[2.197, 1.46, 0], end=[0, 0, 0], color=YELLOW, stroke_width=5)
        line11 = Line(start=[1.96, 1, 0], end=[0, 0, 0], color=YELLOW, stroke_width=5)
        line2 = Line(start=[2.197, 0, 0], end=[0, 0, 0], color=YELLOW, stroke_width=5)
        r = Tex(r"r").scale(0.7).set_color_by_gradient(YELLOW)
        r.move_to([1.2, 1.2, 0])
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
        cos = MathTex(r"\cos").scale(0.7).set_color_by_gradient(RED)
        cos.move_to([1.12, -0.3, 0])

        circle1 = Circle(radius=0.74, color=WHITE)
        circle2 = Circle(radius=1.47, color=WHITE)
        circle3 = Circle(radius=2.2, color=WHITE)
        circle4 = Circle(radius=2.93, color=WHITE)
        

        self.play(Write(Text1))
        self.wait(1)
        self.play(Create(axes), Write(axes_labels))
        self.wait(1)
        self.play(Create(dot))
        #self.play(Create(toado))
        self.play(Create(dashed_line_y), Create(dashed_line_x), Create(Toado))
        self.wait(1)
        self.play(Create(line1), Create(r), Uncreate(Toado), FadeOut(x_numbers), FadeOut(y_numbers), Create(axes1) )
        self.play(dashed_line_x.animate.shift(DOWN * 1.46))
        self.play(Create(angle))
        self.play(Write(angle_label))
        self.wait(1)
        self.play(r1.animate.move_to([2.5, 0.7, 0]), r2.animate.move_to([0.8, -0.3, 0]), Write(sin), Write(cos), angle_label1.animate.move_to([3.1, 0.73, 0]), angle_label2.animate.move_to([1.46, -0.27, 0]))
        self.wait(1)
        self.play(Unwrite(sin), Unwrite(cos), Uncreate(angle_label1), Uncreate(angle_label2), Unwrite(r1), Unwrite(r2))
        self.play(Transform(dot, dot1), Uncreate(dashed_line_x), Uncreate(dashed_line_y), Transform(line1, line11), angle_label.animate.move_to([1.1, 0.3, 0]), r.animate.move_to([1.48, 1, 0]), Transform(angle, angle1))
        self.play(Create(circle1), Create(circle2), Create(circle3), Create(circle4), Transform(Text1, Text2), Create(dot1))
        self.play(Create(pi4), Create(pi34), Create(pi54), Create(pi74))
        self.play(Write(textpi4), Write(textpi34), Write(textpi54), Write(textpi74), Write(textpi2), Write(textpi), Write(textpi32), Write(text0))
        self.wait(1)
        self.play(dot.animate.move_to([2.197, 0, 0]), dot1.animate.move_to([2.197, 0, 0]), Transform(line1, line2))
        self.add(moving_part)
        self.play( Uncreate(line1), Uncreate(angle_label), Uncreate(r), Uncreate(angle))
        self.play(Uncreate(dot1))

        # Phase 1: Xoay nhanh (0 → PI, 2 giây)
        self.play(
            Rotating(
                moving_part,
                radians=PI,
                about_point=ORIGIN,
                run_time=2,
                rate_func=rush_into,  # Nhanh dần
            )
       )

        # Phase 2: Xoay chậm (PI → 1.5PI, 2 giây)
        self.play(
            Rotating(
                moving_part,
                radians=0.5 * PI,
                about_point=ORIGIN,
                run_time=2,
                rate_func=slow_into,  # Chậm dần
            )
       )

        # Phase 3: Xoay nhanh tiếp (1.5PI → 2PI, 1 giây)
        self.play(
            Rotating(
                moving_part,
                radians=0.5 * PI,
                about_point=ORIGIN,
                run_time=1,
                rate_func=rush_from,  # Nhanh dần về cuối
           )
       )




        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
