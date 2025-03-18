#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, n and k are positive integers such that 1 ≤ k < n ≤ 10^5, and a, b are positive integers such that 1 ≤ a, b ≤ n.
def func_1():
    t = int(sys.stdin.readline())
    for z in range(t):
        n, k = list(map(int, sys.stdin.readline().split()))
        
        adj = [[] for i in range(n + 1)]
        
        for i in range(n - 1):
            a, b = list(map(int, sys.stdin.readline().split()))
            adj[a].append(b)
            adj[b].append(a)
        
        L = 1
        
        R = int(100000.0 + 1)
        
        numCuts = 0
        
        while R - L > 1:
            x = (L + R) // 2
            numCuts = 0
            leftover = dfs(1, 1)
            if numCuts > k or numCuts == k and leftover >= x:
                L = x
            else:
                R = x
        
        print(L)
        
    #State: After the loop executes all the iterations, the variable `z` is equal to `t - 1`, indicating that the loop has completed all its iterations. The variables `n`, `k`, `a`, `b`, and `i` retain their last values from the final iteration. The adjacency list `adj` is fully populated with the connections between nodes based on the input pairs. The variables `L` and `R` are such that `R = L + 1`, and `L` is the largest integer satisfying the condition `numCuts > k or (numCuts == k and leftover >= x)`. The variable `numCuts` is reset to 0 for each iteration of the outer loop.
#Overall this is what the function does:The function reads a series of inputs from standard input and processes them to determine a specific value `L` for each test case. It accepts no explicit parameters but relies on input from `sys.stdin`. For each test case defined by the integer `t`, it reads pairs of integers `n` and `k`, followed by `n-1` pairs of integers `a` and `b` which represent edges in a graph. The function constructs an adjacency list for the graph and uses a binary search approach to find the maximum value of `L` that satisfies certain conditions related to the number of cuts (`numCuts`) and a leftover value from a depth-first search (DFS) operation. The function prints the value of `L` for each test case. After processing all test cases, the function completes, and the final state includes the printed results for each test case.

