#!/Applications/anaconda3/bin/python
from turtle import Screen, Turtle, color, colormode
from random import randint, choice
import colorgram


colors = colorgram.extract('/Users/dmar0022/university/udemy/100_Days_of_Code/final_projects/files/d18_hirst_painting/image.jpg', 30)
colorlist = [list(c.rgb) for c in colors][1:]
colormode(255)

t=Turtle()
t.speed(0)
t.hideturtle()
t.up()
t.goto(-200,-200)

for _ in range(10):
    for _ in range(10):
        t.dot(20,choice(colorlist))
        t.forward(50)
    t.left(180)
    t.forward(50*10)
    t.right(90)
    t.forward(50)
    t.right(90)

screen=Screen()
screen.exitonclick()