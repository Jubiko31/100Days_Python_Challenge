from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        
    def add_new_car(self):
        chance = randint(1, 6) # Like rolling dice
        if chance == 6:     
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(300, y=random_y)
            self.all_cars.append(new_car)
        
    def start_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)
    
    def level_up(self):
        self.speed += MOVE_INCREMENT