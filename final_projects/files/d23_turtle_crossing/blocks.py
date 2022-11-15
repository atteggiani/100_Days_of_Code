from turtle import Turtle
from random import choice,randint,random

COLORS=["red","yellow","blue","green","pink","purple"]

class Blocks():
    def __init__(self):
        self.blocks=[]
    
    def move(self):
        for b in self.blocks:
            b.forward(10)
        
    def create(self,probability=1):
        if random() <= probability:
            block=Turtle(shape="square")
            block.color(choice(COLORS))
            block.penup()
            block.shapesize(stretch_len=2, stretch_wid=1)
            block.setheading(180)
            block.setx(320)
            block.sety(randint(-240,260))
            self.blocks.append(block)
    
    def delete(self):
        for b in self.blocks:
            if b.xcor() <= -320:
                self.blocks.remove(b)