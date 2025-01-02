while True:
	n,m=map(int,raw_input().split())
	if n==0:break
	a=raw_input().split()
	b=raw_input().split()
	out=0
	for i in range(21):out+=i*max(a.count(str(i)),b.count(str(i)))
	print(out)