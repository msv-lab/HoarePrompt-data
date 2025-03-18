#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed such that 1 <= k < n, and edges is a list of tuples where each tuple contains two integers representing an edge between two vertices in the tree.
def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        
        g[b].append(a)
        
    #State: `n` is an integer representing the number of vertices in the tree, `k` is an integer representing the number of edges to be removed such that 1 <= k < n, `edges` is a list of tuples where each tuple contains two integers representing an edge between two vertices in the tree, and `g` is a list of `n + 1` lists where each list at index `a` contains all the vertices `b` that are directly connected to `a` by an edge.
    c = 0
    l = 1
    r = n // k
    while l <= r:
        mid = l + (r - l) // 2
        
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
        
    #State: `l` is `r + 1`, `r` is the final value of `r` after the loop, `mid` is the last calculated midpoint, `c` is 0, `g` is unchanged.
    print(r)
    #This is printed: r (where r is the final value of r after the loop)
#Overall this is what the function does:The function `func_1` takes three parameters: `n`, the number of vertices in a tree; `k`, the number of edges to be removed such that 1 <= k < n; and `edges`, a list of tuples representing the edges between vertices. It computes and prints the maximum number of connected components that can be formed by removing exactly `k` edges from the tree.

