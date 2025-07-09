import random

rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Setting up the list and the inputs of the game
options = [rock, paper, scissors]
computer_chosen = random.choice(options)

# Printing the visual aid for the game
try:
    user_chosen = int(input("Please select a number to play: Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print(options[user_chosen])
except (IndexError, ValueError) as e:
    print("Please only enter whole number between 0, 1 or 2")
    quit()

print(f'''Computer chose:
{computer_chosen}''')

# Determining the winer of the game
if options[user_chosen] == rock and computer_chosen == scissors:
    print("You WIN")
elif options[user_chosen] == scissors and computer_chosen == paper:
    print("You WIN")
elif options[user_chosen] == paper and computer_chosen == rock:
    print("You WIN")
elif options[user_chosen] == computer_chosen:
    print("It's a TIE")
else:
    print("You LOSE")
    