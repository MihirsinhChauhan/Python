import turtle
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="What's your bet", prompt="Which turtle will win the race! Enter your color ?")
if user_input:
    is_race_on = True

all_turtle =[]
index = 0
for i in range(-5, 4,2):
    tim = Turtle()
    tim.penup()
    tim.shape('turtle')
    color = ['red', 'green', 'blue', 'yellow', 'purple']
    tim.color(color[index])

    tim.goto(-230, i*20)
    all_turtle.append(tim)
    index+=1



while is_race_on:
    for tim in all_turtle:
        move = random.randint(0, 10)
        tim.forward(move)

        if tim.xcor() == 230:
            is_race_on = False
            winning_turtle = tim.pencolor()
            if user_input == winning_turtle:
                print(f"You've won! the {winning_turtle} turtle won the race.")
            else:
                print(f"You've lose! the {winning_turtle} turtle won the race.")




turtle.done()
