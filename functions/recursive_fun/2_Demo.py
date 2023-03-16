def sum_of_series(n):
    if( n== 0):
        return 0
    else:
        return n + sum_of_series(n-1)

n =  int(input("Enter number: "))
print("Sum of Series : ", sum_of_series(n))