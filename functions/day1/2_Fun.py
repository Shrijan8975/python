#Funtion type: With input, No output
def displayName(x):
    name = input("Enter name: ")
    for i in range(1,x+1):
        print("Hello, ",name)


x = int(input("How many time u wanna print the name ?? "))
displayName(x)