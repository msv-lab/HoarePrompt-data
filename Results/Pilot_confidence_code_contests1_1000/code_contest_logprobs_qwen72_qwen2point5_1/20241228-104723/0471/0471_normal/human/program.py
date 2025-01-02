n = input()
a = list(map(int, raw_input().split()))
a = [0] + a
ans = 0
for i in range(1, n + 1):
	ans += 1 + (a[i] - 1) * i
print(ans)
