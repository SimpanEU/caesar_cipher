#!/usr/bin/env python3

import argparse
from lib.cipher import Cipher


def main():
    parser = argparse.ArgumentParser(description='Caesar Cipher encryption/decryption tool.')
    parser.add_argument('-e', '--encrypt', type=str, action='store', help='Encrypt Ciphertext')
    parser.add_argument('-d', '--decrypt', type=str, action='store', help='Decrypt Ciphertext')
    parser.add_argument('-s', '--shift', type=str, action='store', help='Shift value')
    args = parser.parse_args()

    if args.encrypt is None and args.decrypt is None and args.shift is None:
        print('Caesar Cipher Encryption/Decryption tool.')
        print("Usage:")
        print('-e   --encrypt   "Ciphertext"')
        print('-d   --decrypt   "Ciphertext"')
        print("-s   --shift   Shift Value(1, 2, 3...) or 'A' for auto-mode, testing 26 different shift values.")
        print('')
        print('E.g.')
        print('caesar.py -e "You cant read this!" -s 5')
        print('caesar.py -d "Dtz hfsy wjfi ymnx!" -s A')

    # Encryption Mode
    if args.encrypt and args.shift and args.decrypt is None:
        caesar = Cipher(args.encrypt, args.shift)
        caesar.encrypt()

    # Decryption Mode
    elif args.decrypt and args.shift and args.encrypt is None:
        caesar = Cipher(args.decrypt, args.shift)
        caesar.decrypt()


if __name__ == "__main__":
    main()
