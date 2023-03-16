import array
#Array is a collection of homogeneous elements
#i.e data type must be same

a1 = array.array('i',[1,2,3,4])
print(a1)


for x in a1:
    print(x)

print("Length =",len(a1))
a1.insert(0,10)  
print(a1)
a1.append(50)
print(a1)

#Remove element from specific index
print(a1.pop(0))
print(a1)
print(a1.pop())
print(a1)

#Remove element from end
print(a1.pop())


print("Index = ",a1.index(3))

