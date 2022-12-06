states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# Out of the dirty dozens, the fruits are:
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

# Out of the dirty dozens, the veggies are are:
veggies = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Nested list of the dirty dozens
new_dirty_dozens = [fruits, veggies]

print(new_dirty_dozens)
# This what it will look like
# [['Strawberries', 'Apples', 'Grapes', 'Pears', 'Peaches'], ['Spinach', 'Kale', 'Lettuce', 'Cabbages']]


print(new_dirty_dozens[1][1])
#This goes inside new_dirty_dozens and picks veggies which is in index 1 then goes inside veggies and picks the index one item inside veggies

# Test it here: https://replit.com/@terrykirungo/4-nested-list#main.py
