import sys
inp = lambda func=int: list(map(func, sys.stdin.readline().split()))
t = inp()[0]
for _ in range(t):
	n,m = inp()
	print("? 1 1")
	sys.stdout.flush()
	d1 = int(input())
	print("?",1,m)
	sys.stdout.flush()
	d2 = int(input())
	y = d1+d2-m+1
	y2 = y//2
	if (y%2==0 and y2 >= 0 and y2<=n-1):
		print("?",y2+1,d1-y2+1)
		sys.stdout.flush()
		d3 = int(input())
		if d3==0:
			print("!",y2+1,d1-y2+1)
			sys.stdout.flush()
			continue
	print("?",n,1)
	sys.stdout.flush()
	d4 = int(input())
	y = d1+d4-n+1
	y2 = y//2
	print("!",d1-y2+1,y2+1)
	sys.stdout.flush()
