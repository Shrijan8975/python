a = True
b = False
c = False

if(not a or b):
	print (1)
elif(not a or not b and c):
	print (2)
elif(not a or b or not b and a):
	print (3)
else:
	print (4)

'''
A) 1
B) 2
C) 3
D) 4
E) Error

'''