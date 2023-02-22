from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position: tuple, length: int):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=length)
        self.goto(position)
        self.half_size = False
        self.length = length * 10  # in pixels

    def left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())

    def right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def shrink(self):
        if not self.half_size:
            paddle_size = self.shapesize()
            new_length = paddle_size[1] / 2
            self.shapesize(stretch_wid=1, stretch_len=new_length)
            self.length = self.length / 2
            self.half_size = True
