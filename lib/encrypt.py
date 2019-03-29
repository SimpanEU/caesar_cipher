#!/usr/bin/env python3

def encrypt(ciphertext, shift):
    print('Encryption input:', ciphertext)

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]

    for i in range(5):
        alphabet.extend(alphabet)

    print('Encryption output: ', end="")
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
