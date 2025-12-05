import turtle
import random
import time

screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.goto(0, -280)
player.setheading(90)

PLAYER_SPEED = 20

def move_left():
    x = player.xcor()
    if x > -320:
        player.setx(x - PLAYER_SPEED)

def move_right():
    x = player.xcor()
    if x < 320:
        player.setx(x + PLAYER_SPEED)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.shapesize(stretch_wid=0.3, stretch_len=1)
bullet.penup()
bullet.goto(1000, 1000)
bullet_speed = 12
bullet_state = "ready"

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)

screen.onkeypress(fire_bullet, "space")

barriers = []

def create_barrier(x_pos):
    for i in range(5):
        b = turtle.Turtle()
        b.shape("square")
        b.color("#44ff44")
        b.penup()
        b.shapesize(stretch_wid=0.7, stretch_len=1.2)
        b.goto(x_pos + i * 15, -200)
        barriers.append(b)

create_barrier(-200)
create_barrier(0)
create_barrier(200)

enemies = []
ENEMY_SPEED = 2
wave_number = 1

def spawn_wave():
    global enemies, ENEMY_SPEED
    enemies = []
    ENEMY_SPEED = 2 + wave_number
    for row in range(3):
        for col in range(8):
            e = turtle.Turtle()
            e.shape("square")
            e.color("red")
            e.penup()
            e.goto(-250 + col * 60, 150 + row * 40)
            enemies.append(e)

spawn_wave()

enemy_bullet = turtle.Turtle()
enemy_bullet.shape("square")
enemy_bullet.color("cyan")
enemy_bullet.shapesize(stretch_wid=0.3, stretch_len=1)
enemy_bullet.penup()
enemy_bullet.goto(1000, 1000)
enemy_bullet_speed = 8
enemy_bullet_state = "ready"

def enemy_fire():
    global enemy_bullet_state
    if enemy_bullet_state == "ready" and len(enemies) > 0:
        shooter = random.choice(enemies)
        enemy_bullet.goto(shooter.xcor(), shooter.ycor() - 10)
        enemy_bullet_state = "fire"

def is_collision(a, b):
    return abs(a.xcor() - b.xcor()) < 20 and abs(a.ycor() - b.ycor()) < 20

touched_left = False
touched_right = False

game_over = False

while not game_over:
    screen.update()
    time.sleep(1/60)

    if len(enemies) == 0:
        wave_number += 1
        spawn_wave()
        touched_left = touched_right = False
        continue

    rightmost = max(e.xcor() for e in enemies)
    leftmost = min(e.xcor() for e in enemies)

    if rightmost >= 330:
        touched_right = True
        ENEMY_SPEED *= -1

    if leftmost <= -330:
        touched_left = True
        ENEMY_SPEED *= -1

    if touched_left and touched_right:
        for e in enemies:
            e.sety(e.ycor() - 20)
            if e.ycor() < -250:
                game_over = True
        touched_left = False
        touched_right = False

    for e in enemies:
        e.setx(e.xcor() + ENEMY_SPEED)

    if bullet_state == "fire":
        bullet.sety(bullet.ycor() + bullet_speed)
        if bullet.ycor() > 330:
            bullet.goto(1000, 1000)
            bullet_state = "ready"

    for e in enemies[:]:
        if is_collision(bullet, e):
            bullet.goto(1000, 1000)
            bullet_state = "ready"
            e.goto(1000, 1000)
            enemies.remove(e)

    for b in barriers[:]:
        if is_collision(bullet, b):
            bullet.goto(1000, 1000)
            bullet_state = "ready"
            b.goto(1000, 1000)
            barriers.remove(b)

    if random.random() < 0.02 and len(enemies) > 0:
        enemy_fire()

    if enemy_bullet_state == "fire":
        enemy_bullet.sety(enemy_bullet.ycor() - enemy_bullet_speed)
        if enemy_bullet.ycor() < -330:
            enemy_bullet.goto(1000, 1000)
            enemy_bullet_state = "ready"

    if is_collision(enemy_bullet, player):
        game_over = True

    for b in barriers[:]:
        if is_collision(enemy_bullet, b):
            enemy_bullet.goto(1000, 1000)
            enemy_bullet_state = "ready"
            b.goto(1000, 1000)
            barriers.remove(b)

msg = turtle.Turtle()
msg.hideturtle()
msg.color("white")
msg.write("GAME OVER", align="center", font=("Arial", 36, "bold"))

screen.mainloop()
