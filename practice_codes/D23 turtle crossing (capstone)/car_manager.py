import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

        self.move()

    def createCars(self):
        if random.randint(1, 6) == 1:
            car = Turtle("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            distance = STARTING_MOVE_DISTANCE
            car.forward(distance)
            # distance += MOVE_INCREMENT


