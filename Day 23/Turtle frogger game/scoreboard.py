from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=(f"Level: {self.level}"), align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
