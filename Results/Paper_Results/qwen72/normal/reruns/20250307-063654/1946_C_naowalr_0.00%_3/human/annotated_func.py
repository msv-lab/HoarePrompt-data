#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, n and k are positive integers such that 1 <= k < n <= 10^5, and adj is a list of lists representing the adjacency list of a tree with n vertices.
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
        
    #State: `t` is 0, `z` is `t - 1`, `n` is an input integer greater than 1, `k` is an input integer, `adj` is a list of `n + 1` lists where each list at index `a` and `b` contains the integers `b` and `a` respectively, repeated `n-1` times, `i` is `n - 1`, `a` and `b` are assigned the last pair of input integers, `numCuts` is 0, `leftover` is the result of the `dfs(1, 1)` function call, `R - L <= 1`.
#Overall this is what the function does:The function reads a series of inputs from standard input, processes each input as a tree represented by an adjacency list, and computes a value based on the tree's structure and a given parameter `k`. It performs this computation `t` times, where `t` is the number of test cases provided. For each test case, it outputs a single integer, which is the maximum value `L` that satisfies certain conditions related to the number of cuts (`numCuts`) and a leftover value (`leftover`) obtained from a depth-first search (DFS) on the tree. After processing all test cases, the function concludes with `t` being 0 and `z` being `t - 1`. The function does not return any value but prints the result for each test case.

