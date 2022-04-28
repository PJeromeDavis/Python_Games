from turtle_walker import TurtleWalker
from turtle import Screen
from cars import Cars
from score import Score
import time

t = TurtleWalker()
s = Screen()
s.setup(600, 600)
car = Cars()
score = Score()
#for _ in range(10):
 #   c.append(Cars())

s.tracer(0)
s.listen()
s.onkey(fun=t.move_forwards, key="Up")
game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.05)
    car.create_car()
    car.car_move()
    for item in car.all_cars:
        if item.distance(t) < 30:
            game_is_on = False
            score.game_over()
    if t.ycor() > 250:
        score.score_update()
        t.reset()
        car.increase_speed()

    #TO DETECT COLLISION BETWEEN CAR AND PLAYER
s.exitonclick()
