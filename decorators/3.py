def myDecor(func):
    def wrapper():
        print("Plz login")
        func()
        print("Thank you")
    return wrapper

@myDecor
def f1():
    print("Im f1 function")

@myDecor
def f2():
    print("Im f2 function")

def f3():
    print("Im f3 function")

f1()
f2()