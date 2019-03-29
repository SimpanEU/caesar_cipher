#!/usr/bin/env python3

from lib.encrypt import *
from lib.decrypt import *


class Cipher:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def encrypt(ciphertext=None, shift=None):
        if ciphertext and shift:
            encrypt(ciphertext, shift)

    @staticmethod
    def decrypt(ciphertext=None, shift=None):
        if ciphertext and shift is not None:
            decrypt(ciphertext, shift)
