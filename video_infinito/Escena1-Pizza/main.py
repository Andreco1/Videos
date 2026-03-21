from manim import *

class Pizza(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.5)
        self.reparto(5, 5)
        self.wait(1)
        self.clear()
        self.reparto(5, 4)
        self.wait(1)
        self.clear()
        self.reparto(4, 5)

    def reparto(self, rebanadas, puntos):
        Sectores_filled =[ 
            AnnularSector(
            inner_radius = 0.0,
            outer_radius = 0.5,
            start_angle = -2*PI+n*2*PI/rebanadas,
            angle = -2*PI/rebanadas,
            color = BLUE,
            fill_opacity = 0.5).shift(LEFT)
            for n in range(rebanadas)
        ]
        Sectores_stroke =[ 
            AnnularSector(
            inner_radius = 0.0,
            outer_radius = 0.5,
            start_angle = -2*PI+n*2*PI/rebanadas,
            angle = -2*PI/rebanadas,
            color = BLUE,
            stroke_width=0.8,
            fill_opacity = 0.0).shift(LEFT)
            for n in range(rebanadas)
        ]

        self.play(*[Create(sector) for sector in Sectores_stroke])
        for n in range(rebanadas):
            self.play(Create(Sectores_filled[n]), run_time=0.5)
        
        
        dots = [Dot([2, 1 -  3*n/puntos, 0], radius=0.03) for n in range(puntos)]
        self.play(*[Create(dot) for dot in dots])

        m = min(rebanadas, puntos) 
        for n in range(m):
            self.play(Sectores_filled[n].animate.move_to(dots[n]), Sectores_stroke[n].animate.move_to(dots[n]), run_time=0.5)


