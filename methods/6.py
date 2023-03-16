d1 = [("Lupin", 2020), ("Atypical",2022), ("Money Heist",2022)
,("Kota Factory", 2022), ("Queens Gambit",2019)
,("Our Planet", 2019)
,("Kung-fu-panda",2017)]

n_data =[x for x,y in d1 if(x.lower().startswith("k"))]

print(n_data)
n_data =[x for x,y in d1 if(x.lower().startswith("k") and y >2020)]

print(n_data)