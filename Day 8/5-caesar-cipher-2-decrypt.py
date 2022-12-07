print("Welcome to the Caesar Cipher Game!")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type '1' to encrypt, type '2' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(plain_text, shift_number):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_number
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#   e.g. 
#   cipher_text = "mjqqt"
#   shift = 5
#   plain_text = "hello"
#   print output: "The decoded text is hello"
    
def decrypt(cipher_text, shift_back):
    plain_text = ""
    for letter in cipher_text:
        #Gets the position of each letter in the cipher text
        letter_position = alphabet.index(letter)
        #Gets the original position of the letter in the cipher text before the encryption
        original_position = letter_position - shift_back
        #plain_text = plain_text + alphabet[original_position]
        plain_text += alphabet[original_position]
    #prints decoded text    
    print(f"The decoded text is {plain_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(cipher_text=text, shift_back=shift)
    
#Test it here: https://replit.com/@terrykirungo/5-caesar-cipher-2-decrypt#main.py
