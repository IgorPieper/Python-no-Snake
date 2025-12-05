import turtle
import time

#  SETUP SCREEN
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=500, height=700)
screen.tracer(0)

WALL_COLOR = "#C0C0C0"

# DRAW WALLS
walls = turtle.Turtle()
walls.hideturtle()
walls.speed(0)
walls.color(WALL_COLOR)
walls.pensize(10)

# Left wall
walls.penup()
walls.goto(-240, -350)
walls.pendown()
walls.goto(-240, 330)

# Right wall
walls.penup()
walls.goto(240, -350)
walls.pendown()
walls.goto(240, 330)

# Top wall
walls.penup()
walls.goto(-240, 330)
walls.pendown()
walls.goto(240, 330)


# SCORE SYSTEM
broken_tiles = 0
lost_rounds = 0

score1 = turtle.Turtle()
score1.hideturtle()
score1.color("white")
score1.penup()
score1.goto(-150, 250)
score1.write("000", align="center", font=("Courier", 32, "normal"))

score2 = turtle.Turtle()
score2.hideturtle()
score2.color("white")
score2.penup()
score2.goto(150, 250)
score2.write("000", align="center", font=("Courier", 32, "normal"))


def update_scores():
    score1.clear()
    score1.write(f"{broken_tiles:03}", align="center", font=("Courier", 32, "normal"))

    score2.clear()
    score2.write(f"{lost_rounds:03}", align="center", font=("Courier", 32, "normal"))


# BRICK CREATION SYSTEM
bricks = []


def create_bricks():
    # remove old bricks
    for b in bricks:
        b.hideturtle()
        b.goto(2000, 2000)

    bricks.clear()

    brick_colors = [
        "#CC0000", "#CC0000",
        "#FF6600", "#FF6600",
        "#FFCC00", "#FFCC00",
        "#66CC00", "#66CC00",
    ]

    brick_width = 45
    brick_height = 15

    start_x = -210
    start_y = 180

    for row in range(8):
        for col in range(10):
            brick = turtle.Turtle()
            brick.speed(0)
            brick.shape("square")
            brick.color(brick_colors[row])
            brick.penup()
            brick.shapesize(stretch_wid=0.7, stretch_len=2.2)

            x = start_x + col * (brick_width + 2)
            y = start_y - row * (brick_height + 2)
            brick.goto(x, y)

            bricks.append(brick)


create_bricks()

#  PADDLE
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("#0099FF")
paddle.shapesize(stretch_wid=0.7, stretch_len=3)
paddle.penup()
paddle.speed(0)
paddle.goto(0, -300)

PADDLE_SPEED = 20


def move_left():
    if paddle.xcor() > -220:
        paddle.setx(paddle.xcor() - PADDLE_SPEED)


def move_right():
    if paddle.xcor() < 220:
        paddle.setx(paddle.xcor() + PADDLE_SPEED)


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")


# BALL
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=0.6, stretch_len=0.6)
ball.penup()

START_SPEED = 3.5
ball.dx = START_SPEED
ball.dy = START_SPEED


def speed_up_ball():
    ball.dx *= 1.10
    ball.dy *= 1.10


def reset_game():
    global broken_tiles

    broken_tiles = 0
    update_scores()

    paddle.goto(0, -300)
    ball.goto(0, -250)

    ball.dx = START_SPEED
    ball.dy = START_SPEED

    create_bricks()
    time.sleep(1)


# GAME LOOP
while True:
    screen.update()
    time.sleep(0.004)

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Walls
    if ball.xcor() > 230:
        ball.setx(230)
        ball.dx *= -1

    if ball.xcor() < -230:
        ball.setx(-230)
        ball.dx *= -1

    if ball.ycor() > 320:
        ball.sety(320)
        ball.dy *= -1

    # Paddle collision
    if (
        ball.ycor() < -280
        and paddle.xcor() - 40 < ball.xcor() < paddle.xcor() + 40
        and ball.dy < 0
    ):
        ball.sety(-280)
        ball.dy *= -1
        speed_up_ball()

    # Full reset feather
    if ball.ycor() < -350:
        lost_rounds += 1
        update_scores()
        reset_game()

    # Brick collisions
    for brick in bricks:
        if (
            abs(ball.xcor() - brick.xcor()) < 25 and
            abs(ball.ycor() - brick.ycor()) < 12
        ):
            ball.dy *= -1
            brick.goto(2000, 2000)
            bricks.remove(brick)

            # increase score
            broken_tiles += 1
            update_scores()

            break
