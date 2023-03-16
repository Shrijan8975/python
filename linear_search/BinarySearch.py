def binarySearch(data,x):
    beg = 0
    end = len(data) - 1
    while(beg <= end):
        mid =  (beg + end) //2
        if(x == data[mid]):
            return mid
        elif(x > data[mid]):
            beg= mid +1
        else:
            end = mid -1
    else:
        return -1

data = [3,12,15,45,67,69,78,81,87,98,99]

x =  int(input("Enter number to search : "))
index =  binarySearch(data,x)
#print(index)
if(index == -1):
    print(x, " not found")
else:
    print(x," found at ",index , " index")