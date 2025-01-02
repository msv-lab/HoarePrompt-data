(n, m) = map(int, raw_input().split(' '))
dp = [0 for i in range(0, n + 1)]
dp[0] = 1
for i in range(0, m):
    a = int(raw_input())
    dp[a] = -1
for step in range(1, n + 1):
    if dp[step] < 0:
        continue
    ans = 0
    for prev in [1, 2]:
        if step - prev >= 0 and dp[step - prev] >= 0:
            ans += dp[step - prev]
    dp[step] = ans
print(dp[n] % 1000000007)