from turtle import Turtle, Screen
import random

colors = ["dark gray", "pale turquoise", "magenta", "lavender blush", "spring green"]
directions = [0, 90, 180, 270]

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.speed("fastest")
color = (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255))
current_heading = timmy.heading()
offset = 8
for _ in range( int(360 / offset) ):
    timmy.pencolor(color)
    timmy.circle(100)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy.setheading(timmy.heading() + offset)

screen.exitonclick()
