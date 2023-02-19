from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} ", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} ", False, align=ALIGNMENT, font=FONT)
