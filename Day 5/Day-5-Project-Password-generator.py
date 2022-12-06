# Password Generator Project
# Instructions
# Create a program that uses: letters, symbols(special characters) and numbers to generate a password.

import random # imports the random module

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] # list of letters or char

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #list of whole numbers

symbols = ['!','<','>', '~' ,'#', '{', '}','$', '%', '&', '(', ')', '*', '+', '?'] #list of special characters

print("Welcome to the Terri-PyPassword Generator!")
no_of_letters = int(input("How many letters would you like in your password?\n")) 
no_of_symbols = int(input("How many symbols would you like?\n"))
no_of_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for letter in range(1, no_of_letters+1):
    random_letter = random.choice(letters)
    password = password + random_letter
    
for number in range(1, no_of_numbers +1):
    random_number = random.choice(numbers)
    password = password + random_number

for symbol in range(1, no_of_symbols +1):
    random_symbol = random.choice(symbols)
    password = password + random_symbol
    
print(f"Your easy level password is {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for letter in range(1, no_of_letters+1):
    password_list += random.choice(letters)  
    
for number in range(1, no_of_numbers +1):
    password_list += random.choice(numbers)

for symbol in range(1, no_of_symbols +1):
    password_list += random.choice(symbols) 

# This is how we change the order of items in a list, we can use a for loop or the random.shuffle() function 
random.shuffle(password_list)

new_password =""
for char in password_list:
    new_password += char

print(f"Your complex password is {new_password}")

# Test it here: https://replit.com/@terrykirungo/Day-5-Project-Password-generator#main.py
