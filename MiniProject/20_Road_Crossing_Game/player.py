from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("#D5E3AF")
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        self.goto(0, -280)
