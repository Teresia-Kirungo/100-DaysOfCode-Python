#Step 1 imports the random module
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

answer = input("Hey! Guess a letter in the chosen word ")
guess = answer.lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word
for letter in chosen_word:
    if letter == guess:
        print("It's a match")
    else:
        print("Try again!")
# Test it here: https://replit.com/@terrykirungo/Day-7-Hangman-1-Start#main.py
