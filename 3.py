def odd(li):
	print reduce(lambda x,y: x+y, filter(find_odd,li))

def find_odd(x):
	if x%2 == 0:
		return False
	else:
		return True

lst = [1,2,3,4,5,6,7,8,9,10]
print lst
odd(lst)
