print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
win = 0

while True:
    wybor1 = input("Walking through a quiet forest you meet a cave. Do you want to enter it? (Y/N) ")
    if wybor1 == "Y" or wybor1 == "y":
        print("Excellent, you just entered a suspicious cave and met a bear", end="")
        input()
        print("Or no, the bear wasn't there. It's just your imagination")
        break
    elif wybor1 == "N" or wybor1 == "n":
        print("So you walked away leaving curiosity aside you continued towards the setting sun", end="")
        input()
        print("Until then, it's not very safe in the woods at night. Hearing howling wolves, you decided it should be safer in the cave")
        break
    else:
        print("It's so quiet here, you couldn't hear your thoughts. I'll ask again ...")

print("Walking down a long dark corridor you come across a crossroads. The left road looks like the right road, and the right road looks like the left road.")
wybor = input("It's time to choose a path (L/R):  ")

if wybor == "L" or wybor == "l" or wybor == "Left" or wybor == "left":
    print("However, there is nothing here", end="")
    input()
    print("Or at least that's what you thought. There was a river")
    input("Are you swimming through it? (Y/N) ")
    if wybor1 == "N" or wybor1 == "n":
        print("So what do you plan to do? Are you going to wait here until certain death?", end="")
        input()
        print("Whatever, you are boring me. Grab a bridge and go now", end="")
        input()
        print("Who put the door in the middle of the cave?")
        wybor2 = input("It's time for one last choice. Choose the door you want to go through. (Red/Yellow/Blue) ")
        if wybor2 == "Red" or wybor2 == "red" or wybor2 == "r" or wybor2 == "R":
            print("The warm handle told you that this path would be the right one", end="")
            input()
            print("Your intuition was wrong. You cooked yourself standing up")
            win += 1
        elif wybor2 == "Blue" or wybor2 == "blue" or wybor2 == "b" or wybor2 == "B":
            print("The cold handle told you that this path would be the right one", end="")
            input()
            print("Your intuition was wrong. You have been eaten by a monstrous frozen food")
            win += 1
        elif wybor2 == "Yellow" or wybor2 == "yellow" or wybor2 == "y" or wybor2 == "Y":
            print("The dazzling handle told you that this path would be the right one", end="")
            input()
            print("Your intuition was not wrong. Behold, the treasure appeared to your eyes.")
        else:
            print("No choice is also a choice", end="")
            input()
            print("You were eaten by grandfather time")
            win += 1
    else:
        print("The water was slightly cold, but swimmable", end="")
        input()
        print("You just didn't anticipate one thing. A leg cramp. And the big trout was just waiting for it.")
        win += 1
else:
    print("Well, it was only one way, though. You hit your head VERY hard. And mom said look under your feet")
    win += 1

if win == 0:
    print("And the real treasure was your heart")
else:
    print("Game Over")
    
