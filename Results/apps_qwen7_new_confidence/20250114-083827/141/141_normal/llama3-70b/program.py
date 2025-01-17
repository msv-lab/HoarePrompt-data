n, m = map(int, input().split())
antennas = []
for _ in range(n):
    x, s = map(int, input().split())
    antennas.append((x, s))
antennas.sort()

dp = [float('inf')] * (m + 1)
dp[0] = 0
for x, s in antennas:
    for i in range(m, x - s - 1, -1):
        dp[i] = min(dp[i], dp[max(0, i - x - s)] + (i - x + s))
print(dp[m])
