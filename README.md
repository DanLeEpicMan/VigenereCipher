# Vigenere Cipher
I found this while I was browsing through some of my old files, and figured I may as well upload it here. I made this sometime in Fall 2021 (don't really remember when exactly since I completely forgot about this), most likely out of curiosity while I was Googling encryption algorithms, and decided to try to implement one on my own. This script ignores all non-English Alphabet characters and shifts them according to the Vigenere Cipher (basically a dynamic Caesar Cipher) and converts every character to upper-case. See usage below.

# Usage

The vigenere function has 3 parameters, one of which is optional.

**Text** — The plaintext to be encrypted. You can input anything if you want, but the program will ignore non-English alphabet characters (including spaces and punctuation marks).

**Key** — The key to encrypt the plaintext with. This program is essentially a dynamic Caesar Cipher, shifting individual characters depending on the position in the key and text.

**Decrypt** (Optional) — Whether the program should attempt to encrypt or decrypt a given plaintext. By default this is False.

For command prompt, the usage is (Note: For Decrypt, you can type either "True" or "False", not case-sensitive. It's also still optional):
```
python vigenere.py Plaintext Key {Decrypt = false}
```
Some examples
```
python vigenere.py "super secret text" "immaculatekey" => AGBETMPCKIDXCFF
python vigenere.py "AGBETMPCKIDXCFF" "immaculatekey" true => SUPERSECRETTEXT
```
