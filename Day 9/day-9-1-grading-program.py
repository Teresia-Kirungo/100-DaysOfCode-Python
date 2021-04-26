# Grading Program
# Instructions
# You have access to a database of `student_scores` in the format of a dictionary. 
# The *keys* in `student_scores` are the *names* of the students and the *values* are their exam *scores*. 

# Write a program that *converts their scores to grades*. 
# By the end of your program, you should have a new dictionary called `student_grades` that should contain student *names* for *keys* and their *grades* for *values*. 
# The final version of the `student_grades` dictionary will be checked. 

# **DO NOT** modify lines 1-7 to change the existing `student_scores` dictionary. 
# **DO NOT** write any print statements.
# This is the scoring criteria:

# > Scores 91 - 100: Grade = "Outstanding"
# > Scores 81 - 90: Grade = "Exceeds Expectations"
# > Scores 71 - 80: Grade = "Acceptable"
# > Scores 70 or lower: Grade = "Fail"

# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'

# Hint
# 1. Remember that looping through a Dictionary will only give you the **keys** and not the values. 
# 2. If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values. 
# 3. At the **end** of your program, the print statement will show the final `student_scores` dictionary, do not change this.

# Test Your Code
# https://replit.com/@terrykirungo/day-9-1-exercise#main.py


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for score in student_scores:
# A for loop that loops through the keys in the student_scores
    grade = student_scores[score]
    # the new variable grade is initialised to the 'value' of the 'keys' in student_scores
    # In the if statement we compare the 'value' of the key which represents the grade to the scoring grades set, to see which category they fall under. 
    if grade > 90 :
        student_grades[score]= "Outstanding"
    elif grade > 80:
        student_grades[score]= "Exceeds Expectations"
    elif grade > 70:
        student_grades[score]= "Acceptable"
    else:
        student_grades[score]= "Fail"    

# 🚨 Don't change the code below 👇
print(student_grades)
