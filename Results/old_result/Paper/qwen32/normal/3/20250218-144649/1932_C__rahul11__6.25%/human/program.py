MOD = 10**9 + 6
for _ in range(int(input())):
	n,m = map(int,input().split())
	arr = (list(map(int,input().split())))
	s = list(input())
	res = [0]*(n)
	ans = 1
	for i in arr:
		ans*=i
	res[0] = (ans % m) % MOD
	# print(res, ans)
	c = 1	
	l = 0
	r = n-1
	for k in range(n-1):
		if s[k] == 'L':
			ans = (((ans // arr[l]))) % MOD
			res[c] = (ans % m) % MOD
 
			l+=1
		else:
			ans = (((ans // arr[r]))) % MOD
			res[c] = (ans % m) % MOD
			r-=1
		c+=1
		# print(res,c, ans)
	print(*res)