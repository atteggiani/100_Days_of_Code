from turtle import Turtle

ALIGN="Left"
FONT=('Arial', 20, 'normal')

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.setposition((-280,275))
        self.write(f"Level: {self.level}",align=ALIGN,font=FONT)
    
    def increase(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level}",align=ALIGN,font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="Center",font=FONT)
