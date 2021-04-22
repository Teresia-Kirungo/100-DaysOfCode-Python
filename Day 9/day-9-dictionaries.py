# Dictionaries in python allow us to group items together in the text beneath
# "Bug" is the key and the text "An error..." is the value
# "Function" is the key and the text "A piece of code.." is the value

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
    }

# Retrieving items from a Dictionary
# To print something from a dictionary we reference it's key like this
print(programming_dictionary["Bug"]) #this will print the value of the key "Bug"

# Adding new items to the dictionary
programming_dictionary["Terry"] = "You are going to be a kick-ass woman in Tech."

# To print the entire dictionary
print(programming_dictionary)
