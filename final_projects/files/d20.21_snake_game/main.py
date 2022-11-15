#!/Applications/anaconda3/bin/python
from turtle import Screen, color, colormode
from random import randint
import time
import numpy as np
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.cv._rootwindow.resizable(False, False)
screen.bgcolor("black")
screen.title("Snake!!")
screen.tracer(0)

score=Scoreboard()
snake=Snake()
food=Food()
food.generate(unavailpos=[s.pos() for s in snake.segments])
screen.listen()

game_is_on=False
def reset():
    global game_is_on
    if not game_is_on:
        score.reset()
        snake.reset()
        food.generate(unavailpos=[s.pos() for s in snake.segments])
        game_is_on=True
        while game_is_on:
            screen.update()
            time.sleep(0.1/snake.speed)
            snake.move()

            # Detect collision with food
            if snake.head.distance(food) < 5:
                score.increase()
                snake.extend()
                snake.speedup()
                food.generate(unavailpos=[s.pos() for s in snake.segments])
            
            # Detect collision with snake tail
            for s in snake.segments[1:]:
                if snake.head.distance(s) < 5:
                    score.game_over()
                    game_is_on=False
                    break
            
screen.onkeypress(snake.right,"Right")
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(reset,"r")

reset()
screen.exitonclick()