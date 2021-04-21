alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
def caesar(plain_text, shift_amount, direction_chosen):
    end_text = ""
    for letter in plain_text:
        letter_position = alphabet.index(letter)
        if direction_chosen == "encode":
            new_letter_position = letter_position + shift_amount
            cipher_text += alphabet[new_letter_position]
        print(f"The encoded text is {cipher_text}")
        else:
            original_letter_position = letter_position - shift_amount
            original_text += alphabet[original_letter_position]
        print(f"The decoded text is {original_text}")

caesar(plain_text = text, shift_amount= shift, direction_chosen=direction)
