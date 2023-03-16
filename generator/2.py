import random

def genNum(n):
    for i in range(n):
        yield random.randint(1,100)


result = genNum(5)
print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
#print(next(result))

print("------------------------------------------------")
result = genNum(5)

for x in result:
    print(x)