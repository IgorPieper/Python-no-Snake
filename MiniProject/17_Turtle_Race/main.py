from turtle import Turtle, Screen
from random import randint

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
decision = screen.textinput("Who will win?", "Which ninja turtle will win the race? (Blue, Purple, Orange, Red, Gray): ").lower()

Leonardo = Turtle()
Leonardo.color("blue")
Leonardo.shape("turtle")
Leonardo.penup()
Leonardo.goto(x=-240, y=25)

Donatello = Turtle()
Donatello.color("purple")
Donatello.shape("turtle")
Donatello.penup()
Donatello.goto(x=-240, y=-25)

Michelangelo = Turtle()
Michelangelo.color("orange")
Michelangelo.shape("turtle")
Michelangelo.penup()
Michelangelo.goto(x=-240, y=50)

Raphael = Turtle()
Raphael.color("red")
Raphael.shape("turtle")
Raphael.penup()
Raphael.goto(x=-240, y=-50)

Shredder = Turtle()
Shredder.color("gray")
Shredder.penup()
Shredder.goto(x=-235, y=0)

all_turtles = [Leonardo, Donatello, Michelangelo, Shredder, Raphael]

if decision:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == decision:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
