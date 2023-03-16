def rev(n,r):
    if(n==0):
        return r
    else:
         r = r*10 + n%10
         n //=10
         return rev(n,r)

n = int(input("Enter number: "))
result = rev(n,0)
print("Reverse is: ",result)