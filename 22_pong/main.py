import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0) #turns off the animation

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
s_board = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if the ball didnt collide with paddle
    if ball.xcor() < -380:
        ball.reset_position()
        s_board.r_point()

    if ball.xcor() > 380:
        ball.reset_position()
        s_board.l_point()

screen.exitonclick()
