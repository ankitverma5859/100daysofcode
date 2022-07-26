import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
s_board = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision of snake with food
    if snake.snake_segments[0].distance(food) < 15:
        food.refresh()
        s_board.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.snake_segments[0].xcor() > 280 or snake.snake_segments[0].xcor() < -280 or \
            snake.snake_segments[0].ycor() < -280 or snake.snake_segments[0].ycor() > 280:
        is_game_on = False
        s_board.game_over()

    # Detect collision with its tail
    for segment in snake.snake_segments[1:]:
        if snake.snake_segments[0].distance(segment) < 10:
            is_game_on = False
            s_board.game_over()

screen.exitonclick()
