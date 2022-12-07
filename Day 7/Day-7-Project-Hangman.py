#Step 5

#imports the random module to be used to pick a random word
import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list

#choses a random word from the random list
chosen_word = random.choice(word_list)

#Checks the length of the chosen word
word_length = len(chosen_word)

#sets endgame variable to false to allow "looping through"
endgame = False

#Sets the number of lives the hangman has
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#Loops while endgame is not true; let the games continue
while not endgame:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        #Checks is the number of lives is set to 0
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])
    
    # Test it here: https://replit.com/@terrykirungo/Day-7-Hangman-Project#main.py
