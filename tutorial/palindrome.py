def palindrome(string):

	# assume its poindrome utill its proven otherwise
	is_palindrome = True
	# check the characters, starting from the ends until middle is reached
	for i in range(0, len(string)//2):
		#if the charachters don't match then mark
		#that string is not a polindrome
		if string[i] != string[len(string) -i -1]:
			is_palindrome = False

	if is_palindrome:
		return True
	else:
		return False

print(palindrome('natootan'))

