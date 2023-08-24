import math

d, k = map(int, input().split())
red_values = []
for _ in range(d):
    r, p = map(int, input().split())
    red_values.append((r, p))

# Dynamic programming approach
# dp[i] represents the minimum sum of squared errors for i allowed red values
dp = [math.inf] * (k + 1)
dp[0] = 0

for i in range(1, k + 1):
    for j in range(i):
        for r, p in red_values:
            dp[i] = min(dp[i], dp[j] + p * (r - red_values[i-1][0]) ** 2)
        
if k >= d:
    dp[d] = 0
        
print(dp[k])