# Project Tip Calculator
# Instructions: https://replit.com/@terrykirungo/Day-2-Project-Tip-Calculator

print("Welcome to Sifa tip calculator!")
bill = float(input("What is your food bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
persons = int(input("How many people to split bill? "))

# Calculations for spliting a bill of 150 between 3 people
# percentage_tip = tip% of bill
#                = 12% of 150.00 
#                = 18

# total_bill_plus_tip = bill + percentage_tip 
#            = 150 + 18 
#            = 168
# amountContributedPerPerson = total bill / persons 
#                       = 168 / 5 
#                       = 33.6 

percentage_tip = round((tip/100) * bill, 2)
total_bill_plus_tip = bill + percentage_tip
contribution_per_person = round(total_bill_plus_tip/persons, 2)

print(f"Here's a breakdown of your bill: \n\tFood bill {bill}, \n\tTip given {percentage_tip}, \n\tContribution per person {contribution_per_person}, \n\tYour total bill is therefore {total_bill_plus_tip}")

# Test it here: https://replit.com/@terrykirungo/Day-2-Project-Tip-Calculator#main.py