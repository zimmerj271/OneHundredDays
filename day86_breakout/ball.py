from turtle import Turtle


class Ball(Turtle):
    def __init__(self, speed: float, position: tuple):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.default_speed = speed
        self.move_speed = self.default_speed
        self.max_speed = False
        self.reset_position(position)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self, position: tuple):
        self.goto(position[0], position[1])
        self.bounce_x()
        # self.move_speed = self.default_speed

    def increase_speed(self, bricks_hit, hit_red):
        if not self.max_speed:
            if bricks_hit in [4, 12] or hit_red:
                self.move_speed *= 0.75
        if hit_red:
            self.max_speed = True


class BallCount(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_count = 3
        self.balls = []
        self.position = (-470, 440)
        self.add_balls(self.position, self.ball_count)

    def add_balls(self, position, ball_count):
        y = 0
        for ball in range(ball_count):
            x_pos = position[0]
            y_pos = position[1] - y
            ball = Ball(speed=0, position=(x_pos, y_pos))
            # self.balls[ball] = True
            self.balls.append(ball)
            y += 30

    def clear_balls(self):
        if len(self.balls) > 0:
            for ball in self.balls:
                ball.clear()

    def remove_ball(self):
        if len(self.balls) > 0:
            ball = self.balls.pop()
            ball.hideturtle()
        else:
            self.ball_count = 0
        # self.add_balls(self.position, len(self.balls))
