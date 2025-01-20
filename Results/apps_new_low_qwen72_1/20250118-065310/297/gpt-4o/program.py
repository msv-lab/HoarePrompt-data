def min_unattractiveness(n, a, b, heights):
    # Create a DP table to store the minimum unattractiveness value for each board
    dp = [[float('inf')] * (a + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    # Iterate over each board
    for i in range(1, n + 1):
        for red_paint in range(a + 1):
            # If we can paint the current board red
            if red_paint >= heights[i - 1]:
                dp[i][red_paint] = min(dp[i][red_paint], dp[i - 1][red_paint - heights[i - 1]])
            
            # If we can paint the current board green
            green_paint = sum(heights[:i]) - red_paint
            if green_paint <= b:
                dp[i][red_paint] = min(dp[i][red_paint], dp[i - 1][red_paint] + (heights[i - 1] if i > 1 and dp[i - 1][red_paint] != float('inf') and red_paint < a else 0))
    
    # Find the minimum unattractiveness value
    result = float('inf')
    for red_paint in range(a + 1):
        if dp[n][red_paint] != float('inf'):
            result = min(result, dp[n][red_paint])
    
    return -1 if result == float('inf') else result

import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
a = int(data[1])
b = int(data[2])
heights = list(map(int, data[3:]))

print(min_unattractiveness(n, a, b, heights))
