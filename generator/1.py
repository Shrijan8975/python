import random

def genNum(n):
    num = []
    for i in range(n):
        num.append(random.randint(1,100))
    return num

result = genNum(5)
print(result)