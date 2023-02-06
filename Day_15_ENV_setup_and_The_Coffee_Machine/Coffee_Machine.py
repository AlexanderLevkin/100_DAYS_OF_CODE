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
profit = 0


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

"""MY CODE BELOW"""
# def balance_check(money):
#     print("Please insert coins.")
#     money += int(input(f"how many quarters?:")) * 0.25
#     money += int(input("how many dimes?:")) * 0.10
#     money += int(input("how many nickles?:")) * 0.05
#     money += int(input("how many pennies?:")) * 0.01
#     print(f"Here is {round(money, 2)} in change.")
#     return money
#
#
# def check_resources(kind_of_coffee):
#     if kind_of_coffee == "espresso":
#         if MENU[kind_of_coffee]["ingredients"]["water"] <= resources["water"]:
#             resources["water"] -= MENU[kind_of_coffee]["ingredients"]["water"]
#             if MENU[kind_of_coffee]["ingredients"]["coffee"] <= resources["coffee"]:
#                 resources["coffee"] -= MENU[kind_of_coffee]["ingredients"]["coffee"]
#                 return True
#     elif MENU[kind_of_coffee]["ingredients"]["water"] <= resources["water"]:
#         resources["water"] -= MENU[kind_of_coffee]["ingredients"]["water"]
#         if MENU[kind_of_coffee]["ingredients"]["milk"] <= resources["milk"]:
#             resources["milk"] -= MENU[kind_of_coffee]["ingredients"]["milk"]
#             if MENU[kind_of_coffee]["ingredients"]["coffee"] <= resources["coffee"]:
#                 resources["coffee"] -= MENU[kind_of_coffee]["ingredients"]["coffee"]
#                 return True
#             else:
#                 print("Sorry there is not enough coffee.")
#     else:
#         print("Sorry there is not enough water.")
#
#
# def check_transaction(choice, money):
#     if money >= MENU[choice]["cost"]:
#         money -= MENU[choice]["cost"]
#         print(f"Here is your {choice} ☕️. Enjoy!")
#     else:
#         print("You don't have a money for coffee. Money refunded.")
#         return False
#     return money
#
#
# user_money = 0
# status_coffee_machine = True
# while status_coffee_machine:
#     user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
#     if user_choice == "off":
#         print("coffee_machine is OFF")
#         status_coffee_machine = False
#     elif user_choice == "report":
#         print(
#             f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: "
#             f"${round(user_money, 2)}")
#     elif user_choice == "espresso" or "latte" or "cappuccino":
#         if check_transaction(user_choice, money=balance_check(money=user_money)):
#             check_resources(user_choice)
#     else:
#         print("You entered wrong parameters")
