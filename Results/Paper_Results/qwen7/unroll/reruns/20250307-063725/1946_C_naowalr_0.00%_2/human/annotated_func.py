#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each set of input data such that 1 ≤ k < n ≤ 10^5, and adj is a list of lists where adj[i] is a list of integers representing the neighbors of vertex i in the tree.
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
        
    #State: Output State: t is an integer with a value between 1 and 10^4 (inclusive), each call to `dfs(1, 1)` results in a value of `L` which is the largest integer x such that it is possible to make at most k cuts in the tree and have at least x nodes left uncut.
#Overall this is what the function does:The function processes up to 10,000 sets of input data. For each set, it takes two integers \( n \) and \( k \) along with a tree represented by an adjacency list \( adj \). It then determines the largest integer \( x \) such that it is possible to make at most \( k \) cuts in the tree and still have at least \( x \) nodes left uncut. The function prints this value \( x \) for each set of input data.

