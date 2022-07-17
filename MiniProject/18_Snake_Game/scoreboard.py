from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", False, "center", ("Arial", 16, "normal"))

    def show_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, "center", ("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", ("Arial", 16, "normal"))
