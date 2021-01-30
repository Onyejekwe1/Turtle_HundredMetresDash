from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=500, width=400)

user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race (Red, Yellow, Green, "
                                                          "orange, purple or Blue?)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [-70, -40, -10, 20, 50, 80]
turtles = []
race_started = False

for race_turtle in range(0, 6):
    jim = Turtle(shape="turtle")
    jim.color(colors[race_turtle])
    jim.penup()
    jim.goto(x=-178, y=positions[race_turtle])
    turtles.append(jim)


if user_bet:
    race_started = True

while race_started:
    for turt in turtles:
        if turt.xcor() > 230:
            race_started = False
            winner = turt.pencolor()
            if winner == user_bet:
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You lost! The {winner} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turt.forward(random_distance)


screen.exitonclick()
