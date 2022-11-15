from turtle import Turtle
import numpy as np

class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.sety(-280)
        
    def move(self):
        self.forward(10)    
    
    def reset(self):
        self.sety(-280)
    
    def win(self):
        cond = self.ycor() >= 310
        return cond

    def lose(self,blocks):
        def cond(block):
            c1=np.logical_and(np.logical_or(block.ycor() > (self.ycor() + 22),
                                            block.ycor() < (self.ycor() - 20)),
                              self.distance(b) < np.sqrt(20**2 + 10**2))
            c2=np.logical_and(np.logical_and(block.ycor() <= (self.ycor() + 20),
                                             block.ycor() >= (self.ycor() - 20)),
                              self.distance(b) < 30)
            c=np.logical_or(c1,c2)
            return c
        for b in blocks.blocks:
            if cond(b):
                return True
        return False
