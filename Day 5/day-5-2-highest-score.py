# Highest Score
# Instructions
# You are going to write a program that calculates the highest score from a List of scores. 
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# **Important** 
# You are not allowed to use the max or min functions. 
# The output words must match this example:`The highest score in the class is: x`

# Example Input:  78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: `[78, 65, 89, 86, 55, 91, 64, 89]`
# Example Output:  The highest score in the class is: 91

# Hint

# 1. Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(f"Here's a list of the student_scores: {student_scores}")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0 #initialize highest_score

for score in student_scores:
    if score > highest_score: #if the item(score) we land upon is higher than the value we've set for highest score for example in the first bit when the code runs it will perform 0 > 78, then it will assign highest score to 78, then run again(loop) and perform 78 > 65, this will continue until it reaches 91
        highest_score = score
print(f"\tThe highest score in the class is: {highest_score}")

# Solution
# Test it here: https://replit.com/@terrykirungo/day-5-2-highest-score



