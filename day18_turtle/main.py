# from turtle import Turtle, Screen
#
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("green")
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
# # draw a square
# for x in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

from turtle import Screen
import turtle as t
import random

# import heroes
tim = t.Turtle()
tim.shape("turtle")
tim.color("green")
# print(heroes.gen())
# print dotted line
# for x in range(20):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
def draw_shape(number_sides):
    TOTAL_ANGLE = 360
    sides = number_sides
    for s in range(sides):
        tim.forward(100)
        tim.left(TOTAL_ANGLE / sides)

colors = ["blue", "green", "red", "cyan", "indigo", "dark magenta", "gold", "light sky blue", "lime",
          "firebrick", "dark gray", "cornflower blue", "sea green", "olive drab", "lavender", "orange",
          "medium purple", "sienna", "dark khaki", "rosy brown"]
for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

# screen = Screen()
# screen.exitonclick()