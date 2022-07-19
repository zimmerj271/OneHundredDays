import colorgram
import turtle as t
import random

def get_colors(image_file: str, num_colors: int) -> list:
    colors = colorgram.extract(image_file, num_colors)  # Extract colors from image
    rgb_colors = []
    for color in colors:
        if 230 > color.hsl[2] > 50:
            rgb_colors.append(color.rgb)
    return rgb_colors


color_list = get_colors('image.png', 30)

t.colormode(255)
turtle = t.Turtle()
screen = t.Screen()

width = screen.window_width()
height = screen.window_height()
offset_position = 50
turtle.penup()
turtle.goto(offset_position - screen.window_width()/2, offset_position - screen.window_height()/2)
screen.title("Ripping Off Bad Contemporary Art")
turtle.speed("slow")
turtle.shape("turtle")
number_of_dots = 100
dot_size = 50
step = int(width / number_of_dots)
for dot_count in range(1, number_of_dots + 1):
    random_color = random.choice(color_list)
    # print(rando)
    if dot_count % 10 == 0 and not dot_count % 20 == 0:
        turtle.dot(dot_size, random_color)
        turtle.setheading(90)
        turtle.forward(height / 10)
        turtle.setheading(180)
    elif dot_count % 20 == 0:
        turtle.dot(dot_size, random_color)
        turtle.setheading(90)
        turtle.forward(height / 10)
        turtle.setheading(0)
    else:
        turtle.dot(dot_size, random_color)
        turtle.forward(width / 10)


screen.exitonclick()