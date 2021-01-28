state1 = "Alabama"
state2 = "Arizona"
state3 = "Arkansas"

# Instead of creating different variable state like we did above, we could put all these in a python list like this

states_of_america = ["Alabama","Arizona","Arkansas","California", "Colorado", "Connecticut", "Delaware"]
print(states_of_america[0]) # Prints the first element in the list
print(states_of_america[-1]) # Prints the last element in the list

# Changes the string at index[-1] of the List
states_of_america[-1] = "Delamere" 


# Add an item "Terryland" to the end of the list at index[-1]
states_of_america.append("Terryland") 


# Extend the list by appending all the items given e.g
states_of_america.extend(["Maryland", "MariaAntonett"])


# Insert an item "Merryland" at a given index 0 position.
states_of_america.insert(0,"Merryland")

print(states_of_america)


# Arrays in JavaScript are what Lists are in Python
# Arr =[Item1, Item2, Item3] in JS
# List = [Item1, Item2, Item3] in Python
