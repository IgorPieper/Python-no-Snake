import random
import logo

print(logo.logo)

while True:
    answer = random.randint(1, 100)

    print("I'm thinking of a number between 1 and 100.")
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == "e" or choice == "easy":
        attempts = 10
    else:
        attempts = 5

    while True:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            choice = int(input("Make a guess: "))
        except ValueError:
            choice = 0
        if choice == answer:
            print("BINGO, you guessed the number!")
            break
        elif choice > answer:
            print("Too high.")
        elif choice < answer:
            print("To low.")

        attempts -= 1

        if attempts <= 0:
            print("You've run out of guesses, you lose.")
            print(f"I was thinking of number {answer}")
            break
        else:
            print("Guess again.")

    choice = input("Do you want to play again? Yes(Y) or No(N): ").lower()

    if choice == "no" or choice == "n":
        break

    print("\n"*20)
