l=[] #syntax for list is []
l=[1,2,3,4]  #list can store any type of data.They need not to be of same type.
a = l[1]
for i in range(len(l)):
	if(l[i]>a and l[i]!=max(l)):
		a = l[i];

		print(a)



