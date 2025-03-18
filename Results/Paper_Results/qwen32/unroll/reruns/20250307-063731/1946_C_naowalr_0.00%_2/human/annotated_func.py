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
        
    #State: `n` and `k` hold the values from the last iteration, `adj` is the adjacency list for the last tree, `L` is the largest possible size of a connected component after removing `k` edges in the last iteration, `R` is the upper bound from the binary search in the last iteration, `numCuts` is the number of cuts from the last iteration, and `leftover` is the size of the largest connected component from the last iteration.
#Overall this is what the function does:The function reads multiple test cases from the standard input, where each test case consists of a tree with `n` vertices and the task is to determine the largest possible size of a connected component after removing exactly `k` edges from the tree. The function outputs this largest size for each test case.

