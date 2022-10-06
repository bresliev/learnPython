from turtle import Turtle, Screen

timmy = Turtle()
timmy.pencolor("black")
for i in range(20):
    timmy.pendown()
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
screen = Screen()
screen.exitonclick()

