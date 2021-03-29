# Average Height
# Instructions
# You are going to write a program that calculates the average student height from a List of heights. 
# e.g. `student_heights = [180, 124, 165, 173, 189, 169, 146]`

# The average height can be calculated by adding all the heights together and dividing by the total number of heights. 
# e.g. 180 + 124 + 165 + 173 + 189 + 169 + 146 = **1146**

# There are a total of **7** heights in `student_heights`
# 1146 ÷ 7 = **163.71428571428572**

# Average height rounded to the nearest whole number = **164**
# **Important** You should not use the `sum()` or `len()` functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Example Input  156 178 165 171 187
# Example Output 171

# Hint
# 1. Remember to use the `round()` function to round the average height before you print it.
# Test Your Code

# Solution

# https://replit.com/@terrykirungo/day-5-1-average-height

# Don't change the code below
# split() puts the items separated by a comma(,) in a List like this 123, 145, 236, 267, 190
# 123 145 236 267 190
 
student_heights = input("Input a list of student heights ").split()
print(student_heights)

# for a variable n in a range of 0 to the last item on the list -> student_heights
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Don't change the code above 

# Write your code below this row 👇

# First assigns the total_height variable to 0
total_height = 0 
# Uses the for loop below to calculate the total sum of the student_heights
for height in student_heights:
    total_height = total_height + height # the first one it will execute 0 which is what we have assigned to the total height + the first item(height number) in the list provided, it will run this line of code until the last item on the list
print(f"The total sum of the students height is {total_height}") # prints total height calculated!

# First assigns the no_of_students variable to 0
number_of_students = 0
for student in student_heights:
  number_of_students += 1 #Does number_of_students + 1 everytime it counts student(item) in student_heights
print(f"The number of students is participating is {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"The average height is {average_height}")
