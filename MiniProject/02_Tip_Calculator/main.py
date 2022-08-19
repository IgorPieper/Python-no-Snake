print("Welcome to the SUPER Tip-Calculator", end="")
input()
full_cost = float(input("What was the total bill? "))
while True:
    tip_percentage = int(input("What percentage tip would you like to give? "))
    if 0 <= tip_percentage:
        break
    else:
        print("It is impossible to give such a tip!")
tip_percentage = float((tip_percentage/100)+1)
people_amount = int(input("How many people to split the bill? "))
print(f"Each person should pay: ${round(float((full_cost/people_amount)*tip_percentage),2)}")

