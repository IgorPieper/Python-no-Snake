logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.")
bidder = {}

while True:
    name = input("What is your name!: ")
    try:
        bid = int(input("What is your bid?: $"))
    except ValueError:
        bid = 0

    bidder[name] = bid

    next_one = input("Are there any other bidder? (Yes or No): ").lower()
    print('\n' * 80)
    if next_one == "no" or next_one == "n":
        break

helper1 = "name"
helper2 = 0

for n in bidder:
   if bidder[n] > helper2:
       helper2 = bidder[n]
       helper1 = n

print(f"The winner is {helper1} with a bid of ${helper2}.")
