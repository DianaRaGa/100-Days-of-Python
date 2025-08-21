import math
import random
import re

#Setting the lives for the game
lives = 6

#Importing the list and choosing the word from that list
from Modules.D7_hangman_words import word_list
chosen_word = random.choice(word_list)
#print(chosen_word)

#Importing the artwork and the list for the stages of the hangman
from Modules.D7_hangman_art import stages, logo
print(f"Welcome to the Game\n{logo}\nThis is the word you will be guessing")

#Crating the placeholder to not show the chosen word
placeholder = "_" * len(chosen_word)
print(placeholder)

#Inciating the while loop and the new variable display that is the placeholder as a start
display = placeholder
used_letters = []
while display != chosen_word:
    guess = input("Guess a letter: ").lower()
    #Making sure the user only inputs one character
    if len(guess) != 1 or not guess.isalpha(): #This makes sure is only one character and is in the alphabet
        print("***************WARNING: Please enter a single letter only.***************")
        continue
    count = 0 #Variable to be able to modify the display list with correct answers
    display_list = list(display) #Changing the variable to a list for easier handling
    correct = False #Variable to check for the win/lose aspect and to print the artwork corresponding

    #If loop to see if the chosen word was already being used
    if guess in used_letters:
        print(f"******WARNING:You already used the letter {guess}. Please try another one******")
        continue
    else:
        used_letters.append(guess)

   #For loop to go trough each letter in the chosen word and determine if it is in the word and in witch position with the count variable
    for letter in chosen_word:
        if letter == guess:
            display_list[count] = guess
            count += 1
            correct = True
        else:
            count += 1
    display = "".join(display_list) #This makes the list back to a string to handle it again for the while loop to be able to close
    print(display)

    #If check to print the hangman artwork corresponding and managing the lives accordingly
    if correct: #If there was a correct guess from the user
        print(f"*************NOTICE: The letter you chose {guess} was IN the word.*************")
        print(f"********************Your Remaining Lives is:    {lives}    ********************")
        print(stages[lives])
    else:
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print("**************************You Have no Lives Left***************************")
            msg = f"The word was:     {chosen_word}     "
            print(msg.center(75, "*")) #Helful to make the print statements to be centered and with equal characters to each side to make the code clean
            print("***************************GAME OVER: You Lose.****************************")
            exit()
        print(f"***********NOTICE: The letter you chose {guess} was NOT IN the word.***********")
        print(f"********************Your Remaining Lives is:    {lives}    ********************")
        print(stages[lives])

print("***************************GAME OVER: You Win.****************************")