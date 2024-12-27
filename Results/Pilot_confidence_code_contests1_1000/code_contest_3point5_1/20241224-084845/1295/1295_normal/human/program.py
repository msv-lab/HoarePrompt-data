n= int(raw_input())

l= map(int, raw_input().split())

l.sort()

x= [0 for i in xrange(0, len(l))]

ctr=0

for i in xrange(0, len(l)):
	x[ctr]=l[i]
	ctr+=2
	if ctr>=len(l) and ctr%2==0:
		ctr=1

for i in xrange(0, len(x)) :
	print (x[i])