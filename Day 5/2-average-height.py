# Average Height
# Instructions: https://replit.com/@terrykirungo/2-average-height
 
# 🚨 Don't change the code below 👇
# split() puts the items separated by a comma(,) in a List like this 123, 145, 236, 267, 190
# 123 145 236 267 190
 
student_heights = input("Input a list of student heights ").split()

# for a variable n in a range of 0 to the last item on the list -> student_heights
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# First assigns the total_height variable to 0
total_height = 0 
# Uses the for loop below to calculate the total sum of the student_heights

for height in student_heights:
    #The first time this 👇 line runs the total height will equate to 0  -which is what we have initialised the total height to- . The next time it loops the total height will be added to the first item in the list provided. It will run this line of code(LOOP) until the last item on the list.
    # total_height = total_height + height
    total_height += height 
print(f"The total sum of the students height is {total_height}") # prints total height calculated!

# First creates and initializes the no_of_students variable to 0
number_of_students = 0
for student in student_heights:
    #Does number_of_students + 1 everytime it counts student(item) in student_heights
    number_of_students += 1 
print(f"The number of students participating is {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"The average height is {average_height}")

# Test it here: https://replit.com/@terrykirungo/2-average-height#main.py
