#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed such that 1 <= k < n. adj is a list of lists where adj[i] contains the vertices adjacent to vertex i in the tree.
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
        
    #State: `n` is an integer representing the number of vertices in the tree from the last iteration, `k` is an integer representing the number of edges to be removed from the last iteration, `adj` is a list of lists representing the adjacency list of the tree from the last iteration, `t` is the number of iterations which is unchanged.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a tree defined by the number of vertices `n`, the number of edges to be removed `k`, and the adjacency list `adj`. For each test case, it calculates and prints the maximum number of vertices that can remain in the largest connected component after removing exactly `k` edges from the tree.

