data = [43,23,78,89,3,23,6,66,58,40,79]

smax = 0
max= data[0]
for i in range(1, len(data)):
    if(max < data[i]):
        smax =  max
        max = data[i]
    elif(smax < data[i]):
        smax = data[i]

print(max,smax)