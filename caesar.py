#!/usr/bin/env python3

import argparse
from lib.cipher import Cipher


def main():
    caesar_cipher = Cipher('Caesar Cipher')
    parser = argparse.ArgumentParser(description='Caesar Cipher encryption/decryption tool.')
    parser.add_argument('-e', '--encrypt', type=str, action='store', help='Encrypt Ciphertext')
    parser.add_argument('-d', '--decrypt', type=str, action='store', help='Decrypt Ciphertext')
    parser.add_argument('-s', '--shift', type=int, action='store', help='Shift value')
    args = parser.parse_args()

    if args.encrypt is None and args.decrypt is None and args.shift is None:
        print('Caesar Cipher Encryption/Decryption tool.')
        print("Usage:")
        print('-e   --encrypt   "Ciphertext"')
        print('-d   --decrypt   "Ciphertext"')
        print('-s   --shift   Shift Value(1, 2, 3...)')
        print('')
        print('E.g.')
        print('$ caesar.py -e "You cant read this!" -s 5')
        print('Encryption input: You cant read this!')
        print('Encryption output: Dtz hfsy wjfi ymnx!')

    # Encryption Mode
    if args.encrypt and args.shift and args.decrypt is None:
        caesar_cipher.encrypt(args.encrypt, args.shift)

    # Decryption Mode
    elif args.decrypt and args.shift and args.encrypt is None:
        caesar_cipher.decrypt(args.decrypt, args.shift)


if __name__ == "__main__":
    main()
