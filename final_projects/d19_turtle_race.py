#!/Applications/anaconda3/bin/python
from turtle import Screen, Turtle, color, colormode
from random import randint
import numpy as np

screen=Screen()
width=1000
height=400
screen.setup(width=width,height=height)
colors=["red","orange","#f8e64b","green","cyan","blue","purple"]
hspace=height/(len(colors)+1)
y=height/2-hspace
xstart=-(width/2)*0.97
xfinish=(width/2)*0.94
turtles=[]
for c in colors:
    t=Turtle()
    t.shape('turtle')
    t.color(c)
    t.penup()
    t.speed(0)    
    t.goto(x=xstart,y=y)
    y-=hspace
    turtles.append(t)
bet=screen.textinput(title="Make your bet",
    prompt="Which turtle will win the race?\nPick a color: ('red','orange','yellow','green','cyan','blue','purple')")
if bet is None:
    quit()
while True:
    if bet.strip() == "":
        bet=screen.textinput(title="No colour chosen!",
            prompt="Please pick a color between:\n'red','orange','yellow','green','cyan','blue','purple'")
    elif bet.strip().lower() not in ["red","orange","yellow","green","cyan","blue","purple","r","o","y","g","c","b","p"]:
        bet=screen.textinput(title="Wrong colour choice!",
            prompt="Please pick a color between:\n'red','orange','yellow','green','cyan','blue','purple'")
    else:
        break

xmax=xstart
for t in turtles:
    t.speed(9) 
while xmax<xfinish:
    for t in turtles:
        t.forward(randint(0,10))
    xmax=max([t.pos()[0] for t in turtles])
winner=turtles[np.argmax([t.pos()[0] for t in turtles])]
color = winner.color()[0]
if color == "#f8e64b": color="yellow"

# screen.listen()
# screen.onkey(key="Up", fun=lambda: tim.forward(20))
# screen.onkey(key="Down", fun=lambda: tim.backward(20))
# screen.onkey(key="Left", fun=lambda: tim.left(10))
# screen.onkey(key="Right", fun=lambda: tim.right(10))
# screen.onkey(key="c", fun=lambda: tim.clear())
# screen.onkey(key="r", fun=lambda: tim.home())

screen.exitonclick()