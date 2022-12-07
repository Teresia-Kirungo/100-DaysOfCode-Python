#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# introduce an endgame varible and set it to false to let the game loop through
endgame = False

#use of while loop in negation
while not endgame:
    guess = input("Guess a letter: ").lower()

    #Check the position of the guessed letter
    for position in range(word_length):
        # creates a new variable called letter and initializes it to the current position of the chosen word
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
#Checks for blank spaces in the display, if there are none the user has won the game
#Read more about for in here: https://developers.google.com/edu/python/lists
if "_" not in display:
    endgame = True
    print("You win.")
    
#Test it here: https://replit.com/@terrykirungo/3-hangman#main.py