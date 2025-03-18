#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each set of input data, n and k are integers such that 1 ≤ k < n ≤ 10^5. The adjacency list adj represents a tree where adj[i] is a list of integers representing the neighbors of vertex i. The variable x is the midpoint of the binary search range [L, R], and numCuts keeps track of the number of edges removed during the DFS traversal. The variable leftover represents the size of the largest connected component after removing the edges.
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
        
    #State: The value of `L` after executing the binary search loop for each test case, which represents the maximum length of the cut such that no more than `k` cuts are made and the total leftover material is at least `L`.
#Overall this is what the function does:The function processes multiple test cases, each involving a tree represented by an adjacency list. For each test case, it determines the maximum length of the largest connected component that can be obtained after making no more than `k` cuts, using a binary search approach combined with a depth-first search (DFS) traversal. After completing the binary search for each test case, it prints the value of `L`, which represents the maximum length of the cut under the given constraints.

