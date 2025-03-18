import math
for _ in range(int(input())):
	(n, k) = map(int, input().split())
	a = list(map(int, input().split()))
	m = min(a)
	ans = 0
	if k >= n * m:
		ans = math.factorial(n)
	else:
		k -= n * m
		for i in range(n):
			a[i] = m + min(k, (m + k // n - a[i]))
			k -= min(k, (m + k // n - a[i]))
		ans = a[0]
		for i in range(1, n):
			ans *= a[i] - a[i - 1]
	print(ans)