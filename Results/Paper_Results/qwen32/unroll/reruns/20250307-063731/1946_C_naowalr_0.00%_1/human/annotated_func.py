#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed such that 1 <= k < n, adj is a list of lists representing the adjacency list of the tree, L and R are integers representing the lower and upper bounds for binary search (initially 1 and 100001, respectively), numCuts is an integer representing the number of cuts made during the DFS, and leftover is an integer representing the size of the remaining component after DFS.
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
        
    #State: `n`, `k`, `adj`, `L`, `R`, `numCuts`, `leftover`, `t` are as per the last iteration of the loop. Specifically, `n` and `k` are the values read from the last line of input, `adj` is the adjacency list constructed for the last tree, `L` is the final lower bound determined by the binary search in the last iteration, `R` is the final upper bound determined by the binary search in the last iteration, `numCuts` is the number of cuts made during the DFS in the last iteration, `leftover` is the size of the remaining component after DFS in the last iteration, and `t` is the total number of test cases which remains unchanged.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a tree represented by its number of vertices `n` and its adjacency list `adj`, and an integer `k` representing the number of edges to be removed. For each test case, it performs a binary search to determine the maximum possible size `L` of the remaining connected component after removing `k` edges. The function prints this value `L` for each test case.

