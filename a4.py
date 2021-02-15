def merge(dic1,dic2):
	return(dic2.update(dic1))
dic1={"a":4,"b":5}
dic2={"c":9,"d":7}
print(merge(dic1,dic2))	
print(dic2)