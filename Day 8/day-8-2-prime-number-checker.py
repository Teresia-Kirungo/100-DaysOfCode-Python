# Prime Numbers
# Instructions
# Prime numbers are numbers that can only be cleanly divided by itself and 1. 

# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# Example Input 1:  73
# Example Output 1: It's a prime number.

# Example Input 2:  75
# Example Output 2: It's not a prime number.

# Hint: 
# 1. Use Python modulus: 
# 2. Make sure you name your function/parameters the same as when it's called on the last line of code. 
# 3. Use the same wording as the Example Outputs to make sure the tests pass. 

# Test Your Code
# https://replit.com/@terrykirungo/day-8-2-prime-number-checker#main.py

#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number-1):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} not a prime number.")    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
