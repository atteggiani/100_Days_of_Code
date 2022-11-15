from turtle import Turtle

ALIGN="center"
FONT=('Arial', 40, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left=0
        self.right=0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.color("white")
        self.sety(250)
        self.write(f"{self.left} | {self.right}",align=ALIGN,font=FONT)

    def increase_left(self):
        self.left+=1
        self.clear()
        self.write(f"{self.left} | {self.right}",align=ALIGN,font=FONT)

    def increase_right(self):
        self.right+=1
        self.clear()
        self.write(f"{self.left} | {self.right}",align=ALIGN,font=FONT)