#!/Applications/anaconda3/bin/python
from turtle import Screen, color, colormode, Turtle
from random import randint
import time
import numpy as np
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import threading
from queue import Queue

screen=Screen()
screen.setup(width=800,height=600)
screen.cv._rootwindow.resizable(False, False)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)
screen.listen()

r_paddle=Paddle()
l_paddle=Paddle(pos="l")
score=Scoreboard()
ball=Ball()
    
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")

game_is_on=True
while game_is_on: 
    time.sleep(0.02)
    screen.update()
    ball.move()
    # collision with walls
    if ball.wall_collision():
        ball.bounce(dir="h")
    # collision with paddle
    if (ball.paddle_collision(r_paddle)) or (ball.paddle_collision(l_paddle)):
        ball.bounce(dir="v")
    # exit from extent
    if ball.is_out_left():
        score.increase_right()
        ball.set()
        time.sleep(0.5)
    if ball.is_out_right():
        score.increase_left()
        ball.set()
        time.sleep(0.5)

screen.exitonclick()