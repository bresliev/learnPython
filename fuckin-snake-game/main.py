from turtle import Screen
from snake import Snake
from game import Game

screen = Screen()
screen.setup(width=600, height=600)


the_game = Game(screen)
the_game.run_the_game(screen)

screen.exitonclick()
