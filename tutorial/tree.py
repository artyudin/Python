def triangle():
	for i in range(11,0,-1):
		print((' '*i) +('*'*(11-i)))

triangle()


def test_value(value):
    
    if value < 100:
        return 'The value is right!'
        else:
            return 'The value is to big'
print(test_value(55))
