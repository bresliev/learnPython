from turtle import Turtle


class Player(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.width(20)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x=x, y=y)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor()+20)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor()-20)
