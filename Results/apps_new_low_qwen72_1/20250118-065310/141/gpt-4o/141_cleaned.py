def func_1(n, m, antennas):
    dp = [float('inf')] * (m + 1)
    dp[0] = 0
    antennas.sort()
    for (x, s) in antennas:
        left = max(0, x - s)
        right = min(m, x + s)
        for j in range(left, right + 1):
            dp[j] = min(dp[j], dp[max(0, left - 1)])
        for j in range(right + 1, m + 1):
            dp[j] = min(dp[j], dp[max(0, j - 2 * x)] + (j - right))
    return dp[m] if dp[m] != float('inf') else -1
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
antennas = []
for i in range(n):
    x = int(data[2 + 2 * i])
    s = int(data[2 + 2 * i + 1])
    antennas.append((x, s))
print(func_1(n, m, antennas))