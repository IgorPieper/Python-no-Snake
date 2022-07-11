import random
import logo


def give_card(who):
    who.append(card_list[random.randint(0, 12)])


def blackjack():
    computer = []
    user = []

    print(logo.logo)

    give_card(computer)
    give_card(computer)

    give_card(user)
    give_card(user)

    while True:

        print(f"Computer = [ _ , {computer[1]}]\n")
        print(f"User = {user}\n")

        user_result = sum(user)
        computer_result = sum(computer)

        if user_result == computer_result and user_result == 21:
            return 2
        elif user_result == 21:
            return 0
        elif computer_result == 21:
            print(f"Computer = {computer}\n")
            return 1
        elif user_result > 21:
            if 11 in user:
                user[user.index(11)] = 1
                user_result = sum(user)
                print(f"User = {user}\n")
            if user_result > 21:
                print("Bust!")
                return 1

        choice = input("Do you want to take another card? Yes(y), or No(n): ").lower()
        if choice == "y" or choice == "yes":
            give_card(user)
        else:
            break

    while True:
        print(f"Computer = {computer}\n")
        computer_result = sum(computer)

        if computer_result < 17:
            give_card(computer)
        else:
            break

        computer_result = sum(computer)

        if computer_result > 21:
            if 11 in computer:
                computer[computer.index(11)] = 1
                computer_result = sum(computer)
                print(f"Computer = {computer}\n")
            else:
                print(f"Computer = {computer}\n")
                return 0

    if computer_result > user_result:
        print(f"Computer = {computer}\n")
        return 1
    elif computer_result < user_result:
        return 0
    elif computer_result == user_result:
        return 2


card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

choice = input("Are you over 18 and want to play blackjack. Yes(y), or No(n): ").lower()

while True:
    if choice == "y" or choice == "yes":
        winner = blackjack()
        if winner == 0:
            print("You Won")
        elif winner == 1:
            print("You Lose")
        elif winner == 2:
            print("it's a draw")

    choice = input("Do you want to play again?: ").lower()
    if choice == "n" or choice == "no":
        break
