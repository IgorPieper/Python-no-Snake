from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.create_paddle()
        self.shape("square")

    def create_paddle(self):
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(self.x_pos, self.y_pos)

    def up(self):
        if self.ycor() < 240:
            self.forward(20)

    def down(self):
        if self.ycor() > -240:
            self.backward(20)
