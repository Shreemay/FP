def prod_Even(li):
	ls = filter(find_Even,li)
	print reduce(lambda x,y: x*y, ls)

def find_Even(x):
	if x%2 == 0:
		return True
	else:
		return False

lst = [1,2,3,4,5,6,7,8,9,10]
prod_Even(lst)
