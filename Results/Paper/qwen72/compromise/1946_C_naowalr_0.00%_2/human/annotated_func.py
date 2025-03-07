#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, n and k are positive integers such that 1 ≤ k < n ≤ 10^5, and a, b are integers such that 1 ≤ a, b ≤ n.
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
        
    #State: After the loop executes all the iterations, `t` is 0, `z` is `t - 1` (which is the total number of iterations completed), `n` and `k` are the last values read from the input, `adj` is a list of lists where each list at index `a` contains all the integers `b` that were paired with `a` in the input, and each list at index `b` contains all the integers `a` that were paired with `b` in the input. The variable `i` is `n - 2`, `a` and `b` are the last integers read from the input, `x` is the final value of `(L + R) // 2` before the loop terminates, `leftover` is the result of the `dfs(1, 1)` function, `numCuts` is 0, `R - L <= 1`. The final values of `L` and `R` will be such that `R - L <= 1`, and `L` is the largest integer such that the conditions `numCuts > k` or (`numCuts == k` and `leftover >= x`) are met, and `R` is `L + 1`.
#Overall this is what the function does:The function `func_1` reads a series of inputs from standard input. It first reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`, followed by `n-1` pairs of integers `a` and `b`. These pairs represent edges in a tree structure. The function then performs a binary search to find the maximum value `L` that satisfies certain conditions involving the number of cuts (`numCuts`) and a leftover value from a depth-first search (DFS). The function prints the value of `L` for each test case. After processing all test cases, the function completes without returning any value. The final state includes the processed values of `t`, `n`, `k`, `a`, `b`, and the adjacency list `adj`, with `t` being 0 and `L` being the largest integer that meets the specified conditions.

