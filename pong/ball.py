from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.width(20)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10

    def move(self):
        self.goto(x=self.xcor() + self.x, y=self.ycor() + self.y)
        time.sleep(0.05)

    def bounce(self, coordinate):
        if coordinate == "y":
            self.y *= -1
        else:
            self.x *= -1

    def collision_with_wall(self):
        if self.ycor() > 285 or self.ycor() < -285:
            self.bounce("y")

    def colision_with_paddle(self, paddle):
        if self.distance(paddle) < 50 and (self.xcor() > 340 or self.xcor() < -340):
            self.bounce("x")

    def ball_out(self):
        if self.xcor() > 380:
            self.home()
            self.bounce(self.x)
            return "R"
        elif self.xcor() < -380:
            self.home()
            self.bounce(self.x)
            return "L"
