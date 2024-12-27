def f(n):
	return n * (n + 1) / 2

t = int(raw_input())
for i in xrange(t):
	n, m = map(int, (raw_input().split(" ")))
	
	if m == 0:
		print(0)
		continue

	md = (n - m) % (m + 1)
	d = (n - m) / (m + 1)
	print(f(n) - md * f(d + 1) - (m + 1 - md) * f(d))

