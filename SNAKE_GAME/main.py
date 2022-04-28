import turtle as t
import snake as s
import food
from score import Score
import time
my_screen = t.Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)
snake = s.Snake()
food = food.Food()
score = Score()

my_screen.listen()
my_screen.onkey(fun=snake.move_right, key="d")
my_screen.onkey(fun=snake.move_left, key="a")
my_screen.onkey(fun=snake.move_up, key="w")
my_screen.onkey(fun=snake.move_down, key="s")
game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.movement()
    if snake.snake[0].distance(food) < 15:
        food.location()
        snake.increase_in_body()
        score.score_increase()
    if snake.snake[0].xcor()>280 or snake.snake[0].xcor()<-280 or snake.snake[0].ycor()>280 or snake.snake[0].ycor()<-280:
        snake.snake_reset()
        score.score_reset()
    for body in snake.snake[1:]:
        if snake.snake[0].distance(body)<10:
            snake.snake_reset()
            score.score_reset()

my_screen.exitonclick()



