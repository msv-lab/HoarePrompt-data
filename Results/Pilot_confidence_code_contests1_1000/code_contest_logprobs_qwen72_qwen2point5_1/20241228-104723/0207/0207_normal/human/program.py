#N = int(raw_input())
N = 1422
bitlen = len(bin(N))-2
MOD = 10**9 + 7
dp = [[0 for i in range(N+1)] for j in range(bitlen + 1)]
dp[bitlen][0] = 1
for i in range(bitlen, 0, -1):
	for j in range(N+1):
		if dp[i][j] > 0:
			test = 1 << (i-1)
			dp[i-1][j] += dp[i][j]
			if j+test <= N:
				dp[i-1][j+test] += dp[i][j]
				if j+2*test <= N:
					dp[i-1][j+2*test] += dp[i][j]
print(sum(dp[0]) % MOD)
