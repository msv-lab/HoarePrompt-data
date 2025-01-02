n=input()
a=[int(x) for x in raw_input().split()]
b=[1]
c=[]
for i in range(2,n):
	if a[i]!=a[i-1]+a[i-2]:
		b.append(i)
b.append(n)		
for i in range(1,len(b)):
	c.append(b[i]-b[i-1]+1)
if n==1:
	print('1')
elif n==2:
	print('2')
elif len(c)==0:
	print(n)	
else:
	print(max(c))			

