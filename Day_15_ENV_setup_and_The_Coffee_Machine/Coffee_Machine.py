MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

"""MY CODE BELOW"""
def balance_check(money):
    print("Please insert coins.")
    money += int(input(f"how many quarters?:")) * 0.25
    money += int(input("how many dimes?:")) * 0.10
    money += int(input("how many nickles?:")) * 0.05
    money += int(input("how many pennies?:")) * 0.01
    print(f"Here is {round(money, 2)} in change.")
    return money


def check_resources(kind_of_coffee):
    if kind_of_coffee == "espresso":
        if MENU[kind_of_coffee]["ingredients"]["water"] <= resources["water"]:
            resources["water"] -= MENU[kind_of_coffee]["ingredients"]["water"]
            if MENU[kind_of_coffee]["ingredients"]["coffee"] <= resources["coffee"]:
                resources["coffee"] -= MENU[kind_of_coffee]["ingredients"]["coffee"]
                return True
    elif MENU[kind_of_coffee]["ingredients"]["water"] <= resources["water"]:
        resources["water"] -= MENU[kind_of_coffee]["ingredients"]["water"]
        if MENU[kind_of_coffee]["ingredients"]["milk"] <= resources["milk"]:
            resources["milk"] -= MENU[kind_of_coffee]["ingredients"]["milk"]
            if MENU[kind_of_coffee]["ingredients"]["coffee"] <= resources["coffee"]:
                resources["coffee"] -= MENU[kind_of_coffee]["ingredients"]["coffee"]
                return True
            else:
                print("Sorry there is not enough coffee.")
    else:
        print("Sorry there is not enough water.")


def check_transaction(choice, money):
    if money >= MENU[choice]["cost"]:
        money -= MENU[choice]["cost"]
        print(f"Here is your {choice} ☕️. Enjoy!")
    else:
        print("You don't have a money for coffee. Money refunded.")
        return False
    return money


user_money = 0
status_coffee_machine = True
while status_coffee_machine:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        print("coffee_machine is OFF")
        status_coffee_machine = False
    elif user_choice == "report":
        print(
            f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: "
            f"${round(user_money, 2)}")
    elif user_choice == "espresso" or "latte" or "cappuccino":
        if check_transaction(user_choice, money=balance_check(money=user_money)):
            check_resources(user_choice)
    else:
        print("You entered wrong parameters")
