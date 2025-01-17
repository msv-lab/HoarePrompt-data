import sys
from collections import deque

def solve():
    # Read the dimensions and constraints for the current test case
    n, m, k, d = map(int, input().split())
    # Read the river grid depths
    river = [list(map(int, input().split())) for _ in range(n)]
    
    # Array to store the minimum cost for each row
    ans = [0] * n
    
    # Calculate the minimum cost for each row
    for i in range(n):
        # Initialize the dp array for the current row
        dp = [0] * m
        dp[0] = 1  # Cost at the first column is always 1
        q = deque([0])  # Deque to maintain indices for minimum cost calculation
        
        # Calculate dp values for the current row
        for j in range(1, m):
            # Remove indices from the deque that are out of the allowed distance range
            while abs(q[0] - j) - 1 > d:
                q.popleft()
            # Calculate the cost to reach column j
            dp[j] = dp[q[0]] + river[i][j] + 1
            # Maintain the deque to ensure the front has the minimum dp value
            while q and dp[q[-1]] >= dp[j]:
                q.pop()
            q.append(j)
        
        # Store the minimum cost to reach the last column of the current row
        ans[i] = dp[m - 1]
    
    # Calculate the minimum total cost for k consecutive rows
    s = sum(ans[:k])  # Initial sum for the first k rows
    fans = s  # Initialize the minimum total cost
    for i in range(k, n):
        # Update the sum by sliding the window
        s -= ans[i - k]
        s += ans[i]
        # Update the minimum total cost
        fans = min(fans, s)
    
    # Output the minimum total cost for the current test case
    print(fans)

if __name__ == "__main__":
    # Read the number of test cases
    t = int(input())
    for _ in range(t):
        solve()