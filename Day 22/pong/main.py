from time import sleep
from turtle import Screen
from board import Board
from paddles import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

board = Board()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
# Set controls for Paddle 1
screen.listen()
screen.onkeypress(right_paddle.right_go_up, "Up")
screen.onkeypress(right_paddle.right_go_down, "Down")
screen.onkeypress(left_paddle.left_go_up, "w")
screen.onkeypress(left_paddle.left_go_down, "s")

game_is_on = True
while game_is_on:
    sleep(ball.quickness)
    screen.update()
    ball.move()

    # Collisions with top and bottom wall to make ball bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Ball hitting the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Ball missing right paddle
    if ball.xcor() > 380:
        ball.reset_pos()
        board.l_point()

    # Ball missing left paddle
    if ball.xcor() < -380:
        ball.reset_pos()
        board.r_point()


screen.exitonclick()
