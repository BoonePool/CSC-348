def ceasar_encrypt(plaintext, shift, encrypt):
    encrypted = "" 
    min = 32 # Max and min ascii values
    max = 126
    if not encrypt: # invert shift for decryption
        shift = -shift
    for char in plaintext:
        num = ((ord(char) + shift -min) % (max - min)) + min # gets ascii value of char and normalizes it to 32-126
        encrypted += chr(num)
    return encrypted
print(ceasar_encrypt("Hello, World!", 3, True))
print(ceasar_encrypt("Khoor/#Zruog$", 3, False))

def vigenere_cipher(message, keyword, encrypt):
    result = ""
    min = 32 # Max and min ascii values
    max = 126
    for char in message:
        key_char = keyword[len(result) % len(keyword)] # get corresponding char from keyword
        shift = ord(key_char) - min # calculate shift based on ascii value of char
        result += ceasar_encrypt(char, shift, encrypt)
    return result

print(vigenere_cipher("Hello, World!", "testkeyword", True))
print(vigenere_cipher(">Lab\qyP`fRZf", "testkeyword", False))
