from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()

# Creating player 1
player1 = Paddle(380, 0)  # right side
screen.onkey(player1.moveUp, "Up")
screen.onkey(player1.moveDown, "Down")

# Creating player 2
player2 = Paddle(-380, 0)  # left side
screen.onkey(player2.moveUp, "w")
screen.onkey(player2.moveDown, "s")

# Creatin Ball
ball = Ball()

# Score
score = ScoreBoard()
is_game_on = True
i = 1
# quit
def gameOver():
    global is_game_on
    is_game_on = False

screen.onkey(fun=gameOver,key="q")
while is_game_on:
    ball.move()
    # Detect collision with side walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceBack()
    # Detect collision with paddle
    if ball.distance(player1) <= 30 and ball.xcor() > 360:
        ball.collisionWithPaddle()
    elif ball.distance(player1) > 30 and ball.xcor() > 400:
        score.p2Score += 1
        score.updateScore()
        ball.resetBall()

    if ball.distance(player2) <= 50 and ball.xcor() < -360:
        ball.collisionWithPaddle()
    elif ball.distance(player2) > 50 and ball.xcor() < -400:
        score.p1Score += 1
        score.updateScore()
        ball.resetBall()

    screen.update()
quit()

