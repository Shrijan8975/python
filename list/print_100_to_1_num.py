for i in range(10,0,-1):
    x = i *10
    data = []
    for j in range(0,10):
        data.append(x-j)
        #print(x-j,end=" ")
    if( i%2 != 0):
        data.reverse()
    #print(data)

    for x in data:
        print(x, end= " ")
    print()