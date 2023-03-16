data = [5,4,3,2,1]

n =  len(data)
for i in range(n):
    if(data[i] > data[i+1]):
        data[i],data[i+1] = data[i+1],data[i]
print(data)