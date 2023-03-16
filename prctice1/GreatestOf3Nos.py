x= int(input("Enter 1st no."))
y= int(input("Enter 2nd no."))
z= int(input("Enter 3rd no."))

if(x>y):
    if(x>z):
        print(x," Greater")
    else:
        print(z," Greater")
else:
    if(y>z):
        print(y," Greater")
    else:
        print(z," Greater")