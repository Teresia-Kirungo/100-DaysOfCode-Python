# Rock paper scissors
# Instructions: https://replit.com/@terrykirungo/Day-4-Project-Rock-Paper-Scissors

# Importing random modules
import random

rock = ''' 
    ROCK 
'''

paper = '''
    PAPER
'''

scissors = '''
    SCISSORS
'''
print("Welcome to Rock, Paper, Scissors!")

game = [rock, paper, scissors]
game_length = len(game)

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

computer_choice = random.randint(0, 2)


# Checks if the number entered is within the list index range
if users_choice > game_length-1:
    print("Oops, you've entered an invalid number, try again!")
    
# Checks for a tie
elif users_choice == computer_choice: 
    print(f"You picked: \t{game[users_choice]} \nThe Computer picked: \t{game[computer_choice]}")
    print("It's a tie, you both get 1 point")

# Paper Beats Rock
elif users_choice  == 0 and computer_choice == 1:
    print(f"You picked: \t{game[users_choice]} \nThe Computer picked: \t{game[computer_choice]}")
    print("Paper beats Rock. Computer Wins 2 points! You 0 points.")
elif users_choice  == 1 and computer_choice == 0:
    print(f"You picked: \t{game[users_choice]} \nThe Computer picked: \t{game[computer_choice]}")
    print("Paper beats Rock. You Win 2 points! Computer 0 points.")
  
# Rock beats Scissors
elif users_choice  == 0 and computer_choice == 2:
    print(f"You picked: \t{game[users_choice]} \nThe Computer picked: \t{game[computer_choice]}")
    print("Rock beats Scissors. You Win 2 points! Computer 0 points.")
elif users_choice  == 2 and computer_choice == 0:
    print(f"You picked: \t{game[users_choice]} \nThe Computer picked: \t{game[computer_choice]}")
    print("Rock beats Scissors. Computer Wins 2 points! You 0 points.")

# Scissor beats Paper
elif users_choice  == 1 and computer_choice == 2:
    print(f"You picked: \t{game[users_choice]} \nThe Computer picked: \t{game[computer_choice]}")
    print("Scissor beats Paper. Computer Wins 2 points! You 0 points.")
elif users_choice  == 2 and computer_choice == 1:
    print(f"You picked: \t{game[users_choice]} \nThe Computer picked: \t{game[computer_choice]}")
    print("Scissor beats Paper. You Win 2 points! Computer 0 points.")
else:
    print("Error! try again")
    
# Test it here: https://replit.com/@terrykirungo/Day-4-Project-Rock-Paper-Scissors#main.py
