import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")
screen.onkey(player.move, "Up")

car_amount = 0
loops = 8
cars_collection = []
game_is_on = True
sleeping = 0.05

while game_is_on:
    time.sleep(sleeping)
    screen.update()

    if player.ycor() > 260:
        player.next_level()
        score.level_up()
        if sleeping > 0.02:
            sleeping -= 0.01

    if car_amount < 35 and loops > 10:
        for n in range(0, random.randint(0, 1)):
            car = CarManager()
            car_amount += 1
            cars_collection.append(car)
        loops = 0

    for n in cars_collection:
        if n.xcor() < -320:
            cars_collection.remove(n)
            car_amount -= 1
        else:
            n.drive()

        if player.distance(n) < 20:
            game_is_on = False
            score.game_over()

    loops += 1

screen.exitonclick()
