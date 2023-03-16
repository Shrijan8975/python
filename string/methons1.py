# Accept the string from user 
# and print the frequency of each charectar of the string. 

data = input("Enter the string: ")
char_set=set(data)

for x in char_set:
    print(x," is present ",data.count(x), " times")
