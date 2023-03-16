import functools
data = [1,2,3,4,5]
sum = functools.reduce((lambda x, y: x + y), data)
print (sum)


sum = functools.reduce((lambda x, y: x - y), data)
print (sum)

sum = functools.reduce((lambda x, y: x * y), data)
print (sum)
