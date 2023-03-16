data = []
choice =0

while(choice !=8):
    print('''
    1. Add elemement at the end
    2. Display list
    3. Add element at specific position
    4. Add new list to existing list
    5. Remove Last element
    6. Remove specific element
    7. Remove element from specific (position)index:
    8.Exit
    ''')
    choice =  int(input("Enter your choice: "))
    if(choice == 1):
        ele= int(input("Enter element to add: "))
        data.append(ele)
    elif(choice == 2):
        print(data)
    elif(choice == 3):
        ele= int(input("Enter element to add: "))
        index= int(input("Enter index: "))
        data.insert(index,ele)
    elif(choice == 4):
        newList= [1,2,3]
        data.extend(newList)
    elif(choice == 5 ):
        removedEle = data.pop()
        print("Removed element: ",removedEle)
    elif(choice == 6):
        ele= int(input("Enter element to be removed: "))
        data.remove(ele)
    elif(choice == 7):
        index= int(input("Enter index: "))
        data.pop(index)
        