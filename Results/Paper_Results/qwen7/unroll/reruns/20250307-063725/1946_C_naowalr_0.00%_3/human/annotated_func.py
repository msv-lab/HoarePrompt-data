#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n and k are positive integers such that 1 ≤ k < n ≤ 10^5, and represent the number of vertices in the tree and the number of edges to be removed, respectively. adj is a list of adjacency lists where adj[i] contains the list of vertices adjacent to vertex i. The graph is represented as an undirected tree.
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
        
    #State: t test cases where for each case, the value of L is printed after performing binary search to find the maximum number of cuts such that the number of cuts does not exceed k and the leftover length is at least x.
#Overall this is what the function does:The function processes multiple test cases, each involving a tree represented by its number of vertices `n`, the number of edges to be removed `k`, and an adjacency list `adj`. For each test case, it performs a binary search to find the maximum number of cuts such that the number of cuts does not exceed `k` and the remaining part of the tree has at least `x` vertices. It prints the result `L` for each test case.

