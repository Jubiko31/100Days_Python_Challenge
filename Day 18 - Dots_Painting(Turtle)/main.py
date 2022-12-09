# Idea: https://www.phillips.com/detail/damien-hirst/UK010120/16
# modern "art"...
import turtle
from random import choice
from color_data import colors

turtle.colormode(255)
michelangelo = turtle.Turtle()

michelangelo.speed("fastest")
michelangelo.penup()
michelangelo.hideturtle()

michelangelo.setheading(225)
michelangelo.forward(300)
michelangelo.setheading(0)
number_of_dots = 100

for dot in range(1, number_of_dots + 1):
    michelangelo.dot(20, choice(colors))
    michelangelo.forward(50)

    if dot % 10 == 0:        
        michelangelo.setheading(90)
        michelangelo.forward(50)
        michelangelo.setheading(180)
        michelangelo.forward(500)
        michelangelo.setheading(0)


screen = turtle.Screen()
screen.exitonclick()