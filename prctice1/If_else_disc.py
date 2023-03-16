bill = float(input("Enter bill amount"))

if(bill >= 2000):
    bill -= (bill*0.3)
    # bill = bill - (bill *0.3)
else:
    bill -= (bill*0.05)
    # bill = bill - (bill *0.05)

print("Final bill amt :",bill)

