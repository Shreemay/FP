def length(li):
	ls = map(lambda x: 1, li)
	print reduce(lambda x,y: x+y, ls)

lst = [1,2,3,4,5,6,7,8,9,10]
count=0
length(lst)
