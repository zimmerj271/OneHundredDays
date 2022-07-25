import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

EASY = 8
NORMAL = 6
HARD = 5

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager(difficulty=NORMAL)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:


    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

    # Level up of player makes it across
    if player.crossed_road():
        player.reset_player()
        scoreboard.level_up()
        car_manager.level_up()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()
