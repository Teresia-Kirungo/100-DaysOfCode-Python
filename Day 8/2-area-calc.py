# Area Calc
# Instructions : https://replit.com/@terrykirungo/2-area-calc

# Write your code below this line
import math

# 1 can of paint can cover 5 square meters

# Define a function called paint_calc() so that the code below works.
def paint_calc(height, width, cover):
    # Area is calculated by width times height
    area = height * width
    # Math.ceil rounds up to the nearest whole number.
    number_of_cans = math.ceil(area / cover)
    # number of cans is given by the area divided by the cover(1 can of paint can cover 5 square meters)
    
    print(f"You'll need {number_of_cans} cans of paint.")

# Write your code above this line    
# 🚨 Don't change the code below
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Test Your Code: https://replit.com/@terrykirungo/2-area-calc#main.py
