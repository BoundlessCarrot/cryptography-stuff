from math import gcd as bltin_gcd

def coprime(a, b):
	return bltin_gcd(a,b) == 1

def affine(a, b, message):
	encryptedMessage = ''
	
	for letter in message.casefold():
		if letter.isalpha() == True:
			x = ord(letter) - 97
			encryptedLetterVal = ((a * x) + b) % 26
			encryptedMessage += chr(encryptedLetterVal + 97)
		else:
			encryptedMessage += letter
	
	return encryptedMessage

if __name__ == '__main__':
	message = input("Type your message: ")
	key1 = int(input("Pick your 1st key (must be less than or equal to 26, must be co-prime): "))
	key2 = int(input("Pick your 2nd key (must be less than or equal to 26, must be co-prime): "))
	
	while coprime(key1, key2) != True:
		print("Those keys weren't co-prime. Try again!")
		key1 = int(input("Pick your 1st key (must be less than or equal to 26, must be co-prime): "))
		key2 = int(input("Pick your 2nd key (must be less than or equal to 26, must be co-prime): "))
		
	eMessage = affine(key1, key2, message)
	print("Encrypted message: " + eMessage)