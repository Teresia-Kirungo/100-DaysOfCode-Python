# Leap Year
# Instructions
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:
# This is how you work out whether if a particular year is a leap year. 

# 1. on every year that is evenly divisible by 4
# 2. **except** every year that is evenly divisible by 100
# 3. **unless** the year is also evenly divisible by 400

# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.

# But the year 2100 is not a leap year because:
# 2100 ÷  4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)

# WARNING your output should match the Example Output format exactly, even the positions of the commas and full stops. 

# Example Input 1: 2400
# Example Output 1: Leap year.

# Example Input 2: 1989
# Example Output 2: Not leap year.

# Hint

# 1. Try to visualise the rules by creating a flow chart on www.draw.io
# 2. If you really get stuck, you can see the flow chart I created: 

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
  
