import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.color("yellow")
timmy.shape("turtle")
screen = Screen()


def forwards():
    timmy.forward(10)


def backwards():
    timmy.backward(10)


def counter_clockwise():
    timmy.right(10)


def clockwise():
    timmy.left(10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()


screen.listen()
screen.onkey(key="W", fun=forwards)
screen.onkey(key="S", fun=backwards)
screen.onkey(key="A", fun=counter_clockwise)
screen.onkey(key="D", fun=clockwise)
screen.onkey(key="C", fun=clear)

screen.exitonclick()
