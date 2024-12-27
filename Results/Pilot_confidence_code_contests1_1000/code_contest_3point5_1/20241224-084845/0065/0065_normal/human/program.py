def fun(a,w):
	su1=0
	for x in a:
		su1+=w[x-1]
	return su1

n,m=map(int,raw_input().split())
w=map(int,raw_input().split())
b=map(int,raw_input().split())
a=[1014]*n
curr=0
prev=0
for i in xrange(m):
	if a[b[i]-1]==501:
	     prev=fun(list(set(b[:i])),w) 
	else:
	    prev=fun(list(set(b[a[b[i]-1]+1:i])),w)
	a[b[i]-1]=i
	curr+=prev
print(curr)
