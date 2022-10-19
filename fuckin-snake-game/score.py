from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.pencolor("white")
        self.penup()
        self.goto(x=-30, y=280)
        self.pendown()
        self.print_the_score()
        self.hideturtle()

    def print_the_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align="center")

    def increase(self):
        self.score += 1
        self.print_the_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.print_the_score()

#    def game_over(self):
#        self.clear()
#        self.write(arg=f"Game Over", align="center")
