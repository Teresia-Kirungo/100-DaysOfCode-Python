# Rock paper scissors
# There are only two outcomes to this game a draw, or a win.

# The rules of the game
# 1. Rock beats Scissors
# 2. Paper beats Rock
# 3. Scissor beats Paper

#  If both players choose the same shape, the game is tied and is usually immediately replayed to break the tie. 
#   If you win you get 2 points, 
#     A draw gives you 1 point, 
#       If you lose 0 points.
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

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(f"Your choice is: \t{game[users_choice]}")

computer_choice = random.randint(0, 2)
print(f"Computer choice is: \t{game[computer_choice]}")

# draw
if users_choice == computer_choice:
    print("Its a draw, you both get 1 point")

# Paper Beats Rock
elif users_choice  == 0 and computer_choice == 1:
    print("Paper beats Rock. Computer Wins 2 points! You 0 points.")
elif users_choice  == 1 and computer_choice == 0:
    print("Paper beats Rock. You Win 2 points! Computer 0 points.")
  
# Rock beats Scissors
elif users_choice  == 0 and computer_choice == 2:
    print("Rock beats Scissors. You Win 2 points! Computer 0 points.")
elif users_choice  == 2 and computer_choice == 0:
    print("Rock beats Scissors. Computer Wins 2 points! You 0 points.")

# Scissor beats Paper
elif users_choice  == 1 and computer_choice == 2:
    print("Scissor beats Paper. Computer Wins 2 points! You 0 points.")
elif users_choice  == 2 and computer_choice == 1:
    print("Scissor beats Paper. You Win 2 points! Computer 0 points.")

elif users_choice  >= 3 or users_choice <0:
    print("Invalid input try again!")

