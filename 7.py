def low(li):
	li = map(fun,li)
	li = filter(None,li)
	print li
	

def fun(x):
	if x.isalpha():
		return x.lower()
	else:
		return False

lst = ['Hello World123','abc','NaMo2014','INDIA','python']
low(lst)
