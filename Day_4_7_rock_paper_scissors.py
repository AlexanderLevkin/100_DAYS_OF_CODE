import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
picture = [rock, paper, scissors]
player = int(input("What do you want to choose 0 - rock, 1 - paper, 2 - scissors?\n"))
computer = random.randint(0, 2)
if player >= 3 or player < 0:
    print("You choose invalid number!")
else:
    print(f"You chose:\n{picture[player]}")
    print(f"Computer chose: {picture[computer]}")
if computer == 0 and player == 2:
    print("You lose!")
elif player == computer:
    print("Draw")
elif player == 0 and computer == 2:
    print("You win!")
elif computer > player:
    print("You lose")
elif computer < player < 3:
    print("You win!")





