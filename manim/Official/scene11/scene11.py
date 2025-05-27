from manim import *
import numpy as np

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

def set_unfixed(*mobjects):
    for mobject in mobjects:
        mobject.fixed = False
        for submobject in mobject.family_members_with_points():
            submobject.fixed = False

def func_z(x, y):
    return -0.034 * x**2 - 0.02 * y**2 + 5

class Main(CustomThreeDScene):
    def create_riemann_element(self, dot_x, dot_y, axes):
        # INIT
        color_db9512 = "#db9512"
        color_88bdef = "#88bdef"
        color_03ffff = "#03ffff"
        sphere_radius = 0.08
        dx = 1.0
        dy = 1.0
        h_data_sphere_center = func_z(dot_x, dot_y)
        if h_data_sphere_center < 0.01: h_data_sphere_center = 0.01

        x_scale = axes.x_length / (axes.x_range[1] - axes.x_range[0])
        y_scale = axes.y_length / (axes.y_range[1] - axes.y_range[0])
        z_scale = axes.z_length / (axes.z_range[1] - axes.z_range[0])

        prism_width = dx * x_scale
        prism_depth = dy * y_scale
        h_sphere_center = h_data_sphere_center * z_scale
        # Chiều cao = chiều cao + r
        total_height = h_sphere_center + sphere_radius

        sphere = Sphere(
            radius=sphere_radius,
            fill_color=color_88bdef,
        )
        sphere.move_to(axes.c2p(dot_x, dot_y, h_data_sphere_center))

        prism = Prism(dimensions=[prism_width, prism_depth, total_height])
        prism.set_fill(color_db9512, opacity=1.0)
        prism.set_stroke(color_03ffff, width=1.5)
        prism.move_to(axes.c2p(dot_x, dot_y, 0) + OUT * total_height / 2)    

        return VGroup(prism, sphere)

    def construct(self):
        # INIT
        color_db5897 = "#db5897"
        color_03ffff = "#03ffff"
        color_cc00ff = "#cc00ff"
        color_fececa = "#fececa"
        color_e158d0 = "#e158d0"
        color_88bdef = "#88bdef"
        color_db9512 = "#db9512"

        # miền D
        # miền D
        a = 1
        b = 8
        c = 1
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

        x_label.move_to(axes.c2p(axes.x_range[1] + axes.x_range[2]*0.5, 0, 0))
        y_label.move_to(axes.c2p(0, axes.y_range[1] + axes.y_range[2]*0.5, 0))
        z_label.move_to(axes.c2p(0, 0, axes.z_range[1] + axes.z_range[2]*0.5))
        
        axes_center = axes.c2p(np.mean(axes.x_range[:2]), np.mean(axes.y_range[:2]), np.mean(axes.z_range[:2]))
        # set_fixed(x_label, y_label, z_label)
        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        # Write the equation from the func_z (with fixed)
        equation = MathTex(r"z = f(x, y) = -0.034x^2 - 0.02y^2 + 5", font_size = 34).to_edge(UP, buff = 0.1)
        set_fixed(equation)

        self.set_camera_orientation(phi = 70 * DEGREES, theta = 45 * DEGREES, frame_center = axes_center, zoom = 0.7)
        self.add(equation)
        self.play(Write(axes), Write(x_label), Write(y_label), Write(z_label), run_time = 1)
        self.wait(1.2)

        surface_over_D = Surface(
            lambda u, v: axes.c2p(u, v, func_z(u, v)),
            u_range = [a, b],
            v_range = [c, d],
            resolution = (32, 32),
            fill_opacity = 0.5,
            fill_color = color_e158d0,
            stroke_width = 0.5,
            checkerboard_colors = [color_e158d0, color_88bdef]
        )
        self.play(Create(surface_over_D), run_time = 1)
        self.wait(1)

        target_point_coords = (a, (c+d) / 2, func_z(a, (c+d) / 2))
        target_point = axes.c2p(*target_point_coords)
        start_point = target_point + UP * 2.5 + RIGHT * 2.4 + OUT * 2.6
        arrow = Arrow(
            start_point,
            target_point,
            buff = 0,
            stroke_width = 1,
            stroke_color = WHITE
        )
        surface_label = MathTex(r"z = f(x, y)", font_size = 30, color = YELLOW)
        surface_label.next_to(arrow.get_start(), UP, buff = 0.2)
        self.add_fixed_orientation_mobjects(surface_label)
        self.play(FadeIn(arrow), Write(surface_label), run_time = 1)
        self.wait(1.5)
        self.play(FadeOut(arrow), FadeOut(surface_label), run_time = 1)
        
        pt_a = axes.c2p(a, 0, 0)
        pt_b = axes.c2p(b, 0, 0)
        pt_c = axes.c2p(0, c, 0)
        pt_d = axes.c2p(0, d, 0)
        label_a = Tex(r"a", font_size = 30).next_to(pt_a, DOWN, buff = 0.2)
        label_b = Tex(r"b", font_size = 30).next_to(pt_b, DOWN, buff = 0.2)
        label_c = Tex(r"c", font_size = 30).next_to(pt_c, LEFT, buff = 0.2)
        label_d = Tex(r"d", font_size = 30).next_to(pt_d, LEFT, buff = 0.2)
        for label in [label_a, label_b, label_c, label_d]:
            self.add_fixed_orientation_mobjects(label)
        self.play(Write(label_a), Write(label_b), Write(label_c), Write(label_d), run_time=0.5)

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
        # self.wait(0.5)
        # Vẽ miền D
        domain_D = Polygon(
            axes.c2p(a, c, 0),
            axes.c2p(b, c, 0),
            axes.c2p(b, d, 0),
            axes.c2p(a, d, 0),
            color = color_db5897,
            fill_opacity = 0.5,
            stroke_width = 2,
            stroke_color = RED
        )
        surface_over_D_copy = surface_over_D.copy().set_opacity(0)
        self.add(surface_over_D_copy)
        self.play(Transform(surface_over_D_copy, domain_D, replace_mobject_with_target_in_scene=True), run_time = 0.8)
        self.wait(1)
        # set lại camera
        group3d = VGroup(axes, x_label, y_label, z_label, surface_over_D, domain_D, surface_over_D_copy)

        # Chia vùng D ra thành grid các ô vuông nhỏ
        grid_lines = VGroup()
        x_steps = np.arange(a, b + 1, 1)
        y_steps = np.arange(c, d + 1, 1)
        for i in x_steps:
            grid_lines.add(Line(axes.c2p(i, c, 0), axes.c2p(i, d, 0), stroke_width = 1.5, stroke_color = RED))

        for j in y_steps:
            grid_lines.add(Line(axes.c2p(a, j, 0), axes.c2p(b, j, 0), stroke_width = 1.5, stroke_color = RED))
        self.play(Create(grid_lines), run_time = 1)
        group3d.add(grid_lines)
        # self.wait()

        # peak
        all_initial_prisms = VGroup()
        all_final_prisms = VGroup()
        all_initial_spheres = VGroup()
        all_final_spheres = VGroup()
        
        dx = 1.0 # Kích thước ô
        dy = 1.0
        sphere_radius_manim = 0.08 # Bán kính sphere (Manim units)

        # Lấy scales (cần cho initial_prism)
        x_scale = axes.x_length / (axes.x_range[1] - axes.x_range[0])
        y_scale = axes.y_length / (axes.y_range[1] - axes.y_range[0])
        z_scale = axes.z_length / (axes.z_range[1] - axes.z_range[0])
        initial_prism_height_manim = 0.005 * z_scale
        prism_width_manim = dx * x_scale
        prism_depth_manim = dy * y_scale

        # Vòng lặp qua các ô trong miền D (a, b, c, d đã được định nghĩa trước đó)
        for x_val in np.arange(a + dx / 2, b, dx):
            for y_val in np.arange(c + dy / 2, d, dy):
                # Tạo Prism ban đầu (thấp)
                initial_prism = Prism(dimensions=[prism_width_manim, prism_depth_manim, initial_prism_height_manim])
                initial_prism.set_fill("#db9512", opacity=1.0)
                initial_prism.set_stroke("#03ffff", width=1.0)
                initial_prism.move_to(axes.c2p(x_val, y_val, 0) + OUT * initial_prism_height_manim / 2)
                all_initial_prisms.add(initial_prism)

                # Tạo Sphere ban đầu (ở đáy, z=0)
                initial_sphere = Sphere(
                    radius=sphere_radius_manim, 
                    fill_color="#88bdef", 
                    fill_opacity=0.9,
                    stroke_width=1,
                    stroke_color=WHITE,
                    resolution=(16, 8)
                )
                initial_sphere.move_to(axes.c2p(x_val, y_val, 0))
                all_initial_spheres.add(initial_sphere)

                # Tạo Prism và Sphere cuối cùng bằng hàm
                final_element = self.create_riemann_element(x_val, y_val, axes)
                all_final_prisms.add(final_element[0])
                all_final_spheres.add(final_element[1])

        self.play(Create(all_initial_spheres), run_time=1.5)
        self.wait(0.3)

        self.add(all_initial_prisms)

        # các prism sẽ mọc lên, các sphere sẽ bay lên.
        self.play(
            Transform(all_initial_prisms, all_final_prisms),
            Transform(all_initial_spheres, all_final_spheres),
            run_time = 3 
        )

        group3d.add(all_final_prisms, all_final_spheres)
        self.wait(1)

        # Begin rotation
        rotation_time = 8
        flicker_count = 6
        og_opacity = 1.0
        flicker_opacity = 0.1
        mid_opacity = (og_opacity + flicker_opacity) / 2
        amplitude = (og_opacity - flicker_opacity) / 2

        def update_opacity(mobj, alpha):
            new_opacity = mid_opacity + amplitude * np.cos(2 * PI * flicker_count * alpha)
            mobj.set_opacity(new_opacity)

        rotation_animation = self.camera.theta_tracker.animate.set_value(self.camera.theta_tracker.get_value() + 360 * DEGREES)
        flickering_animation = UpdateFromAlphaFunc(surface_over_D, update_opacity)
        self.play(rotation_animation, flickering_animation, run_time = rotation_time)
        surface_over_D.set_opacity(og_opacity)
        self.wait(0.5)
        
        # self.play(
        #     group3d.animate.scale(1).to_edge(DOWN, buff=-5), # Điều chỉnh buff
        #     run_time=1.25
        # )
        # move
        self.move_camera(phi=75 * DEGREES, theta=0* DEGREES, zoom=0.7, frame_center=axes_center)
        self.move_camera(frame_center=axes_center + (DOWN * -5.0), run_time=1.25)
        self.play(surface_over_D.animate.set_opacity(0), run_time=1)
        self.wait(1.5)

        paragraph_string = r"""
        \begin{minipage}{0.7\textwidth}
        Như vậy, khi cộng tất cả những thể tích
        của những hình hộp chữ nhật nhỏ, chúng
        ta sẽ xấp xỉ được \\thể tích $V$ cần tìm:\\
        \centering 
        $$ V \approx \sum_{i=1}^m \sum_{j=1}^n f(x_{ij}^*, y_{ij}^*)\Delta A
        = \sum_{i=1}^m \sum_{j=1}^n f(x_{ij}^*, y_{ij}^*)\Delta x \Delta y $$
        \end{minipage}
        """

        paragraph_tex = Tex(
            paragraph_string,
            font_size = 32,
            tex_template = VIETNAMESE_TEMPLATE
        )

        paragraph_tex.to_edge(RIGHT, buff = 0.5)
        set_fixed(paragraph_tex)
        self.play(Write(paragraph_tex), run_time = 4.5)
        self.wait(3)
