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

class SCENE13(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        
        #ĐỊNH NGHĨA MÀU
        color_00ffff = "#00ffff"
        color_7cfc00 = "#cc00ff"

        #TEXT CỦA HÌNH MÔ PHỎNG BÊN TRÁI
        TEXT_scene13 = Tex(
            r"\textbf{CÁCH CHUYỂN TỪ TỌA ĐỘ DESCARTES", 
            font_size=45
        ).shift(UP * 0.5)
        TEXT_small_scene13 = Tex(
            r"\textbf{CÁCH CHUYỂN TỪ TỌA ĐỘ DESCARTES", 
            font_size=30
        ).shift(UP * 3 + RIGHT * 3)
        TEXT_1_scene13 = Tex(
            r"\textbf{SANG TỌA ĐỘ CỰC}",#0"
            font_size=45
        ).shift(DOWN * 0.5)
        TEXT_small_1_scene13 = Tex(
            r"\textbf{SANG TỌA ĐỘ CỰC}",#0"
            font_size=30
        ).shift(UP * 2.5 + RIGHT * 3)
        Text1_scene13 = Tex("Tọa độ Descartes").to_edge(UP * 7,  buff=0.5).scale(1)
        Text1_scene13.shift((UP * 3), LEFT * 3)
        Text1_scene13.shift(LEFT * 2)
        Text2_scene13 = Tex("Tọa độ cực").to_edge(UP * 7,  buff=0.5).scale(1)
        Text2_scene13.shift((UP * 3), RIGHT * 3)
        Text2_scene13.shift(LEFT * 3)
        Text1_scene13.set_color_by_gradient(color_00ffff, color_7cfc00)
        Text2_scene13.set_color_by_gradient(RED, ORANGE, YELLOW)

        #TRỤC TỌA ĐỘ 
        axes_scene13 = Axes(
            x_range=[-5, 5, 1],  # [min, max, step]
            y_range=[-5, 5, 1],
            x_length=7.3,  # Giảm chiều dài trục x
            y_length=7.3,
            axis_config={"color": WHITE},
        ).shift(LEFT * 2.5)

        axes1_scene13 = Axes(
            x_range=[-5, 5, 1],  # [min, max, step]
            y_range=[-5, 5, 1],
            x_length=7.3,  # Giảm chiều dài trục x
            y_length=7.3,
            axis_config={"color": WHITE},
        ).shift(LEFT * 2.5)

       #SỐ CỦA TRỤC TỌA ĐỘ
        x_numbers_scene13 = axes_scene13.get_x_axis().add_numbers(font_size=24)
        y_numbers_scene13 = axes_scene13.get_y_axis().add_numbers(font_size=24)

        #NHÃN X VÀ Y CỦA TRỤC TỌA ĐỘ
        axes_labels_scene13 = axes_scene13.get_axis_labels(x_label="x", y_label="y")

        #ĐƯỜNG ĐỨT NÉT 
        dashed_line_x_scene13 = DashedLine(start=LEFT*3, end=RIGHT*3, dash_length=0.2)
        dashed_line_x_scene13 = DashedLine(start=[2.197,1.46,0], end=[0,1.46,0])
        dashed_line_x_scene13.set_color(RED)
        dashed_line_x_scene13.shift(LEFT * 2.5)

        dashed_line_x1_scene13 = DashedLine(start=LEFT*3, end=RIGHT*3, dash_length=0.2)
        dashed_line_x1_scene13 = DashedLine(start=[1.46,1.46,0], end=[0,1.46,0])
        dashed_line_x1_scene13.set_color(RED)

        dashed_line_y_scene13 = DashedLine(start=LEFT*3, end=RIGHT*3, dash_length=0.2)
        dashed_line_y_scene13 = DashedLine(start=[2.197,1.46,0], end=[2.197,-0,0])
        dashed_line_y_scene13.set_color(RED) 
        dashed_line_y_scene13.shift(LEFT * 2.5)

        dashed_line_y1_scene13 = DashedLine(start=LEFT*3, end=RIGHT*3, dash_length=0.2)
        dashed_line_y1_scene13 = DashedLine(start=[1.46,1.46,0], end=[1.46,-0,0])
        dashed_line_y1_scene13.set_color(RED)

        #ĐƯỜNG CHÉO XUẤT HIỆN CHIA ĐƯỜNG TRÒN RA THÀNH MIẾNG
        pi4_scene13 = Line(start=[0, 0, 0], end=[2.08, 2.08, 0], color=WHITE, stroke_width=5).shift(LEFT * 2.5)
        pi34_scene13 = Line(start=[0, 0, 0], end=[-2.08, 2.08, 0], color=WHITE, stroke_width=5).shift(LEFT * 2.5)
        pi54_scene13 = Line(start=[0, 0, 0], end=[-2.08, -2.08, 0], color=WHITE, stroke_width=5).shift(LEFT * 2.5)
        pi74_scene13 = Line(start=[0, 0, 0], end=[2.08, -2.08, 0], color=WHITE, stroke_width=5).shift(LEFT * 2.5)

        #VỊ TRÍ TRÊN ĐƯỜNG TRÒN 
        textpi4_scene13 = MathTex(r"\frac{\pi}{4}").scale(0.7).set_color_by_gradient(WHITE)
        textpi4_scene13.move_to([2.35, 2.35, 0]).shift(LEFT * 2.5)
        textpi34_scene13 = MathTex(r"\frac{3\pi}{4}").scale(0.7).set_color_by_gradient(WHITE)
        textpi34_scene13.move_to([-2.35, 2.35, 0]).shift(LEFT * 2.5)
        textpi54_scene13 = MathTex(r"\frac{5\pi}{4}").scale(0.7).set_color_by_gradient(WHITE)
        textpi54_scene13.move_to([-2.35, -2.35, 0]).shift(LEFT * 2.5)
        textpi74_scene13 = MathTex(r"\frac{7\pi}{4}").scale(0.7).set_color_by_gradient(WHITE)
        textpi74_scene13.move_to([2.35, -2.35, 0]).shift(LEFT * 2.5)
        textpi2_scene13 = MathTex(r"\frac{\pi}{2}").scale(0.7).set_color_by_gradient(WHITE)
        textpi2_scene13.move_to([-0.5, 3.3, 0]).shift(LEFT * 2.5)
        textpi_scene13 = MathTex(r"\pi").scale(0.7).set_color_by_gradient(WHITE)
        textpi_scene13.move_to([-3.17, 0.3, 0]).shift(LEFT * 2.5)
        textpi32_scene13 = MathTex(r"\frac{3\pi}{2}").scale(0.7).set_color_by_gradient(WHITE)
        textpi32_scene13.move_to([-0.5, -3.3, 0]).shift(LEFT * 2.5)
        text0_scene13 = MathTex(r"0").scale(0.7).set_color_by_gradient(WHITE)
        text0_scene13.move_to([3.17, 0.3, 0]).shift(LEFT * 2.5)

        #TỌA ĐỘ TRÊN TRỤC
        x_1_scene13 = MathTex(r"x_1").scale(0.7).set_color_by_gradient(YELLOW)
        x_1_scene13.move_to(axes_scene13.c2p(3, 0)).shift(DOWN * 0.5)
        y_1_scene13 = MathTex(r"y_1").scale(0.7).set_color_by_gradient(YELLOW)
        y_1_scene13.move_to(axes_scene13.c2p(0, 2)).shift(LEFT * 0.5)

        #ĐƯỜNG CHÌM TRÙNG VỚI TRỤC X
        x_line_scene13 = Line(start=[0, 0, 0], end=[5, 0, 0], color=RED, stroke_width=5)

        #CỤC ĐỎ MÔ PHỎNG ĐIỂM
        dot_scene13 = Circle(radius=0.1, color=RED, fill_opacity=1)
        dot_scene13.move_to([2.197, 1.46, 0]).shift(LEFT * 2.5)
        dot1_scene13 = Circle(radius=0.1, color=RED, fill_opacity=1)
        dot1_scene13.move_to([1.96, 1, 0])
        dot1_scene13.shift(LEFT * 2.5)
        
        #NHÃN CỦA CỤC ĐỎ ĐÓ
        Px1y1_scene13 = MathTex(r"P(x_1, y_1)").scale(0.7).set_color_by_gradient(YELLOW)
        Px1y1_scene13.move_to([2.5, 1.9, 0])
        Px1y1_scene13.shift(LEFT * 2.5)
        Px1y1_copy_scene13 = Px1y1_scene13.copy()
        Px1y1_copy_scene13.shift(LEFT * 1)

        #ĐƯỜNG KÉO TỪ ĐIỂM XUỐNG TÂM
        line1_scene13 = Line(start=[2.197, 1.46, 0], end=[0, 0, 0], color=YELLOW, stroke_width=5).shift(LEFT * 2.5)
        line11_scene13 = Line(start=[1.96, 1, 0], end=[0, 0, 0], color=YELLOW, stroke_width=5).shift(LEFT * 2.5)
        line2_scene13 = Line(start=[2.197, 0, 0], end=[0, 0, 0], color=YELLOW, stroke_width=5).shift(LEFT * 2.5)
        r_scene13 = Tex(r"r").scale(0.7).set_color_by_gradient(YELLOW)
        r_scene13.move_to([1.2, 1.2, 0])
        r_scene13.shift(LEFT * 2.5)
        r1_scene13 = r_scene13.copy()
        r2_scene13 = r_scene13.copy()

        dotxoay_scene13 = Dot(line2_scene13.get_start(), color=RED)  # Đánh dấu điểm cần xoay
        
        #NHÓM ĐƯỜNG THẲNG VÀ DẤU CHẤM ĐỂ DUY CHUYỂN 
        moving_part_scene13 = VGroup(line2_scene13.copy(), dot_scene13)

        #VẼ GÓC
        angle_scene13 = Angle(
            x_line_scene13, line1_scene13,
            radius=0.9,
            color=BLUE,
            quadrant=(1,-1),  # Chọn phần tư
            other_angle=False,  # Vẽ góc lớn hơn 180°
            fill_opacity=0.5   # Độ trong suốt
        )
        angle1_scene13 = Angle(
            x_line_scene13, line11_scene13,
            radius=0.9,
            color=BLUE,
            quadrant=(1,-1),  # Chọn phần tư
            other_angle=False,  # Vẽ góc lớn hơn 180°
            fill_opacity=0.5   # Độ trong suốt
        )
           
        #NHÃN CỦA GÓC
        angle_label_scene13 = MathTex(r"\theta").scale(0.7).set_color_by_gradient(BLUE)
        angle_label_scene13.move_to([1.2, 0.3, 0])
        angle_label_scene13.shift(LEFT * 2.5)
        angle_label1_scene13 = angle_label_scene13.copy()
        angle_label2_scene13 = angle_label_scene13.copy()
        
        #NHÃN CỦA CẠNH SẼ BIẾN ĐỔI SANG TỌA ĐỘ CỰC
        sin_scene13 = MathTex(r"\sin").scale(0.7).set_color_by_gradient(RED)
        sin_scene13.move_to([2.8, 0.73, 0])
        sin_scene13.shift(LEFT * 2.5)
        cos_scene13 = MathTex(r"\cos").scale(0.7).set_color_by_gradient(RED)
        cos_scene13.move_to([1.12, -0.3, 0])
        cos_scene13.shift(LEFT * 2.5)
        
        #VẼ ĐƯỜNG TRÒN
        circle1_scene13 = Circle(radius=0.74, color=WHITE).shift(LEFT * 2.5)
        circle2_scene13 = Circle(radius=1.47, color=WHITE).shift(LEFT * 2.5)
        circle3_scene13 = Circle(radius=2.2, color=WHITE).shift(LEFT * 2.5)
        circle4_scene13 = Circle(radius=2.93, color=WHITE).shift(LEFT * 2.5)
        
        #LÝ THUYẾT 
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


        Text_3_scene13[0].shift(RIGHT * 4.5 + UP * 1.5)
        Text_3_scene13[1].shift(RIGHT * 4.5 + UP * 1.5)
        Text_3_scene13[2].shift(RIGHT * 4.5 + UP * 1.5)
        Text_3_scene13[3].shift(RIGHT * 4.5 + UP * 1.5)
        Text_3_scene13[4].shift(RIGHT * -0.3 + UP * 1.14)
        Text_3_scene13[5].shift(RIGHT * -0.25 + UP * 1.14)
        Text_3_scene13[6].shift(RIGHT * 5.3 + UP * 1.52)

        Text_4_scene13 = MathTex(r"r^2=x_1^2+y_1^2").scale(1)
        Text_4_scene13.shift(RIGHT * 3.5)
        Text_4_scene13.set_color(WHITE)
        Text_5_scene13 = MathTex(r"x_1=rcos\varphi").scale(1)
        Text_5_scene13.shift(RIGHT * 3.5 + UP * 0.4)
        Text_5_scene13.set_color(WHITE)
        Text_6_scene13 = MathTex(r"y_1=rsin\varphi").scale(1)
        xy = VGroup(Text_5_scene13, Text_6_scene13)#chỉnh
        Text_6_scene13.shift(RIGHT * 3.5 + UP * -0.1)
        Text_6_scene13.set_color(WHITE)
        Text_7_scene13 = MathTex(r"tan\varphi =\frac{y_1}{x_1}")
        Text_7_scene13.shift(RIGHT * 3.5 + UP * -0.9)
        Text_7_scene13.set_color(WHITE)

        #CHẠY ANIMATION
        self.play(Write(Text_1_scene13[0]), Write(Text_1_scene13[1]), run_time=2)
        self.play(Write(Text_1_scene13[2]), Write(Text_1_scene13[3]), Write(Text1_scene13), run_time=1)
        self.play(Write(Text_1_scene13[4]), Write(Text_1_scene13[5]))
        self.wait(1)
        self.play(Create(axes_scene13), Write(axes_labels_scene13), run_time=1)
        self.wait(1)
        self.play(Create(dot_scene13))
        self.play(Create(dashed_line_y_scene13), Create(dashed_line_x_scene13), Create(Px1y1_scene13))
        self.wait(1)
        self.play(Unwrite(Text_1_scene13[0]), Unwrite(Text_1_scene13[1]), Unwrite(Text_1_scene13[2]), Unwrite(Text_1_scene13[3]), Unwrite(Text_1_scene13[4]), Unwrite(Text_1_scene13[5]), run_time=1 )
        self.play(Write(Text_2_scene13[0]), Write(Text_2_scene13[1]), Write(Text_2_scene13[2]), Write(Text_2_scene13[3]), Write(Text_2_scene13[4]), 
                Write(Text_2_scene13[5]), Write(Text_2_scene13[6]), Write(Text_2_scene13[7]), Write(Text_2_scene13[8]),
                 run_time=2)
        self.wait(1)
        self.remove(Text_1_scene13, Text_2_scene13, axes_scene13, axes_labels_scene13, x_numbers_scene13, y_numbers_scene13, dot_scene13, Px1y1_scene13, dashed_line_y_scene13, dashed_line_y_scene13,
                Text_2_scene13[0], Text_2_scene13[1], Text_2_scene13[2], Text_2_scene13[3], Text_2_scene13[4], 
                Text_2_scene13[5], Text_2_scene13[6], Text_2_scene13[7], Text_2_scene13[8], dashed_line_x_scene13, Text1_scene13)
        self.play(Write(TEXT_scene13), Write(TEXT_1_scene13), run_time=2)
        self.wait(1)
        self.add(Text_1_scene13, axes_scene13, axes_labels_scene13, x_numbers_scene13, y_numbers_scene13, dot_scene13, Px1y1_scene13, dashed_line_y_scene13, dashed_line_y_scene13, dashed_line_x_scene13, Text1_scene13)
        self.play(Transform(TEXT_scene13, TEXT_small_scene13), Transform(TEXT_1_scene13, TEXT_small_1_scene13), run_time=1)
        self.play(Create(line1_scene13), Create(r_scene13), FadeOut(x_numbers_scene13), FadeOut(y_numbers_scene13), Create(axes1_scene13), Create(x_1_scene13), Create(y_1_scene13), run_time=2 )
        self.play(Write(Text_3_scene13[0]), Write(Text_3_scene13[1]), Write(Text_3_scene13[2]), Write(Text_3_scene13[3]), Create(Px1y1_copy_scene13),
                Transform(Px1y1_scene13, Text_3_scene13[4]), Write(Text_3_scene13[5]), Write(Text_3_scene13[6]),
                run_time=2)
        self.wait(1)
        self.play(Unwrite(Text_3_scene13[0]), Unwrite(Text_3_scene13[1]), Unwrite(Text_3_scene13[2]), Unwrite(Text_3_scene13[3]), Uncreate(Px1y1_scene13),
                Unwrite(Text_3_scene13[4]), Unwrite(Text_3_scene13[5]), Unwrite(Text_3_scene13[6]))
        self.play(Write(Text_4_scene13), run_time=1)
        self.play(dashed_line_x_scene13.animate.shift(DOWN * 1.46), Unwrite(Px1y1_copy_scene13), Unwrite(x_1_scene13), Unwrite(y_1_scene13))
        self.play(Create(angle_scene13))
        self.play(Write(angle_label_scene13))
        self.wait(1)
        self.play(r1_scene13.animate.move_to([0, 0.7, 0]), r2_scene13.animate.move_to([-1.7, -0.3, 0]), Write(sin_scene13), Write(cos_scene13), angle_label1_scene13.animate.move_to([0.6, 0.73, 0]), angle_label2_scene13.animate.move_to([-1.05, -0.27, 0]), Transform(Text_4_scene13, xy))
        self.wait(1)
        self.play(Unwrite(sin_scene13), Unwrite(cos_scene13), Uncreate(angle_label1_scene13), Uncreate(angle_label2_scene13), Unwrite(r1_scene13), Unwrite(r2_scene13))
        self.play(Transform(dot_scene13, dot1_scene13), Uncreate(dashed_line_x_scene13), Uncreate(dashed_line_y_scene13), Transform(line1_scene13, line11_scene13), angle_label_scene13.animate.move_to([-1.4, 0.3, 0]), r_scene13.animate.move_to([-1.4, 0.8, 0]), Transform(angle_scene13, angle1_scene13))
        self.play(Create(circle1_scene13), Create(circle2_scene13), Create(circle3_scene13), Create(circle4_scene13), Transform(Text1_scene13, Text2_scene13), Create(dot1_scene13), TEXT_1_scene13.animate.shift(RIGHT * 0.5 + DOWN * 1.1), TEXT_scene13.animate.shift(RIGHT * 0.5 + DOWN * 1.1))
        self.play(Create(pi4_scene13), Create(pi34_scene13), Create(pi54_scene13), Create(pi74_scene13))
        self.play(Write(textpi4_scene13), Write(textpi34_scene13), Write(textpi54_scene13), Write(textpi74_scene13), Write(textpi2_scene13), Write(textpi_scene13), Write(textpi32_scene13), Write(text0_scene13))
        self.wait(1)
        self.play(dot_scene13.animate.move_to([2.197, 0, 0]).shift(LEFT * 2.5), dot1_scene13.animate.move_to([2.197, 0, 0]).shift(LEFT * 2.5), Transform(line1_scene13, line2_scene13))
        self.add(moving_part_scene13)
        self.play(Uncreate(line1_scene13), Uncreate(angle_label_scene13), Uncreate(r_scene13), Uncreate(angle_scene13))
        self.play(Uncreate(dot1_scene13), Transform(xy, Text_7_scene13))

        #BẮT ĐẦU QUAY
        diem_quay_scene13 = ORIGIN + LEFT * 2.5

        # Phase 1: Xoay nhanh (0 → PI, 2 giây)
        self.play(
            Rotating(
                moving_part_scene13,
                radians=PI,
                about_point=diem_quay_scene13,
                run_time=2,
                rate_func=rush_into,  # Nhanh dần
            )
       )

        # Phase 2: Xoay chậm (PI → 1.5PI, 2 giây)
        self.play(
            Rotating(
                moving_part_scene13,
                radians=0.5 * PI,
                about_point=diem_quay_scene13,
                run_time=2,
                rate_func=slow_into,  # Chậm dần
            )
       )

        # Phase 3: Xoay nhanh tiếp (1.5PI → 2PI, 1 giây)
        self.play(
            Rotating(
                moving_part_scene13,
                radians=0.5 * PI,
                about_point=diem_quay_scene13,
                run_time=1,
                rate_func=rush_from,  # Nhanh dần về cuối
           )
       )
        self.play(Uncreate(moving_part_scene13), Unwrite(textpi4_scene13), Unwrite(textpi34_scene13), Unwrite(textpi54_scene13), Unwrite(textpi74_scene13), Unwrite(textpi2_scene13), Unwrite(textpi_scene13), Unwrite(textpi32_scene13), Unwrite(text0_scene13),
                Uncreate(circle1_scene13), Uncreate(circle2_scene13), Uncreate(circle3_scene13), Uncreate(circle4_scene13),
                Unwrite(Text1_scene13), Unwrite(Text_5_scene13), Unwrite(Text_6_scene13), Unwrite(Text_7_scene13), Uncreate(axes1_scene13), Unwrite(axes_labels_scene13),
                Uncreate(pi4_scene13), Uncreate(pi34_scene13), Uncreate(pi54_scene13), Uncreate(pi74_scene13), Unwrite(Text_4_scene13), Unwrite(TEXT_scene13), Unwrite(TEXT_1_scene13), run_time=0.5
         )




        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
