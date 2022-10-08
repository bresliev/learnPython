import turtle
from turtle import Turtle, Screen
import random

#
# timmy = Turtle(shape="turtle")
# goki = Turtle(shape="turtle")
# boki = Turtle(shape="turtle")
# coki = Turtle(shape="turtle")
# moki = Turtle(shape="turtle")
# floki = Turtle(shape="turtle")

colors = ["yellow", "red", "green", "black", "orange", "blue", "violet"]
racers = []
race_started = False


def set_the_turtles(race_number):
    racing_guy = Turtle(shape="turtle")
    racing_guy.color(colors[race_number])
    racing_guy.penup()
    racing_guy.goto(x=-230, y=100 - 40 * race_number)
    racers.append(racing_guy)


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

for idx in range(0, 7):
    set_the_turtles(idx)


def run_lola():
    if user_bet:
        race_started = True

    while race_started:
        turtle = random.choice(racers)
        if turtle.xcor() > 230:
            race_started = False
            return turtle
        else:
            turtle.forward(random.randint(1, 10))


winner = run_lola()
winner_index = racers.index(winner)
if user_bet == colors[winner_index]:
    print(user_bet + " " + colors[winner_index])
    print("You winn")
else:
    print(user_bet + " " + colors[winner_index])
    print("Loooooseeeer!!!")
for idx in range(0, 7):
    print(str(idx) + " "+ str(racers[idx].xcor()) )
screen.exitonclick()
