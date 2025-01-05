import operator
t=int(raw_input())
ls=[]
while(t>0):
	a=raw_input()
	ls.append(a)
	t=t-1


dict1={}


for x in ls:
	count=0
	for z in ls:
		if(x in z):
			count=count+1
	dict1[x]=count

sorted_x = sorted(dict1.items(), key=operator.itemgetter(1))

sorted_x.reverse()
c2=0
for item in sorted_x:
	if(item[1]==1):
		c2=c2+1

if(c2>1):
	print("NO")
else:
	print("YES")
	for x in sorted_x:
		c1=ls.count(x[0])
		for z in range(c1):
			print(x[0])
