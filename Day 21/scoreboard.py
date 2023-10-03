from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level=1
        self.update_score()
        
    def update_score(self):
        self.goto(-220,250)
        self.write(f"Level:{self.level}",align="center",font=FONT)
    
    def increase_score(self):
        self.clear()
        self.level+=1
        self.update_score()

    
    def game_over(self):
        self.goto(0,0)
        self.color("black")
        self.penup()
        self.hideturtle()
        self.write("Game Over",align="center",font=FONT)
        