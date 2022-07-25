from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
HEADING = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(HEADING)
        self.reset_player()

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def crossed_road(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

