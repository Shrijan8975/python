print('''
1. Summation
2. Check if number is even  or odd
3. Area of circle
4. Greater of 2 no.s
5. Exit
''')

ch = int(input("Enter your choice : "))
if(ch == 1):
    print("summation")
elif(ch == 2):
    print("Even or odd")
elif(ch ==3):
    print("Area of circle")
elif(ch == 4):    
    print("Greater")
elif(ch == 5):
    print("Thank you! Tata bye bye...")
else:
    print("Invalid input")