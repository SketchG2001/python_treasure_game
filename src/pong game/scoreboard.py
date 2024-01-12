from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
    def l_point(self):
        # self.clear()
        self.l_score += 1
        self.update_scoreboard()
    def r_point(self):
        # self.clear()
        self.r_score += 1
        self.update_scoreboard()