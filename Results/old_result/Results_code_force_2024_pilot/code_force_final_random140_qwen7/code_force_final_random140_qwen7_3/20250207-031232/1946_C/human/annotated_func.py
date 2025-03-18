#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, k is an integer representing the number of edges to be removed, and edges is a list of tuples where each tuple (a, b) represents an edge connecting vertices a and b.
def func_1(n, k, edges):
    g = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        g[a].append(b)
        
        g[b].append(a)
        
    #State: After the loop executes all the iterations, for every edge (a, b) in the `edges` list, both `g[a]` and `g[b]` will contain each other.
    c = 0
    visited = set()
    l = 1
    r = n // k + 1
    while l <= r:
        mid = l + (r - l) // 2
        
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
        
    #State: The output state after the loop executes all the iterations is that `c` is still 0, `visited` is still an empty set, and both `l` and `r` will converge to the same value which is the result of the binary search performed by the loop.
    print(r)
    #This is printed: the result of the binary search
#Overall this is what the function does:The function accepts three parameters: `n` (the number of vertices), `k` (the number of edges to be removed), and `edges` (a list of tuples representing edges in a tree). It constructs an adjacency list representation of the tree, performs a binary search to find a specific value, and prints the result of the binary search. The function does not return any value but prints the outcome of the binary search.

#State of the program right berfore the function call: x is an integer representing a vertex in the tree, y is an integer representing the required minimum size of each remaining connected component after removing k edges. g is a dictionary where keys are vertices and values are lists of adjacent vertices, and visited is a set of visited vertices during the DFS traversal.
def dfs(x, y):
    c = 1
    r = 0
    visited.add(x)
    for node in g[x]:
        if node not in visited:
            ans, rn = dfs(node, y)
            r += rn
            if ans >= y:
                r += 1
            else:
                c += ans
        
    #State: Output State: `r` is the sum of all `rn` values plus the number of times `ans` was greater than or equal to `y`. `c` is the sum of all `ans` values when `ans` was less than `y`. `x` is an integer representing a vertex in the tree, `y` is an integer representing the required minimum size of each remaining connected component after removing k edges, `g` is a dictionary where keys are vertices and values are lists of adjacent vertices, `visited` is a set of visited vertices during the DFS traversal including the vertex `x`, and `node` is a vertex not in `visited`. `ans` and `rn` are the results returned by the dfs function.
    #
    #In simpler terms, after all iterations of the loop, `r` will be the total count of nodes that meet or exceed the minimum size requirement (`y`), plus the sum of counts of nodes that do not meet the requirement but were still processed. `c` will be the total count of nodes that do not meet the minimum size requirement. The variables `x`, `y`, `g`, `visited`, and the way the loop processes `node` remain as described.
    return c, r
    #The program returns a tuple containing two values: `c`, which is the sum of all `ans` values when `ans` was less than `y`, and `r`, which is the sum of all `rn` values plus the number of times `ans` was greater than or equal to `y`.
#Overall this is what the function does:The function `dfs` takes two parameters, `x` (an integer representing a vertex in the tree) and `y` (an integer representing the required minimum size of each remaining connected component after removing k edges). It performs a depth-first search (DFS) traversal of the tree starting from vertex `x`. During this traversal, it calculates two values: `c` and `r`. The value `c` represents the total count of nodes that do not meet the minimum size requirement (`y`), while `r` represents the total count of nodes that meet or exceed the minimum size requirement (`y`). The function returns these two values as a tuple.

#State of the program right berfore the function call: x is an integer representing the size of each remaining connected component, visited is a set initialized to keep track of visited nodes, and dfs is a function that performs a depth-first search to determine if it's possible to remove exactly k edges such that each remaining connected component has at least x vertices.
def check(x):
    visited.clear()
    ans, r = dfs(1, x)
    if (ans >= x and r >= k) :
        return True
        #The program returns True
    #State: `visited` is an empty set, `ans` is the result of the dfs function call with parameters (1, x), `r` is the second return value of the dfs function call with parameters (1, x). Either `ans` is less than `x` or `r` is less than `k`
    return False
    #The program returns False
#Overall this is what the function does:The function `check(x)` accepts an integer `x` and determines whether it's possible to remove exactly `k` edges from a graph such that each remaining connected component contains at least `x` vertices. If this condition can be met, the function returns `True`; otherwise, it returns `False`.

