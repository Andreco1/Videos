from manim import *
class Naturales(Scene):
    def construct(self):
        dots = [Dot([-2 + n * 1/4, 0, 0], color = BLUE, radius=0.03) for n in range(16)]
        labels = []
        
        self.play(*[Create(dot) for dot in dots], run_time=2)
        dots_even = [dots[2*n] for n in range(8)]
        self.play(*[dots_even[n].animate.set_color(RED) for n in range(8)], run_time=1) 

        self.play(*[Transform(dots[n], dots_even[n // 2 ]) for n in range(16)], run_time=2)


