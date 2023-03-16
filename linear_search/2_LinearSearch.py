def linearSearch(data,x):
    size = len(data)
    for i in range(0,size):
        if(x == data[i]):
            return i
    else:
        return -1

data = [34,45,6,45,67,33,78,98,56,44,32,1,9]
x = int(input("Enter search element : "))
index = linearSearch(data,x)
if(index == -1):
    print(x ," not found")
else:
    print(x," found at index ",index)