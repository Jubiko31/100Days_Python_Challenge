from turtle import Screen
from time import sleep
from player import Player
from car_manager import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game🐢")
screen.tracer(0)

player = Player()
car = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.front, "Up")
screen.onkey(player.back, "Down")

game_on = True
while game_on:
    sleep(0.1)
    screen.update()
    car.add_new_car()
    car.start_cars()
    
    for cars in car.all_cars:
        if cars.distance(player) < 20:
           game_on = False 
           scoreboard.game_over()
    
    if player.check_finish_line():
        player.next_level()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()