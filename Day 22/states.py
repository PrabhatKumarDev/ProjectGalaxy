from turtle import Turtle

class State(Turtle):
    def __init__(self,x,y,name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.write(f"{name}",align="center",font=("Arial",7,"normal"))
        self.a=0

        