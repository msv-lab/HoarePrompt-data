import sys
input = sys.stdin.readline
from collections import deque

# Constants
MOD = 998244353

# Read number of test cases
t = int(input())

for _ in range(t):
    # Read number of intersections
    n = int(input())
    
    # Initialize adjacency list for the tree
    q = [[] for _ in range(n)]
    
    # Read the roads and build the tree
    for _ in range(n - 1):
        u, v = map(int, input().split())
        q[u - 1].append(v - 1)
        q[v - 1].append(u - 1)
    
    # Initialize arrays for DFS
    seen = [0] * n  # To track visited nodes
    pa = [-1] * n   # To track parent nodes
    dp = [0] * n    # DP array to store number of good sets for each subtree
    
    # Stack for iterative DFS
    ali = deque()
    ali.append((0, 1))  # Start DFS from node 0 with task 1 (pre-processing)
    seen[0] = 1  # Mark the root as seen
    ans = 1  # Initialize answer
    
    # Perform DFS
    while ali:
        v, task = ali.pop()
        if task == 0:
            # Post-processing task
            tot = 1
            for w in q[v]:
                if w != pa[v]:
                    tot *= (dp[w] + 1)
                    tot %= MOD
            dp[v] = tot
            for w in q[v]:
                if w != pa[v]:
                    ans += dp[w]
                    ans %= MOD
        else:
            # Pre-processing task
            ali.append((v, 0))  # Add post-processing task
            seen[v] = 1
            for w in q[v]:
                if seen[w] == 0:
                    ali.append((w, 1))  # Add pre-processing task for child
                    pa[w] = v  # Set parent of child
    
    # Add the DP value of the root to the answer
    ans += dp[0]
    
    # Output the result for the current test case
    print(ans % MOD)