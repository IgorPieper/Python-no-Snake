from turtle import *
from random import *


def starting():
    screen = Screen()
    cursor = Turtle()
    cursor.color("green", "lime")
    cursor.pencolor("brown")
    screen.bgcolor("white")
    return screen, cursor


def paint_shapes():
    how_many = 3

    for n in range(0, 8):
        for m in range(0, how_many):
            cursor.forward(100)
            cursor.left(360 / how_many)
        how_many += 1
        random_color()


def random_color():
    screen.colormode(255)
    cursor.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))


def random_direction():
    direction = randint(1, 4)
    if direction == 1:
        cursor.left(90)
    elif direction == 2:
        cursor.left(180)
    elif direction == 3:
        cursor.left(270)


while True:
    print("+--------------------------------------------------- +")
    print("| 1. Ten dollar painting                             |")
    print("| 2.Thousand dollar painting                         |")
    print("| 3. One hundred thousand dollar painting            |")
    print("| 4. Million dollar painting                         |")
    print("+--------------------------------------------------- +")
    try:
        choice = int(input("How expensive image you want to generate: "))
    except ValueError:
        choice = 0

    screen, cursor = starting()

    if choice == 1:
        cursor.penup()
        cursor.goto(-100, -100)
        cursor.pendown()
        paint_shapes()
        break
    elif choice == 2:
        cursor.pensize(10)
        cursor.speed(100)
        for n in range(0, 300):
            random_direction()
            random_color()
            cursor.forward(20)
        break
    elif choice == 3:
        cursor.speed(100)
        cursor.pensize(2)
        for n in range(0, 90):
            random_color()
            cursor.circle(100)
            cursor.left(4)
        break
    elif choice == 4:
        cursor.penup()
        for n in range(-5, 5):
            for m in range(-5, 5):
                cursor.goto(n*50, m*50)
                random_color()
                cursor.dot(20)
        break


screen.exitonclick()
