from turtle import Turtle


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center",
                   font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align="center",
                   font=('Courier', 80, 'normal'))

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()
