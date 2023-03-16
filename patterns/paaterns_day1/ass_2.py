import random
userid = input("Enter user name")
pws = input("Enter password")

if(userid == "firstbit" and pws == "firstbit"):
    #print("Success")
    x = random.randint(1000,9999)
    print(x)
    y = int(input("Enter the captch shown"))
    if(x==y):
        print("Login successful")
    else:
        print("Please try again")
else:
    print("Invalid Credentials")