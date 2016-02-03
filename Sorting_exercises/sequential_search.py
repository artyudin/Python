# unsorted list

def sequential_search_unsort(list_, item ):
	pos = 0
	found = False

	while pos < len(list_) and not found:
		if list_[pos] == item:
			found = True
		else:
			pos += 1

	return found


new_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search_unsort(new_list, 13))

# sorted list

def sequential_search_sort(list_, item):
	pos = 0
	found = False
	stop = False

	while pos < len(list_) and not found and not stop:
		if list_[pos] == item:
			found = True
		else:
			if list_[pos] > item:
				stop = True
			else:
				pos += 1

	return found


new_list = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
print(sequential_search_sort(new_list, 13))










