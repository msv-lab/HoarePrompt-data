for _ in range(int(input())):
	n,m = map(int,input().split())
	arr = (list(map(int,input().split())))
	s = (input())			
	l = 0
	r = n - 1
	for k in s:
		if k == 'L':
			l+=1
		else:
			r-=1
	p = 1
	ans = []
	# print(" ", l, r)
	for strr in s[::-1]:
		if strr == 'R':
			r+=1
			p = (p * arr[r])%m
		else:
			l-=1
			p = (p * arr[l])%m
 
		# print(l+1,r-1)	
		ans.append(p)
	print(*ans[::-1])