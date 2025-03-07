#State of the program right berfore the function call: t is a positive integer representing the number of test cases; n and k are positive integers such that 1 ≤ k < n ≤ 10^5 for each test case; adj is a list of lists where adj[i] contains the list of vertices adjacent to vertex i; the input is read from stdin and the output is printed to stdout.
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
        
    #State: `L` is 33334, `R` is 33335, `numCuts` is 0, `x` is 33334, `leftover` is `dfs(1, 1)`.
#Overall this is what the function does:The function processes multiple test cases, each defined by positive integers \(t\), \(n\), and \(k\), and a graph represented by adjacency lists. For each test case, it determines the minimum value \(L\) such that cutting the graph at certain edges results in at least \(k\) connected components, with each component having at most \(L\) vertices. The function then prints the value of \(L\) for each test case.

