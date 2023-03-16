data = [43,23,78,89,3,23,6,66,58,40,79]
max= data[0]
s_max=0
t_max =0

for i in range(1,len(data)):
	if (max<data[i]):
		t_max=s_max
		s_max=max
		max=data[i]
	elif(s_max<data[i]):
		t_max=s_max
		s_max=data[i]
	elif(t_max < data[i]):
		t_max=data[i]

print(max,s_max,t_max)