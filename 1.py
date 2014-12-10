def summ(li):
	print reduce(lambda x,y: x+y,li)

lst = [1,2,3,4,5]
print lst
summ(lst)
