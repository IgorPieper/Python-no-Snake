from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import logo

print(logo)
menu = Menu()
machine = MoneyMachine()
coffee = CoffeeMaker()

while True:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "report" or choice == "r":
        coffee.report()
        machine.report()
    elif choice == "espresso" or choice == "e":
        drink = menu.find_drink("espresso")
        pour = coffee.is_resource_sufficient(drink)
        if pour:
            result = machine.make_payment(drink.cost)
            if result:
                coffee.make_coffee(drink)
    elif choice == "latte" or choice == "l" or choice == "latt":
        drink = menu.find_drink("latte")
        pour = coffee.is_resource_sufficient(drink)
        if pour:
            result = machine.make_payment(drink.cost)
            if result:
                coffee.make_coffee(drink)
    elif choice == "cappuccino" or choice == "c":
        drink = menu.find_drink("cappuccino")
        pour = coffee.is_resource_sufficient(drink)
        if pour:
            result = machine.make_payment(drink.cost)
            if result:
                coffee.make_coffee(drink)
    elif choice == "off" or choice == "o":
        break
