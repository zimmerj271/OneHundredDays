from turtle import Turtle

FONT = ("Courier", 10, "normal")
GAME_OVER_FONT = ("Courier", 24, "bold")


class MapLabeler(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def add_state(self, state, coordinate):
        self.goto(coordinate)
        self.write(state, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("You guessed all the states!", align="center", font=GAME_OVER_FONT)

