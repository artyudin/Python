def ceaser_cipher():
	
	message = 'moscow'
	shift = int(3)

	new_message = ""

	for charachter in message:
		if charachter >= 'a' and charachter <= 'z':
			position = ord(charachter) - ord('a')
			position = (position + shift) % 26
			new_charachter = chr(position + ord('a'))
			new_message = new_message + new_charachter

		else:
			charachter >= 'A' and charachter <= 'Z'
			position = ord(charachter) - ord('A')
			position = (position + shift) % 26
			new_charachter = chr(position + ord('A'))
			new_message = new_message + new_charachter

	print("The shifted message is", new_message)

ceaser_cipher()
