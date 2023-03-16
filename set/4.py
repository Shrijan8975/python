A = {10,20,30,40}
B = {30,40,50,60}

result = A.union(B)
print(A)
print(B)
print("Union:",result)

result = A | B #union
print("Union: ",result)

result = A.intersection(B)
print("Intersection:", result)

result = A & B
print("Intersection:", result)

result = A.difference(B)
print("Difference:", result)

result = B - A
print("Difference:", result)

result = A ^ B
print("Symmetric difference: ",result)


result = A.symmetric_difference(B)
print("Symmetric difference: ",result)


x= A.copy()
print(x)
y=x
x.add(77)
print(y)

'''
A.symmetric_difference_update(B)
print("Symmetric difference: ",A)

A.intersection_update(B)
print(A)
'''