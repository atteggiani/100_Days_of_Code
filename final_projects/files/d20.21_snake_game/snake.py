from turtle import Turtle
import time

MOVING_DISTANCE=20

class Snake():
    def __init__(self):
        self.segments=[]
        self.reset()

    def create_snake(self):
        pos=[(20,0),(0,0),(-20,0)]
        for p in pos:
            self.add(p)

    def move(self):
        for i in range(len(self.segments)-1,-1,-1):
            if i == 0:
                self.head.forward(MOVING_DISTANCE)
            else:
                self.segments[i].goto(self.segments[i-1].pos())
        
        # cross walls
        if self.head.xcor() > 280:
                self.head.setx(-280) 
        elif self.head.xcor() < -280:
            self.head.setx(280) 
        elif self.head.ycor() > 280:
            self.head.sety(-280) 
        elif self.head.ycor() < -280:
            self.head.sety(280) 

    def right(self):
        if int(self.head.heading()) not in (0,180): 
            self.head.setheading(0)
    def left(self):
        if int(self.head.heading()) not in (0,180): 
            self.head.setheading(180)
    def up(self):
        if int(self.head.heading()) not in (90,270):
            self.head.setheading(90)
    def down(self):
        if int(self.head.heading()) not in (90,270):
            self.head.setheading(270)
    
    def add(self,pos):
        t=Turtle(shape="square")
        t.color("white")
        t.penup()
        t.setpos(pos)
        self.segments.append(t)
    
    def extend(self):
        self.add(self.tail.position())

    def speedup(self):
        self.speed*=1.03
    
    def reset(self):
        for s in self.segments:
            s.reset()
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        self.tail=self.segments[-1]
        self.speed=1