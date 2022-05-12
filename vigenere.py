# note: everything will be converted to uppercase and all non-alphabet characters will be ignored.
import sys

def vigenere(text, key, decipher=False): # usage: text = text to be encryped. key = key to encrypt with. decipher = whether the program should attempt to encrypt or decrpyt text
    text = text.upper()
    key = key.upper()
    keyLen = len(key)
    cipher = ""
    offset = 0 # allows the program to skip non-alphabet characters while maintaining the algorithm's consistency
    for i in range(len(text)):
        currentText = text[i]  # current character in text
        if not (65 <= ord(currentText) and 90 >= ord(currentText)): # checks if the current character is usable
            offset = offset + 1
            continue
        currentKey = key[(i % keyLen - offset)] # current character in key
        if not decipher:
            cipher = cipher + chr((ord(currentText) + ord(currentKey)) % 26 + 65)
        else:
            cipher = cipher + chr((ord(currentText) - ord(currentKey)) % 26 + 65)

    return cipher

decyph = 0 if (len(sys.argv) < 4) else int(sys.argv[3])

print(vigenere(sys.argv[1], sys.argv[2], True if decyph == 1 else False))