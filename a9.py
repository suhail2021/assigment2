a=["A","B","C"]
x=map(lambda s:s[0]=="A",a)
print(list(x))
print(list(filter(lambda s:s[0]=="A",a)))
from functools import reduce
def add (x,y):
	return x+y
a=[1,2,3]
print(reduce(add,a))	