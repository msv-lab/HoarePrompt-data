s=raw_input()
z=list(s)
min=[]
max=[]
final=[]
for i in range(len(z)):
	if z[i]=='(':
		min.append(i)
for i in range(len(z)-1,-1,-1):		
	if z[i]==')':
		max.append(i)
if len(max)>=len(min):
	c=len(min)
else:
	c=len(max)			
for i in range(c):
	if min[i]<max[i]:
		final.append(min[i])
		final.append(max[i])
final=sorted(final)
if len(final)==0:
	print('0')
else:	
	print('1')
	print(len(final))
	for i in range(len(final)):
		print(final[i]+1),		

