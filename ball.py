from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape('circle')
        