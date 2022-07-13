import data
import logo


def drink_exists(drink):
    for n in data.MENU[drink]["ingredients"]:
        if data.MENU[drink]['ingredients'][n] > data.resources[n]:
            print(f"Sorry there is not enough {n}.")
            return 1
        else:
            data.resources[n] -= data.MENU[drink]['ingredients'][n]

        return 0


def money(money):
    try:
        return int(input(f"How many {money}?: "))
    except ValueError:
        return 0


def transaction(drink):
    print(f"It will be ${data.MENU[drink]['cost']}. Please insert coins")
    quarters = money("quarters")
    dimes = money("dimes")
    nickles = money("nickles")
    pennies = money("pennies")
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    if total >= data.MENU[drink]['cost']:
        refund = round(total - data.MENU[drink]['cost'], 2)
    else:
        print(f"Sorry that's not enough money. Money refunded: {total}")
        return -1
    return refund


print(logo.logo)
balance = 0.0

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report" or choice == "r":
        print(f"Water: {data.resources['water']}ml")
        print(f"Milk: {data.resources['milk']}ml")
        print(f"Coffee: {data.resources['coffee']}g")
        print(f"Money: ${balance}")
    elif choice == "espresso" or choice == "e":
        pour = drink_exists("espresso")
        if pour == 0:
            refund = transaction("espresso")
            if refund != -1:
                if refund != 0:
                    print(f"Money refunded: {refund}")
                balance += data.MENU['espresso']['cost']
                for n in data.MENU['espresso']["ingredients"]:
                    data.resources[n] -= data.MENU['espresso']['ingredients'][n]
                print("Here is your espresso. Enjoy!")
    elif choice == "latte" or choice == "l" or choice == "latt":
        pour = drink_exists("latte")
        if pour == 0:
            refund = transaction("latte")
            if refund != 0:
                print(f"Money refunded: {refund}")
            balance += data.MENU['latte']['cost']
            for n in data.MENU['latte']["ingredients"]:
                data.resources[n] -= data.MENU['latte']['ingredients'][n]
            print("Here is your latte. Enjoy!")
    elif choice == "cappuccino" or choice == "c":
        pour = drink_exists("cappuccino")
        if pour == 0:
            refund = transaction("cappuccino")
            if refund != 0:
                print(f"Money refunded: {refund}")
            balance += data.MENU['cappuccino']['cost']
            for n in data.MENU['cappuccino']["ingredients"]:
                data.resources[n] -= data.MENU['cappuccino']['ingredients'][n]
            print("Here is your cappuccino. Enjoy!")
    elif choice == "off" or choice == "o":
        break
