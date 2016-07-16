def f(x):
	return x**2

print(f(8))

l = lambda x: x**2

print(l(8))


foo = {2,18,9, 22, 17, 24, 8, 12, 27}

print(filter(lambda x: x% 3 == 0, foo))

# lambda runs for each element






















# nums = range(2,50)
# for i in range(2,8):
# 	nums = (list(filter(lambda x: x == i or x % i, nums)))
	

# print(nums)