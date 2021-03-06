# Adding Evens
# Instructions

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100: i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

# Hint
# 1. There are quite a few ways of solving this problem, but you will need to use the `range()` function in any of the solutions.

# Solution
# Test it here: https://replit.com/@terrykirungo/day-5-3-adding-even-numbers

# Write your code below this row 👇
total_sum = 0
for even in range(1, 101):
    if even % 2 == 0:
        total_sum += even
       #print(total_sum)  if i print it on this indentation, it will execute inside this loop so it will give me all number addition in this loop
print(total_sum) # If i have it here i'll have the final result only which is what we want!
