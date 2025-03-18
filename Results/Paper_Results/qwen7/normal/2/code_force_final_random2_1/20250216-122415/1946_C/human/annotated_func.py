#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each set of input data, n and k are integers such that 1 ≤ k < n ≤ 10^5. The adjacency list adj represents a tree where adj[i] is a list of integers representing the neighbors of vertex i. The value of x is initially set to 1 and R is set to 100001.
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
        
    #State: Output State: `numCuts` is 0, `L` is 50001, `R` is 50001, `x` is 50001, `leftover` is the result of `dfs(1, 1)`.
    #
    #Explanation: After the loop completes all its iterations, the binary search process converges such that `L` and `R` become equal. Given that `numCuts` remains 0 throughout the iterations, the condition `numCuts > k` or `(numCuts == k and leftover >= x)` is never satisfied. Therefore, `L` and `R` both end up being 50001. The variable `x` is set to the final value of `L` (or `R`), which is 50001. The value of `leftover` is the result of the `dfs(1, 1)` function call, which is not modified by the loop.
#Overall this is what the function does:The function performs a binary search to find the minimum value of `x` such that the number of cuts required to remove all leaves from the tree is less than or equal to `k`. If no such `x` exists, it returns the smallest possible value of `x` that satisfies the condition. The function reads input values for `t`, `n`, `k`, and constructs an adjacency list representation of a tree. It then iteratively narrows down the range of possible values for `x` until it finds the correct value or determines that no valid `x` exists. Finally, it prints the determined value of `x`.

