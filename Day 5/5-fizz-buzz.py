# FizzBuzz
# Instructions: https://replit.com/@terrykirungo/5-fizz-buzz

#Write your code below this row 👇

for number in range(1,101): #prints from 1 to 100
    #have it at the top so that it proceeds with the execution
    #checks divisibility by 3 and 5
    if number % 3 == 0 and number % 5 == 0: 
        number = "FizzBuzz"
        
    #checks divisibility by 3
    elif number % 3 == 0:
        number = "Fizz"

    #checks divisibility by 3 and 5
    elif number % 5 == 0:
        number = "Buzz"
    print(number)
    
# If we have this if number % 3 == 0 and number % 5 == 0: at the bottom the program willl execute to completion before it reaches this block of code rememeber the rock paper scissor game!

# Test it here: https://replit.com/@terrykirungo/5-fizz-buzz#main.py
