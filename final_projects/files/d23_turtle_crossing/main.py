#!/Applications/anaconda3/bin/python
from turtle import Screen, color, colormode, Turtle
from random import randint
import time
import numpy as np
from character import Character
from blocks import Blocks
from level import Level

screen=Screen()
screen.setup(width=600,height=600)
screen.cv._rootwindow.resizable(False, False)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

ch=Character()
level=Level()
blocks=Blocks()

game_is_on=True

screen.onkeypress(ch.move,"Up")

sleep=0.1
prob=0.1
while game_is_on: 
    screen.update()
    time.sleep(sleep)
    blocks.create(probability=prob)
    blocks.move()
    blocks.delete()

    # Win level
    if ch.win():
        level.increase()
        ch.reset()
        prob*=1.2
        sleep*=0.95
        time.sleep(0.3)
    
    # Lose
    if ch.lose(blocks):
        level.game_over()
        game_is_on=False

screen.exitonclick()