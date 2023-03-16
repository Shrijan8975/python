
import math
def getFare(source,destination):
    Path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
    BusStops = [ "TH", "GA", "IC", "HA", "TE", "LU", "NI","CA" ]
    start = BusStops.index(source)
    stop = BusStops.index(destination)
    print("Start : ",start, "Stop : ",stop)
    start += 1
    stop +=1
    dist = 0
    if(start == stop):
        print("Invalid Input")
        return
    elif(start <  stop):
        for i in range(start,stop):
            dist += Path[i]
    else:
        while(start != stop):
            if(start == len(Path)):
                start = 0
            print(">>>",Path[start])
            dist += Path[start]
            start +=1

    print("Dist :",dist)
    fare = dist/1000 * 5
    print( "Final fare: ",fare, ": : ",math.ceil(fare))


source = input("Enter the source")
destination = input("Enter the destination")
getFare(source,destination)
