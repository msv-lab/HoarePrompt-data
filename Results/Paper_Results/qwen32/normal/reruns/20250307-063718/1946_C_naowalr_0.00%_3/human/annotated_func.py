#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed such that 1 <= k < n.
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
        
    #State: The loop will have executed `t` times, with each iteration processing a separate tree. For each tree, `adj` will be a list of `n + 1` lists representing the adjacency list of the tree. `n` and `k` will be the values read for that specific tree. `t` will remain the total number of trees to process, and `z` will be equal to `t` after all iterations. `L` and `R` will be the final values that satisfy the condition `R - L <= 1` after the binary search completes for the last tree. `numCuts` will be 0 at the end of the loop, as it is reset at the start of each iteration. The final output will be the value of `L` for the last tree, printed to the standard output.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a tree with `n` vertices and a requirement to remove `k` edges. For each test case, it calculates and prints the minimum number of connected components that can be achieved after removing exactly `k` edges from the tree.

