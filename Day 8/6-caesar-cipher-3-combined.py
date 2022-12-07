alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type '1' to encrypt, type '2' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
def caesar(plain_text, shift_amount, direction_chosen):
    end_text = ""
    if direction_chosen == "2":
        #shift_amount = shift_amount x -1
        shift_amount *= -1
    for letter in plain_text:
        letter_position = alphabet.index(letter)
        new_letter_position = letter_position + shift_amount
        end_text += alphabet[new_letter_position]
    print(f"The decoded text is {end_text}")
            


caesar(plain_text = text, shift_amount= shift, direction_chosen=direction)

#Test it here: https://replit.com/@terrykirungo/6-caesar-cipher-3-combined#main.py
