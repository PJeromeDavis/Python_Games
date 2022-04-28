from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.goto(100, 250)
        self.write(arg=f"{self.r_score}", align=ALIGNMENT, font=FONT)
        self.goto(-100, 250)
        self.write(arg=f"{self.l_score}", align=ALIGNMENT, font=FONT)

    def right_score(self):
        self.r_score += 1
        self.clear()
        self.score_update()

    def left_score(self):
        self.l_score += 1
        self.clear()
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
