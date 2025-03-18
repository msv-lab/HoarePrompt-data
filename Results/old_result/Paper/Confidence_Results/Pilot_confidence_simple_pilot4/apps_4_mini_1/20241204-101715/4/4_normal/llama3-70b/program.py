n, q = map(int, input().split())
painters = [list(map(int, input().split())) for _ in range(q)]

painters.sort(key=lambda x: x[1])

dp = [0] * (n + 1)
for l, r in painters:
    dp[l] += 1
    dp[r + 1] -= 1

for i in range(1, n + 1):
    dp[i] += dp[i - 1]

ans = 0
for i in range(1, n + 1):
    if dp[i] > 2:
        ans += 1

print(ans)
