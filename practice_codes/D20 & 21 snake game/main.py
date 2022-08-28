from turtle import Screen
from food import Food
from snake import Snake, Border
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

is_game_on = True
snake = Snake()
border = Border()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food and extend
    if snake.head.distance(food) < 15:
        food.refresh()
        score.updateScore()
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -275:
        score.reset()
        is_game_on = False
        score.gameOver()

    # Detect tail collision
    for body in snake.snake_body[1:]:

        if snake.head.distance(body) < 5:
            is_game_on = False
            score.gameOver()

screen.exitonclick()
