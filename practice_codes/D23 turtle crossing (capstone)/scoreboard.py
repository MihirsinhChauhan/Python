from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-220, 250)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def nextLevel(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)
