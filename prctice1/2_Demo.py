x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
op = input("Enter your choice(+,-,/,*): ")
result = 0

if(op == '+'):
    result = x + y 
elif(op == '-'):
    result = x - y 
elif(op == '/'):
    result = x / y 
elif(op == '*'):
    result = x * y 
else:
    print("Jao..pehle english sikh ke aao n then choose correct option...")

print("Result : ",result) 
