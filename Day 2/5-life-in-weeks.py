# Your Life in Weeks
# Instructions: https://replit.com/@terrykirungo/5-life-in-weeks

# Hint
# 1. There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# 2. Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 1 year = 12 months
# 1 year = 52 weeks
# 1 year = 365 days

# check the data type
# print(type(age)) 

# Data type conversion 
new_age = int(age)

# minimum_years = 120
minimum_years = 90
# print(type(new_age))

#years lived
months_lived = new_age * 12
weeks_lived = new_age* 52
days_lived = new_age * 365

#years left
years_left = minimum_years - new_age
weeks_left = years_left * 52
months_left = years_left * 12
days_left = years_left * 365

# Hint: How the f string works
# the f string, allows us to be able to print different data types in one print statement, example below
# print(f"your score is {score}, your height is {height}, your winning is {isWin}.")

# prints years lived
print(f"You have walked on this earth for\n\t {new_age} years, {months_lived} months, {weeks_lived} weeks and {days_lived} days.") 

# print(years_left)
display = f"If you were to live upto 120 years: \n\tyou have {years_left} years, {months_left} months, {weeks_left} weeks, and {days_left} days."
print(display)

# Test it here: https://replit.com/@terrykirungo/5-life-in-weeks#main.py