
def Table():
	MIN = 1
	MAX = 11

	#upper level
	# print("    ", end="")

	# for i in range(MIN, MAX +1):
	# 	print("%4d" %i, end="")
	# print()
	
	#multiplication level
	for i in range(MIN, MAX):
		# print (i, end="" )

		for j in range(MIN,MAX):
			print("%4d" %(i * j), end="")
		print()

		


Table()