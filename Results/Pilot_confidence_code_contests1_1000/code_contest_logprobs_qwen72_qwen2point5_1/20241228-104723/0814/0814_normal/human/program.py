n, k = map(int, raw_input().split())
a = map(int, raw_input().split())

a.sort()

cnt_from = [0] * n
for i in range(n):
	while (i+cnt_from[i] < n) and (a[i+cnt_from[i]] - a[i] <= 5):
		cnt_from[i] += 1

dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(n):
	for j in range(k+1):
		dp[i+1][j] = max(dp[i+1][j], dp[i][j])
		if j+1 <= k:
			dp[i+cnt_from[i]][j+1] = max(dp[i+cnt_from[i]][j+1], dp[i][j] + cnt_from[i])
print(dp[n][k])