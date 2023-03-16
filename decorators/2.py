def f2():
    print("Im f2 function")

def f3():
    print("Im f3 function")

def f1(t):
    t()
    result = f2
    return result

x= f3
data = f1(x)
data()