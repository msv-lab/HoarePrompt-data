n = int(input())
s = input()
dp = [0] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    dp[i] = i
    for j in range(i):
        if s[j:i] in s[:j]:
            dp[i] = min(dp[i], dp[j] + (i - j) // (i - j - j) + 1)
print(dp[n])
