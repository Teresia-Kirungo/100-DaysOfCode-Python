import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# How many items are in the list
how_many_people = len(names)

random_person = random.randint(0,how_many_people - 1)

random_person_paying = names.pop(random_person)

# The above code could be simplified to be:
# random_person_paying = random.choice(names)

print(random_person_paying + " is going to buy the meal today!")




