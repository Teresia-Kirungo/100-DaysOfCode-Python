# BMI 2 
# Instructions: https://replit.com/@terrykirungo/2-bmi-2

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

bmi = round(weight/(height ** 2)) #height to the power of 2
print(bmi)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25.0:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30.0:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35.0:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

#Test it here: https://replit.com/@terrykirungo/2-bmi-2#main.py
