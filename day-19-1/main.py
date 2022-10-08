from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward(move):
    timmy.forward(move)

def on_key():
    move_forward(50)

screen.listen()
screen.onkey(key="space", fun=on_key)

screen.exitonclick()
