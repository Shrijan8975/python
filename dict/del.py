dict1 = {101:"Kajol", 102:"Priyal", 1001:"Amol", 1002:"Shital"}

dict2 = dict1.copy()
dict3 = dict1
print(dict1)
print(dict2)
print(dict3)
print("---------------------------------------")
dict3[1001] ="Rajesh"
dict1[1002]="Ankita"
print("---------------------------------------")
print(dict1)
print(dict2)
print(dict3)

dict3.clear()
print("---------------------------------------")
print(dict1)
print(dict2)
print(dict3)

'''
#print(dict1[10001])

print(dict1)
del dict1
print(dict1)

print(dict1)
del dict1[1001]
print(dict1)

print(dict1.get(10001,"Not Found"))

dict1.clear()
print(dict1)

'''