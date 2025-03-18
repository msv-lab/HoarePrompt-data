#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, n and k are positive integers such that 1 ≤ k < n ≤ 10^5, and adj is a list of lists where each sublist represents the adjacency list of a vertex in the tree.
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
        
    #State: The loop will iterate `t` times, and for each iteration, it will read `n` and `k` from the input, construct the adjacency list `adj` for a tree with `n` vertices, and then perform a binary search to find the maximum value `L` such that the number of cuts required to split the tree into subtrees of size at least `L` is at most `k`. After all iterations, the final value of `L` for each iteration will be printed. The variables `t`, `n`, `k`, and `adj` will be updated for each iteration, but the final state of these variables after the loop will be the state after the last iteration. The variable `L` will be the result of the binary search for the last iteration, and `R` will be `L + 1`. The variable `numCuts` will be the number of cuts required for the last iteration, and `leftover` will be the size of the largest subtree after the cuts for the last iteration.
#Overall this is what the function does:The function `func_1` reads a series of test cases from the standard input. For each test case, it reads two integers `n` and `k`, constructs an adjacency list `adj` representing a tree with `n` vertices, and performs a binary search to determine the maximum value `L` such that the tree can be cut into subtrees of size at least `L` using at most `k` cuts. After processing all test cases, the function prints the value of `L` for each test case. The function does not return any value; it only prints the results to the standard output. The variables `t`, `n`, `k`, and `adj` are updated for each test case, and the final state of these variables will be the state after the last test case. The variables `L`, `R`, `numCuts`, and `leftover` are used internally and reset for each test case.

