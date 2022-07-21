from turtle import Turtle
import random


COLORS = ["#F7BCD6", "#D0B3DD", "#FFEBC4", "#ABD9B4", "#ABD9B4", "#ABD9B4", "#AFE4FE"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(COLORS[random.randint(0, 6)])
        self.goto(300, random.randint(-240, 220))

    def drive(self):
        self.forward(random.randint(1, 2))


