from sys import stdin, stdout
ti = lambda : stdin.readline().strip()
ma = lambda fxn, ti : map(fxn, ti.split())
ol = lambda arr : stdout.write(' '.join(str(i) for i in arr) + '\n')
os = lambda i : stdout.write(str(i) + '\n')
olws = lambda arr : stdout.write(''.join(str(i) for i in arr) + '\n')
import math


n, m = ma(int, ti())
a = ma(int, ti())

remaining = m
ans = []
for i in range(n):
	if remaining > a[i]:
		ans.append(0)
		remaining -= a[i]
	elif remaining == a[i]:
		ans.append(1)
		remaining = m
	else:
		temp = 0
		a[i] -= remaining
		temp = 1
		temp += int(math.floor(a[i]/m))
		remaining = m - a[i]%m
		ans.append(temp)

ol(ans)