n=int(input("enter no.:"))
org = n

rev=0
while(n>0):
    rev=(rev*10+n%10)
    n//=10
if(org==rev):
    print("this is palindrom number")
else:
    print("this is not palindrom number")
    