import turtle as t
import random

t.colormode(255)
turtle = t.Turtle()
TOTAL_ANGLE = 360
turtle.speed("fastest")


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb = (red, green, blue)
    return rgb


def draw_spirograph(angle, radius):
    for _ in range(int(TOTAL_ANGLE / angle)):
        current_heading = turtle.heading()
        turtle.pencolor(random_color())
        turtle.circle(radius)
        turtle.setheading(current_heading + angle)

draw_spirograph(5, 180)
screen = t.Screen()
screen.exitonclick()
