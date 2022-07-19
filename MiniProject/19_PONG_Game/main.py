from turtle import Screen
from paddle import Paddle
from scoreboard import Score
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

paddle1 = Paddle(-360, 20)
paddle2 = Paddle(360, 20)
score1 = Score(-100, 200)
score2 = Score(100, 200)
ball = Ball()

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

game_is_on = True
speed = 0.1

while game_is_on:
    screen.update()
    time.sleep(speed)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(paddle2) < 50 and ball.xcor() > 330) or (ball.distance(paddle1) < 50 and ball.xcor() < -330):
        ball.bounce_x()
        speed -= 0.01

    if ball.xcor() < -400:
        score2.show_score()
        ball.reset()
        speed = 0.1
    elif ball.xcor() > 400:
        score1.show_score()
        ball.reset()
        speed = 0.1

    if score1.score > 5:
        score1.game_over("Player 1")
        game_is_on = False
    elif score2.score > 5:
        score2.game_over("Player 2")
        game_is_on = False


screen.exitonclick()
