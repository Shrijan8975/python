def testFunc(x):
	return x % 5

mylist = [15, 3, 11, 7]

print("Normamylist sort :", sorted(mylist))
print("Sorted with key:", sorted(mylist, key=testFunc))
