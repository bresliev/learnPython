from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard


class Game:
    def __init__(self):
        # create the screen for the game 600x800, black colored

        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(height=600, width=800)
        self.screen.title("Pong")
        self.screen.tracer(0)

        self.player_right = Player(x=380, y=0)
        self.player_left = Player(x=-380, y=0)

        self.sore_board = Scoreboard()

        self.screen.update()

        self.ball = Ball()

        self.screen.onkey(self.player_right.up, "Up")
        self.screen.onkey(self.player_right.down, "Down")
        self.screen.onkey(self.player_left.up, "A")
        self.screen.onkey(self.player_left.down, "Y")
        self.screen.listen()
        self.game_is_on = True

    def run_the_game(self):

        while self.game_is_on:
            looser = ""
            self.ball.move()
            self.screen.update()
            self.ball.collision_with_wall()
            self.ball.colision_with_paddle(self.player_left)
            self.ball.colision_with_paddle(self.player_right)
            looser = self.ball.ball_out()
            if looser == "R":
                self.sore_board.l_point()
            elif looser == "L":
                self.sore_board.r_point()
            self.sore_board.write_score()


