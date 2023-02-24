# Supposing we have more than one condition, to check before someone uses the rollercoaster we use a Nested if/else
# Source Code looks like this: 👇

print("Welcome to the rollercoaster!")
height = float(input("What is your height in cm? ")) #use of float to accomodate both whole numbers and whole numbers with decimal points
bill = 0

if height >= 120: #height greater or equal to 120
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12: #checks the age of the rider, to determine amount payable.
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ").upper() #converts input to capital letter before its checked because the function only accepts capital letter
  if wants_photo == "Y":
    # bill = bill + 3
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

# Test it here: https://replit.com/@terrykirungo/2-roller-coaster-nested-conditions#main.py
