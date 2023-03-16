data = {101:"Kajol", 102:"Priyal", 1001:"Amol", 1002:"Shital"}
choice = 0

while(choice != 10):
    print('''
        1. Add item
        2. Search for an Item based on the key
        3. Edit item
        4. Remove last item
        5. Remove the item based on the key
        6. Display
        ''')

    choice = int(input("Enter the choice: "))
    if(choice == 6):
        print(data)
    elif(choice == 1):
        key = int(input("Enter a key: "))
        val = input("Enter a value: ")
        data[key] = val
    elif(choice == 4):
        print(data.popitem(), "is removed")
    elif(choice == 4):
        print(data.popitem(), "is removed")
    elif(choice == 5):
        key = int(input("Enter a key: "))
        print(data.pop(key), "is removed")
    elif(choice == 2):
        key = int(input("Enter a key: "))
        print(data.get(key,"Not Present"))
    elif(choice == 3):
        key = int(input("Enter a key: "))
        val = input("Enter a value: ")
        data[key] = val
    