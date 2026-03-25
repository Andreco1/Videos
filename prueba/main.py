from manim import *
import numpy as np


class Escena(MovingCameraScene):
    def construct(self):
        triangle =  NumberPlane(x_range=[-1,1,0.1], x_length=6, y_range=[-1,1,0.1], y_length=6)
        self.play(Create(triangle), run_time=2)
        self.play(self.camera.frame.animate.scale(2))
        copy = triangle.copy()
        copy.apply_complex_function(lambda z : np.log(z))
        self.play(Transform(triangle, copy), run_time=3)