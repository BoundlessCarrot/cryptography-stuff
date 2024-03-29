# Just a simple caesar cipher. decryption will maybe be another program, but if it's small enough it can be its own function here 

def caesar(n, message):
	encryptedMessage = ''
	
	for letter in message.casefold():
		if letter.isalpha() == True:
			encryptedLetterVal = ord(letter) + n
			
			if encryptedLetterVal > 122:
				offset = encryptedLetterVal - 122
				encryptedMessage += chr(96 + offset)
			else:
				encryptedMessage += chr(encryptedLetterVal)
				
		else:
			encryptedMessage += letter	
	return encryptedMessage

#This is a brute force decryption, rather than a cryptoanalysis one
def decryptor(message): 
	messagePossibilities = []
	
	for i in range(1, 27):
		decryptedMessage = ''
		
		for letter in message.casefold():
			if letter.isalpha() == True:
				decryptedLetterVal = ord(letter) - i
				
				if decryptedLetterVal < 97 :
					offset = decryptedLetterVal - 96
					decryptedMessage += chr(122 + offset)
				else:
					decryptedMessage += chr(decryptedLetterVal)
			else:
				decryptedMessage += letter
				
		messagePossibilities.append(decryptedMessage)
	
	printer(messagePossibilities)

def printer(message):
	count = 1
	print("\nKey | Message")
	print("=========================================")
	for possibility in message:
		print("{} | {}".format(count, str(possibility)))
		count += 1

# Trying to do this in the style of the affine cipher
#def smartCaesar(n, message):
#	encryptedMessage = ''
#	
#	for letter in message:
#		if letter.isalpha == True:
#			x = ord(letter) - 97
#			encryptedLetterVal = (x + n) % 26
#			encryptedMessage += chr(encryptedLetterVal + 97)
#			
#		else:
#			encryptedMessage += letter
#		
#	return encryptedMessage
	
if __name__ == '__main__':
	message = input("Type your message: ")
	key = int(input("Pick a key (must be less than or equal to 26): "))
	
	if key > 27 or key < 0:
		key = int(input("Key is not valid, pick a new key: "))
	
	eMessage = caesar(key, message)
#	eMessage = smartCaesar(key, message)
	print("Encrypted message: " + str(eMessage))
	decryptor(eMessage)