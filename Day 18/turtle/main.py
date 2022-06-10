from turtle import Turtle, Screen
import random


turtle = Turtle()


def random_color():
    R = random.random()
    G = random.random()
    B = random.random()

    rgb = (R, G, B)
    return rgb


def draw_shape(num_sides):
    turtle.pencolor(random_color())
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.left(angle)


def random_walk(paces):
    turtle.pensize(10)
    turtle.speed(0)
    for _ in range(paces):
        turtle.pencolor(random_color())
        turtle.forward(20)
        turtle.left(random.choice((0, 90, 180, 270, 360)))


def spirograph(heading_shift):
    turtle.speed(0)
    for _ in range(int(360 / heading_shift)):
        turtle.pencolor(random_color())
        turtle.circle(100)
        turtle.left(heading_shift)


spirograph(7)

screen = Screen()
screen.colormode(255)
screen.exitonclick()
