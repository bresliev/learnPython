import time
from turtle import Turtle


class Snake:
    def __init__(self):
        self.body = []
        for idx in range(0, 3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.setx(0 - idx * 20)
            segment.shape()
            self.body.append(segment)
        self.head = self.body[0]

    def move_the_snake(self):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].goto(x=self.body[idx - 1].xcor(), y=self.body[idx - 1].ycor())
        self.body[0].forward(20)

    def add_a_segment(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(self.body[-1].position())
        self.body.append(segment)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)
