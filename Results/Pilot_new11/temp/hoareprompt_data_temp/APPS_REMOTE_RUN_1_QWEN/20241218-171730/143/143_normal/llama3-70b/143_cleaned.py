(n, L) = map(int, input().split())
costs = list(map(int, input().split()))
dp = [float('inf')] * (L + 1)
dp[0] = 0
for i in range(1, L + 1):
    for j in range(n):
        vol = 2 ** j - 1
        if vol <= i:
            dp[i] = min(dp[i], dp[i - vol] + costs[j])
print(dp[L] if dp[L] != float('inf') else -1)