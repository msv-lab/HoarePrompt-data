#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, k is an integer such that 1 ≤ k < n, and edges is a list of tuples where each tuple (a, b) represents an edge in the tree with 1 ≤ a, b ≤ n.
def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        
        g[b].append(a)
        
    #State: Output State: The variable `g` will be a dictionary where each key is a node (integer from 1 to n) and its corresponding value is a list of all nodes directly connected to it via an edge. Each edge `(a, b)` in the `edges` list will result in both `g[a]` containing `b` and `g[b]` containing `a`.
    #
    #In other words, after the loop has executed all iterations, the dictionary `g` will represent the entire adjacency list of the tree defined by the `edges`. Every node will have a list of all its neighboring nodes, ensuring bidirectional connections as specified by each tuple in `edges`.
    c = 0
    l = 1
    r = n // k
    while l <= r:
        mid = l + (r - l) // 2
        
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
        
    #State: Output State: `g` is a dictionary where each key is a node (integer from 1 to n) and its corresponding value is a list of all nodes directly connected to it via an edge; `c` is 0; `l` and `r` are final values determined by the binary search process within the loop; `mid` is the last calculated midpoint value before the loop terminates, which is either `l` + (r - l) // 2 + 1 if `check(mid)` returned True on the last iteration, or `l` + (r - l) // 2 if `check(mid)` returned False on the last iteration.
    #
    #This output state indicates that the loop has completed all its iterations, and the values of `l` and `r` represent the final bounds determined by the binary search algorithm. The variable `c` remains 0 as it was not modified within the loop, and `mid` holds the last computed midpoint value used in the final comparison.
    print(r)
    #This is printed: r (where r is the upper bound determined by the binary search process)
#Overall this is what the function does:The function accepts integers `n` and `k`, and a list of tuples representing edges in a tree. It constructs an adjacency list representation of the tree and then performs a binary search to find a specific value `r`. Finally, it prints the value of `r`.

