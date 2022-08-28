import turtle
import pandas

screen = turtle.Screen()

screen.title("US state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess = turtle.textinput(title="Guess the state", prompt="What's the another state name?").title()
guessed_state = []
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
score = 0
while True:

    if guess in states:
        guessed_state.append(guess)
        score += 1
        t = turtle.Turtle()
        t.ht()
        t.penup()
        t.goto(int(data[data.state == guess].x), int(data[data.state == guess].y))
        t.write(guess, align="center", font=("Courier", 10, "normal"))
    guess = turtle.textinput(title=f"{score}/50 States correct", prompt="What's the another state name?").title()


    if score == 50 or guess == "Exit":
        break
stateToLearn = [state for state in states if state not in guessed_state]

state_to_learn = pandas.DataFrame({"state to learn":stateToLearn})
state_to_learn.to_csv("state_to_learn.csv")
