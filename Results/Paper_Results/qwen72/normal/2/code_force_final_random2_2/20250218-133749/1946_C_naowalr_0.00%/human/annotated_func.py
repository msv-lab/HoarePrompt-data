#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), n and k are integers such that 1 ≤ k < n ≤ 10^5, and adj is a list of lists where each sublist represents the adjacency list of a vertex in the tree.
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
        
    #State: After the loop executes all iterations, `t` is a positive integer (1 ≤ t ≤ 10^4), `n` and `k` are integers such that 1 ≤ k < n ≤ 10^5, `adj` is a list of `n + 1` lists where each list at index `a` and `b` contains the corresponding connected nodes as specified by the input pairs, `z` is `t - 1`, `i` is `n - 1`, `a` and `b` are the last pair of integers read from the input, `numCuts` is 0, `x` is `(L + R) // 2`, `leftover` is the result of the `dfs(1, 1)` function call, `R - L` is 1 or less. If `numCuts` is greater than `k` or (`numCuts` equals `k` and `leftover` is greater than or equal to `x`), then `L` is the final value of `x`. Otherwise, `R` is the final value of `x`. The loop has printed the value of `L` for each of the `t` test cases.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a tree represented by its adjacency list and two integers `n` and `k`. For each test case, it calculates the maximum number of cuts that can be made in the tree such that no subtree has more than a certain number of nodes. The function prints the maximum number of nodes that can remain in any subtree after making at most `k` cuts, for each test case. After processing all test cases, the function has no return value, but it has printed the results for each test case.

