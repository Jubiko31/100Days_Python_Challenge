import turtle as t
from random import randint

_t = t.Turtle()
t.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

_t.speed("fastest")

def draw_spinograph(gap_size):
    for _ in range(int(360 / gap_size)):
        _t.color(random_color())
        _t.circle(100)
        _t.setheading(_t.heading() + 10)


draw_spinograph(5)

screen = t.Screen()
screen.exitonclick()