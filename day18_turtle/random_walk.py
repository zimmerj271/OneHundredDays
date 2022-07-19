import turtle as t
import random

t.colormode(255) # change colormode within turtle module
turtle = t.Turtle()
turtle.pensize(10)
turtle.speed("fastest")
colors = ["blue", "green", "red", "cyan", "indigo", "dark magenta", "gold", "light sky blue", "lime",
          "firebrick", "dark gray", "cornflower blue", "sea green", "olive drab", "lavender", "orange",
          "medium purple", "sienna", "dark khaki", "rosy brown"]
direction = [x * 90 for x in range(0, 4)]

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb = (red, green, blue)
    return rgb


for _ in range(500):
    turtle.pencolor(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(direction))