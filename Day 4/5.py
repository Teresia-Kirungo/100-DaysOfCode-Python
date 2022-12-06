# Who's Paying - Random Person Pays Bill
# Instructions: https://replit.com/@terrykirungo/5-random-person-pays-bill

#imports the random module
import random

# Split string method; Split function, enables you to split or separate a string into a List(separate components) based on some sort of divider like a comma or a fullstop or any symbol of your choice.
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# How many items are in the list
number_of_people = len(names)

# Get's the random person by picking a random index number of a person in the list from index[0] to the last person index[-1] in the list
random_person = random.randint(0, number_of_people - 1)

# Pops ups the name of the randpm index picked
random_person_paying = names.pop(random_person)

# The above code could be simplified to be:
# random_person_paying = random.choice(names)

print(random_person_paying + " is going to buy the meal today!")

#Test it here: https://replit.com/@terrykirungo/5-random-person-pays-bill#main.py
