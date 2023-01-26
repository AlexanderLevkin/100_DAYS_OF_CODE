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


def stack_of_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def start_game():
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n' :")
    if start == "y":
        print(logo)
        user_stack.append(stack_of_cards())
        user_stack.append(stack_of_cards())
        print(user_stack)
    else:
        exit()
    return start

start_game()
# if start_game() == "y":
#     user_score.append(stack_of_cards())
#     print(f"Your cards: {}, current score: {sum(computer_score)}")
#     print(f"Computer's first card: {computer_score}")
#
#     switcher = True
#     while switcher:
#         if input("Type 'y' to get another card, type 'n' to pass:") == "y":
#             next_round = main_round_user.append(random.choice(cards))
#             current_user_score = sum(main_round_user)
#             print(f"Your cards: {main_round_user}, current score: {current_user_score}")
#             print(f"Computer's card: {computer_score + computer_score}")
#             if current_user_score > 21:
#                 for i in range(current_user_score):
#                     if i == 11:
#                         i = 1
#                         sum(main_round_user)
#                 print(f"Your final hand: {main_round_user}, final score: {sum(main_round_user)}")
#
#
#         else:
#             print(f"Your final hand: {main_round_user}, final score: {sum(main_round_user)}")
#             print(computer_score)
#             final_computer_score = computer_score.append(random.choice(cards))
#             print(final_computer_score)
#             print(f"Computer's final hand: {final_computer_score}, final score: {sum(computer_score)}")
#
#             if sum(main_round_user) < sum(computer_score):
#                 print("You lose 😤")
#             elif sum(main_round_user) == sum(computer_score):
#                 print("Draw")
#             else:
#                 print("You win")
#
#             switcher = False
# else:
#     exit()
