#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each set of input data, n and k are integers such that 1 ≤ k < n ≤ 10^5. The adjacency list adj represents a tree where adj[i] is a list of integers representing the neighbors of vertex i. The variable L is initialized to 1 and R is initialized to 100001. The function dfs is assumed to exist and returns the number of vertices in the largest connected component that remains after removing the edges according to the current value of x.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ `t` ≤ 10^4, `L` is 1, `R` is 1.
    #
    #Explanation: The loop iterates `t` times, and in each iteration, it performs a binary search to find the maximum value `x` such that the number of cuts required to divide the tree into components where no component has more than `x` nodes is less than or equal to `k`. After each iteration, the value of `L` is updated based on the result of the binary search. Since the binary search converges to a specific value within the range `[L, R]`, and `R` is initially set to `int(100000.0 + 1)` which is 100001, the final value of `L` will be the largest value that satisfies the condition. However, since the loop ends when `R - L` is no longer greater than 1, the final value of `L` will be 1, and `R` will also be 1.
#Overall this is what the function does:The function reads multiple sets of inputs, each consisting of the number of vertices \( n \), the number of cuts \( k \), and an adjacency list representing a tree. It then performs a binary search to find the maximum value \( x \) such that the number of cuts required to divide the tree into components where no component has more than \( x \) nodes is less than or equal to \( k \). The function outputs the value of \( L \) after the binary search completes, which represents the largest possible value \( x \) satisfying the condition.

