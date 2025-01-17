for _ in range(int(input())):
	n,b,x=map(int,input().split())
	l=list(map(int,input().split()))
	l.sort()
	prefix=[0]
	for i in l:
		prefix.append(prefix[-1]+b*i*(i-1)//2)
	m=l[-1]
	ans=[-(i-1)*x for i in range(m+1)]
	for i in range(1,m+1):
		j=n-1
		while j>=0 and l[j]>i:
			y=l[j]%(i)
			z=l[j]//(i)
			ans[i]+=b*(z*z*(i)*(i-1)//2+y*(i-1)*z+y*(y-1)//2)
			j-=1
		ans[i]+=prefix[j+1]
 
	print(max(ans[1:]))