from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-350, 350)
        self.write(self.score, align="center", font=("Courier", 80, "normal"))

    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 80, "normal"))
        self.goto(0, self.ycor() - 80)  # Drop down for next write
        self.write(f"Final Score: {self.score}", align="center", font=("Courier", 40, "normal"))

    def winner(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"YOU WIN!!!", align="center", font=("Courier", 80, "normal"))
        self.goto(0, self.ycor() - 80)
        self.write(f"Final Score: {self.score}", align="center", font=("Courier", 40, "normal"))
