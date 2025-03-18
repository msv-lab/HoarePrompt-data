#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, and k is an integer representing the number of edges to be removed such that 1 <= k < n.
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
        
    #State: The loop has executed `t` times, processing `t` different trees. For each tree, `n` and `k` are read from the input, `adj` is constructed as an adjacency list representing the tree, and a binary search is performed to determine the maximum number of vertices that can remain connected after removing exactly `k` edges. The final value of `L` (which equals `R` after convergence) is printed for each tree.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a tree with `n` vertices and `k` edges to be removed. For each test case, it determines and prints the maximum number of vertices that can remain in a single connected component after removing exactly `k` edges.

