# 🚨 Don't change the code below 👇
# split() puts the items separated by a comma(,) in a List like this 123, 145, 236, 267, 190#
# 123 145 236 267 190
 
student_heights = input("Input a list of student heights ").split()
print(student_heights)

# for a variable n in a range of 0 to the last item on the list -> student_heights
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# First assigns the total_height variable to 0
total_height = 0 
# Uses the for loop below to calculate the total sum of the student_heights
for height in student_heights:
    total_height = total_height + height
print(total_height)

# First assigns the no_of_students variable to 0
number_of_students = 0
for student in student_heights:
    number_of_students = number_of_students + student   
print(number_of_students) 

average_height = round(total_height / number_of_students)
print(average_height)



