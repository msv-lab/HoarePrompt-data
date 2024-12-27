import sys

[n,p,w,d]=[int(i) for i in sys.stdin.readline().split()]

x=-1
y=-1
z=-1

done=0

for i in range(w):
	if((p-i*d)%w==0):
		j=(p-i*d)//w
		if(i+j<=n):
			x,y,z=j,i,n-j-i
			done=1
			break

if(done==1):
	print(str(x)+" "+str(y)+" "+str(z))
else:
	print(-1)