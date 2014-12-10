def fibo(i):
	if i == 0:
		return [1,1]
	lst=fibo(i-1)
	print lst[0]
	return [lst[1],lst[0]+lst[1]]

i=998
fibo(i)

#Highest value for which fibonacci series is printed is 998
