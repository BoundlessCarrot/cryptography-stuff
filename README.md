# Cryptography experiments and things...
This is a place where I want to try to code different encryption techniques. I'll start with substitution ciphers, and possibly end with a one-time pad or an Enigma emulator. Who knows?

## Table of Contents:
- [Vocabulary][1]
- [Explanations][2]
	 - [Caesar cipher][3]
	 - [Affine cipher][4]
	- [Atbash cipher][5]

## Vocabulary
- [ASCII][6]: A system to represent characters in a way a computer can understand. More specifically, a system for encoding characters (letters, numbers, symbols) in decimal, binary, and hexadecimal numbers.
	- [This is the ASCII table I reference][7]
- [Substitution cipher][8]: A method of encryption where each character is substituted for another character, using either a key or a mathematical function. Comes in 2 varieties:
	- [Monoalphabetic Substitution cipher][9]: Uses a single alphabet to encrypt a message. Examples include the Caesar cipher and ROT13. 
	- [Polyalphabetic Substitution cipher][10]: Uses multiple alphabets to encrypt a message. Examples include the Vignère cipher and the Enigma machine.

## Explanations

### Caesar cipher
[Wikipedia][11] | 
[Code][12] |
[Try it online!][13]

The Caesar cipher is one of the oldest ciphers known to man, as well as one of the simplest and well known ciphers. It works by taking a key, that both the sender and the recipient know, and shifting each letter in your message by that key (a substitution cipher). 

So, as an example, say we have the word `github` as our plaintext, and our key is 12. The resulting cipher-text would be `suftgn`.

Let's break that down step-by-step:
  1. Take a letter, our first letter being `g`.
  2. Our key is 12, so we take our letter and go 12 letters down the alphabet. In this case, the resulting letter is `s`.
  3. Repeat until you get to the end of the message.

Keep in mind that as a substitution cipher, and especially as a monoalphabetic substitution cipher, the encrypted message is vulnerable to cryptanalysis as well as frequency analysis, as the frequency of letters in the text doesn't change, it is just shifted by the key.

The program I wrote takes a string for the message, as well as an integer the key. It then outputs an encrypted message by converting each letter to its ASCII value, adding the key, then converting back, all the while correcting for mistakes (A 'mistake' in this case would be an ASCII value over 122, which is z. In this case, the program finds the difference between the given encrypted ASCII value and 122, and just starts again from the beginning of the alphabet). For simplicity's sake, the program skips (and therefore keeps) punctuation and spaces as well as makes/outputs all letters in lowercase.

Let's break that down as well, as it's a bit more of an involved process:

  1. Take a character from your message.
  2. If the character is part of the alphabet (i.e. not punctuation or a space), continue. Otherwise, skip to step 7.
  3. Get the encrypted value of the letter. This involves converting the letter to its ASCII value and adding the key to it.
  4. If the encrypted value is less than 122, skip to step 6. Otherwise, continue.
  5. Calculate the offset. If we are at this step, it means that the encrypted value is greater than 122, which means we are substituting letters for punctuation and/or symbols, which we don't want to do. In this case, we:
	  1. Take the difference between the encrypted value and the end of the alphabet in ASCII (encrypted value - 122)
	  2. Add the offset to the beginning of the alphabet in ASCII (96 + offset)
	  3. Convert your offset/encrypted value to a character and add the letter to the encrypted message.
  6. Convert your encrypted value to a character.
  7. Add the character to the encrypted message.

The decryption function is simply a brute force decryption, as the number of possibilities is relatively small. The program cycles through every possible key (1 - 26) and outputs what might be the plaintext for each related key. 

<sub>It could be interesting to use the actual encryption function as the decryption function by giving it the encrypted text and cycling through all possible keys. (This is kinda what the decryption function is already doing but within its own function)</sub>

---- 
### Affine cipher
[Wikipedia][14] | 
[Code][15] |
[Try it online!][16]

The Affine cipher is also a monoalphabetic substitution cipher, but a more generalized one. The cipher takes two keys, the first of which must be co-prime with the size of your alphabet (have no common divisors besides 1) and a message. It encrypts the message by taking the numeric value of each letter (0-25, not 1-26, at least for the English alphabet) and applying a short algebraic function to it:

```MATH
E(x) = (ax + b) mod m
```

Where:
- _a_ = key #1
- _b_ = key #2
- _x_ = numeric value of the letter in question
- _m_ = the size of the alphabet used (for the English alphabet, m = 26).

NOTE: `mod` refers to the ‘modulus’ operator, which in many programming languages is represented by the percent sign (`%`). This operator works by returning the _remainder_ of a division operation rather than the quotient.

NOTE 2: _a_ and _m_ must be co-prime because non-co-prime values there lead to encrypted text that can have multiple decrypted possibilities, which is obviously not desirable.

In fact, you could define the Caesar cipher as an Affine cipher where _a_ = 1, since _a_ = 1 translates to a linear shift of letters.

So, let’s take `github` as an example again. Using the Affine cipher, and keys 5 and 8, our encrypted message would be `mwzren`.

Let’s break that down:
1. Take a letter, our first letter again being `g`.
2. Convert the letter to its numeric equivalent, starting the count from 0 (like in an array). Numeric equivalent of `g` is `6`.
3. Now we apply our encryption function:
	1. `(5*6 + 8) = 38`
	2. `38 mod 26 = 12`
4. Now, we simply convert our encrypted numeric value back to a letter. In this case, the numeric value is `12`, which, when converted back to a letter, becomes `m`.
5. Repeat for the rest of your message.

Again, as this is a monoalphabetic substitution cipher, it is very weak and is vulnerable to nearly all methods of forceful decryption such as frequency analysis, brute force, and even guessing. Mathematically, there are 12 numbers co-prime with 26 that are less than 26 (_a_ values) as well as 26 possible values for each value of _a_ (_b_ values). Therefore there are 312 `(12 * 26)` possible encryptions using the Affine cipher. However, this number also includes trivial solutions that the Caesar cipher could also produce (where `a = 1`). Without the trivial solutions, this number drops to 286 unique encryptions, which is very low and very vulnerable.

My program takes 2 integers (the 2 keys) and a string (the message), checks if the first key is co-prime with _m_, and then encrypts using the encryption function after converting each letter to a number. It then converts each number to a character and adds it to an empty string initialized when we called the affine function. After converting the entire message it returns and prints the string. Again, for simplicity’s sake, this program keeps spaces and punctuation.

Let’s break that down, because, as always, the code is much more involved than the actual cipher:
1. Get the message and the keys.
2. If the _a_ (key1) is co-prime with _m_ (26), continue. If not get new keys from the user.
3. Now, take a character from your message. If the character is a letter, continue. Otherwise, skip to step 4.
	1. Convert the character to its ASCII value and subtract 97 from it to get its 0 - 25 value.
	2. Apply the encryption function to the character value to get its encrypted character value.
	3. Add 97 back to the encrypted character value to bring it back into the ASCII letter value range, and convert it back into a character.
4. Add the character to the encrypted message string (initialized as an empty string just before step 3).
5. Repeat for the rest of the message.

The decryption function for this cipher isn’t done yet but it’s also a mathematical function, so it should be trivial to program (famous last words?). In fact, it’s almost the same function as the encryption function:

```MATH
D(x) = a^-1(x - b) mod m
```

<sub>Full explanation including the decryption function coming soon!</sub>

---- 
### Atbash cipher
[Wikipedia][17] | 
[Code][18] | 
[Try it online!][19]

The Atbash cipher is a monoalphabetic substitution cipher that was originally used to encrypt the Hebrew alphabet, although it can be used to encrypt any alphabet with a standard order.

The cipher works by taking a message and replacing each letter in the message with its equal in the alphabet’s reverse order. 

So, let’s again take `github` as an example message. The resulting cipher-text would then be `trgsfy`.

Step-by-step:
1. Take a letter from the message. In this case our first letter is `g`.
2. Get the letter’s opposite. `g`’s opposite is `t` (g is the 7th letter, so we take the 7th letter starting from z to get the encrypted letter).
3. Repeat for the rest of the message.

My program first gets a message (as a string) from the user. Then it finds each character’s alphabetical value (0-25), then subtracts that value from 122 to bring it back into ASCII range. For simplicity’s sake, the message is case-folded within the cipher and the cipher only returns lowercase letters

Step-by-step:
1. Get the message from the user.
2. Initialize an empty string for the encrypted message.
3. Cycle through the characters in the message. 
4. If the character is a letter, continue. Otherwise, skip to step 5.
	1. First we need to get our letter’s 0-25 value, initialized as letterValue. We do this by taking the ASCII value of each letter and subtracting 97 from it.
	2. Then we need to get our reverse alphabet value. We do this by subtracting the letter value from 122. While you could go the extra step of subtracting letterValue from 26 and adding that to 97 to get the ASCII value of the letter, doing it this way gets our correct encrypted letter and brings us into ASCII range in one step, simplifying the process.
	3. Convert the reverse alphabet value to a character.
5. Add the character to the encrypted message string.

Because this cipher doesn’t take a key and the encrypted message is simply the opposite values of each letter, we can use our encryption function as our decryption function, as it just reverses the effects of the first pass through the encryption function.

---- 

[1]:	#vocabulary
[2]:	#explanations
[3]:	#caesar-cipher
[4]:	#affine-cipher
[5]:	#atbash-cipher
[6]:	https://en.wikipedia.org/wiki/ASCII
[7]:	http://www.asciitable.com
[8]:	https://en.wikipedia.org/wiki/Substitution_cipher
[9]:	https://en.wikipedia.org/wiki/Substitution_cipher#Simple_substitution
[10]:	https://en.wikipedia.org/wiki/Polyalphabetic_cipher
[11]:	https://en.wikipedia.org/wiki/Caesar_cipher
[12]:	https://github.com/BoundlessCarrot/cryptography-stuff/blob/master/caesar%20cipher.py
[13]:	https://repl.it/@BoundlessCarrot/Caesar
[14]:	https://en.wikipedia.org/wiki/Affine_cipher
[15]:	https://github.com/BoundlessCarrot/cryptography-stuff/blob/master/affine%20cipher.py
[16]:	https://repl.it/@BoundlessCarrot/Affine
[17]:	https://en.wikipedia.org/wiki/Atbash
[18]:	https://github.com/BoundlessCarrot/cryptography-stuff/blob/master/atbash%20cipher.py
[19]:	https://repl.it/@BoundlessCarrot/Atbash