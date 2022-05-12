# Vigenere Cipher
I found this while I was browsing through some of my old files, and figured I may as well upload it here. I made this sometimes in Fall 2021 (don't remember exactly as I had completely forgotten about this), most likely out of boredom while I was Googling encryption algorithms, and decided to try to implement one on my own. I did modify this a bit, since previously my code simply shifted the Unicode, whereas now this script ignores all non-English alphabet characters and shifts it within modulo 26 (that is, it goes from Z to A instead of Z to special characters). I also added some functionality for command prompt. See usage below.

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
python vigenere.py "AGBETMPCKIMDIVB" "immaculatekey" false => SUPERSECRETTEXT
```
