def low(li):
	li = map(fun,li)
	print li

def fun(x):
	return x.lower()

lst = ['Hello World','abc','NaMo','INDIA','python']
low(lst)
