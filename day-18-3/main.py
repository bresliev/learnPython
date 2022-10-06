from turtle import Turtle, Screen
from random import randint
from time import sleep
screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.pencolor("red")
timmy.penup()
timmy.goto(-100, 100)
timmy.pendown()
c = 25

for j in range(1, 5):
    for i in range(1, j + 3):
        timmy.forward(80)
        timmy.right(360 / (j + 3 - 1))
    timmy.goto(-100, 100)
    c += (j + 4 - 1) * 10
    timmy.pencolor((c, 41, c))

screen.exitonclick()


