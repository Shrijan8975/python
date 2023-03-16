def fact(x):
    f = 1
    for i in range(1,x+1):
        f = f *i
    return f

n= int(input("Enter n : "))
sum =0
for i in range(1, n+1):
    sum += fact(i)

print("Factorial : ",sum)
