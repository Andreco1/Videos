from manim import *
class DefaultTemplate(MovingCameraScene):
    
    def puntos(self, t, lado):
        dot1 = Dot(point=LEFT, radius=0.03, fill_opacity =0.5)
        dot2 = Dot(point= LEFT, radius=0.03, fill_opacity =0.5).shift(UP*0.5)
        dot3 = Dot(point = LEFT, radius=0.03, fill_opacity =0.5).shift(DOWN*0.5)
        dot4 = Dot(point=RIGHT, radius=0.03, fill_opacity =0.5).shift(UP)
        dot5 = Dot(point= RIGHT, radius=0.03, fill_opacity =0.5).shift(UP*0.3)
        dot6 = Dot(point = RIGHT, radius=0.03, fill_opacity =0.5).shift(DOWN*0.3)
        dot7 = Dot(point = RIGHT, radius=0.03, fill_opacity =0.5).shift(DOWN)

        self.add(dot1, dot2, dot3, dot4, dot5, dot6, dot7)

        self.play(Indicate(dot2, color = RED))
        self.play(Indicate(dot1), color = RED)
        self.play(Indicate(dot3), color = RED)
        self.play(Indicate(dot4, color = RED), run_time=0.5)
        self.play(Indicate(dot5, color =  RED), run_time=0.5)
        self.play(Indicate(dot6, color = RED), run_time=0.5)
        self.play(Indicate(dot7, color = RED), run_time = 0.5)


    def construct(self):
        circle = Circle(stroke_width=0.8).set_color(WHITE).move_to(LEFT*1.2).scale(1)
        circle2 = Circle(stroke_width=0.8).set_color(BLUE_B).move_to(RIGHT*1.2).scale(1)
        elipse = Ellipse(width=1.0, height=2.5, color=BLUE_B, stroke_width=0.8)
        elipse2 = Ellipse(width=1.0, height=2, color=WHITE, stroke_width=0.8)
        elipse2.move_to(LEFT)
        elipse.move_to(RIGHT)

        self.add(circle, circle2)
        self.play(
            self.camera.frame.animate.scale(1.5), 
            Transform(circle2, elipse), 
            Transform(circle, elipse2), 
            run_time=1
        )

        self.wait(1)
        self.puntos(2, 1)
        self.wait(0.5)
        self.play(
            self.camera.frame.animate.scale(0.75)
        )
        fle1 = CurvedArrow(
            LEFT, 
            RIGHT, 
            stroke_width=0.6, 
            stroke_color = WHITE, 
            tip_length = 0.1,
            angle = -0.3
        ).shift(UP*0.75).rotate(15*DEGREES)
        fle2 = CurvedArrow(
            start_point = [-1,0.2,0], 
            end_point = [1,0,0], 
            stroke_width=0.6, 
            stroke_color = WHITE, 
            tip_length = 0.1,
            angle = -0.3
        ).shift(UP*0.05).rotate(15*DEGREES)
        fle3 = CurvedArrow(
            start_point = [-1,0, 0], 
            end_point = [1,-0.3,0], 
            stroke_width=0.6, 
            stroke_color = WHITE, 
            tip_length = 0.1,
            angle = 0.3
        ).shift(DOWN*0.25).rotate(15*DEGREES)


        self.play(Create(fle1),Create(fle2), Create(fle3))
        self.wait(1.5)



