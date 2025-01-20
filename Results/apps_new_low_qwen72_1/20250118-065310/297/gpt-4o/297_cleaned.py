def func_1(n, a, b, heights):
    dp = [[float('inf')] * (a + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for red_paint in range(a + 1):
            if red_paint >= heights[i - 1]:
                dp[i][red_paint] = min(dp[i][red_paint], dp[i - 1][red_paint - heights[i - 1]])
            green_paint = sum(heights[:i]) - red_paint
            if green_paint <= b:
                dp[i][red_paint] = min(dp[i][red_paint], dp[i - 1][red_paint] + (heights[i - 1] if i > 1 and dp[i - 1][red_paint] != float('inf') and (red_paint < a) else 0))
    result = float('inf')
    for red_paint in range(a + 1):
        if dp[n][red_paint] != float('inf'):
            result = min(result, dp[n][red_paint])
    return -1 if result == float('inf') else result
input = sys.stdin.read
data = input().split()
n = int(data[0])
a = int(data[1])
b = int(data[2])
heights = list(map(int, data[3:]))
print(func_1(n, a, b, heights))