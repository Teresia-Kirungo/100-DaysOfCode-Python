# Inputs
# Instructions: https://replit.com/@terrykirungo/4-inputs-function

#Write your code below this line 
name = input("Hello, what is your name? ")

#len() function counts the number of characters in a string
characterNumber = len(name)
# characterNumber is a variable - temporariy holds a value 

print(f"Hi {name}, your name is {characterNumber} characters long.") 
# f-strings are a great new way to format strings. Not only are they more readable, more concise, and less prone to error than other ways of formatting, but they are also faster! On the line above f-string enables us to use both strings and numbers in one line using the curly braces {}

# This program can also be written like this: 👇
print(len(input("What is your other name? "))) 

# Test it here: 👇
# https://replit.com/@terrykirungo/4-inputs-function#main.py