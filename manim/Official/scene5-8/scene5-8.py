from manim import *
import textwrap

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
# config.enable_wireframe = True
# Idea: Tạo một trục tọa độ 3D với các nhãn cố định, không bị ảnh hưởng bởi sự thay đổi góc nhìn của camera.
# Vẽ mặt 3D và miền đóng D tạo thành một khối \Omega.
# Sau đó, thu nhỏ hình lại và di chuyển về bên trái.
# Phần còn trống sẽ viết lý thuyết.
class CustomCamera(ThreeDCamera):
    def transform_points_pre_display(self, mobject, points):
        return points if getattr(mobject, "fixed", False) else super().transform_points_pre_display(mobject, points)

class CustomThreeDScene(ThreeDScene):
    def __init__(self, **kwargs):
        super().__init__(camera_class=CustomCamera, **kwargs)

def set_fixed(*mobjects):
    for mobject in mobjects:
        mobject.fixed = True
        for submobject in mobject.family_members_with_points():
            submobject.fixed = True

def func_z(x, y):
    return 0.05 * x**2 + 0.5 * y

class Main(CustomThreeDScene):
    def construct(self):
        # INIT
        color_db5897 = "#db5897"
        color_03ffff = "#03ffff"
        color_cc00ff = "#cc00ff"
        color_fececa = "#fececa"
        color_e158d0 = "#e158d0"
        color_88bdef = "#88bdef"


        title = Tex(r"\textbf{I. ĐỊNH NGHĨA TÍCH PHÂN KÉP}", font_size=70)
        subtitle = Tex(r"\textbf{1.1 Đặt vấn đề}", font_size=60)
        title.set_color_by_gradient(color_03ffff, color_cc00ff)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.5)
        
        self.play(Write(title_group), run_time=1)
        self.wait(1)
        self.play(FadeOut(title_group), run_time=0.5)
        self.wait(0.5)

        # miền D
        a = 2
        b = 8
        c = 3
        d = 8

        axes = ThreeDAxes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            z_range=[0, 7, 1],
            x_length=6,
            y_length=6,
            z_length=6,
        )
        x_label = MathTex(r"x").set_color(RED).scale(0.8)
        y_label = MathTex(r"y").set_color(GREEN).scale(0.8)
        z_label = MathTex(r"z").set_color(BLUE).scale(0.8)

        x_label.move_to(axes.c2p(axes.x_range[1] + axes.x_range[2], 0, 0))
        y_label.move_to(axes.c2p(0, axes.y_range[1] + axes.y_range[2], 0))
        z_label.move_to(axes.c2p(0, 0, axes.z_range[1] + axes.z_range[2]))
        
        axes_center = axes.c2p((axes.x_range[0]+axes.x_range[1])/2, (axes.y_range[0]+axes.y_range[1])/2, (axes.z_range[0]+axes.z_range[1])/2)

        self.set_camera_orientation(phi=0, theta=-90 * DEGREES, frame_center = 10 * OUT)
        self.play(Write(axes), run_time=0.4)
        self.move_camera(phi=70 * DEGREES, frame_center = axes_center, zoom=0.5)
        self.wait(0.01)
        self.move_camera(theta=45 * DEGREES, frame_center = axes_center, zoom=0.7)
        # self.move_camera(phi=60 * DEGREES, theta= 45 * DEGREES, frame_center = axes_center, zoom=0.6)
        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        self.play(Write(x_label), Write(y_label), Write(z_label), run_time=1)
        self.wait(1)
        self.begin_ambient_camera_rotation(rate = PI/5)
        self.wait(5)

        # --- Vẽ hình các kiểu ---
        # Vẽ các điểm a, b, c, d
        pt_a = axes.c2p(a, 0, 0)
        pt_b = axes.c2p(b, 0, 0)
        pt_c = axes.c2p(0, c, 0)
        pt_d = axes.c2p(0, d, 0)
        label_a = Tex(r"a", font_size = 30).next_to(pt_a, DOWN, buff = 0.15)
        label_b = Tex(r"b", font_size = 30).next_to(pt_b, DOWN, buff = 0.15)
        label_c = Tex(r"c", font_size = 30).next_to(pt_c, LEFT, buff = 0.15)
        label_d = Tex(r"d", font_size = 30).next_to(pt_d, LEFT, buff = 0.15)
        for label in [label_a, label_b, label_c, label_d]:
            self.add_fixed_orientation_mobjects(label)
        
        self.play(Write(label_a), Write(label_b), Write(label_c), Write(label_d), run_time=0.5)
        self.wait(0.5)

        # Vẽ mặt cong
        surface = Surface(
            lambda u, v: axes.c2p(u, v, func_z(u, v)),
            u_range=[axes.x_range[0], axes.x_range[1]],
            v_range=[axes.y_range[0], axes.y_range[1]],
            resolution=(48, 24),
            fill_opacity = 0.5,
            stroke_width = 1.5
        )
        self.play(Create(surface), run_time=2)
        self.wait(1)

        # Vẽ các đường chiếu từ các điểm a, b, c, d xuống mặt cong
        P1 = axes.c2p(a, c, 0)
        P2 = axes.c2p(b, c, 0)
        P3 = axes.c2p(b, d, 0)
        P4 = axes.c2p(a, d, 0)

        dashed_lines_to_D = VGroup(
            DashedLine(pt_a, P1, stroke_width = 1.5),
            DashedLine(pt_a, P4, stroke_width = 1.5),
            DashedLine(pt_b, P2, stroke_width = 1.5),
            DashedLine(pt_b, P3, stroke_width = 1.5),
            DashedLine(pt_c, P1, stroke_width = 1.5),
            DashedLine(pt_c, P2, stroke_width = 1.5),
            DashedLine(pt_d, P3, stroke_width = 1.5),
            DashedLine(pt_d, P4, stroke_width = 1.5),
        )

        self.play(Write(dashed_lines_to_D), run_time=1)
        self.wait(0.5)

        # Vẽ miền D
        domain_D = Polygon(P1, P2, P3, P4, color = color_db5897, fill_opacity = 0.5, stroke_width = 2, stroke_color = RED)
        label_domain_D = MathTex(r"\mathcal{D}", font_size = 30).move_to(domain_D.get_center())
        self.add_fixed_orientation_mobjects(label_domain_D)

        self.play(Create(domain_D), Write(label_domain_D), run_time=1)
        self.wait(1)

        # Chiếu rồi cắt hình
        P1z = axes.c2p(a, c, func_z(a, c))
        P2z = axes.c2p(b, c, func_z(b, c))
        P3z = axes.c2p(b, d, func_z(b, d))
        P4z = axes.c2p(a, d, func_z(a, d))

        projection_lines = VGroup(
            DashedLine(P1, P1z, stroke_width = 1.5),
            DashedLine(P2, P2z, stroke_width = 1.5),
            DashedLine(P3, P3z, stroke_width = 1.5),
            DashedLine(P4, P4z, stroke_width = 1.5),
        )
        self.play(Create(projection_lines), run_time=1)

        surface_over_D = Surface(
            lambda u, v: axes.c2p(u, v, func_z(u, v)),
            u_range=[a, b],
            v_range=[c, d],
            resolution=(32, 16),
            fill_opacity=0.5,
            color=color_db5897,
            stroke_width=1.5
        )
        self.play(
            FadeOut(surface, shift = DOWN * 5, run_time = 1.5),
            FadeIn(surface_over_D, shift = DOWN * 0.5),
        )
        self.wait(5)

        # Di chuyển sao cho trục về bên trái màn hình (vẫn quay)
        # Để phần bên phải màn hình có thể viết lý thuyết
        self.move_camera(phi=70 * DEGREES, theta=0 * DEGREES, zoom=0.7)
        self.stop_ambient_camera_rotation()
        # self.set_camera_orientation(phi=70 * DEGREES, theta=0 * DEGREES, frame_center = axes_center, zoom=0.7)

        # Group lại để di chuyển
        label_domain_D.clear_updaters()
        group3d = VGroup(axes, x_label, y_label, z_label, domain_D, label_a, label_b, label_c, label_d, label_domain_D, surface_over_D, dashed_lines_to_D, projection_lines)
        scale = 1
        self.play(
            group3d.animate.scale(scale).to_edge(DOWN, buff = -5),
            run_time=2
        )
        # self.begin_ambient_camera_rotation(rate = PI/10)
        self.wait(0.5)
        # In chữ

        theory_description_0 = Tex(
            r"\parbox{6cm}{"
            r"Cho $z = f(x, y)$ là hàm số xác định trên miền đóng $\mathcal{D} = \{(x,y), \mathbb{R}^2 : a \leq x \leq b, c \leq y \leq d\}$. "
            r"$\Omega$ là vật thể được giới hạn bởi:\\ $\Omega = \{(x,y,z) \in \mathbb{R}^3 : 0 \leq z \leq f(x,y), (x,y) \in \mathcal{D}\}$"
            r"}",
            font_size=40,
            color=WHITE,
            tex_environment=None
        )
        theory_group_0 = VGroup(theory_description_0).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.3
        )
        theory_group_0.to_edge(RIGHT, buff=1)
        set_fixed(theory_group_0)

        self.play(Write(theory_group_0), run_time=2)
        self.wait(7)
        self.play(Unwrite(theory_group_0), run_time=1.5)
        self.wait(0.5)

        self.play(FadeOut(group3d))
        sub_1_2 = Tex(r"\textbf{1.2 Giải quyết bài toán}", font_size=60)
        set_fixed(sub_1_2)
        self.play(Write(sub_1_2), run_time=1)
        self.wait(1)
        self.play(FadeOut(sub_1_2), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(group3d))

        theory_description_1 = Tex(
            r"\parbox{6cm}{"
            r"Vậy ta muốn tìm thể tích của vật thể $\Omega$ thì xử lí bài toán như thế nào ?"
            r"}",
            font_size=40,
            color=WHITE,
            tex_environment=None
        )
        theory_group_1 = VGroup(theory_description_1).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.3
        )
        theory_group_1.to_edge(RIGHT, buff=1)
        set_fixed(theory_group_1)

        self.play(Write(theory_group_1), run_time=2)
        self.wait(5)
        self.play(Unwrite(theory_group_1), run_time=0.5)
        self.wait(0.5)
        # self.play(Uncreate(group3d), run_time=0.5)











































        theory_description_2 = Tex(
            r"\parbox{6cm}{" 
            r"Hãy nhìn vào miền $\mathcal{D}$ là hình chiếu vuông góc của hàm $z = f(x, y)$ lên mặt phẳng Oxy. "
            r"Tại đây chiếu vuông góc miền $\mathcal{D}$ lên trục Ox ta có được miền $[a, b]$, và chiếu lên Oy, ta có được miền $[c, d]$."
            r"}",
            font_size=40,
            color=WHITE,
            tex_environment=None
        )

        theory_group_2 = VGroup(theory_description_2).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.3
        )
        theory_group_2.to_edge(RIGHT, buff=1)

        set_fixed(theory_group_2)

        self.play(Write(theory_group_2), run_time=2)

        self.wait(8)

        self.play(Unwrite(theory_group_2), run_time=1.5)







