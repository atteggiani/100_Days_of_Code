from turtle import Turtle
from random import choice
import numpy as np

class Ball(Turtle):
    def __init__(self,pos="r"):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.set()

    def set(self):
        a=np.append(np.arange(90-10,90+11),np.arange(270-10,270+11))
        possible_headings=np.setdiff1d(np.arange(0,360),a)
        self.setheading(choice(possible_headings))
        self.goto(0,0)

    def move(self,heading=None):
        self.forward(5)
    
    def bounce(self,dir="h"):
        self.setheading(360-self.heading())
        if dir != "h":
            self.setheading(self.heading()+180)
        self.setheading(self.heading()%360)

    def wall_collision(self):
        return np.logical_and(np.logical_or(self.ycor()>=287,self.ycor()<=-277),
                                np.logical_and(self.xcor()>=-340,self.xcor()<=340))

    def paddle_collision(self,paddle):
        # ball going right and x >330
        condright=np.logical_and(self.xcor()>=330,
                                 np.logical_or(self.heading()<90,self.heading()>270)),
        # ball going left and x <-330
        condleft=np.logical_and(self.xcor()<=-330,
                                np.logical_and(self.heading()>90,self.heading()<270)),
        # distance
        conddist=self.distance(paddle)<=np.sqrt(10**2+50**2)
        cond=np.logical_and(np.logical_or(condleft,condright),conddist)
        return cond
    
    def is_out_left(self):
        return self.xcor()<-410
    
    def is_out_right(self):
        return self.xcor()>410