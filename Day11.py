import art
import random

# Defining functions for repeatability
def playing_cards():
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    if len(player_cards) < 2:
        player_cards.append(random.choice(cards))

def over_21(checking_cards):
    if sum(checking_cards) > 21:
        final_hands()
        print("You went over. You lose 😭")
        quit()

def final_hands():
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

def print_cards():
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

def computer_hand():
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
    over_21(computer_cards)

# Initializing variables
playing = input("Dou you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # To choose the cards from
player_cards = []
computer_cards = []

# Initializing the game
if playing == 'y':
    print(art.logo)
    playing_cards()
    print_cards()

    checking = True
    while checking:
        continue_playing = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if continue_playing == 'y':
            playing_cards()
            over_21(player_cards)
            print_cards()

        else:
            computer_hand()
            checking = False

else:
    print("What a shame...")
    print(art.goodbye)