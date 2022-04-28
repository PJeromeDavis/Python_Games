import turtle as t
import random

colors = ["blue", "yellow", "orange", "red", "green"]
#racers = ["tim", "tom", "jerry", "brute"]
race_screen = t.Screen()
race_screen.setup(width = 500, height = 500)
user_bet = race_screen.textinput(title = "Turtle_race", prompt = "Chose your racer:")
#tim = t.Turtle()
#tim.penup()
#tim.setposition(x=-230, y=-100)
number = 0
x = -230
y = -100
racers_list = []
for racer_color in colors:
    racer_color = t.Turtle()
    racer_color.shape("turtle")
    racer_color.penup()
    racer_color.setposition(x, y)
    y += 50
    racer_color.color(colors[number])
    number += 1
    racers_list.append(racer_color)
race_is_on = False
if user_bet:
    race_is_on = True

while race_is_on:
    for racer_color in racers_list:
        racer_color.forward(random.randint(0, 10))
        if racer_color.xcor() > 230 :
            race_is_on = False
            winner = racer_color.pencolor()

if winner == user_bet:
    print(f"Your racer won.")
else:
    print(f"You lost. {winner} won the race.")




race_screen.exitonclick()
