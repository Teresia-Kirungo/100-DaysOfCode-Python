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
        if direction_chosen == "decode":
            shift_amount = shift_amount * -1
            new_letter_position = letter_position +shift_amount
            end_text += alphabet[new_letter_position]
    print(f"The {direction_chosen}d text is{end_text}")

caesar(plain_text = text, shift_amount= shift, direction_chosen=direction)
