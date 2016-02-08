### Checking off

def anagramSolution(anag1, anag2):
	list_ = list(anag2)

	pos1 = 0
	still_ok = True
	

	while pos1 < len(anag1) and still_ok:
		pos2 = 0
		found = False
		while pos2 < len(list_) and not found:
			if anag1[pos1] == list_[pos2]:
				found = True
			else:
				pos2 = pos2 + 1
		if found:
			list_[pos2] = None
		else:
			still_ok = False
		pos1 = pos1 + 1
	return still_ok

print(anagramSolution('siobhan donaghy', 'shanghai nobody'))

# Sort and Compare

def anagramSolution2(anag1, anag2):
	list_one = list(anag1)
	list_two = list(anag2)

	list_one.sort()
	list_two.sort()

	pos = 0
	matches = True

	while pos < len(anag1) and matches:
		if list_one[pos] == list_two[pos]:
			pos = pos + 1
		else:
			matches = False
	return matches


print(anagramSolution2('siobhan donaghy', 'shanghai nobody'))


def anagramSolution3(anag1, anag2):
	list_one = [0]*26 #26 possible char in vacabular 
	list_two = [0]*26

	for i in range(len(anag1)):
		pos = ord(anag1[i]-ord('a'))
		list_one[pos] = list_one[pos] + 1

	for i in range(len(anag2)):
		pos = ord(anag2[i]-ord('a'))
		list_two[pos] = list_two[pos] + 1

	j = 0
	still_ok = True
	while j<26 and still_ok:
		if anag1[j] == anag2[j]:
			j = j + 1
		else:
			still_ok = False
	return still_ok


print(anagramSolution2('siobhan donaghy', 'shanghai nobody'))









