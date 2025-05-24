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

        x_label.move_to(axes.c2p(axes.x_range[1] + axes.x_range[2]*0.5, 0, 0))
        y_label.move_to(axes.c2p(0, axes.y_range[1] + axes.y_range[2]*0.5, 0))
        z_label.move_to(axes.c2p(0, 0, axes.z_range[1] + axes.z_range[2]*0.5))
        
        axes_center = axes.c2p(np.mean(axes.x_range[:2]), np.mean(axes.y_range[:2]), np.mean(axes.z_range[:2]))
        # set_fixed(x_label, y_label, z_label)
        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        # Write the equation from the func_z (with fixed)
        equation = MathTex(r"z = -0.034x^2 - 0.02y^2 + 5", font_size = 34).to_edge(UP, buff = 0.1)
        set_fixed(equation)

        self.set_camera_orientation(phi = 70 * DEGREES, theta = 45 * DEGREES, frame_center = axes_center, zoom = 0.7)
        self.play(Write(axes), Write(x_label), Write(y_label), Write(z_label), Write(equation), run_time = 1)
        self.wait(2)

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
        self.play(Transform(surface_over_D_copy, domain_D, replace_mobject_with_target_in_scene=True), run_time = 0.4)
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

        dot_x = a + 0.5 + 2
        dot_y = c + 0.5 + 2
        # Chọn ra 1 ô để một dấu chấm nhỏ ở giữa và kéo ô vuông chứa nó lên đến surface thành 1 khối hình hộp chữ nhật đứng thể hiện thể tích tích phân
        center_dot_on_base = Sphere(axes.c2p(dot_x, dot_y, 0), color = color_88bdef, radius = 0.08, fill_opacity = 1)
        self.play(Create(center_dot_on_base), run_time = 0.5)
        self.wait(1)
        dx = 1.0
        dy = 1.0

        h_prism = func_z(dot_x, dot_y) + center_dot_on_base.radius
        if h_prism < 0.01: h_prism = 0.01

        base_vertices_2d = [
            axes.c2p(dot_x - dx / 2, dot_y - dy / 2, 0), # bottom-left
            axes.c2p(dot_x + dx / 2, dot_y - dy / 2, 0), # bottom-right
            axes.c2p(dot_x + dx / 2, dot_y + dy / 2, 0), # top-right
            axes.c2p(dot_x - dx / 2, dot_y + dy / 2, 0)  # top-left
        ]
        base_polygon = Polygon(*base_vertices_2d, stroke_color = color_03ffff, stroke_width = 1.5, fill_color = color_db9512, fill_opacity = 1)
        top_vertices_3d = [axes.c2p(v[0]/axes.x_length*10, v[1]/axes.y_length*10, h_prism) for v in base_vertices_2d]
        base_data_coords = [
            [dot_x - dx / 2, dot_y - dy / 2, 0],
            [dot_x + dx / 2, dot_y - dy / 2, 0],
            [dot_x + dx / 2, dot_y + dy / 2, 0],
            [dot_x - dx / 2, dot_y + dy / 2, 0]
        ]
        top_data_coords = [[x, y, h_prism] for x,y,z_base in base_data_coords]
        world_base_vertices = [axes.c2p(x,y,z) for x,y,z in base_data_coords]
        world_top_vertices = [axes.c2p(x,y,z) for x,y,z in top_data_coords]
        base_face = Polygon(*world_base_vertices, 
                            stroke_color=color_03ffff, stroke_width=1.5, 
                            fill_color=color_db9512, fill_opacity=1.0)
        top_face = Polygon(*world_top_vertices, 
                           stroke_color=color_03ffff, stroke_width=1.5, 
                           fill_color=color_db9512, fill_opacity=1.0)

        side_faces = VGroup()
        for i in range(4):
            idx_next = (i + 1) % 4
            side_face = Polygon(
                world_base_vertices[i], world_base_vertices[idx_next],
                world_top_vertices[idx_next], world_top_vertices[i],
                stroke_color=color_03ffff, stroke_width=1.5,
                fill_color=color_db9512, fill_opacity=1.0
            )
            side_faces.add(side_face)
        solid_prism_manual = VGroup(base_face, top_face, *side_faces)
        dot_on_surface = Dot(axes.c2p(dot_x, dot_y, h_prism), color=color_88bdef, radius=0.08)

        self.play(Create(base_face), run_time=0.7)
        self.wait(0.2)

        x_scale = axes.x_length / (axes.x_range[1] - axes.x_range[0])
        y_scale = axes.y_length / (axes.y_range[1] - axes.y_range[0])
        z_scale = axes.z_length / (axes.z_range[1] - axes.z_range[0])

        prism_width_manim = dx * x_scale
        prism_depth_manim = dy * y_scale
        prism_height_manim = h_prism * z_scale
        initial_prism_height_manim = 0.01 * z_scale
        volumetric_element = Prism(dimensions=[prism_width_manim, prism_depth_manim, initial_prism_height_manim])
        volumetric_element.set_fill(color_db9512, opacity=1.0)
        volumetric_element.set_stroke(color_03ffff, width=1.5)
        target_bottom_center_world = axes.c2p(dot_x, dot_y, 0)
        volumetric_element.move_to(target_bottom_center_world)
        volumetric_element.shift(OUT * initial_prism_height_manim / 2)

        self.play(Create(volumetric_element), run_time=0.5)
        group3d.add(volumetric_element, center_dot_on_base)
        self.wait(0.5)

        final_prism = Prism(dimensions=[prism_width_manim, prism_depth_manim, prism_height_manim])
        final_prism.set_fill(color_db9512, opacity=1.0)
        final_prism.set_stroke(color_03ffff, width=1.5)
        final_prism.move_to(target_bottom_center_world)
        final_prism.shift(OUT * prism_height_manim / 2)

        # Tạo animation cho sphere và prism
        sphere_animation = center_dot_on_base.animate.move_to(axes.c2p(dot_x, dot_y, h_prism))
        prism_animation = Transform(volumetric_element, final_prism, replace_mobject_with_target_in_scene=True)

        self.play(
            prism_animation,
            sphere_animation,
            run_time=2
        )
        if volumetric_element in group3d: group3d.remove(volumetric_element)
        group3d.add(final_prism) # final_prism giờ là đối tượng trong scene
        group3d.add(center_dot_on_base) # Đảm bảo dấu chấm vẫn trong group
        group3d.add(solid_prism_manual, dot_on_surface)

        self.wait(1) # Giảm thời gian chờ

        # Di chuyển camera và scale toàn bộ group
        self.move_camera(phi=75 * DEGREES, theta=-30 * DEGREES, zoom=0.8, frame_center=axes.c2p(dot_x, dot_y, h_prism/2))
        self.wait(0.5)
        self.move_camera(phi=60 * DEGREES, theta=20 * DEGREES, zoom=0.75, frame_center=axes_center)
        self.move_camera(phi=70 * DEGREES, theta=0 * DEGREES, zoom=0.7, frame_center=axes_center)
        
        # self.play(
        #     group3d.animate.scale(1).to_edge(DOWN, buff=-5), # Điều chỉnh buff
        #     run_time=1.25
        # )

        self.move_camera(frame_center=axes_center + (DOWN * -5.0), run_time=1.25)
        self.wait(2)
        
        paragraph_string = r"""
        \begin{minipage}{0.7\textwidth}
        Chúng ta có thể xấp xỉ được thể tích $V$ cần tìm, 
        bằng cách tính tổng các thể tích hình 
        hộp chữ nhật nhỏ với đáy là $D_{ij}$ có diện tích 
        $\Delta A = \Delta x \Delta y$ và chiều cao là $f(x_{ij}^*, y_{ij}^*)$, 
        với $(x_{ij}^*, y_{ij}^*)$ là điểm được chọn trên miền D. 
        Thể tích hình hộp chữ nhật nhỏ khi này bằng: \\[1em]
        \centering
        $f(x_{ij}^*, y_{ij}^*)\Delta A = f(x_{ij}^*, y_{ij}^*)\Delta x \Delta y$
        \end{minipage}
        """

        paragraph_tex = Tex(
            paragraph_string,
            font_size = 32,
            tex_template = VIETNAMESE_TEMPLATE
        )

        paragraph_tex.to_edge(RIGHT, buff = 0.5)
        set_fixed(paragraph_tex)
        self.play(Write(paragraph_tex), run_time = 4)
        self.wait(3)

