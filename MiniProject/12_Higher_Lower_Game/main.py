import random
import game_data
import logo


def game():
    score = 0
    print(logo.logo)
    who1 = random.randint(1, 50)

    while True:
        who2 = random.randint(1, 50)

        print(f"Compare A: {game_data.data[who1]['name']}, {game_data.data[who1]['description']}, from {game_data.data[who1]['country']}")
        print(logo.vs)
        print(f"Against B: {game_data.data[who2]['name']}, {game_data.data[who2]['description']}, from {game_data.data[who2]['country']}")
        while True:
            choice = input("Who has more followers? Type 'A' or 'B': ").lower()
            if choice == "a" or choice == "b":
                break

        personA = game_data.data[who1]["follower_count"]
        personB = game_data.data[who2]["follower_count"]

        if personA > personB:
            if choice == "b":
                print(f"Sorry, that's wrong. Final score: {score}")
                break
        elif personB > personA:
            if choice == "a":
                print(f"Sorry, that's wrong. Final score: {score}")
                break

        score += 1
        print("\n" * 20)
        print(f"You're right! Current score: {score}.")

        who1 = who2


while True:
    game()
    choice = input("Do you want to play again?? Yes(y), or No(n): ").lower()
    if choice == "no" or choice == "n":
        break
