from turtle import Turtle, Screen
from random import randint

racing = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
user_bet = screen.textinput(title="Place your bet!", prompt="Which turtle will win the race? Enter a color: ").lower()
turtles = []
y = -100
for c in colors:
    t = Turtle(shape="turtle")
    t.penup()
    t.color(c)
    t.goto(x=-230, y=y)
    turtles.append(t)
    y += 40

if user_bet:
    racing = True

while racing:
    for t in turtles:
        t.forward(randint(0, 10))
        if t.xcor() > 230:
            racing = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You win! The winner of the race is {winning_color}!")
            else:
                print(f"You lose.  The winner of the race is {winning_color}")


screen.exitonclick()
