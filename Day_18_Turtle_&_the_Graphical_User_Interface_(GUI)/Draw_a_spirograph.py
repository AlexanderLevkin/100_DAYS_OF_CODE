import random
import turtle as t

timmy_the_turtle = t.Turtle()
color = t.colormode(255)
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tupp = (r, g, b)
    return tupp


def cirlce_draw(step, speed):
    for i in range(1, 360, step):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.speed(speed)
        timmy_the_turtle.position()
        timmy_the_turtle.setheading(i)
        timmy_the_turtle.circle(120)


cirlce_draw(1,1000)

screen = t.Screen()
screen.exitonclick()