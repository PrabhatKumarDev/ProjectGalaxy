import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player=Player()
screen.onkeypress(player.move_up,"Up")
car_list=[]
scoreboard=Scoreboard()


game_is_on = True
i=0
while game_is_on:
    time.sleep(0.1)
    i+=1
    if(i%6==0):
        Car=CarManager()
        car_list.append(Car)
    
    # make car moves
    for j in car_list:
        j.car_move()
    
    # Detect collision with the cars
    for k in range(len(car_list)):
        if player.distance(car_list[k])<30:
            scoreboard.game_over()
            game_is_on=False

    if(player.ycor()==280):
        scoreboard.increase_score()
        player.reset_location()
    
    screen.update()

screen.exitonclick()

