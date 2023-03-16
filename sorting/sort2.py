# function to return the second element of the
# two elements passed as the parameter

def sortSecond(val):
	return val[1]
	
list1 = [(1, 22), (3, 33), (1, 11)]
	

#ascending according to second element
list1.sort(key = sortSecond)
print(list1)
	
#descending according to second element
list1.sort(key = sortSecond, reverse = True)
print(list1)
