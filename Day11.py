import art
import random

# Defining functions for repeatability
def choosing_random_card():
    random_card = random.choice(cards)
    return random_card

# Initializing variables
playing = input("Dou you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # To choose the cards from
player_cards = []
computer_cards = []

if playing == 'y':
    print(art.logo)

    #Making the player have 2 initial cards
    player_cards.append(choosing_random_card())
    player_cards.append(choosing_random_card())

    # Giving the computer a card as well
    computer_cards.append(choosing_random_card())

    # Printing the scores and cards for the player and computer for the user
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    continue_playing = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if continue_playing == 'y':
        player_cards.append(choosing_random_card())

else:
    print("What a shame...")
    print(art.goodbye)