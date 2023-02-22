from turtle import Turtle


class Brick(Turtle):
    def __init__(self, color, length, position, score):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=length)
        self.goto(position)
        self.score = score


class BrickArray:
    def __init__(self, screen: tuple, length: int):
        self.screen_width = screen[0]
        self.screen_height = screen[1]
        self.brick_length = length
        self.array_height = int(self.screen_height / 2)
        self.x_start = -1 * int(self.screen_width / 2)
        self.y_start = int(self.screen_height / 8)
        self.num_bricks = 15
        self.max_bricks = self.num_bricks * 16
        self.bricks_hit = 0
        self.bricks = {}
        self.lay_bricks()

    def lay_bricks(self):
        brick_length = self.brick_length / 10
        for y in range(0, 8):
            y_pos = self.y_start + y * 25
            for x in range(0, self.num_bricks):
                # x_pos = x * self.brick_length + int(self.brick_length / 2)
                x_pos = 5 + self.x_start + self.brick_length + x * (self.brick_length + 35)
                if y < 2:
                    color = "yellow"
                    score = 1
                elif (y >= 2) & (y < 4):
                    color = "green"
                    score = 3
                elif (y >= 4) & (y < 6):
                    color = "orange"
                    score = 5
                else:
                    color = "red"
                    score = 7
                position = (x_pos, y_pos)
                brick = Brick(color=color, length=brick_length, position=position, score=score)
                self.bricks[brick] = True