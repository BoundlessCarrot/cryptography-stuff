def atbash(message):
	encryptedMessage = ''
	
	for letter in message.casefold():
		if letter.isalpha() == True:
			letterValue = ord(letter) - 97
			encryptedMessage += chr(122 - letterValue)
		else:
			encryptedMessage += letter
	
	return encryptedMessage

if __name__ == '__main__':
	message = input("Type your message: ")
	eMessage = atbash(message)
	print("Encrypted message: {}".format(eMessage))
	print("Decrypted message: {}".format(atbash(eMessage)))