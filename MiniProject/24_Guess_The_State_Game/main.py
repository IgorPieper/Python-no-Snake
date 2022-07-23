import turtle
import pandas


def write_on_screen(what, x_position, y_position):
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()
    writer.goto(x_position, y_position)
    writer.write(what, False, "center", ("Deja Vu Sans Mono", 8, "bold"))


# creation of a window
screen = turtle.Screen()
screen.title("U.S. States Game")

# adding a background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed = 0
answered_states = []

# data import
states_information = pandas.read_csv("50_states.csv")

while guessed != 50:
    answer = screen.textinput(title=f"{guessed}/50 Guess the State", prompt="What's another state's name?")
    try:
        answer = answer.title()
    except AttributeError:
        answer = "Exit"

    states_list = states_information["state"].to_list()

    if answer == "Exit":
        print("You haven't guessed: ")
        for n in states_list:
            if n not in answered_states:
                print(f"{n}, ", end="")
        break

    if answer in states_list:
        if answer not in answered_states:
            guessed += 1
            answered_states.append(answer)
            state_data = states_information[states_information.state == answer]
            x_position = state_data.x
            y_position = state_data.y
            write_on_screen(answer, int(x_position), int(y_position))

screen.exitonclick()
