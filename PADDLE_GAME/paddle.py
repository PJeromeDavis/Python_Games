from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(position)


    def moving(self):
        self.forward(40)

    def move_up(self):
        self.setheading(90)
        self.moving()

    def move_down(self):
        self.setheading(270)
        self.moving()
