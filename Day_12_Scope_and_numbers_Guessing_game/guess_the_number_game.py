# Number Guessing Game Objectives:
import random

# Include an ASCII art logo.
from logo import art


# Allow the player to submit a guess for a number between 1 and 100.
NUMBER = random.randint(1, 100)

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.

user_input = input(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPssst, "
                   f"the correct answer is "
                   f"{NUMBER}\nChoose a difficulty. Type 'easy' or 'hard': \n").lower()


if user_input == "easy":
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
elif user_input == "hard":
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
else:
    print("You type wrong symbols")

while attempts > 0:
    guess = int(input("Make a guess: "))
    attempts -= 1
    if guess == NUMBER:
        print("YOU WON!!!.")
        attempts = 0
    elif guess > NUMBER:
        print("Too hight.")
    elif guess < NUMBER:
        print("Too low.")
    print(f"You have {attempts} attempts remaining to guess the number.")

else:
    print("You've run out of guesses, you lose.")
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
