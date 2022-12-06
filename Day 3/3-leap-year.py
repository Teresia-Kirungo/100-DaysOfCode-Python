# Leap Year Challenge
# Instructions: https://replit.com/@terrykirungo/3-leap-year

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
  # print("Could be!")
  if year % 100 == 0:
    # print("Still could be a leap year")
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# Test it here: https://replit.com/@terrykirungo/3-leap-Year#README.md