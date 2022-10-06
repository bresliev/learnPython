import random
from turtle import Turtle, Screen
import colorgram

colors = colorgram.extract("DHS8614againstwall_771_0.jpg", 30)

screen = Screen()
print(screen.screensize())
screen.colormode(255)

timmy = Turtle()
timmy.penup()
timmy.goto(-310, -250)
move = 50
for y in range(1, 11):
    for x in range(1, 11):
        timmy.dot(20, random.choice(colors).rgb)
        timmy.forward(move)
    if timmy.heading() == 0:
        timmy.setheading(90)
        timmy.forward(move)
        timmy.setheading(180)
        timmy.forward(move)
    else:
        timmy.setheading(90)
        timmy.forward(move)
        timmy.setheading(0)
        timmy.forward(move)



screen.exitonclick()