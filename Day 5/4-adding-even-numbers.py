# Adding Evens
# Instructions: https://replit.com/@terrykirungo/4-adding-even-numbers#main.py

# Write your code below this row 👇

# Step 1 way of tackling 

# set the total sum to 0
total_even_sum = 0

#Set  a range of 1 to 101
for even in range(1, 101):
    #check if the number in the range is an even
    if even % 2 == 0:
        #Add's to total sum
        total_even_sum += even
       #print(total_sum)  if i print it on this indentation, it will execute inside this loop so it will give me all number addition in this loop

# Indentation! If i have it here i'll have the final result only which is what we want!      
print(f"{total_even_sum} is the total sum of all even numbers between 1 and 101, using step 1") 

# Step 2 way of tackling 
even_numbers = 0
# In the for loop we provide a range of numbers the range(start(2), stop(101), step(2)) basically we are telling the loop to start count at 2 then go upto 101 exclude it but move from one number to another is steps of 2
for number in range(2, 101, 2):
    #Add the numbers in the range
    even_numbers += number

print(f"\n{even_numbers} is the total number of even numbers between 1 to 100, using the range(start, stop, step) method.") 

# Sum of all odd numbers
total_odd = 0
for odd in range(1, 101):
    if odd % 2 != 0:
        total_odd += odd

print(f"\n{total_odd} is the total_sum of all the odd numbers between 0 to 101.") # If i have it here i'll have the final result only which is what we want!

# Test it here: https://replit.com/@terrykirungo/4-adding-even-numbers
