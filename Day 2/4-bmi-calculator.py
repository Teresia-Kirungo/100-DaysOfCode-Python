# BMI Calculator
# Instructions: https://replit.com/@terrykirungo/day-2-4-bmi-calculator

# 🚨 Don't change the code below 👇
height = input("Enter your height in Meters(m): ")
weight = input("Enter your weight in Kilograms(kg): ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
print(height, "which is height is a", type(height)) #checks the data type of the height which is a str
print(weight, "which is the weight is a", type(weight)) #checks the data type of the weight which is a str

# Conversion of the data types to intergers
# 👇opted to use the float data types incase a user uses a whole number or one with a decimal point 👇
new_height = float(height) 
new_weight = float(weight)

# Confirms if the data type conversion was successful
print("Height data type conversion to",type(new_height))
print("Weight data type conversion to",type(new_weight))

# Calculation of the bmi, the int() function converts the float to an interger(a whole number without a decimal)
bmi = int(new_weight / (new_height * new_height))
# bmi = int(new_weight / (new_height ** 2)) is another formula, **2 means raised to the power of two
print(f"Your BMI is {bmi}.")

#Test it here: https://replit.com/@terrykirungo/day-2-4-bmi-calculator#main.py
