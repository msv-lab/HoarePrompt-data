#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n and k are positive integers such that 1 ≤ k < n ≤ 10^5. The adjacency list adj represents a tree with n vertices, where adj[i] is a list of vertices connected to vertex i.
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
        
    #State: `L` is 50001, `R` is 50001, `x` is 50001, `numCuts` is 0, `leftover` is the result of the `dfs(1, 1)` function call.
#Overall this is what the function does:The function processes multiple test cases, each involving a tree represented by an adjacency list. For each test case, it determines the minimum number of cuts required to ensure that the longest path in the tree is less than or equal to a specified value. The function returns the minimum number of cuts needed for each test case.

