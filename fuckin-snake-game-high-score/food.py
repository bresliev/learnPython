import random
from turtle import Turtle
import _random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(random.randint(-280, 280), random.randint(-250, 250))

    def move_it(self):
        self.goto(random.randint(-280, 280), random.randint(-250, 250))
