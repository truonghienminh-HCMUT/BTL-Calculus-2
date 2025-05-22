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

        
