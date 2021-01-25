# Data Types
# Instructions
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Example Input: 39
# Example Output: 3 + 9 = 12

# Hint
# 1. Try to find out the data type of two_digit_number.
# 2. Think about what you learnt about subscripting.
# 3. Think about type conversion.

# Source Code

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# find out the data type of the input received
print(type(two_digit_number)) # the input received from the user will be a string

# Converting the string data type to intergers
first_digit = int(two_digit_number[0])
last_digit = int(two_digit_number[1])

# Find the data type, checks if conversion was successful
print(type(first_digit)) # successful conversion of string data type to interger
print(type(last_digit))

# Prints the sum of the two-digit-number
print("The sum of the two-digit-number is: ")
sum = first_digit + last_digit
print(sum)
