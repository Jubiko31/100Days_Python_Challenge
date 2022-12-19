import pandas
import turtle

BG_IMAGE = "states_img.gif"

data = pandas.read_csv('50_states.csv')
states = data.state.tolist()

screen = turtle.Screen()
screen.title("U.S. States Quiz Game")
screen.addshape(BG_IMAGE)
turtle.shape(BG_IMAGE)

guessed_states = []

while len(guessed_states) < 50:
    input_field = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="Enter state name")
    answer = input_field.title()
    if answer == 'Exit':
        missed_states = [state for state in states if state not in guessed_states]
        res = pandas.DataFrame(missed_states, columns=["Missed States"])
        res.to_csv('results.csv')
        break
    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())