#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, n and k are positive integers such that 1 <= k < n <= 10^5, and adj is a list of lists representing the adjacency list of the tree with n vertices.
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
        
    #State: `t` is 0, `z` is `t - 1`, `n` is the last input integer read, `k` is the last input integer read, `adj` is a list of `n + 1` lists where each list `adj[i]` (for 1 <= i <= n) contains the integers that were paired with `i` in the input, `i` is `n - 1`, `a` and `b` are the last integers read from the input, `adj[a]` includes all the `b` values read in the loop as elements, `adj[b]` includes all the `a` values read in the loop as elements, `numCuts` is 0, `leftover` is the result of the `dfs(1, 1)` function call, `L` is the largest integer such that the condition `numCuts <= k and (numCuts < k or leftover < L)` holds, `R` is the smallest integer such that the condition `numCuts > k or (numCuts == k and leftover >= R)` holds, and `R - L` is 1.
#Overall this is what the function does:The function reads a series of inputs from standard input, processes each input as a tree represented by an adjacency list, and for each tree, it calculates and prints the largest integer `L` such that the condition `numCuts <= k and (numCuts < k or leftover < L)` holds, where `numCuts` is the number of cuts made in the tree and `leftover` is the result of a depth-first search (DFS) function. The function does not return any values but prints the result for each test case. After processing all test cases, the function concludes with `t` being 0 and the other variables (`z`, `n`, `k`, `adj`, `i`, `a`, `b`, `numCuts`, `leftover`, `L`, `R`) in their final states as described in the annotations.

