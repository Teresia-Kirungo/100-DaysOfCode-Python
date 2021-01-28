# Treasure Map
# Instructions
# You are going to write a program which will mark a spot with an X.

# In the starting code, you will find a variable called `map`.
# This ```map``` contains a nested list.
# When ```map``` is printed this is what the nested list looks like:

# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

# In the starting code, we have used new lines (```\n```) to format the three rows into a square, like this:

# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

# This is to try and simulate the coordinates on a real map. 

# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
# First your program must take the user input and convert it to a usable format.
# Next, you need to use it to update your nested list with an "x". 

# The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:
# Example Input 1: column 2, row 3 would be entered as: 23

# Example Output 1:

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', 'X', '⬜️']

# Example Input 2: column 3, row 1 would be entered as: 31

# Example Output 2:

# ['⬜️', '⬜️', 'X']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']


# # Hint

# 1. Remember that Lists start at index 0!
# 2. ```map``` is just a variable that contains a nested list. It's not related to the map function in Python.

# 🚨 Don't change the code below 👇
#         1    2      3   COLUMNS
row1 = ["⬜️","⬜️","⬜️"] # 1     R
row2 = ["⬜️","⬜️","⬜️"] # 2     O
row3 = ["⬜️","⬜️","⬜️"] # 3     WS
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

# rows first column last/next
# If the input given is 23 it will move 2 rows 3 columns

x_position = int(position[0]) #2 since they are still strings we'll change them to intergers -> int()
y_position = int(position[1])  #3

# On  row 2 rows and column 3 put X
map[x_position - 1][y_position - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
