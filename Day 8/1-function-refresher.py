# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
    print("Hi, My name is Terry.")
    print("I am a Python developer.")
    print("\n")

greet()

# function(Parameter) with Parameters
# The parameter is the name of the data,used inside a function to refer to the argument 
# It's is like a variable but for a function e.g 
def greet_with_name(name):
    print(f"{name}, Isn't the weather lovely today?")
    print("\n")

# function(Argument) Argument - Actual piece of data passed into a function when it's callled -like a value in a variable-
greet_with_name("Kelly")

#Function takes two parameters 
def greet_with(name, location):
    print(f"Hello {name}, What's you favorite drink in {location}?")
    print("\n")

#Without specifying the keywords the function will just pick the arguments as they follow each other from left to right

greet_with("London","Marie") #check how this is printed, it should be the other way now to avoid this error this is how we do it 

#Calling the function with keyword arguments
greet_with(name = "Marie", location = "London")

#Test it here: https://replit.com/@terrykirungo/1-function-refresher#main.py
