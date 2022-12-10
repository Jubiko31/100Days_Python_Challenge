from turtle import Turtle, Screen
from random import randint

race_on = False
screen = Screen()
screen.setup(width = 600, height = 500)
bet = screen.textinput(title='Place your bet', prompt='Which turtle will win the race? Enter the color: ')

colors = ["red", "orange", "purple", "blue", "green", "yellow"]
x_positions = []
y_positions = [90, 60,30, 0,-30,-60]
turtles = []

for turtle_index in range(0, 6):
    leonardo = Turtle(shape = "turtle")
    leonardo.color(colors[turtle_index])
    leonardo.penup()
    leonardo.goto(x = -270, y = y_positions[turtle_index])
    
    turtles.append(leonardo)
    
if bet:
    race_on = True

while race_on:
    for t in turtles:
        if t.xcor() > 270:
            race_on = False
            winner = t.pencolor()
            if winner == bet:
                print('YOU WIN!🏆')
            else:
                print(f'You lose. Winner is {winner.upper()} turtle')
        random_distance = randint(0, 10)
        t.forward(random_distance)

screen.exitonclick()