# Your Life in Weeks
# Instructions
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if a person lives until 120 years old. 
# It will take the current age of the user as the input and output a message with their time left in this format:
# You have x days, y weeks, and z months left. 
# Where x, y and z are replaced with the actual calculated numbers. 
# Example Input: 56
# Example Output: You have 12410 days, 1768 weeks, and 408 months left.

# Hint

# 1. There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# 2. Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.

# Source Code

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 1 year = 12 months
# 1 year = 52 weeks
# 1 year = 365 days

# check the data type
print(type(age)) 

# Data type conversion 
new_age = int(age)

# minimum_years = 120
# print(type(new_age))
years_left = 120 - new_age
weeks_left = years_left * 52
months_left = years_left * 12
days_left = years_left * 365

years_lived = new_age
months_lived = years_lived * 12
weeks_lived = years_lived * 52
days_lived = years_lived * 365

# Hint: How the f string works
# the f string, allows us to be able to print different data types in one print statement, example below
# score = 0 # interger data type
# height = 1.8 # float data type
# isWin = True #Boolean
# print(f"your score is {score}, your height is {height}, your winning is {isWin}.")

# prints years lived
lived = f"Thou good and faithful servant: \n\tYou have walked on this earth for {years_lived} years, {months_lived} months, {weeks_lived} weeks and {days_lived} days"
print(lived)

# print(years_left)
display = f"\tTime left {years_left} years, {days_left} days, {weeks_left} weeks, and {months_left} months."
print(display)
print("Keep up with the good work!")
