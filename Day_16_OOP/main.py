from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_report = CoffeeMaker()
money_report = MoneyMachine()
money_report.report()
machine_report.report()

menu = Menu()
kind_of_coffee = menu.get_items()


is_on = True

while is_on:
    choice = input(f"What would you like? {kind_of_coffee}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_report.report()
        machine_report.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        is_resource_sufficient = CoffeeMaker().is_resource_sufficient(drink)
        # if is_resource_sufficient(drink["ingredients"]):
        #     payment = process_coins()
        #     if is_transaction_successful(payment, drink["cost"]):
        #         make_coffee(choice, drink["ingredients"])