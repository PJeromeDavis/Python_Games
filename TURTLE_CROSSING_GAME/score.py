from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.hideturtle()
        self.goto(-200, 250)
        self.score_update()

    def score_update(self):
        self.clear()
        self.player_score += 1
        self.write(arg=f"LEVEL:{self.player_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER. YOUR LEVEL {self.player_score}", align=ALIGNMENT, font=FONT)

