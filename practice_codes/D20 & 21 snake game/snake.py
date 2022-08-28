from turtle import Turtle

STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.addSegments(position)

    def addSegments(self, position):
        body = Turtle(shape="square")
        body.shapesize(0.5, 0.5)
        body.penup()
        body.color("white")
        body.goto(position)
        self.snake_body.append(body)

    def extend(self):
        self.addSegments(self.snake_body[-1].position())
        self.addSegments(self.snake_body[-1].position())

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_cor = self.snake_body[i - 1].position()
            self.snake_body[i].goto(new_cor)

        self.head.forward(10)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, -280)
        self.color("white")
        self.speed(0)
        self.drawBorder()

    def drawBorder(self):
        self.forward(285)
        self.left(90)
        self.forward(555)
        self.left(90)
        self.forward(570)
        self.left(90)
        self.forward(555)
        self.left(90)
        self.forward(285)
