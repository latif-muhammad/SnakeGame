from turtle import Turtle


class Score(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))
        self.hideturtle()

    def updateScore(self):
        self.goto(0, 260)
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 15, "normal"))
