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

        #SCENE 18
        # create the axes and the curve
        ax_scene18 = Axes(x_range=[-1, 10], 
                y_range=[-1, 10],
                x_length=6,  # Độ dài trục x (đơn vị màn hình, không phải giá trị)
                y_length=4,  # Độ dài trục y
                 x_axis_config={
                    "include_numbers": False,
                    "tip_width": 0.25,     # rộng mũi tên trục x
                    "tip_height": 0.25     # cao mũi tên trục x
                },  # Tắt số mặc định
                 y_axis_config={
                    "include_numbers": False,
                    "tip_width": 0.25,     # rộng mũi tên trục x
                    "tip_height": 0.25     # cao mũi tên trục x
                })#tạo trục tọa độ
        labels_scene18 = ax_scene18.get_axis_labels(
            x_label=Tex(r"$x$"), y_label=Tex(r"$y$")#tạo nhãn cho các trục
        )
        labels_scene18.shift(DOWN * 1)
        ax_scene18.shift(DOWN * 1)

        a_scene18 = 5  # bán kính trong
        b_scene18 = 6    # bán kính ngoài
        alpha_scene18 = 0.3  # góc alpha (rad)
        beta_scene18 = 0.5   # góc beta (rad)
        origin_scene18 = ax_scene18.c2p(0, 0)

        outer_arc_scene18 = Arc(radius=b_scene18, start_angle=alpha_scene18, angle=beta_scene18 - alpha_scene18, arc_center=origin_scene18)
        inner_arc_scene18 = Arc(radius=a_scene18, start_angle=beta_scene18, angle=-(beta_scene18 - alpha_scene18), arc_center=origin_scene18)


        # Tính điểm đầu dựa trên góc alpha
        left_point_scene18 = origin_scene18 + b_scene18 * np.array([np.cos(alpha_scene18), np.sin(alpha_scene18), 0])
        right_point_scene18 = origin_scene18 + b_scene18 * np.array([np.cos(beta_scene18), np.sin(beta_scene18), 0])

        # Tạo các đoạn thẳng từ origin
        left_line_scene18 = Line(origin_scene18, left_point_scene18)
        right_line_scene18 = Line(origin_scene18, right_point_scene18)

        angle_scene18 = Angle(
            left_line_scene18, right_line_scene18,
            radius=4,
            other_angle=False,      # Lấy góc nhỏ
            quadrant=(1, 1),        # Đặt góc phía trên phải
            color=YELLOW
        )

        outer_points_scene18 = [origin_scene18 + b_scene18 * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(alpha_scene18, beta_scene18, 30)]
        inner_points_scene18 = [origin_scene18 + a_scene18 * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(beta_scene18, alpha_scene18, 30)]

        region_points_scene18 = outer_points_scene18 + inner_points_scene18
        region_scene18 = VMobject()
        region_scene18.set_points_as_corners(region_points_scene18)
        region_scene18.set_fill(RED, opacity=0.5)
        left_line_scene18.set_color(BLUE)
        right_line_scene18.set_color(BLUE)
        outer_arc_scene18.set_color(RED)
        inner_arc_scene18.set_color(RED)

        Text_1_scene18 = Tex(
            r"Khi chuyển từ hệ toạ độ Descartes sang hệ toạ độ cực bằng cách đổi \textbf{$x=rcos\varphi$}, \textbf{$y=rsin\varphi$} sử dụng tính gần đúng của giới hạn khi tính tích phân đối với \textbf{$r$} và \textbf{$\varphi$}, ta có thể viết lại ",
            r"\textbf{$dA = rdrd\varphi$}.",
            font_size=35
        ).shift(UP * 3)



        d_phi_scene18 = CurvedArrow(start_point=[1.2, -1 , 0],  end_point=[1, 0, 0], angle=PI/2, color=WHITE,  stroke_width=2)
        d_phi_scene18.tip.scale(0.5)
        d_A_scene18 = Arrow(start=[4, -0.5, 0], end=[2.6, -0.5, 0], buff=0, stroke_width=2, color=WHITE)
        d_A_scene18.tip.scale(0.5)
        d_r_scene18 = CurvedArrow(start_point=[2.04, -0.5, 0], end_point=[2, 1, 0], angle=PI/2, color=WHITE,  stroke_width=2)
        d_r_scene18.tip.scale(0.5)
        r_d_phi_scene18 = Arrow(start=[2, -2, 0], end=[3, -0.9, 0], buff=0, stroke_width=2, color=WHITE)
        r_d_phi_scene18.tip.scale(0.5)

        d_phi_text_scene18 = Tex(
            r"$d\varphi$",
            font_size=30
        ).move_to([[1, 0, 0]]).shift(UP * 0.1)
        d_A_text_scene18 = Tex(
            r"$dA$",
            font_size=30
        ).move_to([4, -0.5, 0]).shift(RIGHT * 0.3)
        d_r_text_scene18 = Tex(
            r"$dr$",
            font_size=30
        ).move_to([2, 1, 0]).shift(UP * 0.1)
        r_d_phi_text_scene18 = Tex(
            r"$rd\varphi$",
            font_size=30
        ).move_to([2, -2, 0]).shift(LEFT * 0.2 + DOWN * 0.2)

        Text_2_scene18 = Tex(
            r"\textbf{Định lý.}",
            r" Nếu $f(x, y)$ là hàm liên tục trên miền $D = \{(r, \varphi): 0 \leq a \leq r \leq b, \alpha \leq \varphi \leq \beta\}$, với $0 \leq \beta - \alpha \leq 2\pi$, thì:",
            font_size=40
        ).shift(UP * 2)

        Text_3_scene18 = MathTex(
            r"\iint_D f(x, y) \,dx\,dy = \int_{\alpha}^{\beta} \int_{a}^{b} f(r\cos\varphi, r\sin\varphi) \cdot r \,dr\,d\varphi",
            font_size=40
        )

        part_scene18 = VGroup(outer_arc_scene18, inner_arc_scene18, left_line_scene18, right_line_scene18, region_scene18)
        self.play(Create(ax_scene18), run_time=2)
        self.play(Create(labels_scene18), run_time=1)
        self.play(Write(Text_1_scene18), run_time=4)
        self.play(Create(part_scene18), Create(angle_scene18), run_time=4)
        self.play(Create(d_phi_scene18), Create(d_A_scene18), Create(d_r_scene18), Create(r_d_phi_scene18), Write(d_r_text_scene18), Write(d_phi_text_scene18), Write(d_A_text_scene18), Write(r_d_phi_text_scene18), Wiggle(Text_1_scene18[1]), run_time=2)
        self.wait(2)
        self.play(Uncreate(d_phi_scene18), Uncreate(d_A_scene18), Uncreate(r_d_phi_scene18), Uncreate(d_r_text_scene18), Unwrite(r_d_phi_text_scene18), Unwrite(d_A_text_scene18), Unwrite(r_d_phi_text_scene18), Unwrite(d_r_scene18), Uncreate(part_scene18), Unwrite(labels_scene18), Uncreate(ax_scene18), Transform(Text_1_scene18, Text_2_scene18[0]), 
                  Uncreate(angle_scene18), Unwrite(d_phi_text_scene18), run_time=1)
        self.play(Write(Text_2_scene18[1]), run_time=2)
        self.play(Write(Text_3_scene18), run_time=2)
        self.play(Circumscribe(Text_3_scene18))
        self.wait(2)
        self.play(Unwrite(Text_2_scene18[1]), Unwrite(Text_3_scene18), Unwrite(Text_1_scene18), run_time=2)

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))