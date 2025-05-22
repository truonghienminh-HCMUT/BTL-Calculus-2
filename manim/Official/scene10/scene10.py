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

        x_label.move_to(axes.c2p(axes.x_range[1] + axes.x_range[2], 0, 0))
        y_label.move_to(axes.c2p(0, axes.y_range[1] + axes.y_range[2], 0))
        z_label.move_to(axes.c2p(0, 0, axes.z_range[1] + axes.z_range[2]))
        
        axes_center = axes.c2p((axes.x_range[0]+axes.x_range[1])/2, (axes.y_range[0]+axes.y_range[1])/2, (axes.z_range[0]+axes.z_range[1])/2)
        # set_fixed(x_label, y_label, z_label)
        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)

        self.set_camera_orientation(phi = 70 * DEGREES, theta = 45 * DEGREES, frame_center = axes_center, zoom = 0.7)
        self.play(Write(axes), Write(x_label), Write(y_label), Write(z_label), run_time = 1)
        self.wait(2)

        surface_over_D = Surface(
            lambda u, v: axes.c2p(u, v, func_z(u, v)),
            u_range = [a, b],
            v_range = [c, d],
            resolution = (1, 1),
            fill_opacity = 0.5,
            fill_color = color_e158d0,
            stroke_width = 1.5,
            checkerboard_colors = [color_e158d0, color_88bdef]
        )
        self.play(FadeIn(surface_over_D), run_time = 2)
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
        surface_over_D_copy = surface_over_D.copy()
        self.play(Transform(surface_over_D_copy, domain_D), run_time = 0.4)
        self.wait(1)
        # set lại camera
        group3d = VGroup(axes, x_label, y_label, z_label, surface_over_D, domain_D, surface_over_D_copy)

        # Chia vùng D ra thành grid các ô vuông nhỏ
        grid_lines = VGroup()
        for i in range(a, b, 1):
            for j in range(c, d, 1):
                grid_lines.add(Line(axes.c2p(i, c, 0), axes.c2p(i, d, 0), stroke_width = 1.5, stroke_color = RED))

        for j in range (c, d, 1):
            for i in range (a, b, 1):
                grid_lines.add(Line(axes.c2p(a, j, 0), axes.c2p(b, j, 0), stroke_width = 1.5, stroke_color = RED))
        self.play(Create(grid_lines), run_time = 1)
        # self.wait()

        dot_x = (a+b)/2 + 0.5 - 1
        dot_y = (c+d)/2 + 2
        # Chọn ra 1 ô để một dấu chấm nhỏ ở giữa và kéo ô vuông chứa nó lên đến surface thành 1 khối hình hộp chữ nhật đứng thể hiện thể tích tích phân
        dot = Dot(axes.c2p(dot_x, dot_y, 0), color = color_88bdef, radius = 0.08)
        self.play(Create(dot), run_time = 1)
        self.wait(1)

        sq_side_length = 1.0

        p_bl_base_world = axes.c2p(dot_x - sq_side_length / 2, dot_y - sq_side_length / 2, 0)
        p_br_base_world = axes.c2p(dot_x + sq_side_length / 2, dot_y - sq_side_length / 2, 0)
        p_tr_base_world = axes.c2p(dot_x + sq_side_length / 2, dot_y + sq_side_length / 2, 0)
        p_tl_base_world = axes.c2p(dot_x - sq_side_length / 2, dot_y + sq_side_length / 2, 0)

        base_of_prism = Polygon(
            p_bl_base_world, p_br_base_world, p_tr_base_world, p_tl_base_world,
            stroke_color = color_03ffff,
            stroke_width = 2.0,
            fill_color = color_db9512,
            fill_opacity = 1
        )
        prism = VGroup(base_of_prism, dot)
        group3d.add(prism)
        self.play(Create(prism))
        self.wait(1)
        top_face_moving = prism.copy()

        h_data = func_z(dot_x, dot_y)
        if h_data < 0.01 : h_data = 0.01

        init_center_world = axes.c2p(dot_x, dot_y, 0)
        target_center_world = axes.c2p(dot_x, dot_y, h_data)
        z_shift_vector_world = target_center_world - init_center_world
        vertices_base_world = base_of_prism.get_vertices()
        vertical_edges = VGroup()
        # vertical_edges.add(dot)
        final_top_verttices_world = [v + z_shift_vector_world for v in vertices_base_world]
        for i in range(len(vertices_base_world)):
            start = vertices_base_world[i]
            edge = Line(start, start, stroke_color = color_03ffff, stroke_width = 2.0)
            vertical_edges.add(edge)

        self.add(top_face_moving, vertical_edges)
        self.play(
            dot.animate.shift(z_shift_vector_world),
            top_face_moving.animate.shift(z_shift_vector_world),
            AnimationGroup(*[
                vertical_edges[i].animate.put_start_and_end_on(vertices_base_world[i], final_top_verttices_world[i])
                for i in range(len(vertical_edges))
            ]),
            run_time = 2
        )
        group3d.add(top_face_moving, vertical_edges, grid_lines) # Added grid_lines here bc i forgor
        self.wait(3)

        self.move_camera(phi = 70 * DEGREES, theta = 0 * DEGREES, zoom = 0.7)
        scale = 1
        self.play(
            group3d.animate.scale(scale).to_edge(DOWN, buff = -5),
            run_time = 1.25
        )
        self.wait(0.5)
        
        