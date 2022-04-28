from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../../../high_score.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.hideturtle()
        self.write(arg=f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def update_highscore(self):
        if self.score>self.high_score:
            with open("../../../../high_score.txt", mode="w") as file:
                file.write(f"{self.score}")

            self.high_score = self.score

    def score_reset(self):
        self.clear()
        self.score = 0
        self.write(arg=f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score+=1
        self.update_highscore()
        self.clear()
        self.write(arg=f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
