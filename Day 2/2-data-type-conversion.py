#Data Type Conversion

num_char = len(input("What is your name? "))

print(type(num_char)) # num_char is an int data type because of the len function.

new_num_char = str(num_char) #converts num_char to a string

print(f"Your name has " + new_num_char + " characters.")

#Test it here: https://replit.com/@terrykirungo/2-data-type-conversion#main.py