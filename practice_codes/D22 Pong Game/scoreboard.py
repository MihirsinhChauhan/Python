from  turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(-100,200)
        self.p1Score = 0
        self.write(self.p1Score,align="center",font=("Courier",80,"normal"))
        self.goto(100, 200)
        self.p2Score = 0
        self.write(self.p2Score, align="center", font=("Courier", 80, "normal"))

    def updateScore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p2Score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.p1Score, align="center", font=("Courier", 80, "normal"))
