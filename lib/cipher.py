#!/usr/bin/env python3

from lib.encrypt import *
from lib.decrypt import *


class Cipher:

    def __init__(self, ciphertext, shift):
        self.ciphertext = ciphertext
        self.shift = shift

    def encrypt(self):
        encrypt_cipher(self.ciphertext, self.shift)

    def decrypt(self):
        decrypt_cipher(self.ciphertext, self.shift)
