#State of the program right berfore the function call: adj is a list of lists representing the adjacency list of a tree with n vertices, n is an integer representing the number of vertices in the tree, and k is an integer representing the number of edges to be removed such that 1 <= k < n.
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
        
    #State: `z` is `t - 1`; `adj` is the adjacency list of the last tree; `n` and `k` are the values from the last iteration; `L` and `R` are two consecutive integers; `numCuts` and `leftover` are the values from the last binary search iteration.
#Overall this is what the function does:The function reads multiple test cases from standard input, each consisting of a tree represented by an adjacency list and a number of edges to be removed. For each test case, it calculates and prints the maximum possible size of the smallest connected component after removing exactly `k` edges from the tree.

