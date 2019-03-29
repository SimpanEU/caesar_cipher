#!/usr/bin/env python3


def decrypt(ciphertext, shift):
    print('Decryption input:', ciphertext)
    print('Shift:', shift)

    alphabet = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g",
                "f", "e", "d", "c", "b", "a"]

    for i in range(5):
        alphabet.extend(alphabet)

    print('Decryption output: ', end="")
    for item in list(ciphertext):
        if item.isalpha():
            if item.isupper():
                caesar_output = alphabet.index(item.lower()) + shift
                print(alphabet[caesar_output].upper(), end="")
            else:
                caesar_output = alphabet.index(item) + shift
                print(alphabet[caesar_output], end="")
        else:
            print(item, end="")
