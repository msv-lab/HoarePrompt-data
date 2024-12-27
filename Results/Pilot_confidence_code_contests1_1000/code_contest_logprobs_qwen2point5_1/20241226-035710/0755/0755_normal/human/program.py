import sys
l=list(map(int ,raw_input().split()))
n=l[0]
m=l[1]
a=b=c=d=0

k=0
i=1
while i<=m:
	if m>=2*n+1+a:
		sys.stdout.write(str(2*n+1+a)+" ")
		i+=1
		a+=2


	if m>=1+b:
		sys.stdout.write(str(1+b)+" ")
		i+=1
		b+=2

	if m>=2*n+2+c:
		sys.stdout.write(str(2*n+2+c)+" ")
		i+=1
		c+=2

	if m>=2+d:
		sys.stdout.write(str(2+d)+" ")
		d+=2
		i=i+1