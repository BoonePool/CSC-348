
from random import random
from part1 import ceasar_encrypt, vigenere_cipher

from part2 import (
    frequency_analysis,
    cross_correlation,
    get_ceasar_shift,
    get_vigenere_keyword,
    x  # expected frequency distribution
)

plaintext = "THIS IS A SIMPLE CAESAR CIPHER TEST"
shift = int(random() * 94)

ciphertext = ceasar_encrypt(plaintext, shift, True)
print("Ciphertext:", ciphertext)

recovered_shift = get_ceasar_shift(ciphertext, x)
print("Recovered shift:", recovered_shift)

decrypted = ceasar_encrypt(ciphertext, recovered_shift, False)
print("Decrypted:", decrypted)
print()

plaintext = "Examples to test your code for this part (the goal is to derive the right key and decrypt the following ciphertexts) (Hit: you might need to copy the text into a notepad before using it as an input to your code, there are some hidden/white characters that could through the decryption process off):"
keyword = "TEST KEYWORD"
key_length = len(keyword)

ciphertext = vigenere_cipher(plaintext, keyword, True)
print("Ciphertext:", ciphertext)

recovered_keyword = get_vigenere_keyword(ciphertext, key_length, x)
print("Recovered keyword:", recovered_keyword)

decrypted = vigenere_cipher(ciphertext, recovered_keyword, False)
print("Decrypted:", decrypted)

text = "HELLO WORLD"
freq = frequency_analysis(text)
print( "\n", freq, "\n")
    

