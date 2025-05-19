from manim import *
import numpy as np

class ArtichokeBud(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Tạo hình dạng khối chính
        body = Surface(
            lambda u, v: np.array([
                2.2 * np.cos(u) * np.sin(v),
                2.2 * np.sin(u) * np.sin(v),
                5 * np.cos(v)
            ]),
            u_range=[0, TAU],
            v_range=[0, PI / 2.2],
            resolution=(40, 20),
            fill_opacity=0.05,
            checkerboard_colors=[GREEN, TEAL_D]
        )

        # Gom vào một nhóm
        group = VGroup()
        group.add(body)

        # Vẽ các dải xoắn ốc (đường dẫn khung kính)
        num_strips = 6
        turns = 3
        for i in range(num_strips):
            spiral = VMobject(color=GRAY_B, stroke_width=2)
            spiral.set_points_smoothly([
                np.array([
                    2.2 * np.cos(t + i * TAU / num_strips) * np.sin(t / turns),
                    2.2 * np.sin(t + i * TAU / num_strips) * np.sin(t / turns),
                    5 * np.cos(t / turns)
                ]) for t in np.linspace(0.1, PI * turns / 2.2, 150)
            ])
            group.add(spiral)

        group.shift(UP * 3)  # Dịch toàn bộ khối xuống
        shift_vec = UP * 3
        group.shift(shift_vec)
        self.move_camera(frame_center=shift_vec)
        self.begin_ambient_camera_rotation(rate=0.1)


        self.add(group)
        self.wait(8)
