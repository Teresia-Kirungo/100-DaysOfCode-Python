import random

# This is how you generate a random interger(whole number)
random_interger = random.randint(1, 5)
print(random_interger)

# Random float starts from 0.0 to 0.9 it never gets to 1
random_float = round(random.random() * 5) #round() rounds offto the nearest whole number.
print(random_float)
