def fibo(a,b,n):
    if(n==0):
        return
    else:
        c= a+b
        print(c, end=" ")
        fibo(b,c,n-1)

n= int(input("Enter number of terms: "))
a=1
b=0
fibo(a,b,n)