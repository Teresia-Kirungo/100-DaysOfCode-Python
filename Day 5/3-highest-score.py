# Highest Score
# Instructions: https://replit.com/@terrykirungo/3-highest-score

#🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(f"Here's a list of the student_scores: {student_scores}")
#🚨 Don't change the code above 👆

#Write your code below this row 👇

#initialize highest_score
highest_score = 0 

#Combining two functions a for loop and an if
for score in student_scores:
    #if the item(score) we land upon is higher than the value we've set for highest score for example in the first bit when the code runs it will perform 0 > 78, then it will assign highest score to 78, then run again(loop) and perform 78 > 65, this will continue until it reaches 91
    if score > highest_score: 
        highest_score = score
print(f"\tThe highest score in the class is: {highest_score}")

# Test it here: https://replit.com/@terrykirungo/3-highest-score#main.py
