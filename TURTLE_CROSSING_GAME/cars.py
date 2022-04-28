import turtle
from turtle import Turtle
import random
turtle.colormode(255)
SPEED = 5
COLOR_LIST = [(232, 229, 220), (226, 161, 72), (45, 102, 148), (116, 165, 193), (155, 63, 88), (191, 162, 30), (26, 135, 95), (201, 133, 154), (167, 79, 47), (216, 87, 57)]
class Cars():

    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.speed("fastest")
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLOR_LIST))
            new_car.goto(300, random.randint(-250, 230))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += SPEED
        self.car_move()
