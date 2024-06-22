from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
       super().__init__()
       self = Turtle()
       self.color('white')
       self.shape('square')
       self.shapesize(4, 1, 0)
       self.penup()
       self.goto(350, 0)
       
    def go_up(self):
        new_y = self.ycor() + 20.0
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20.0
        self.goto(self.xcor(), new_y)







