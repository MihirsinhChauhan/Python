from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        with open("data.txt") as highScore:
            self.high_score = int(highScore.read())
        self.score = 0
        self.updateScore()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt",mode="w") as highScore:
                highScore.write(str(self.score))

    def gameOver(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def updateScore(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.score += 1
        return self.score
