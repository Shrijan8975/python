#Functions with variable number of arguments

def sum(*p):
    sum = 0
    for i in p:
        sum += i
    return sum

print(sum(10,20))
print(sum(1,2,3))
print(sum(1,2,3,4,5,6,7))