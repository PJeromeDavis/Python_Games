from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)
right_paddle = Paddle((380,0))
left_paddle = Paddle((-380,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350 or ball.distance(left_paddle) < 50 and ball.xcor() < -350:
        ball.paddle_bounce()
        #ball.ball_speed()
    if ball.xcor() > 400:
        score.left_score()
        ball.ball_reset()
    if ball.xcor() < -400:
        score.right_score()
        ball.ball_reset()

screen.exitonclick()
