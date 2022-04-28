from turtle import Turtle
from snake import Snake
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.location()

    def location(self):
        self.goto((random.randint(-270, 270)), (random.randint(-270, 270)))
