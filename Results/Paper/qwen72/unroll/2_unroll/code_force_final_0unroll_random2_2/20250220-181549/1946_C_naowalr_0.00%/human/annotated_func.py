#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, (n, k) are pairs of integers read from input where 1 <= k < n <= 10^5, and adj is a list of lists representing the adjacency list of the tree with n vertices.
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
        
    #State: The loop has finished executing for all `t` test cases. For each test case, the variables `n`, `k`, and `adj` have been updated according to the input for that test case, and the final value of `L` for each test case has been printed. The variables `L`, `R`, and `numCuts` have been reset for each test case, and `leftover` is a temporary variable used within the `dfs` function. The initial state of `t` remains unchanged.
#Overall this is what the function does:The function `func_1` reads multiple test cases from the standard input, each defined by a tree with `n` vertices and a specific vertex `k`. For each test case, it constructs the adjacency list of the tree, performs a binary search to determine the maximum value `L` such that the number of cuts required to isolate a subtree of at least `L` vertices does not exceed `k`, and prints the result `L` for each test case. The function does not return any value; it only prints the results to the standard output. After processing all test cases, the function concludes, and the initial state of `t` remains unchanged.

