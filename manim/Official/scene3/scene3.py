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

def get_artichoke_radius(v, H_total, R_base, R_max_bulge, H_max_bulge, R_top_tip):
    if H_total <= 0: return 0.01
    v = np.clip(v, 0, H_total)
    radius = 0
    if v <= H_max_bulge:
        if H_max_bulge < 1e-6:
            radius = R_max_bulge
        else:
            denominator_a = H_max_bulge**2
            if abs(denominator_a) < 1e-9:
                radius = R_base + (R_max_bulge - R_base) * (v / H_max_bulge if H_max_bulge > 1e-7 else 0)
            else:
                a = (R_base - R_max_bulge) / denominator_a
                radius = a * (v - H_max_bulge)**2 + R_max_bulge
    else:
        denominator_b_val = (H_total - H_max_bulge)
        if abs(denominator_b_val) < 1e-6:
            radius = R_top_tip
        else:
            denominator_b_sq = denominator_b_val**2
            if abs(denominator_b_sq) < 1e-9:
                radius = R_top_tip
            else:
                b = (R_top_tip - R_max_bulge) / denominator_b_sq
                radius = b * (v - H_max_bulge)**2 + R_max_bulge
    return max(0.001, radius)

class scene3(CustomThreeDScene):
    def construct(self):
        # General param
        H_total = 4.0
        R_base = 2.0
        R_max_bulge = 2.4
        H_max_bulge = H_total * 0.35
        R_top_tip = 0.5

        # Thông số spiral
        N_spirals = 14
        total_twist_angle = 1.8 * PI
        twist_factor = total_twist_angle / H_total if H_total > 0 else 0
        dir1, dir2 = 0.6, -1

        line_stroke_width = 1.0 
        line_color = color_gradient(["#e158d0", "#88bdef"], 10)
        horizontal_lines_vgroup = VGroup()
        spiral_lines_vgroup = VGroup()

        self.set_camera_orientation(phi=80 * DEGREES, theta = -70 * DEGREES, focal_distance=9.5)

        num_rings = 20
        ring_resolution = 50
        height_steps = np.linspace(0, H_total, num_rings)

        for z_val in height_steps:
            current_r = get_artichoke_radius(z_val, H_total, R_base, R_max_bulge, H_max_bulge, R_top_tip)
            if current_r < 0.001:
                continue
            ring_points = []
            for angle_rad in np.linspace(0, 2 * PI, ring_resolution, endpoint=False):
                x = current_r * np.cos(angle_rad)
                y = current_r * np.sin(angle_rad)
                ring_points.append([x, y, z_val])

            if ring_points:
                ring_points.append(ring_points[0])
                horizontal_ring = VMobject(stroke_color=line_color, stroke_width=line_stroke_width * 0.8)
                horizontal_ring.set_points_as_corners(np.array(ring_points))
                horizontal_lines_vgroup.add(horizontal_ring)

        # Spiral lines
        spiral_res = 60
        z_points = np.linspace(0, H_total, spiral_res)


        # dir1 dir2
        for direction in [dir1]:
            for i in range(N_spirals):
                start_angle = i * (2 * PI / N_spirals)
                spiral_points = []
                for z_val in z_points:
                    current_r = get_artichoke_radius(z_val, H_total, R_base, R_max_bulge, H_max_bulge, R_top_tip)
                    current_phi = start_angle + direction * twist_factor * z_val
                    x = current_r * np.cos(current_phi)
                    y = current_r * np.sin(current_phi)
                    if current_r < 0.005 and not (np.isclose(z_val, H_total) or np.isclose(z_val, 0)):
                        spiral_points.append([0, 0, z_val])
                    else:
                        spiral_points.append([x, y, z_val])

                # bỏ duplicate points
                unique_points = []
                for point in spiral_points:
                    if not unique_points or not np.allclose(point, unique_points[-1], atol=1e-3):
                        unique_points.append(point)

                if len(unique_points) > 1:
                    spiral_line = VMobject(stroke_color=line_color, stroke_width=line_stroke_width)
                    spiral_line.set_points_as_corners(np.array(unique_points))
                    spiral_lines_vgroup.add(spiral_line)

        # Center
        all_mobjects = VGroup(horizontal_lines_vgroup, spiral_lines_vgroup)
        if all_mobjects.submobjects:
            temp_group = VGroup()
            if horizontal_lines_vgroup.submobjects:
                temp_group.add(horizontal_lines_vgroup)
            if spiral_lines_vgroup.submobjects:
                temp_group.add(spiral_lines_vgroup)

            if temp_group.submobjects:
                center_point = temp_group.get_center()
                horizontal_lines_vgroup.shift(-center_point)
                spiral_lines_vgroup.shift(-center_point)

        question = Tex(r"Các bạn có biết Bông hoa Atiso ở quảng trường Lâm Viên Đà Lạt hay không?", font_size=38).to_edge(UP)
        set_fixed(question)
        self.play(Write(question))

        self.play(Create(horizontal_lines_vgroup), run_time=2)
        self.play(Create(spiral_lines_vgroup), run_time=2.5)
        self.wait(0.5)
        self.play(Uncreate(horizontal_lines_vgroup), run_time=1)

        self.begin_ambient_camera_rotation(rate=PI/4, about="theta")
        self.wait(9)
        self.stop_ambient_camera_rotation()