def fibo(a,b,n,s):
    if(n==0):
        return s
    else:
        c= a+b
        #print(c, end=" ")
        #str() converts int to str
        s +=  str(c)+" "
        return fibo(b,c,n-1,s)

n= int(input("Enter number of terms: "))
a=1
b=0
print(fibo(a,b,n,''))