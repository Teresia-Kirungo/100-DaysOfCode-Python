# Python sPizza Order
# Instructions: https://replit.com/@terrykirungo/6-pizza-program


# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# To make sure all inputs are capitalized we will use the upper() function that transforms all lower case to uppercase
size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()

bill = 0

# Checks first for the size
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25
else:
  print("Try again, check what you have typed")

# Checks for pepperoni
if add_pepperoni == "Y":
  if size == "S":
      bill += 2
  else:
      bill += 3

# Checks for Cheese
if extra_cheese== "Y":
    bill += 1

print(f"Your final bill is: ${bill}")

# Test it here: https://replit.com/@terrykirungo/6-pizza-program#main.py