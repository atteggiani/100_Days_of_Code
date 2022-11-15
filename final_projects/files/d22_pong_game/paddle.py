from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos="r"):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=5)
        if pos == "r":
            self.setx(350)
        else:
            self.setx(-350)
        self.left(90)

    def up(self):
        if self.ycor() < 240:
            # self.sety(self.ycor()+10)
            self.forward(10)

    def down(self):
        if self.ycor() > -220:
            self.backward(20)