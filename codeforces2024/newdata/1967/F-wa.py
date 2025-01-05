import sys
input = sys.stdin.read
from collections import deque

def solve():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Initialize pre and nxt arrays
        pre = [-10**100] * n
        nxt = [10**100] * n
        
        # Stack to calculate pre array
        stack = []
        for i in range(n):
            while stack and p[stack[-1]] < p[i]:
                stack.pop()
            if stack:
                pre[i] = stack[-1]
            stack.append(i)
        
        # Stack to calculate nxt array
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and p[stack[-1]] < p[i]:
                stack.pop()
            if stack:
                nxt[i] = stack[-1]
            stack.append(i)
        
        # Precompute the sum of min(nxt(i) - pre(i), x) for all x from 1 to q
        min_diff = [0] * n
        for i in range(n):
            min_diff[i] = nxt[i] - pre[i]
        
        # Precompute the prefix sums for all q
        prefix_sums = [[0] * (n + 1) for _ in range(n)]
        for q in range(1, n + 1):
            for i in range(q):
                prefix_sums[q - 1][i + 1] = prefix_sums[q - 1][i] + min(min_diff[i], q)
        
        # Process the queries
        q = 1
        while q <= n:
            k = int(data[idx])
            idx += 1
            queries = list(map(int, data[idx:idx + k]))
            idx += k
            
            for x in queries:
                results.append(str(prefix_sums[q - 1][x]))
            q += 1
    
    sys.stdout.write("\n".join(results) + "\n")

# Call the solve function
solve()