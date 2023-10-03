from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.random_x=random.randint(280,400)
        self.random_y=random.randint(-250,220)
        self.starting_speed=STARTING_MOVE_DISTANCE
        self.random_location()


    def car_move(self):
        self.backward(self.starting_speed)

    def random_location(self):
        self.goto(self.random_x,self.random_y)
