# Python program to demonstrate sorting by user's
# choice
	
# function to return the second element 
# of the two elements passed as the parameter
def sortSecond(val):
	return len(val[1])
	
list1 = [(1, 'aa'), (3, 'ggg'), (8, 'k')]
	
#ascending according to second element
list1.sort(key = sortSecond)
print('ascending: ',list1)
	
#descending according to second element
list1.sort(key = sortSecond, reverse = True)
print('descending: ',list1)
