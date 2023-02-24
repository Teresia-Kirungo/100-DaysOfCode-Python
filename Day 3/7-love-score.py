# Love Calculator
# Instructions: https://replit.com/@terrykirungo/7-love-score

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \t")
name2 = input("What is their name? \t")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
both_names = name1 + name2 #concatenation

# lower() converts a string from uppercase
lower_case_names = both_names.lower()

# Checks for the number of times the letters of the word true appears
# The count() function will give you the number of times a letter occurs in a string.
t = lower_case_names.count("t") #data type int
r = lower_case_names.count("r")
u = lower_case_names.count("u")
e = lower_case_names.count("e")

true = t + r + u + e

# Checks for the number of times the letters of the word love appears
l = lower_case_names.count("l")
o = lower_case_names.count("o")
v = lower_case_names.count("v")
e = lower_case_names.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

score = int(love_score)

if (score < 10) or (score > 90):
  print(f"Your love score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

# Test it here: https://replit.com/@terrykirungo/7-love-score#main.py
