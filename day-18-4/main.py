from turtle import Turtle, Screen
import random

colors = ["dark gray", "pale turquoise", "magenta", "lavender blush", "spring green"]
directions = [0, 90, 180, 270]

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.pensize(6)
timmy.speed("slow")
color = (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255))
for _ in range(60):
    timmy.pencolor(color)
    timmy.setheading(random.choice(directions))
    timmy.forward(30)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

screen.exitonclick()
