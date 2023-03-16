def fact(x):
    f = 1
    for i in range(1,x+1):
        f = f *i
    return f

def sum(x,y):
    z= x+y
    return z

def greater(x,y):
    if(x>y):
        return x
    else:
        return y

x = int(input("Enter a number : "))
y = int(input("Enter a number : "))

result = fact(x)
print("Result:  ",result)

result = greater(x,y)
print("Greater is :", result)

result = sum(x,y)
print("Sum : ",result)