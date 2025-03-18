#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, n and k are positive integers such that 1 <= k < n <= 10^5, and adj is a list of lists where each inner list contains integers representing the adjacent vertices of the corresponding vertex.
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
        
    #State: The loop iterates `t` times, and for each iteration, it reads `n` and `k` from the standard input, constructs the adjacency list `adj`, and performs a binary search to find the maximum value `L` such that the number of cuts `numCuts` is greater than or equal to `k` or `numCuts` equals `k` and the leftover value is greater than or equal to `x`. After all iterations, the final value of `L` is printed for each iteration. The variables `t`, `n`, `k`, and `adj` are reset for each iteration, and the final output is the sequence of `L` values for each test case.
#Overall this is what the function does:The function reads a series of test cases from the standard input. For each test case, it reads the number of vertices `n` and the number of cuts `k`, constructs an adjacency list `adj` representing a tree, and performs a binary search to determine the maximum value `L` such that the number of cuts required to achieve a certain condition is greater than or equal to `k` or exactly `k` with a leftover value meeting a specific threshold. The function prints the value of `L` for each test case. The variables `t`, `n`, `k`, and `adj` are reset for each test case, and the final state of the program is the sequence of printed `L` values corresponding to each test case.

