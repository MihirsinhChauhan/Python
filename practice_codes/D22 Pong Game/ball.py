from turtle import Turtle
import random
import time

RANDOM_DIR_RiGHT = random.randint(-80, 80)
RANDOM_DIR_LEFT = random.randint(120, 250)
RANDOM_DIR = random.choice([RANDOM_DIR_RiGHT, RANDOM_DIR_LEFT])


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(10)
        self.setheading(RANDOM_DIR)
        # self.move_x = 10
        # self.move_y = 10
        self.sleep = 0.1


    def move(self):
        time.sleep(self.sleep)
        # new_x = self.xcor() + self.move_x
        # new_y = self.ycor() + self.move_y
        # self.goto(new_x,new_y)
        self.forward(10)

    def bounceBack(self):
        # self.move_y *= -1
        self.setheading(-1*self.heading())
    def collisionWithPaddle(self):
        # self.move_x *= -1
        self.sleep *= 0.9

        self.setheading(-1*self.heading())

    def resetBall(self):
        self.sleep = 0.1
        self.goto(0,0)
        time.sleep(1)
        # self.move_y *= -1
        # self.move_x *= -1

