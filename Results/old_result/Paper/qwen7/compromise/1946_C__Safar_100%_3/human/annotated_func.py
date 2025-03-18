#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed, and edges is a list of tuples where each tuple (a, b) represents an edge connecting vertices a and b.
def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        
        g[b].append(a)
        
    #State: `g[a]` now contains a list of all `b` values from the `edges` list, and `g[b]` now contains a list of all `a` values from the `edges` list. The length of both lists is equal to the number of edges in the `edges` list. `n` is an integer representing the number of vertices in the tree, `k` is an integer representing the number of edges to be removed, and `edges` is a list of tuples representing all the edges in the tree.
    c = 0
    l = 1
    r = n // k
    while l <= r:
        mid = l + (r - l) // 2
        
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
        
    #State: Output State: `l` is greater than `r`.
    #
    #Explanation: The binary search algorithm continues to narrow down the range defined by `l` and `r` until no more valid midpoints can be found that satisfy the condition of the `check(mid)` function. Since the loop continues to adjust `l` and `r` based on the result of `check(mid)`, it will eventually reach a point where `l` becomes greater than `r`. At this point, the loop terminates, indicating that the search space has been exhausted without finding a value that satisfies the `check(mid)` condition.
    print(r)
    #This is printed: r (where r is the last value of r before l became greater than r)
#Overall this is what the function does:The function accepts three parameters: `n` (the number of vertices in the tree), `k` (the number of edges to be removed), and `edges` (a list of tuples representing the edges in the tree). It constructs an adjacency list representation of the tree, then performs a binary search to find the maximum number of connected components that can be achieved by removing up to `k` edges. The function prints the result, which is the last value of `r` before `l` becomes greater than `r`.

