# Treasure Map
# Instructions: https://replit.com/@terrykirungo/6-treasure-map

# 🚨 Don't change the code below 👇
# ----------> ROWS ------->
row1 = ["⬜️","️⬜️","️⬜️"] # 1
row2 = ["⬜️","⬜️","️⬜️"] # 2
row3 = ["⬜️️","⬜️️","⬜️️"] # 3 COLUMNS
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# rows first column last/next
# If the input given is 23 it will move 2 rows 3 columns

#Of the numbers given by the user for the horizontal position we will pick the number that is at index 0 of that number e.g if the number given is 23, position[0] will be index 0 of 23 which is 2
horizontal = int(position[0]) #2 since they are still strings we'll change them to intergers -> int()

#Of the numbers given by the user for the vertical position we will pick the number that is at index 0 of that number e.g if the number given is 23, position[1] will be index 1 of  23 which is 3
vertical = int(position[1])  #3

# On  row 2 rows and column 3 put X
map[vertical - 1][horizontal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# Test it here: https://replit.com/@terrykirungo/6-treasure-map#main.py
