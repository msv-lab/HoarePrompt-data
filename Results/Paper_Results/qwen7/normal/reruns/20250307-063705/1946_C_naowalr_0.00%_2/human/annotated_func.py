#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n and k are positive integers such that 1 ≤ k < n ≤ 10^5. The adjacency list adj is a list of lists where adj[i] contains the neighbors of vertex i in the tree. The value of n - 1 is the number of edges in the tree.
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
        
    #State: `numCuts` is 0, `L` and `R` are consecutive integers with `R - L` equal to 1, `x` is the smaller of `L` and `R`, `leftover` is the result of `dfs(1, 1)` from the last iteration.
#Overall this is what the function does:For each test case, the function reads the number of test cases \( t \), the number of vertices \( n \) and a threshold \( k \) from standard input, along with the adjacency list \( adj \) representing a tree. It then determines the smallest integer \( x \) such that cutting the tree at height \( x \) results in at most \( k \) connected components, with the total number of vertices in the largest component being less than or equal to 100001. The function prints this integer \( x \) for each test case.

