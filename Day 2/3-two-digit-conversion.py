# Data Types
# Instructions: https://replit.com/@terrykirungo/3-two-digit-conversion

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# find out the data type of the input received
print(two_digit_number, " is of type ",type(two_digit_number)) # the input received from the user is a string

# Converting the string data type to intergers
first_digit = int(two_digit_number[0])
print(first_digit, "after type conversion is of type",type(first_digit))

last_digit = int(two_digit_number[1])
print(last_digit, "after type conversion is of type",type(last_digit))

# Checks if conversion was successful
# print(type(first_digit)) # successful conversion of string data type to interger
# print(type(last_digit))

# Prints the sum of the two-digit-number
sum = first_digit + last_digit
print("The sum of the two-digit-number is:", sum)

# Test it here: https://replit.com/@terrykirungo/3-two-digit-conversion#main.py
