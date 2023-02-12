import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=700, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "green", "orange", "yellow", "blue", "purple"]

turtles_in_race = []
position = -100

for turtle_index in range(0, 6):
    new_tim = Turtle(shape="turtle")
    new_tim.color(color[turtle_index])
    new_tim.penup()
    new_tim.goto(x=-330, y=position)
    new_tim.shapesize(2)
    position += 70
    turtles_in_race.append(new_tim)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles_in_race:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 330:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won! The {wining_color} turtle is the winner!")
            else:
                print(f"You've lost! The {wining_color} turtle is the winner!")

screen.exitonclick()


