from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball, BallCount
from bricks import BrickArray
import time

screen = Screen()
screen_size = (988, 950)
screen.setup(width=screen_size[0], height=screen_size[1])
screen.bgcolor("black")
screen.title("BREAKOUT!")
screen.tracer(100)

wall = {'N': screen_size[1] / 2, 'S': -1 * screen_size[1] / 2,
        'W': -1 * screen_size[0] / 2, 'E': screen_size[0] / 2}
bounce_limit = {side: int(loc * 0.95) for (side, loc) in wall.items()}

# instantiate scoreboard
score_board = Scoreboard()
ball_count = BallCount()

# instantiate paddle
paddle_length = 6  # in units of 5x5 pixels squared
paddle_location = (0, wall['S'] * 0.9)
paddle = Paddle(position=paddle_location, length=6)
paddle_length = paddle_length * 10  # in pixels

# instantiate bricks
brick_length = 30  # in pixels
brick_array = BrickArray(screen=screen_size, length=brick_length)

# instantiate ball
ball_start_position = (paddle_location[0], paddle_location[1] + 20)
ball = Ball(speed=0.05, position=ball_start_position)

# Bind key to paddle movement
screen.listen()
screen.onkeypress(paddle.left, "Left")
screen.onkeypress(paddle.right, "Right")


def main():
    game_is_on = True
    hit_top = False
    hit_red = False
    while game_is_on:
        time.sleep(ball.move_speed)  # sleep to slow screen updates, otherwise goes too fast
        screen.update()
        ball.move()

        # detect collision with top wall
        if ball.ycor() > bounce_limit['N']:
            hit_top = True
            ball.bounce_y()

        if (ball.xcor() > bounce_limit['E']) or (ball.xcor() < bounce_limit['W']):
            ball.bounce_x()

        # detect collision with paddle
        if ball.distance(paddle) < paddle.length and ball.ycor() < ball_start_position[1] + 10:
            ball.bounce_y()

        # detect if paddle misses
        if ball.distance(paddle) > paddle.length and ball.ycor() < ball_start_position[1]:
            new_position = (paddle.xcor(), ball_start_position[1])
            ball_count.remove_ball()
            ball.reset_position(position=new_position)
            ball.bounce_y()

        # if paddle goes beyond boundary
        if paddle.xcor() < wall['W'] + paddle.length:
            xcor = wall['W'] + paddle.length
            paddle.goto(xcor, paddle.ycor())

        if paddle.xcor() > wall['E'] - paddle.length:
            xcor = wall['E'] - paddle.length
            paddle.goto(xcor, paddle.ycor())

        # detect if ball collides with brick
        for brick, state in brick_array.bricks.items():
            if (ball.distance(brick) < brick_length) and (ball.ycor() > brick.ycor() - 10) and state:
                brick.hideturtle()
                points = brick.score
                score_board.increase_score(points)
                ball.bounce_y()
                brick_array.bricks[brick] = False
                brick_array.bricks_hit += 1
                if brick.fillcolor() == "red":
                    hit_red = True
                ball.increase_speed(brick_array.bricks_hit, hit_red)

        if hit_red and hit_top:
            paddle.shrink()

        if ball_count.ball_count == 0:
            score_board.game_over()
            game_is_on = False

        if brick_array.bricks_hit == brick_array.max_bricks:
            score_board.winner()
            game_is_on = False

    screen.exitonclick()


if __name__ == "__main__":
    main()

