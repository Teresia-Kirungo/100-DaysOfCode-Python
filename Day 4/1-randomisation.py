#imports the random module
import random
import my_module

# This is how you generate a random interger(whole number) that is within the range of 1 to 5
random_interger = random.randint(1, 5)
print(f"{random_interger} is a random_interger generated from a range of 1 to 5.") #

# Random float starts from 0.0 to 0.9 it never gets to 1
random_float = random.random()
print(f"\n{random_float} is a random_float generated from a range of 0.0 to 0.9, it never gets to 1.\n")

random_float_multiplied = round(random.random() * 5) #round() rounds off to the nearest whole number.
print(f"{random_float_multiplied} is a random_float_multiplied generated from a range of 0.0 to 0.9, but multipled by 5 and rounded off.\n")

#1. Let's create a module for pi and call it here
#2. we've created our module and called it my_module.py
#3. To use it we have imported it at the top
#4. Let's use it; let's print the value of pi
print(f"This is the value of pie imported from the local module I created and imported {my_module.pi}.")

#Test it here: https://replit.com/@terrykirungo/1-randomisation
