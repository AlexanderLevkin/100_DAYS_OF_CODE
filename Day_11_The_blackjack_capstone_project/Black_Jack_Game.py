import random

from art import logo

############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


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
    ace()
    if continue_message == "y" and sum(user_stack) < 21:
        user_stack.append(stack_of_cards())
        print(f"Your cards: {user_stack}, current score: {sum(user_stack)}")
        computer_stack.append(stack_of_cards())
        print(f"Computer's card: {computer_stack[0]}")
    elif continue_message == "y" and sum(user_stack) > 21:
        print(f"Your cards: {user_stack}, current score: {sum(user_stack)}")
        print(f"Computer's card: {computer_stack}")

