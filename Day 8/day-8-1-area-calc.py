# Area Calc
# Instructions
# You are painting a wall. The instructions on the paint can says that **1 can of paint can cover 5 square meters** of wall. 
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can. 
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 ✖️ 4) ÷ 5 
#                          = 1.6
# But because you can't buy 0.6 of a can of paint, the **result should be rounded up** to **2** cans. 
# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

# Hint
# **1. To round up a number**: use math.ceil()

# Test Your Code
# https://replit.com/@terrykirungo/day-8-1-area-calc#main.py

# Write your code below this line 
import math

def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    print(f"You'll need {number_of_cans} cans of paint.")

# Write your code above this line 
# Define a function called paint_calc() so that the code below works.   

# Don't change the code below
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


