# Who's Paying
# Instructions
# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill. 
# **Important**: You are not allowed to use the `choice()` function.
# **Line 20** splits the string `names_string` into individual names and puts them inside a **List** called `names`. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name
# Example Input: Angela, Ben, Jenny, Michael, Chloe

# Note: notice that there is a space between the comma and the next name. 

# Example Output: Michael is going to buy the meal today!

# Hint
# 1. You might need the help of the `len()` function.   
# 2. Remember that Lists start at index 0!

import random

# Split string method
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




