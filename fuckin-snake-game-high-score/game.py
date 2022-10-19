from snake import Snake
from food import Food
from score import Score
import time


class Game:
    def __init__(self, screen):
        screen.bgcolor("black")
        screen.tracer(0)
        self.game_is_on = True
        self.my_snake = Snake()
        self.food = Food()
        self.score = Score()
        screen.update()
        screen.onkey(self.my_snake.up, "Up")
        screen.onkey(self.my_snake.down, "Down")
        screen.onkey(self.my_snake.left, "Left")
        screen.onkey(self.my_snake.right, "Right")
        screen.listen()

    def collision_detection(self):
        if self.my_snake.head.distance(self.food) < 15:
            self.food.move_it()
            self.score.increase()
            self.my_snake.add_a_segment()

    def collision_with_wall(self):
        if self.my_snake.head.xcor() > 280 or self.my_snake.head.xcor() < -280 or self.my_snake.head.ycor() > 280 \
                or self.my_snake.head.ycor() < -280:
            self.score.reset()

    def collision_with_itself(self):
        for segment in self.my_snake.body[1:]:
            if self.my_snake.head.distance(segment) < 10:
                self.score.reset()

    def run_the_game(self, screen):
        while self.game_is_on:
            self.my_snake.move_the_snake()
            self.collision_detection()
            self.collision_with_wall()
            self.collision_with_itself()
            time.sleep(0.1)
            screen.update()
