n = int(input("Enter value of n: "))

a,b= 1,0

for i in range(1, n+1):
    c = a+b
    print(c, end= " ")
    a=b
    b=c