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

        color_03ffff = "#03ffff"
        color_cc00ff = "#cc00ff"
        color_4dbbbe0 = "#4dbbe0"
        color_fe7051 = "#fe7051"
        color_7fb663 = "#7fb663"
        color_ff8d28 = "#ff8d28"

        Text_1_scene19 = Tex(
            r"Khi đổi biến trong \textbf{tích phân đôi} (ví dụ như",
            r" $\iint_R f(x, y) \, dxdy$)",
            r", nếu chuyển sang",
            r" tọa độ cực",
            r", ta phải nhân thêm hệ số",
            r"\textbf{ r}",
            r":",
            font_size=40
        )
        ToaDoCuc = Text_1_scene19[3].copy()
        ToaDoCuc.set_color(BLUE)

        Text_1_scene19[3].set_color(BLUE)
        Text_1_scene19[5].set_color(YELLOW)

        Text_2_scene19 = Tex(
            r"Công thức đổi biến sang hệ",
            r" toạ độ cực:",
            font_size=40
        ).shift(UP * 3)
        Text_2_scene19[1].set_color(BLUE)

        Text_3_scene19 = MathTex(
            r"x=",
            r"r",
            r"\cos\varphi",
            font_size=80
        )
        r1_scene19 = Text_3_scene19[1].copy()
        Text_4_scene19 = MathTex(
            r"y=",
            r"r",
            r"\sin\varphi", 
            font_size=80
        )
        r2_scene19 = Text_4_scene19[1].copy()
        Text_5_scene19 = MathTex(
            r"r",
            r" \ge 0",
            font_size=80
        )
        Text_5_scene19[1].shift(RIGHT * 1 + DOWN * 1)

        CongThucToaDoCuc = VGroup(Text_4_scene19, Text_3_scene19)

        Text_6_scene19 = Tex(
            r"Định thức Jacobian khi chuyển sang hệ toạ độ cực là:",
            font_size=40
        ).shift(UP * 3)

        Jacobian = MathTex(
            r"J = \frac{\partial (x, y)}{\partial (r, \varphi)} = ",
            r"\begin{vmatrix}"
            r"\frac{\partial x}{\partial r} & \frac{\partial x}{\partial \varphi} \\"
            r"\frac{\partial y}{\partial r} & \frac{\partial y}{\partial \varphi}"
            r"\end{vmatrix}",
            r"=",
            r"\begin{vmatrix}"
            r"\cos \varphi & -r \sin \varphi \\"
            r"\sin \varphi & r \cos \varphi"
            r"\end{vmatrix}",
            r"= r",
            font_size=55
        )


        self.play(Write(Text_1_scene19), run_time=3)
        self.play(Unwrite(Text_1_scene19), Transform(ToaDoCuc, Text_2_scene19[1]), Write(Text_2_scene19[0]), run_time=1)
        self.play(Write(Text_3_scene19), run_time=2)
        self.play(Text_3_scene19.animate.move_to(UP * 1), Write(Text_4_scene19))
        self.play(r2_scene19.animate.move_to(DOWN * 1), Write(Text_5_scene19[1]), run_time=1)
        self.wait(1)
        self.play(Unwrite(r2_scene19), Unwrite(Text_5_scene19[1]))
        self.remove(ToaDoCuc)
        self.play(Transform(Text_2_scene19, Text_6_scene19), run_time=2)
        self.play(Transform(CongThucToaDoCuc, Jacobian), run_time=2)
        self.play(Unwrite(Jacobian), Unwrite(Text_6_scene19), Unwrite(Text_2_scene19), Unwrite(CongThucToaDoCuc))

        Text_1_scene22 = Tex(
            r"III. ỨNG DỤNG CỦA TÍCH PHÂN KÉP",
            font_size=50
        )
        Text_1_1_scene22 = Tex(
            r"TRONG TỌA ĐỘ CỰC VỚI ĐỜI SỐNG",
         font_size = 50
        )
        
        Text_1_scene22.shift(UP * 1.5)

        Text_1_scene22.set_color_by_gradient(color_03ffff, color_cc00ff)
        Text_1_1_scene22.set_color_by_gradient(color_03ffff, color_cc00ff)

        Text_2_scene22 = Tex(
            r"\textbf{Đồ họa máy tính (Computer Graphics)",
            font_size = 35, 
            color = WHITE
        )
        background_box_dohoamaytinh = SurroundingRectangle(
            Text_2_scene22,
            color=RED_E,            # màu viền
            fill_color=RED_E,    # màu nền
            fill_opacity=0.5,       # độ đậm nền (1 = đặc)
            buff=0.15             # khoảng cách mép khung đến chữ
        )
        Text_2_box_scene22 = VGroup(background_box_dohoamaytinh, Text_2_scene22)

        Text_2_2_scene22 = Tex(
            r"Tính shading trong mô hình ánh sáng như",
            font_size = 40
        )
        Text_2_3_scene22 = Tex(
            r"Phong Reflection Model",
            r" hoặc",
            r" Radiosity",
            r".",
            font_size = 40
        )

        Text_2_2_scene22.shift(UP * 2 + LEFT * 1)
        Text_2_3_scene22.shift(UP * 1.5 + RIGHT * 1.5)

        Phong_Reflection_Model = Text_2_3_scene22[0].copy()
        Radiosity = Text_2_3_scene22[2].copy().shift(DOWN * 4.5 + LEFT * 4.2)
        
        Blinn_Phong = ImageMobject("Blinn_Phong.png")
        Phong = ImageMobject("Phong.png")
        Blinn_Phong_higher_eponent = ImageMobject("Blinn_Phong_higher_exponent.png")
        Radiosity_image = ImageMobject("Radiosity.jpg")

        Blinn_Phong.scale(1.4)
        Blinn_Phong.shift(LEFT * 3.5 + DOWN * 0.8)
        Phong.scale(1.4)
        Phong.shift(DOWN * 0.8)
        Blinn_Phong_higher_eponent.scale(1.4)
        Blinn_Phong_higher_eponent.shift(DOWN * 0.8 + RIGHT * 3.5)
        Radiosity_image.scale(0.35)
        Radiosity_image.shift(DOWN * 2 + UP * 1.3)

        Text_3_scene22 = Tex(
            r"\textbf{Thị giác máy tính (Computer Vision)}",
            font_size = 35,
            color = WHITE
        )
        background_box_thigiacmaytinh = SurroundingRectangle(
            Text_3_scene22,
            color=BLUE,            # màu viền
            fill_color= color_4dbbbe0,    # màu nền
            fill_opacity=0.5,       # độ đậm nền (1 = đặc)
            buff=0.15             # khoảng cách mép khung đến chữ
        )
        Text_3_box_scene22 = VGroup(background_box_thigiacmaytinh, Text_3_scene22)
        Text_3_box_scene22.shift(UP * 3 + RIGHT * 7)

        Text_4_scene22 = Tex(
            r"Trong quá trình trích xuất đặc trưng hoặc tính toán các đặc trưng dạng hình tròn,",
            r" việc tích phân trong tọa độ cực giúp chuẩn hóa và tính toán chính xác hơn các thuộc tính hình học",
            r" như",
            r" diện tích",
            r",",
            r" mật độ điểm ảnh",
            r", ...",
            font_size=35
        ).shift(UP * 1.9)

        DienTich = Text_4_scene22[3].copy()
        MatDoDiemAnh = Text_4_scene22[5].copy()

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=3,
            y_length=3,
            axis_config={"include_tip": True},
        ).move_to(LEFT * 3.5 + DOWN * 1)

        Text0 = Tex("O").to_edge(UP * 7,  buff=0.5).scale(1)
        Text0.shift(LEFT * 5.1 + DOWN * 3)

        x_axes_labels = axes.get_x_axis_label("x")
        y_axes_labels = axes.get_y_axis_label("y")

        a = 2  # bán kính trong
        b = 3.5    # bán kính ngoài
        alpha = 0.3  # góc alpha (rad)
        beta = 1.2   # góc beta (rad)
        origin = axes.c2p(0, 0)

        outer_arc = Arc(radius=b, start_angle=alpha, angle=beta - alpha, arc_center=origin)
        inner_arc = Arc(radius=a, start_angle=beta, angle=-(beta - alpha), arc_center=origin)

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

        TrucDienTich = VGroup(axes, x_axes_labels, y_axes_labels, Text0, outer_arc, inner_arc, left_line, right_line, region)

        MatDoDiemAnh_Image = ImageMobject("MatDoDiemAnh.jpg")
        MatDoDiemAnh_Image.scale(1).shift(RIGHT * 3 + DOWN * 1)


        Text_5_scene22 = Tex(
            r"\textbf{Xử lý tín hiệu số (Digital Signal Processing - DSP)}",
            font_size=35
        )
        background_box_xulytinhieuso = SurroundingRectangle(
            Text_5_scene22,
            color=GREEN,            # màu viền
            fill_color= color_7fb663,    # màu nền
            fill_opacity=0.5,       # độ đậm nền (1 = đặc)
            buff=0.15             # khoảng cách mép khung đến chữ
        )
        Text_5_box_scene22 = VGroup(background_box_xulytinhieuso, Text_5_scene22)
        Text_5_box_scene22.shift(UP * 3)

        Text_6_scene22 = Tex(
            r"Tích phân trong tọa độ cực giúp tối ưu hóa và đánh giá hiệu suất của các bộ lọc không gian hình tròn trong việc làm mịn ảnh, phát hiện biên hình tròn, ...", 
            font_size=35
        )
        axes2_scene12 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4,
            y_length=4,
            axis_config={"color": RED}
        ).shift(LEFT * 3 )
        half_circle_scene22 = Annulus(
            inner_radius=0.6,
            outer_radius=1.2,
            fill_opacity=0.8,
            stroke_width=0
        ).set_color([BLUE_E, TEAL_B, GREEN]).move_to(axes2_scene12.c2p(0, 0))
        half_circle_after_scene22 = half_circle_scene22.copy()

        LamMinAnh_before_Image = ImageMobject("LamMinAnh_before.png")
        LamMinAnh_before_Image.scale(1).shift(LEFT  * 3.8 + UP * 0.8)
        LamMinAnh_after_Image = ImageMobject("LamMinAnh_after.png")
        LamMinAnh_after_Image.scale(1).shift(RIGHT  * 3 + DOWN * 2.4)


        Text_7_scene22 = Tex(
            r"\textbf{Robot học và điều khiển}"
        )
        background_box_robothocvadieukhien = SurroundingRectangle(
            Text_7_scene22,
            color=ORANGE,            # màu viền
            fill_color= color_ff8d28,    # màu nền
            fill_opacity=0.5,       # độ đậm nền (1 = đặc)
            buff=0.15             # khoảng cách mép khung đến chữ
        ).shift(UP * 3)
        Text_7_box_scene22 = VGroup(background_box_robothocvadieukhien, Text_7_scene22)

        # Tạo robot với thiết kế đẹp hơn
        body = RoundedRectangle(
            width=1.2, height=1.8, 
            corner_radius=0.2,
            fill_color=BLUE_E, fill_opacity=1,
            stroke_color=BLUE_A, stroke_width=3
        )
        
        head = Circle(
            radius=0.4,
            fill_color=BLUE_C, fill_opacity=1,
            stroke_color=BLUE_A, stroke_width=3
        ).shift(UP*1.2)
        
        eyes = VGroup(
            Dot(color=WHITE).shift(UP*1.3 + LEFT*0.15),
            Dot(color=WHITE).shift(UP*1.3 + RIGHT*0.15)
        )
        
        # Chân và tay sẽ được animate
        left_arm = Line(ORIGIN, LEFT*0.5 + DOWN*0.5, stroke_width=8)
        right_arm = Line(ORIGIN, RIGHT*0.5 + DOWN*0.5, stroke_width=8)
        arms = VGroup(left_arm, right_arm).shift(UP*0.5)
        
        left_leg = Line(ORIGIN, LEFT*0.3 + DOWN*0.7, stroke_width=8)
        right_leg = Line(ORIGIN, RIGHT*0.3 + DOWN*0.7, stroke_width=8)
        legs = VGroup(left_leg, right_leg).shift(DOWN*0.9)
        
        robot = VGroup(body, head, eyes, arms, legs)
        robot.scale(0.8).shift(LEFT*5 + DOWN*0.5)
        
        # Thêm bóng đổ
        shadow = Circle(radius=0.8, fill_color=BLACK, fill_opacity=0.2, stroke_width=0)
        shadow.scale(0.5).shift(DOWN*2.2)
        
        # Tạo hiệu ứng chạy
        start_pos = robot.get_center()
        end_pos = start_pos + RIGHT*10
        
        
        Text_7_scene22.next_to(robot, UP)  # đặt trên đầu robot

        Text_8_scene22 = Tex(
            r"Tích phân trong tọa độ cực dùng để tính diện tích quét, phân bố năng lượng, hoặc tối ưu hóa đường đi của robot khi hoạt động trong không gian có tính đối xứng tròn.",
            font_size=35
        ).shift(UP * 1.8)
        self.play(Write(Text_1_scene22), Write(Text_1_1_scene22), run_time=3)
        self.play(Unwrite(Text_1_1_scene22), Unwrite(Text_1_scene22))
        self.play(LaggedStart(FadeIn(background_box_dohoamaytinh), Write(Text_2_scene22), lag_ratio=0.3), run_time=2)
        self.play(background_box_dohoamaytinh.animate.move_to(UP * 3), Text_2_scene22.animate.move_to(UP * 3))
        self.play(Write(Text_2_2_scene22), run_time=2)
        self.play(Write(Text_2_3_scene22), run_time=2)
        self.play(Phong_Reflection_Model.animate.move_to(DOWN * 3), run_time=1)
        self.play(SpinInFromNothing(Blinn_Phong), SpinInFromNothing(Phong), SpinInFromNothing(Blinn_Phong_higher_eponent), run_time=2)
        self.wait(1)
        self.play(Blinn_Phong.animate.move_to( DOWN * 0.8), Blinn_Phong_higher_eponent.animate.move_to(DOWN * 0.8))
        self.play(FadeOut(Phong), FadeOut(Blinn_Phong), FadeOut(Blinn_Phong_higher_eponent), run_time=2)
        self.play(Transform(Phong_Reflection_Model, Radiosity), SpinInFromNothing(Radiosity_image), run_time=2)
        self.wait(1)
        self.play(FadeOut(Radiosity_image), Unwrite(Radiosity), Unwrite(Text_2_2_scene22), Unwrite(Text_2_3_scene22), Unwrite(Phong_Reflection_Model))
        self.play(Text_2_box_scene22.animate.move_to(LEFT * 13 + UP *3), run_time=2)
        self.play(Text_3_box_scene22.animate.move_to( UP * 3), run_time=2)
        self.play(Uncreate(Text_2_box_scene22))
        self.play(Write(Text_4_scene22), run_time = 2)
        self.play(DienTich.animate.move_to(DOWN * 1 + LEFT * 3.5), MatDoDiemAnh.animate.move_to(DOWN * 1 + RIGHT * 3.5), run_time=1)
        self.play(Transform(DienTich, TrucDienTich), run_time=2)
        self.play(FadeOut(MatDoDiemAnh), FadeIn(MatDoDiemAnh_Image), run_time=2)
        self.play(Transform(Text_3_scene22, Text_5_box_scene22), Write(Text_5_scene22), Transform(background_box_dohoamaytinh, background_box_xulytinhieuso), Uncreate(Text_3_box_scene22), Unwrite(Text_4_scene22), Uncreate(TrucDienTich), FadeOut(MatDoDiemAnh_Image), Unwrite(DienTich), run_time=1)
        self.play(Write(Text_6_scene22), run_time=2)
        self.play(Text_6_scene22.animate.move_to(UP * 1.9), run_time=1)
        self.play(Create(half_circle_scene22), run_time=2)
        self.play(SpinInFromNothing(LamMinAnh_before_Image), run_time=2)
        self.play(LamMinAnh_before_Image.animate.move_to(DOWN * 2.5 + LEFT * 3), run_time=1)
        self.play(half_circle_after_scene22.animate.move_to(RIGHT * 3), SpinInFromNothing(LamMinAnh_after_Image), run_time=2)
        self.play(Uncreate(half_circle_after_scene22), Uncreate(half_circle_scene22), FadeOut(LamMinAnh_after_Image), FadeOut(LamMinAnh_before_Image), Uncreate(background_box_dohoamaytinh), Unwrite(Text_5_scene22), Unwrite(Text_6_scene22), FadeOut(Text_5_box_scene22), Uncreate(background_box_xulytinhieuso))
        self.add(shadow, robot)
        # Animation di chuyển
        run_time = 3
        frames_per_step = 5
        
        for i in range(frames_per_step):
            alpha = i / frames_per_step
            new_pos = interpolate(start_pos, end_pos, alpha)

            leg_angle = 20 * np.sin(2 * PI * alpha * 4)
            arm_angle = 30 * np.sin(2 * PI * alpha * 4 + PI / 2)

            # Tính delta từ vị trí hiện tại đến vị trí mới
            delta = new_pos - robot.get_center()

            # Di chuyển toàn bộ robot cũ sang vị trí mới
            new_robot = robot.copy().shift(delta)

            # Tạo tay/chân mới (gắn đúng vị trí theo new_pos)
            leg_origin = new_pos + DOWN * 0.9
            new_left_leg = Line(leg_origin, leg_origin + LEFT*0.3 + DOWN*0.7).rotate(leg_angle * DEGREES, about_point=leg_origin)
            new_right_leg = Line(leg_origin, leg_origin + RIGHT*0.3 + DOWN*0.7).rotate(-leg_angle * DEGREES, about_point=leg_origin)

            arm_origin = new_pos + UP * 0.5
            new_left_arm = Line(arm_origin, arm_origin + LEFT*0.5 + DOWN*0.5).rotate(arm_angle * DEGREES, about_point=arm_origin)
            new_right_arm = Line(arm_origin, arm_origin + RIGHT*0.5 + DOWN*0.5).rotate(-arm_angle * DEGREES, about_point=arm_origin)

            # Gắn lại tay và chân mới vào robot
            new_robot.submobjects[3] = VGroup(new_left_arm, new_right_arm)
            new_robot.submobjects[4] = VGroup(new_left_leg, new_right_leg)

            # Cập nhật bóng
            new_shadow = shadow.copy().shift(delta)
            new_shadow.stretch_to_fit_width(1.2 - 0.3 * abs(np.sin(2 * PI * alpha * 4)))

            # Cập nhật màn hình
            self.remove(robot, shadow)
            robot = new_robot
            shadow = new_shadow
            self.add(shadow, robot)
            self.wait(run_time / frames_per_step)
            self.add(Text_7_scene22)
            Text_7_scene22.shift(delta)
        self.play(Text_7_scene22.animate.move_to(UP * 3), Create(background_box_robothocvadieukhien), run_time=1)
        self.play(Uncreate(robot), Uncreate(shadow))
        self.add(Text_7_box_scene22)
        self.play(Write(Text_8_scene22), run_time=2)
        circle1_scene13 = Circle(radius=2, color=WHITE).shift(DOWN * 1)
        circle2_scene13 = Circle(radius=1.5, color=WHITE).shift(DOWN * 1)
        line2_scene13 = Line(start=[2.5, 0, 0], end=[0, 0, 0], color=YELLOW, stroke_width=5).shift(LEFT * 2.5 + DOWN * 1)
        diem_quay_scene13 = ORIGIN + DOWN * 1
        self.add(circle1_scene13)
        angle_tracker = ValueTracker(0)
        center = ORIGIN + DOWN * 1

        # Đường tròn nền
        circle = Circle(radius=2, color=WHITE).move_to(center)
        self.add(circle)
        circle1 = Circle(radius=1.5, color=WHITE).move_to(center)
        self.add(circle1)
        circle2 = Circle(radius=1, color=WHITE).move_to(center)
        self.add(circle2)
        circle3 = Circle(radius=0.5, color=WHITE).move_to(center)
        self.add(circle3)

        dot_scene22 = Circle(radius=0.1, color=RED, fill_opacity=1)
        dot_scene22.move_to(center)
        dot_scene22.shift(DOWN * 0.5 + LEFT * 0.5)
        self.add(dot_scene22)

        # Bộ theo dõi góc quay
        angle_tracker = ValueTracker(0)

        # Đoạn thẳng quay, cập nhật theo góc
        rotating_line = always_redraw(lambda: Line(
            start=center,
            end=center + rotate_vector(RIGHT * 2, angle_tracker.get_value()),
            color=YELLOW,
            stroke_width=5
        ))

        # Vùng tô động theo góc
        dynamic_sector = always_redraw(lambda: Sector(
            arc_center=center,
            radius=2,
            angle=angle_tracker.get_value(),
            start_angle=0,
            color=BLUE,
            fill_opacity=0.3,
            stroke_width=0,
        ))

        self.add(dynamic_sector, rotating_line)

        # Animation: tăng góc từ 0 đến 2π
        self.play(
            angle_tracker.animate.set_value(2 * PI),
            run_time=4,
            rate_func=rush_into
        )
        
        self.wait(1)




        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))