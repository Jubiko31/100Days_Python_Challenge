from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def front(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def back(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
    
    def next_level(self):
        self.goto(STARTING_POSITION)
    
    def check_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
    
    