from turtle import Turtle, position

PADDLE_POSITIONS = [(350, 0), (-350, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def right_go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def right_go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def left_go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def left_go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
