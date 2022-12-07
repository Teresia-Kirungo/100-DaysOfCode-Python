#Step 1 imports the random module
import random

word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guessed_letter = input("Guess a letter in the random word: ")
guess = guessed_letter.lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word
for letter in chosen_word:
    if letter == guess:
        print("Right!")
    else:
        print("Wrong!")
        
#Test it here: https://replit.com/@terrykirungo/1-hangman#main.py
