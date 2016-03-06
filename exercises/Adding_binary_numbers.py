'''
Adding binary numbers
Check if input str or int
'''


def add(x,y):
	maxlen = max(len(x), len(y))

	#Normalize lengths
	x = x.zfill(maxlen)
	y = y.zfill(maxlen)

	result = ''
	carry = 0

	for i in range(maxlen-1, -1, -1):
		r = carry
		r += 1 if x[i] == '1' else 0
		r += 1 if y[i] == '1' else 0

		# r can be 0,1,2,3 (carry + x[i] + y[i])
		# and among these, for r==1 and r==3 you will have result bit = 1
		# for r==2 and r==3 you will have carry = 1

		result = ('1' if r % 2 == 1 else '0') + result
		carry = 0 if r < 2 else 1       

	if carry !=0 : result = '1' + result

	print (result.zfill(maxlen))
add('111', '1')