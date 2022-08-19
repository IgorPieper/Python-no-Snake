import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the stone paper and scissors competition. ", end="")
input()
print("You're about to play for the CEO's handshake with the invincible computer itself.", end="")
input()
print("Good Luck", end="")
input()

while True:
    try:
        choice = int(input("Write 1 to play stone, 2 to play paper and 3 to play scissors: "))
    except ValueError:
        choice = 4
    if choice == 1:
        print(rock)
        break
    elif choice == 2:
        print(paper)
        break
    elif choice == 3:
        print(scissors)
        break

computer_choice = random.randint(1, 3)

print("The computer played:")

if computer_choice == 1:
    print(rock)
elif computer_choice == 2:
    print(paper)
elif computer_choice == 3:
    print(scissors)

if choice == 1 and computer_choice == 1:
    print("You have a draw")
elif choice == 2 and computer_choice == 2:
    print("You have a draw")
elif choice == 3 and computer_choice == 3:
    print("You have a draw")
elif choice == 1 and computer_choice == 2:
    print("You have lost")
elif choice == 2 and computer_choice == 3:
    print("You have lost")
elif choice == 3 and computer_choice == 1:
    print("You have lost")
elif choice == 1 and computer_choice == 3:
    print("You have won")
elif choice == 2 and computer_choice == 1:
    print("You have won")
elif choice == 3 and computer_choice == 2:
    print("You have won")
