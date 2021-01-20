## BMI Calculator
# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m): weight /(height * height)

# **Warning** you should convert the result to a whole number. 

# Example Input: weight = 80, height = 1.75
#   80 ÷ (1.75 x 1.75) =  26.122448979591837
# Example Output: 26

# Hint

# 1. Check the data type of the inputs.
# 2. Try to use the exponent operator in your code.
# 3. Remember PEMDAS.
# 4. Remember to convert your result to a whole number (int). 

# SOURCE CODE 👇

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(type(height)) #checks the data type of the height which is a str
print(type(weight)) #checks the data type of the weight which is a str

# Conversion of the data types to intergers
new_height = float(height)
new_weight = int(weight)

# Confirms if the data type conversion was successful
print(type(new_height))
print(type(new_weight))

# Calculation of the bmi, the int() function converts the float to an interger(a whole number without a decimal)
bmi = int(new_weight / (new_height * new_height))
# bmi = int(new_weight / (new_height ** 2)) is another formula, **2 means raised to the power of two
print(bmi)

