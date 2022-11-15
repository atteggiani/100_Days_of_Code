from turtle import Turtle
from random import choice
import numpy as np

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.85, stretch_wid=0.85)
        self.color("blue")
        self.speed("fastest")

    def generate(self,pos=None,unavailpos=None):
        if pos is None:
            pos = unavailpos[0]
            while pos in unavailpos:
                pos=(choice(np.arange(-280.0,300.0,20)),
                        choice(np.arange(-280.0,300.0,20)))
        self.goto(pos)