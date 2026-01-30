def ceasar_encrypt(plaintext, shift, encrypt):
    encrypted = "" 
    min = 32
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
        key_char = keyword[len(result) % len(keyword)]
        shift = ord(key_char) - min
        result += ceasar_encrypt(char, shift, encrypt)
    return result

print(vigenere_cipher("Hello, World!", "testkeyword", True))
print(vigenere_cipher(">Lab\qyP`fRZf", "testkeyword", False))

def frequency_analysis(text):
    frequency = {' ': 0,'E': 0, 'T': 0, 'A': 0, 'O': 0, 'N':
0, 'I': 0,'S': 0,'R': 0,'H': 0,'L': 0,'D':
0,'U': 0,'C': 0,'M': 0,'F': 0,'W': 0,'G':
0,'P': 0,'Y': 0,'B': 0,'V': 0,'K': 0,'X':
0,'J': 0,'Q': 0,'Z': 0}
    for char in text:
        if char.upper() in frequency:
            frequency[char.upper()] += 1/len(text)
    return frequency
print(frequency_analysis("Hello, World! Hello!"))

def cross_correlation(freq1, freq2):
    total = 0
    for s in freq1:
        total += freq1[s] * freq2[s]
    return total
print(cross_correlation({'A': 0.1, 'B': 0.2}, {'A': 0.2, 'B': 0.1}))


def get_ceasar_shift(ciphertext, exp):
    corr = []
    for shift in range(95):
        decrypted = ceasar_encrypt(ciphertext, shift, False)
        freq = frequency_analysis(decrypted)
        correlation = cross_correlation(freq, exp)
        corr.append(correlation)
    return corr.index(max(corr))

x = {' ': .1828846265,'E': .1026665037, 'T': .0751699827, 'A': .0653216702, 'O': .0615957725, 'N':
.0571201113, 'I': .0566844326,'S': .0531700534,'R': .0498790855,'H': .0497856396,'L': .0331754796,'D':
.0328292310,'U': .0227579536,'C': .0223367596,'M': .0202656783,'F': .0198306716,'W': .0170389377,'G':
.0162490441,'P': .0150432428,'Y': .0142766662,'B': .0125888074,'V': 0.0079611644,'K': 0.0056096272,'X':
0.0014092016,'J': 0.0009752181,'Q': 0.0008367550,'Z': 0.0005128469}

print(get_ceasar_shift(ceasar_encrypt("Using your implemented cross-correlation as described above," \
" it should return an int: the likely shift used to encrypt the message. The variable expected_dist in our " \
"test cases will contain the following dictionary:", 6, True), x))

def get_vigenere_keyword(ciphertext, keyword_length, exp):
    keyword = ""
    for i in range(keyword_length):
        segment = ""
        for j in range(i, len(ciphertext), keyword_length):
            segment += ciphertext[j]
        shift = get_ceasar_shift(segment, exp)
        keyword += chr(shift + 32)
    return keyword

print(get_vigenere_keyword(vigenere_cipher("Using your implemented cross-correlation as described above," \
" it should return an int: the likely shift used to encrypt the message. The variable expected_dist in our " \
"test cases will contain the following dictionary:", "keyword", True), 7, x))