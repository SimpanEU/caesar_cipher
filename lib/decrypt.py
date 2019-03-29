#!/usr/bin/env python3


def decrypt(ciphertext, shift):
    print('Decryption input:', ciphertext)
    print('Shift:', shift)

    alphabet = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g",
                "f", "e", "d", "c", "b", "a"]

    for i in range(5):
        alphabet.extend(alphabet)

    if shift.isdigit():
        print('Decryption output: ', end="")
        for item in list(ciphertext):
            if item.isalpha():
                if item.isupper():
                    caesar_output = alphabet.index(item.lower()) + int(shift)
                    print(alphabet[caesar_output].upper(), end="")
                else:
                    caesar_output = alphabet.index(item) + int(shift)
                    print(alphabet[caesar_output], end="")
            else:
                print(item, end="")

    elif shift is 'A' or shift is 'a':

        for i in range(26):
            print('Decryption output', str(i+1)+': ', end="")
            for item in list(ciphertext):
                if item.isalpha():
                    if item.isupper():
                        caesar_output = alphabet.index(item.lower()) + i
                        print(alphabet[caesar_output].upper(), end="")
                    else:
                        caesar_output = alphabet.index(item) + i
                        print(alphabet[caesar_output], end="")
                else:
                    print(item, end="")
            print()
