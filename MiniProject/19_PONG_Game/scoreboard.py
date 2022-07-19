from turtle import Turtle


class Score(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x_pos, y_pos)
        self.write(self.score, False, "center", ("Arial", 60, "normal"))

    def show_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, False, "center", ("Arial", 60, "normal"))


    def game_over(self, player):
        self.goto(0, 0)
        self.write(f"{player} have won!", False, "center", ("Arial", 16, "normal"))
