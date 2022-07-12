logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return 0


print(logo)

def calculator():

    math = {"+": add, "-": subtract, "*": multiply, "/": divide}

    try:
        num1 = float(input("What's the first number?: "))
    except ValueError:
        num1 = 0

    while True:

        try:
            num2 = float(input("What's the next number?: "))
        except ValueError:
            num2 = 0

        for n in math:
            print(n)

        operator = input("Pick an operation from the line above: ")

        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            function = math[operator]
            answer = function(num1, num2)
            print(f"{num1} {operator} {num2} = {answer}")
        else:
            print("Symbol not recognized")
            answer = num1

        loop = input("Do you want to continue (c), start over (s), or turn off the calculator (e)? ").lower()

        if(loop == "s"):
            calculator()
        elif(loop == "e"):
            break
            break

        num1 = answer

calculator()
