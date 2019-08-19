# Cryptography experiments and things...
This is a place where I want to try to code different encryption techniques. I'll start with substitution ciphers, and possibly end with a one-time pad or an Enigma emulator. Who knows?

## Table of Contents:
  Caesar cipher
  Affine cipher

## Explanations

### Caesar cipher
[Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
[Code](https://github.com/BoundlessCarrot/cryptography-stuff/blob/master/simple%20caesar%20cipher.py)

The Caesar cipher is one of the oldest ciphers known to man, as well as one of the simplest and well known ciphers. It works by taking a key, that both the sender and the recipient know, and shifting each letter in your message by that key. This is known as a monoalphabetic substitutionion cipher.
So, as an example, say we have the word ```github``` as our plaintext, and our key is 12. The resulting ciphertext would be ```suftgn```.
Keep in mind that as a substituition cipher, and especially as a monoalphabetic substitution cipher, the encrypted message is vulnerable to cryptanalysis as well as frequency analysis, as the frequency of letters in the text doesn't change, it is just shifted by the key.

The program I wrote takes a string for the message, as well as an integer the key. It then outputs an encrypted message by converting each letter to its ASCII value, adding the key, then converting back, all the while correcting for mistakes (A 'mistake' in this case would be an ASCII value over 122, which is z. In this case, the program finds the difference between the given encrypted ASCII value and 122, and just starts again from the beginning of the alphabet). 
The decryption function is simply a brute force decryption, as the number of possibilities is relatively small. The program cycles through every possible key (1 - 26) and outputs what might be the plaintext for each related key. As a note to come back to, it could be interesting to use the actual encryption function as the decryption function by giving it the encrypted text and cycling through all possible keys.

### Affine cipher
[Wikipedia](https://en.wikipedia.org/wiki/Affine_cipher)
[Code](https://github.com/BoundlessCarrot/cryptography-stuff/blob/master/affine%20cipher.py)
Explanation coming soon!