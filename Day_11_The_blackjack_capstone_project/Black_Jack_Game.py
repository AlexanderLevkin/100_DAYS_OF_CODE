import random
from art import logo
user_stack = []
computer_stack = []


def ace():
    if 11 in user_stack and sum(user_stack) > 21:
        user_stack.remove(11)
        user_stack.append(1)
    return user_stack


def stack_of_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def start_game(cards):
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n' :")
    if start == "y":
        print(logo)
        for _ in range(1, 3):
            user_stack.append(cards())
        print(f"Your cards: {user_stack}, current score: {sum(user_stack)}")
        for _ in range(1, 3):
            computer_stack.append(cards())
        print(f"Computer's first card: {computer_stack[0]}")
    else:
        exit()
    return start


start_game(stack_of_cards)

switcher = True
while switcher:
    continue_message = input("Type 'y' to get another card, type 'n' to pass:")
    if continue_message == "y" and sum(user_stack) < 21:
        user_stack.append(stack_of_cards())
        if sum(user_stack) < 21:
            print(f"Your cards: {user_stack}, current score: {sum(user_stack)}")
            print(f"Computer's card: {computer_stack[0]}")
        elif 21 > sum(user_stack) > sum(computer_stack):
            ace()
            print(f"Your cards: {user_stack}, current score: {sum(user_stack)}")
            print(f"Computer's score: {sum(computer_stack)}")
        elif 21 >= sum(user_stack) > sum(computer_stack):
            print(f"Your cards: {user_stack}, current score: {sum(user_stack)}")
            print(f"Computer's score: {sum(computer_stack)}")
            print("You win")
        elif 21 >= sum(user_stack) == sum(computer_stack):
            print(f"Your cards: {user_stack}, current score: {sum(user_stack)}")
            print(f"Computer's score: {sum(computer_stack)}")
            print("Draw")
        else:
            print(f"Your cards: {user_stack}, current score: {sum(user_stack)}")
            print(f"Computer's score: {sum(computer_stack)}")
            print(f"You loose")
            switcher = False
    else:
        if 21 >= sum(user_stack) > sum(computer_stack):
            print(f"Your cards: {user_stack}, current score: {sum(user_stack)}")
            print(f"Computer's score: {sum(computer_stack)}")
            print(f"You win")
        elif 21 >= sum(user_stack) == sum(computer_stack):
            print(f"Your cards: {user_stack}, current score: {sum(user_stack)}")
            print(f"Computer's score: {sum(computer_stack)}")
            print("Draw")
        else:
            print(f"Your cards: {user_stack}, current score: {sum(user_stack)}")
            print(f"Computer's score: {sum(computer_stack)}")
            print(f"You loose")
        switcher = False


