#State of the program right berfore the function call: adj is a list of lists representing the adjacency list of a tree with n vertices, where each sublist contains the vertices adjacent to the corresponding vertex. n is the number of vertices in the tree, and k is a non-negative integer such that 1 <= k < n.
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
        
    #State: `z` is equal to `t`, `L` is the final lower bound determined by the last iteration of the loop, `R` is `L + 1`, `n` and `k` are the values read from the last iteration, `adj` is the adjacency list built from the last iteration's input, `numCuts` is the final number of cuts determined by the last iteration of the loop, and `leftover` is the final leftover value determined by the last iteration of the loop.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a tree represented by its number of vertices `n` and an integer `k`. It calculates and prints the maximum size of the smallest component that can be obtained by making at most `k` cuts in the tree.

