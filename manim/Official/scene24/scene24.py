from manim import *
import numpy as np

class HalfSpherePlot(ThreeDScene):
    def construct(self):
        # Thiết lập hệ trục tọa độ 3D
        axes = ThreeDAxes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            z_range=[-10, 2, 1],
            axis_config={"color": WHITE}
        )
        
        # Định nghĩa hàm số z = -sqrt(25 - x^2 - y^2)
        def half_sphere(x, y):
            return -np.sqrt(np.clip(25 - x**2 - y**2, 0, None))
        
        # Tạo bề mặt đồ thị
        surface = Surface(
            lambda x, y: axes.c2p(x, y, half_sphere(x, y)),
            u_range=[-5, 5],  # Giới hạn x
            v_range=[-5, 5],  # Giới hạn y
            resolution=(50, 50),  # Độ phân giải cao để mượt
            fill_opacity=0.8,
            fill_color=BLUE,
            stroke_width=0.2
        )
        
        # Thêm nhãn trục
        labels = axes.get_axis_labels(
            MathTex("x").scale(0.7), 
            MathTex("y").scale(0.7), 
            MathTex("z").scale(0.7)
        )
        
        # Thiết lập camera và hiển thị
        self.set_camera_orientation(phi=60*DEGREES, theta=-45*DEGREES)
        self.add(axes, labels, surface)
        self.begin_ambient_camera_rotation(rate=0.1)  # Tự động xoay
        self.wait(6)  # Hiển thị trong 6 giây