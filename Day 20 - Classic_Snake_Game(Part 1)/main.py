# Classic Snake game - Part 1
# Do NOT run this game, not finished. Go to Day 21 for full game
from turtle import Screen, Turtle
from time import sleep
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game🐍")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    snake.move()

screen.exitonclick()