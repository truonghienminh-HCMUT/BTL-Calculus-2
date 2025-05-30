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

class thanhvien_new(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
         
        #SCENE 2: TABLE OF CONTENTS
        TEXT_scene24 = Tex(r"\textbf{VIDEO ĐƯỢC THỰC HIỆN BỞI NHÓM NM02 LỚP CN01 DƯỚI SỰ HƯỚNG DẪN CỦA THẦY TRƯƠNG VĂN TRÍ}", font_size=35)
        TEXT_1_scene24 = Tex(r"THÀNH VIÊN NHÓM NM02", font_size=50)
        TEXT_2_scene24 = Tex(r"THÀNH VIÊN NHÓM NM02", font_size=40).shift(UP * 3)
        ThanhVien1 = Tex(r"Phạm Nguyễn Thiên Ân - 2452112", font_size=40).shift(UP * 2)
        ThanhVien2 = Tex(r"Lê Anh Khoa - 2411599", font_size=40).shift(UP * 1)
        ThanhVien3 = Tex(r"Trần Ngọc Phương Mai - 2452720", font_size=40)
        ThanhVien4 = Tex(r"Trương Hiển Minh - 2452771", font_size=40).shift( DOWN * 1)
        ThanhVien5 = Tex(r"Nguyễn Võ Hoàng Sơn - 2453128", font_size=40).shift( DOWN * 2)
        ThanhVien6 = Tex(r"Lê Anh Thư - 2453217", font_size=40).shift( DOWN * 3)

        MucLuc = VGroup( ThanhVien1, ThanhVien2, ThanhVien3, ThanhVien4, ThanhVien5, ThanhVien6, TEXT_1_scene24)

        self.play(Write(TEXT_scene24), run_time=2)
        self.wait(1)
        self.play(FadeOut(TEXT_scene24))
        self.play(Write(TEXT_1_scene24), run_time=2)
        self.wait(1)
        self.play(Transform(TEXT_1_scene24, TEXT_2_scene24), run_time=1)
        self.play(Write(ThanhVien1), Write(ThanhVien2), Write(ThanhVien3), Write(ThanhVien4), Write(ThanhVien5), Write(ThanhVien6),  run_time=2)
        self.play(FadeOut(MucLuc))


        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.remove_updater(update_curve)

        # self.play(Restore(self.camera.frame))
