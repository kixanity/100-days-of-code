alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(n_text, n_shift, n_direction):
    textile = ""
    for letter in n_text:
        position = alphabet.index(letter)
        if n_direction == 'encode':
            new_position = position + n_shift
        elif n_direction == 'decode':
            new_position = position - n_shift
        textile += alphabet[new_position]
    print(f"The encoded text is {textile}")


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(n_text=text, n_shift=shift, n_direction=direction)
