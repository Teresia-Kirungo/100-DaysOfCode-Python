# Music Band Name Generator
# Instructions : 👇
# Write a program that welcomes the user to the  Music Band Name Generator. 
# The Name Generator prompts a user for the name of the City they grew up in and the name of their pet. 
# The Name Generator then combines these two names to give the user their Band Name.

# Source Code

#1. Creates a greeting that welcomes the user to the Band Name Generator.
print("Welcome to the Music Band Name Generator.")

#2. Ask the user for the name of the city that they grew up in.
city = input("What's the name of the city you grew up in?\n")

#3. Ask the user for the name of their pet.
pet_name = input("What's the name of your pet?\n")

#4. Combines the name of their city and pet and show them their band name.
print("Your band name is " + pet_name + " " + city)

# This can also be written like this because of using f-string
print(f"Your generated Music band-Name is {city} {pet_name} ")

#5. Make sure the input cursor shows on a new line
# \n means new line, the input given is printed on a new line

# Test it here: 👇
# https://replit.com/@terrykirungo/Music-band-name-generator-start#main.py
