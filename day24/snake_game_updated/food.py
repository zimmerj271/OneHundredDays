from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()  # inherit from the Turtle class
        self.shape("circle")  # initialize shape as 'circle'
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # default size is 20x20 px, resize to half
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-230, 230)
        random_y = random.randint(-230, 230)
        self.goto(random_x, random_y)