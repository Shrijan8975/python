data = [4,5,7,9,12,15,13]

'''
cube = lambda x: x*x*x

for  y in data:
    print(cube(y), end= " ")

print()
final = list(map(cube, data))
print(final)

'''

final = list(map(lambda x: x*x*x, data))
print(final)
