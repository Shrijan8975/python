data= input("Enter the string: ")

start= 0
end=  len(data)-1

while(start<end):
    if(data[start] == data[end]):
        start += 1
        end -= 1
    else:
        print(data, " is not palindrome")
        break
else:
    print(data,' is palindrome')