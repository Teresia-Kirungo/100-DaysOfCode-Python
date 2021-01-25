# Project Tip Calculator
# Instructions
# Write a program that builts Tip-Calculator. 
# The Tip-Calculator should welcome the user.
# The Tip-Calculator should prompt the user for:
# 1) the total bill to be paid,
# 2) the number of people the bill is to be split amongst.
# 3) show the user the percentage range and ask them what percentage tip they would like to give 
# The Tip-Calculator should show the user the amount of money each person should contribute.

# Source Code
# Hints:
# 1. round() -> print(round(8/3)) rounds off numbers to the nearest whole number, in this case this will be 3
#            -> print(round(8/3,2)) rounds off a number to a given precision in decimal digits in this case to 2 decimal places so the output will be 2.67
#            -> print(round(2.66666667,2)) will give an output of 2.67
# 2. Floor division // -> print(8 // 3) drops off any number after the decimal point the output will be 2

# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to the Tip Calculator.")
bill = float(input("What is the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
persons = int(input("How many people to split bill? "))

# Calculations for spliting the bill
# percentage_tip = tip% of bill
#                = 12% of 150.00 
#                = 18
# total_bill = bill + percentage_tip 
#            = 150 + 18 
#            = 168
# persons_to_split_bill = total bill / persons 
#                       = 168 / 5 
#                       = 33.6 
percentage_tip = (tip/100) * bill
total_bill = bill + percentage_tip
tip_given = round(total_bill / persons, 2) # rounds off the number to 2 decimal places

print(f"Here's how much tip to give: Kes {tip_given}")
