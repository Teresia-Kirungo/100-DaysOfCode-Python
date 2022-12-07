#Caesar Cipher is a way of encoding text seen during the times of Julius Caesar where he would shift each letter of the alphabet by a certain pre-determined amount.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type '1' to encrypt, type '2' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#   e.g. 
#   plain_text = "hello"
#   shift = 5
#   cipher_text = "mjqqt"

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    #for an alphabet in the plain text
    for letter in plain_text:
        #finding the position of the letter in the alphabet
        letter_position = alphabet.index(letter)
        #new letter position after encrypting shift
        shifted_letter = letter_position + shift_amount

        new_letter = alphabet[shifted_letter]
        #cipher_text = cipher_text + new_letter
        cipher_text += new_letter
        
    print(f"The encoded text is {cipher_text}")
    

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# Bug alert: What happens if you try to encode the word 'civilization'?🐛
#Bug fixed there are two ways: have another length of alphabets or create a loop function where the alphabet loops back to the start when we have a letter at the end of the document

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(plain_text=text,shift_amount=shift)

#Test it here: https://replit.com/@terrykirungo/4-caesar-cipher-1-encrypt#main.py