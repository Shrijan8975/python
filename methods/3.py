data = [10,20,30,40,40]

n_data = [x*2 for x in data]
c_data = {x**3 for x in data}
d_data = {x:x**3 for x in data}
print(n_data)
print(c_data)
print(d_data)