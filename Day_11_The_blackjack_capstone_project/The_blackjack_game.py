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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_score = random.sample(cards, 1)
print(computer_score)
main_round_user = random.sample(cards, 2)

if input("Do you want to play a game of Blackjack? Type 'y' or 'n' :") == "y":
    print(logo)
    print(f"Your cards: {main_round_user}, current score: {sum(main_round_user)}")
    print(f"Computer's first card: {computer_score}")

switcher = True
while switcher:
    if input("Type 'y' to get another card, type 'n' to pass:") == "y":
        next_round = main_round_user.append(random.choice(cards))
        print(f"Your cards: {main_round_user}, current score: {sum(main_round_user)}")
    else:
        print(f"Your final hand: {main_round_user}, final score: {sum(main_round_user)}")
        print(computer_score)
        final_computer_score = computer_score.append(random.choice(cards))
        print(final_computer_score)
        print(f"Computer's final hand: {final_computer_score}, final score: {sum(computer_score)}]")

        if sum(main_round_user) < sum(computer_score):
            print("You lose 😤")
        else:
            print("You win")

        switcher = False
