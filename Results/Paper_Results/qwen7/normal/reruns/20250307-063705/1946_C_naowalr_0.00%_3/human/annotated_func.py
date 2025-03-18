#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each set of input data, n and k are integers such that 1 ≤ k < n ≤ 10^5. The adjacency list adj represents a tree with n vertices, where adj[v] is a list of integers representing the neighbors of vertex v. The value of each element in adj is an integer such that 1 ≤ v, u ≤ n.
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
        
    #State: Output State: `numCuts` is 0, `leftover` equals the result of `dfs(1, 1)`, `L` is 1, and `R` is 100001.
    #
    #Explanation: After the loop has executed all its iterations, the condition `R - L > 1` will no longer be true, causing the loop to terminate. Given the behavior of the loop, where `L` and `R` are updated based on the value of `x` (which is the midpoint of the current range), and considering the initial range of `[1, 100001]`, `L` and `R` will eventually converge to the same value or be as close as possible while still maintaining `R - L > 1` is false. The provided output states indicate that after the third iteration, `L` and `R` are 1 and 100001 respectively, and `numCuts` remains 0. Since the loop does not modify `numCuts` or `leftover` after the loop exits, these values remain unchanged. Therefore, after all iterations of the loop have completed, `numCuts` is 0, `leftover` is the result of `dfs(1, 1)`, `L` is 1, and `R` is 100001.
#Overall this is what the function does:The function processes an adjacency list representing a tree with \( n \) vertices. It reads \( t \) test cases, where each case includes \( n \) and \( k \). The function then determines the smallest integer \( L \) such that cutting the tree at depth \( L \) results in at most \( k \) connected components, with each component having at least \( x \) vertices, where \( x \) is calculated by a depth-first search (DFS) starting from vertex 1. The function returns the value of \( L \).

