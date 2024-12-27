n=int(raw_input())
x=raw_input().split(" ")
for i in xrange(len(x)):
	x[i]=int(x[i])
x.sort()
solved=False
while True:
	#print x
	x.sort()
	for j in xrange(n-1):
		if x[j+1] > x[j]:
			x[j+1]=x[j+1]-x[j]
	solved=True
	for j in xrange(n-1):
		if x[j+1]!=x[j]:
			solved=False
			break
	if solved: break
	#print x
print (x[0]*n)
