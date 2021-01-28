#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

# randomly picks a whole number(interger) between 0 and 1
random_side = random.randint(0, 1)

if random_side == 1:
  print("Heads")
else:
  print("Tails")
