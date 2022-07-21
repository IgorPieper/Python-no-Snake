from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
apple = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "w")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(apple) < 17:
        apple.refresh()
        snake.extend()
        score.update_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
