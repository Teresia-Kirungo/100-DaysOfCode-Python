# Use of for loop in calculating love score

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Converts names to UPPERCASE
new_name1 = name1.upper()
new_name2 = name2.upper()

#concatenates the two names to form one name
both_names = new_name1 + new_name2

#Initializes the counts of the number of times the letters of the word TRUE appear in the combined(Concatenated name)
true_count = 0

##Initializes the counts of the number of times the letters of the word LOVE appear in the combined(Concatenated name)
love_count = 0

#Loops through the combined name checking how many times the letters of the word TRUE appears. Everytime it appears true_count is increased by 1
for letter in both_names:
    if letter == "T":
        true_count = true_count + 1
    elif letter == "R":
        true_count = true_count + 1
    elif letter == "U":
        true_count = true_count + 1
    elif letter == "E":
        true_count = true_count + 1
#prints the total number of times the letters of TRUE appear in the combined name
print(true_count)

#Loops through the combined name checking how many times the letters of the word LOVE appears. Everytime it appears love_count is increased by 1
for character in both_names:
    if character == "L":
        love_count = love_count + 1
    elif character == "O":
        love_count = love_count + 1
    elif character == "V":
        love_count = love_count + 1
    elif character == "E":
        love_count = love_count + 1
print(love_count)

#Concatenates the love_score through conversion to str, e.g 5 and 8 become 58
love_score = str(true_count) + str(love_count)

#Converts the total love score to int
total_score = int(love_score)

#Checks the compatibility of the two people through their name
if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score > 40 and total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
    
# Test it here: https://replit.com/@terrykirungo/5-1-love-score-using-loop#main.py 