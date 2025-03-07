#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each set of input data, n and k are integers such that 1 ≤ k < n ≤ 10^5. For each edge, a and b are integers such that 1 ≤ a, b ≤ n.
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
        
    #State: `L` is 50001, `R` is 50001, `x` is 50001, `numCuts` is 0, `leftover` is `dfs(1, 1)`, `i` is 2, `z` is 9999.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers \( n \) and \( k \), along with a graph represented by edges between nodes. It determines the minimum value \( L \) such that the graph can be cut into at most \( k \) connected components, with each component having at least \( L \) nodes. The function reads input from standard input, constructs the graph, and uses a binary search approach combined with a depth-first search (DFS) to find the value of \( L \). After processing all test cases, it prints the value of \( L \) for each case.

