# Variables
# Instructions
# Write a program that switches the values stored in the variables a and b. 
# **Warning.** Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g. any value of a and b.

# Example Input: 
#   a: 3
#   b: 5

# Example Output
#   a: 5
#   b: 3

# # Hint

# 1. You should not have to type any numbers in your code. 
# 2. You might need to make some more variables.


# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a # creates a new variable c that holds the value of a
a = b # asigns a to be the value of b
b = c # asigns b to be the value of what a was which is now held in c



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
