#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, and k is an integer representing the number of edges to be removed such that 1 <= k < n <= 10^5.
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
        
    #State: The variables `n`, `k`, `adj`, `L`, `R`, `numCuts` will reflect the state of the last iteration of the loop, but the specific values depend on the input provided for that iteration. The value of `t` remains unchanged.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a tree with `n` vertices and `k` edges to be removed. It calculates and prints the minimum number of connected components that can be formed in the tree after removing exactly `k` edges.

