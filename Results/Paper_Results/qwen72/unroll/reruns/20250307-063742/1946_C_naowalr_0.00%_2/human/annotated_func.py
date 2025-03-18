#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, n and k are positive integers such that 1 <= k < n <= 10^5, and adj is a list of lists where each sublist represents the adjacency list of a vertex in the tree.
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
        
    #State: The loop iterates `t` times, and after each iteration, `n` and `k` are updated with new values from the input, `adj` is reset to a new list of lists representing the adjacency list of a new tree, `L` is set to 1, `R` is set to 100001, and `numCuts` is set to 0. After the loop finishes, the final value of `L` is printed for each iteration. The values of `t`, `n`, `k`, `adj`, `L`, `R`, and `numCuts` are not retained between iterations, and the loop ends when all `t` iterations are completed.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k`, and then reads `n-1` pairs of integers to construct an adjacency list `adj` representing a tree. It then performs a binary search to determine the maximum integer `L` such that the tree can be cut into at most `k` connected components, each having at least `L` vertices. The function prints the value of `L` for each test case. The function does not return any value, and the state of the program is reset for each test case, with `n`, `k`, `adj`, `L`, `R`, and `numCuts` being reinitialized. After all test cases are processed, the function concludes.

