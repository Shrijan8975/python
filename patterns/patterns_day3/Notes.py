total_notes = 0
amt=int(input("Enter the amount:"))

notes =amt//2000 
amt%=2000
print("Total 2000 Notes=", notes)
total_notes +=notes

notes=amt//500
amt%=500
print("Total 500 Notes=", notes)
total_notes +=notes

notes=amt//200
amt%=200
print("Total 200 Notes=", notes)
total_notes +=notes

notes=amt//100
amt%=100
print("Total 100 Notes=", notes)
total_notes +=notes

notes=amt//50
amt%=50
print("Total 50 Notes=", notes)
total_notes +=notes

notes=amt//20
amt%=20
print("Total 20 Notes=", notes)
total_notes +=notes

notes=amt//10
amt%=10
print("Total 10 Notes=", notes)
total_notes +=notes

print("Coins of 1 : ",amt)

print("Total Notes=", total_notes)