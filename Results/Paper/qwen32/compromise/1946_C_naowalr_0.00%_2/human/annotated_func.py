#State of the program right berfore the function call: adj is a list of lists representing the adjacency list of a tree with n vertices, where each inner list contains the vertices adjacent to the vertex corresponding to its index. n is an integer representing the number of vertices in the tree, and k is an integer representing the number of edges to be removed such that 1 <= k < n.
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
        
    #State: `adj` is a list of `n + 1` lists where each list at index `a` includes all nodes `b` that are directly connected to `a` as per the input; `n` is at least 2; `k` is the second integer read from input; `t` is an integer greater than 0; `L` and `R` are consecutive integers; `x` is the last calculated midpoint; `leftover` is the value returned by `dfs(1, 1)`; `z` is equal to `t`; `i` is -1; `numCuts` is 0.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a tree represented by an adjacency list and an integer `k`. For each test case, it calculates and prints the maximum possible size of the smallest connected component after removing exactly `k` edges from the tree.

