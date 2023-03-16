#Accept the string from user and print 
#the count of vowels, spaces, digits and consonents 
#in the given string

data = input("Enter the string: ")
v=0
c=0
d=0
s=0

for x in data:
    if(x in"aeiou"):
        v +=1
    elif(x.isdigit()): #elif(x in "0123456789"):
        d +=1
    elif(x.isspace()):
        s+=1
    else:
        c+=1
print("Count of Digits: ",d)
print("Count of Vowels: ",v)
print("Count of Spaces: ",s)
print("Count of Consonents: ",c)

