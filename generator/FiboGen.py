def fibo(limit):
    
    cnt =0
    a, b =  1, 0
    while(cnt < limit):
        yield a+b
        a, b = b, a + b
        cnt +=1


x = fibo(5)

print(next(x), end=" ")
print(next(x), end=" ")
print(next(x), end=" ")
print(next(x), end=" ")
print(next(x), end=" ")


print("\n---------------------------------------")
for i in fibo(5):
	print(i, end=" ")
