from manim import *
class Naturales(MovingCameraScene):
    def construct(self):
        dots = [Dot([-15 + n * 1/4, 0, 0], color = BLUE, radius=0.03) for n in range(100)]
        labels = []
        
        self.play(*[Create(dot) for dot in dots], run_time=2)
        dots_even = [dots[2*n] for n in range(50)]
        self.play(*[dots_even[n].animate.set_color(RED) for n in range(50)], run_time=1) 

        self.play(*[Transform(dots[n], dots_even[n // 2 ]) for n in range(100)], run_time=2)
                
        line1 = Line([-20,0,0], [20,0,0], color = RED, stroke_width = 0.5)

        self.play(self.camera.frame.animate.scale(1.5))
        self.wait(1)
        self.play(self.camera.frame.animate.scale(2))
        self.wait(2)
        self.play(*[Transform(dot, line1) for dot in dots], run_time=2)
        self.play(self.camera.frame.animate.scale(0.5))
        self.remove(*[dots[n] for n in range(len(dots))])
        infty = MathTex("\infty")
        self.play(Transform(line1, Circle(color = RED, stroke_width = 0.5)))
        self.play(*[Transform(line1, infty)], run_time=2)
        self.wait(1)
