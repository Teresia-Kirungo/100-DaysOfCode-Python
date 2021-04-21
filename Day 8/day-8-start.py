# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
    print("Hi")
    print("My name is Terry.")
    print("I am a flutter developer.")
    print("\n")

greet()

# function(Parameter) Parameter- is the name of that data, it is used inside a function to refer to the argument -this is like a variable-
def greet_with_name(name):
    print(f"Hello {name}")
    print("Isn't the weather lovely today?")
    print("\n")

# function(Argument) Argument - Actual piece over data passed into a function when it's callled -like a value in a variable-
greet_with_name("Kelly")

#Function takes two parameters 
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How's the weather like in {location}?")

greet_with("Terry","London")