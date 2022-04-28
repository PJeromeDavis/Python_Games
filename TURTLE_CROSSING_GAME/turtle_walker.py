from turtle import Turtle

class TurtleWalker(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.speed("fastest")
        self.setheading(90)
        self.goto(0, -280)

    def move_forwards(self):
        self.forward(20)

    def reset(self):
        self.goto(0, -280)
