'''
Default argument goes from right to left.
    -   Should not start from left
    -   Should start from right always
    -   Should be in continuation
'''
def sum(x=0,y=0,z=0):
    return x+y+z

z= sum(1,2,3)
#print(z)

z = sum(1,2)
print(z)

z = sum(1)
print(z)

z = sum(0,12,0)
print(z)

