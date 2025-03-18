#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, n and k are positive integers such that 1 <= k < n <= 10^5, and adj is a list of lists representing the adjacency list of the tree with n vertices.
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
        
    #State: The loop has executed `t` times, and for each execution, `n`, `k`, and `adj` are the same as their initial values for that iteration. `L` is the largest integer such that the number of cuts `numCuts` required to make the leftover value less than `L` is less than or equal to `k`, and `R` is `L + 1`.
#Overall this is what the function does:The function `func_1` reads a series of test cases from the standard input. For each test case, it reads the number of vertices `n` and the maximum number of cuts `k`, constructs an adjacency list `adj` representing a tree with `n` vertices, and then performs a binary search to find the largest integer `L` such that the number of cuts required to make the leftover value less than `L` is less than or equal to `k`. The function prints this value `L` for each test case. After processing all test cases, the function terminates.

