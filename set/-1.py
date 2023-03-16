data = {10,20,30}

data.add(30)

t= (11,22,33,10)
data.update(t)
print(data)

t= [1,2,3,1]
data.update(t)
print(data)

t= {101,201,301,101}
data.update(t)
print(data)

data.remove(30)
print(data)

print(data.pop(), "is removed")
print(data)

print(data.discard(22))
print(data)

data.clear()
print(data)

del data
print(data)