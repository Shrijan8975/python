k=7
for i in range(1,6):
    ch = 65
    for j in range(1,i+1):
        print(chr(ch),end = " ")
        ch +=1

    for j in range(1, k+1):
        print(" ",end=" ")
    k -= 2

    ch -=1
    for j in range(1,i+1):
        if(i==5 and j == 1):
            print("",end="")
        else:
            print(chr(ch),end = " ")
        ch -=1
    print()

