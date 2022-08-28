from turtle import Turtle
UP = 90

class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.shapesize(stretch_wid=0.5,stretch_len=5)
        self.setheading(UP)
        self.color("white")
        self.penup()
        self.goto(x,y)

    def moveUp(self):

        if self.ycor() <= 200:
            self.forward(50)

    def moveDown(self):
        if self.ycor() >= -200:
            self.backward(50)
