s= input("input a string:")
d=l=0
for c in s:
	if c.isdigit():
		d=d=1
	elif c.isalpha():
	     l=l+1
	else:
		pass
print("letters",l)
print("digits",d)		     
