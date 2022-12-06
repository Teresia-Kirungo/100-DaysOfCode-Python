# Day 3 Main Project - Africa Treasure Island

# Imports the art of the African map
from africa_art import logo
print(logo)

print("Welcome to African Treasure Island.")
print("Your mission is to find the African hidden treasure.")

start = input("To start type 1 to head right or 2 to head left? ")
if start == "1":
    print("You are in a misile zone. Game Over!")

elif start == "2":
    print("\tAwesome! You are in River Nyando.")

    next_level = input("To swim across select 0, to wait for boat type 1!")
    if next_level == "0":
        print("You've been swallowed by the Johna fish. Game Over!")

    elif next_level == "1":
        print("\tFine day to be on a boat Pal! Bon Voyage to the house.")

        door_number = input(
            "To enter the BLUE door type 0, the RED door type 1, the YELLOW door type 2 "
        )
        if door_number == "0":
            print(
                "\tBlue Door! Sorry Pal, you are in the Lions Den. Game over!")

        elif door_number == "1":
            print(
                "\tRed Door! Trapped in the Moses' time Lapse, there's no way out. Game Over!"
            )

        elif door_number == "2":
            print(
                "\tYOU WIN! Thou good and faithful servant, Collect Your Treasure."
            )

        else:
            print("\tToo close! I bid you farewell. GAME OVER!")

    else:
        print("You appear lost mate, call Askari!")

else:
    print("Wrong choice! Game Over")