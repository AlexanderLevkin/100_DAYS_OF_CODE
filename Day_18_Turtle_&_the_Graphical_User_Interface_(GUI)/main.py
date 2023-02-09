import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed(50)

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#
#
# def square():
#     count = 0
#     while count < 4:
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(90)
#         count += 1

# for i in range(20):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)

# def square():
#     score = 0
#     a = 3
#     while score < 5:
#         score += 1
#         for _ in range(a):
#             timmy_the_turtle.forward(20)
#             timmy_the_turtle.right(360/a)
#         a += 1


# square()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def moves(count):
    list_of_move = [timmy_the_turtle.forward(count), timmy_the_turtle.right(90), timmy_the_turtle.back(count)]
    return random.choice(list_of_move)


for step in range(1, 1000):
    timmy_the_turtle.color(random.choice(colours))
    moves(random.randint(1, 100))

screen = Screen()
screen.exitonclick()
