dict1 = {101:"Kajol", 102:"Priyal", 1001:"Amol", 1002:"Shital"}

for x in dict1:
    print(x)

print("--------------------------------------------")

for x in dict1.keys():
    print(x ," : : ",dict1[x])

print("--------------------------------------------")

for x in dict1.values():
    print(x)

print("--------------------------------------------")

for x,y in dict1.items():
    print(x ," = ",y)