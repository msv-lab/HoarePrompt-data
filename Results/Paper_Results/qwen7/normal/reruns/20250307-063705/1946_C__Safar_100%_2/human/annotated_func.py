#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed, and edges is a list of tuples where each tuple (a, b) represents an edge connecting vertices a and b.
def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        
        g[b].append(a)
        
    #State: All edges in the `edges` list have been processed, and for every edge (a, b), both `g[a]` and `g[b]` contain each other.
    c = 0
    l = 1
    r = n // k
    while l <= r:
        mid = l + (r - l) // 2
        
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
        
    #State: c is 0, l is either 1 or the last calculated mid + 1, r is either 1 or the last calculated mid - 1, mid is the final calculated mid value, and the loop has terminated based on the condition l > r.
    print(r)
    #This is printed: r (where r is the last calculated mid - 1)
#Overall this is what the function does:The function accepts parameters `n` (number of vertices), `k` (number of edges to be removed), and `edges` (list of tuples representing edges). It constructs an adjacency list representation of the graph, then performs a binary search to find a specific value `r`. Finally, it prints the value of `r`, which is the last calculated mid - 1 when the loop terminates.

