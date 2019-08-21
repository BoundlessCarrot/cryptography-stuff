# Cryptography experiments and things...
This is a place where I want to try to code different encryption techniques. I'll start with substitution ciphers, and possibly end with a one-time pad or an Enigma emulator. Who knows?

## Table of Contents:
  - [Caesar cipher](#caesar-cipher)
  - [Affine cipher](#affine-cipher)

## Explanations

### Caesar cipher
[Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher) | 
[Code](https://github.com/BoundlessCarrot/cryptography-stuff/blob/master/simple%20caesar%20cipher.py)

The Caesar cipher is one of the oldest ciphers known to man, as well as one of the simplest and well known ciphers. It works by taking a key, that both the sender and the recipient know, and shifting each letter in your message by that key. This is known as a substitution cipher. Specifically, this is a monoalphabetic substitution cipher becuase we are only using one alphabet (26 letters) rather than possibly cycling the message through multiple alphabets.

So, as an example, say we have the word ```github``` as our plaintext, and our key is 12. The resulting ciphertext would be ```suftgn```.

Let's break that down step-by-step:
  1. Take a letter, our first letter being `g`.
  2. Our key is 12, so we take our letter and go 12 letters down the alphabet. In this case, the resulting letter is `s`.
  3. Repeat until you get to the end of the message.

Keep in mind that as a substituition cipher, and especially as a monoalphabetic substitution cipher, the encrypted message is vulnerable to cryptanalysis as well as frequency analysis, as the frequency of letters in the text doesn't change, it is just shifted by the key.

The program I wrote takes a string for the message, as well as an integer the key. It then outputs an encrypted message by converting each letter to its ASCII value, adding the key, then converting back, all the while correcting for mistakes (A 'mistake' in this case would be an ASCII value over 122, which is z. In this case, the program finds the difference between the given encrypted ASCII value and 122, and just starts again from the beginning of the alphabet). For simplicity's sake, the program skips (and therefore keeps) punctuation and spaces as well as makes/outputs all letters in lowercase.

Let's break that down as well, as it's a bit more of an involved process:

  1. Take a character from your message.
  2. If the charcater is part of the alphabet (i.e. not punctuation or a space), continue. Otherwise, skip to step 7.
  3. Get the encrypted value of the letter. This involves converting the letter to its ASCII value and adding the key to it.
  4. If the encrypted value is less than 122, skip to step 6. Otherwise, continue.
  5. Calculate the offset. If we are at this step, it means that the encrypted value is greater than 122, which means we are substituting letters for punctuation and/or symbols, which we don't want to do. In this case, we:
      1. Take the difference between the encrypted value and the end of the alphabet in ASCII (encrypted value - 122)
      2. Add the offset to the beginning of the alphabet in ASCII (96 + offset)
      3. Convert your offset/encrypted value to a character and add the letter to the encrypted message.
  6. Convert your encrypted value to a character.
  7. Add the character to the encrypted message.

The decryption function is simply a brute force decryption, as the number of possibilities is relatively small. The program cycles through every possible key (1 - 26) and outputs what might be the plaintext for each related key. 

As a note to come back to, it could be interesting to use the actual encryption function as the decryption function by giving it the encrypted text and cycling through all possible keys. (This is kinda what the decryptor is already doing but within its own function)

### Affine cipher
[Wikipedia](https://en.wikipedia.org/wiki/Affine_cipher) | 
[Code](https://github.com/BoundlessCarrot/cryptography-stuff/blob/master/affine%20cipher.py)

Explanation coming soon!