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
        
    #State: After the loop executes all iterations, the values of `t`, `n`, `k`, and `adj` remain unchanged. The variables `L`, `R`, and `numCuts` are modified within each iteration of the loop, but their final values depend on the specific input for each test case. The variable `L` will hold the maximum number of cuts that can be made to the tree such that the number of cuts is at most `k` and the leftover length is at least `L`. The variable `R` will be `L + 1`. The variable `numCuts` will be the number of cuts made in the last iteration of the loop.
#Overall this is what the function does:The function `func_1` reads multiple test cases from standard input, each consisting of a tree represented by its adjacency list and two integers `n` and `k`. For each test case, it determines the maximum number of cuts that can be made to the tree such that the number of cuts is at most `k` and the leftover length of the tree after these cuts is at least a certain value. The function prints this maximum number of cuts for each test case. The input parameters `t`, `n`, `k`, and `adj` are not modified by the function, and the function does not return any value.

