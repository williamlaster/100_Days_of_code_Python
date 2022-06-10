from turtle import Turtle, Screen
import random


turtle = Turtle()
turtle.hideturtle()

rgb_colors = [
    (1, 13, 31), (53, 25, 17), (219, 127, 106), (10,
                                                 105, 160), (241, 214, 69), (149, 84, 39),
    (214, 87, 64), (164, 162, 32), (158, 7,
                                    25), (157, 63, 102), (11, 63, 32), (97, 6, 19),
    (207, 74, 104), (11, 96, 57), (1, 63, 145), (173,
                                                 135, 162), (8, 172, 216), (158, 33, 23),
    (4, 212, 207), (9, 139, 86), (145, 227,
                                  216), (122, 193, 148), (221, 178, 215),
    (100, 219, 229), (253, 196, 0), (80, 135, 179)
]


def paint_line(number_of_dots):
    turtle.speed(0)
    turtle.penup()
    rgb = ()
    for _ in range(number_of_dots):
        rgb = random.choice(rgb_colors)
        turtle.dot(20, rgb)
        turtle.forward(50)


def paint(number_of_rows, number_of_dots):
    y = 0
    for _ in range(number_of_rows):
        paint_line(number_of_dots)
        y += 40
        turtle.setpos(0, y)


screen = Screen()
screen.colormode(255)


paint(10, 10)


screen.exitonclick()
