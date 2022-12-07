# Prime Numbers
# Instructions: https://replit.com/@terrykirungo/3-prime-number-checker

# Write your code below this line 👇

def prime_checker(number):
    # sets is_prime to a boolean of True
    is_prime = True
    
    # i represents a number in the range from 2 to the actual number being checked minus(-1) for example if we are cheking 7 the range would be 2 to 7-1 which is 6
    # number-1 represents the last number in the range
    # if the number picked divided(modulus) by the range gives a remainder then its not a prime number therefore 👇
    for i in range(2, number-1): 
        if number % i == 0:
            is_prime = False

    # if the number picked divided(modulus) by the range does not give a remainder then its a prime number.     
    if is_prime == True:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} not a prime number.")    

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

# Test it here: https://replit.com/@terrykirungo/3-prime-number-checker#main.py
