import math
n, a, b, c = [int(i) for i in raw_input().split()]
ans = 0

for i in range(0, a+1):
	for j in range(0, b+1):
		t = (n - 0.5*i - j)/2
		if t >= 0 and t <= c and t == math.floor(t):
			ans += 1

print(ans)