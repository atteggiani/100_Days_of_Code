from turtle import Turtle

ALIGN="center"
FONT=('Arial', 20, 'normal')
FONT2=('Arial', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.reset()

    def increase(self):
        self.score+=1
        self.mywrite()
    
    def game_over(self):
        if self.score > self.highscore:
            self.highscore=self.score
            write_highschore(self.highscore)
        self.mywrite()
        self.color([1,0.2,0.1])
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGN,font=FONT)
        self.goto(0,-30)
        self.write(f"Press R to restart. Click on the screen to exit.",align=ALIGN,font=FONT2)

    def reset(self):
        self.score=0
        self.highscore=read_highschore()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.sety(275)
        self.mywrite()

    def mywrite(self):
        self.clear()
        self.write(f"Score: {self.score}   |   Highscore: {self.highscore}",align=ALIGN,font=FONT)

def read_highschore():
    with open("/Users/dmar0022/university/udemy/100_Days_of_Code/final_projects/files/d20.21_snake_game/highscore","r") as file:
        hs=int(file.read())
    return hs

def write_highschore(hs):
    with open("/Users/dmar0022/university/udemy/100_Days_of_Code/final_projects/files/d20.21_snake_game/highscore","w") as file:
        file.write(str(hs))