from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


def etch_a_sketch():
    screen.listen()
    screen.onkeypress(key="w", fun=move_forwards)
    screen.onkeypress(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="d", fun=turn_right)
    screen.onkey(key="c", fun=clear)


etch_a_sketch()

screen.exitonclick()
