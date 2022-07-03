import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
while True:
    try:
        nr_letters = int(input("How many letters would you like in your password? "))
        if nr_letters >= 1:
            break
        else:
            print("Password must be longer")
    except ValueError:
        print("Please specify length")

try:
    nr_symbols = int(input(f"How many symbols would you like? "))
    if nr_symbols < 0:
        nr_symbols = 0
except ValueError:
    nr_symbols = 0

try:
    nr_numbers = int(input(f"How many numbers would you like? "))
    if nr_numbers < 0:
        nr_numbers = 0
except ValueError:
    nr_numbers = 0

password = []

for n in range(0, nr_letters):
    helper = random.randint(0, len(letters)-1)
    password += letters[helper]

for n in range(0, nr_symbols):
    helper = random.randint(0, len(symbols) - 1)
    helper2 = random.randint(0, len(password)-1)
    password.insert(helper2, symbols[helper])

for n in range(0, nr_numbers):
    helper = random.randint(0, len(numbers) - 1)
    helper2 = random.randint(0, len(password)-1)
    password.insert(helper2, numbers[helper])

passw = ""

for n in password:
    passw += n

print("Your password is:\n")

print(passw)
