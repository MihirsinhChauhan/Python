import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fd():
    tim.forward(10)
def move_bd():
    tim.backward(10)
def turn_right():
    tim.right(10)
def turn_left():
    tim.left(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(key="w",fun=move_fd)
screen.onkey(key="s",fun=move_bd)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=clear)


turtle.done()