from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
# Setup Screen
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SSnakers")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect Collision with wall
    if snake.segments[0].xcor()>290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor()>290 or snake.segments[0].ycor() < -290 :
        scoreboard.reset()
        snake.reset()

    
    # Detect Collision with tail
    # if head collides with any segment in the tail:
        # trigger game_over

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()