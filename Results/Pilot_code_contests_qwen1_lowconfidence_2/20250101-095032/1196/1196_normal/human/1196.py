(r,c)=map(int,raw_input().split())

if r==1 and c==1:
	print(0)
	
else:

	flag=False
	if c==1:
		flag=True
		(r,c)=(c,r)

	l=[[1 for _ in range(c)] for _ in range(r)]
	b=[i+1 for i in range(r+c)]

	for i in range(r):
		for j in range(c):
			l[i][j]*=b[i]*b[r+j]

	if flag==False:
		for i in range(r):
			s=""
			for j in range(c):
				s+=str(l[i][j])+" "

			print(s)

	else:
		for j in range(c):	
			s=""
			for i in range(r):
				s+=str(l[i][j])+" "

			print(s)
