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
        
    #State: After the loop finishes, `t` is decremented by the number of iterations, `n` and `k` retain their last assigned values from the last iteration, and `adj` is the last constructed adjacency list for the tree with `n` vertices. The variables `L`, `R`, and `numCuts` are reset to their initial values or updated based on the last iteration's conditions, and the final value of `L` is printed for each iteration.
#Overall this is what the function does:The function reads an integer `t` from standard input, which represents the number of test cases. For each test case, it reads two integers `n` and `k` from standard input, where `n` is the number of vertices in a tree and `k` is a positive integer less than `n`. It then reads `n-1` lines to construct an adjacency list `adj` representing the tree. The function performs a binary search to determine the maximum value `L` such that the tree can be cut into at most `k` connected components, each with a size of at least `L`. After processing all test cases, the function prints the value of `L` for each test case. The function does not return any value; it only prints the results.

