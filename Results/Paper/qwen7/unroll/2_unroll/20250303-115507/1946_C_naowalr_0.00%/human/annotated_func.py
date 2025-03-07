#State of the program right berfore the function call: t is a positive integer representing the number of test cases; for each test case, n and k are positive integers such that 1 ≤ k < n ≤ 10^5; for each edge, a and b are integers such that 1 ≤ a, b ≤ n and represent the vertices connected by the edge; the adjacency list adj is constructed based on the input edges, where adj[i] is a list of integers representing the neighbors of vertex i.
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
        
    #State: t test cases where for each case, the value of L after performing the binary search to find the maximum number of edges that can be removed such that the graph remains connected, with the constraint that the number of cuts does not exceed k.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer `n` (number of vertices) and another positive integer `k` (a specific condition). For each test case, it constructs an adjacency list representing the graph's structure. It then performs a binary search to find the maximum number of edges that can be removed while ensuring the graph remains connected, with the constraint that the number of cuts does not exceed `k`. The function outputs the result for each test case, which is the maximum number of edges that can be removed under the given constraints.

