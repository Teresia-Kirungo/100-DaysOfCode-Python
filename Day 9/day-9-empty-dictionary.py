programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
    }

# Retrieving items from a Dictionary
print(programming_dictionary["Bug"]) 

# Adding new items to the dictionary
programming_dictionary["Terry"] = "You are going to be a kick-ass woman in Tech."

# Printing the entire dictionary
print(programming_dictionary)

# Wipiing an existing dictionary
# programming_dictionary = {}

# Creating a new empty dictionary
empty_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "Chew bugs for breakfast that's what he told me!"

# Loop through a dictionary using a for loop will only give you the key, watch!
for item in programming_dictionary:
    print(item) #this prints the keys in the dictionary

# If i wanted to print the key and the value in the entire dictionary, i would do this
for key in programming_dictionary:
    print(key) # prints key
    print(programming_dictionary[key]) # prints value
    
# Test it here    
# https://replit.com/@terrykirungo/day-9-empty-dictionary#main.py
