#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of integers n, m, u, v, and w, where 3 ≤ n ≤ m ≤ min(⌊n(n-1)/2⌋, 2⋅10^5), 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program reads an integer from standard input, strips any trailing whitespace, and returns it as an integer.
#Overall this is what the function does:The function reads an integer from standard input, removes any trailing whitespace, and returns it as an integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(\frac{n\cdot(n - 1)}{2}, 2 \cdot 10^5), and the subsequent m lines contain three integers u, v, and w representing an edge between vertices u and v with weight w, where 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the resulting string. This action is performed regardless of the content or length of the input line.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(\frac{n\cdot(n - 1)}{2}, 2 \cdot 10^5), and m represents the number of edges in the graph. Each of the next m lines contains three integers u, v, and w such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6, representing an edge between vertices u and v with weight w.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns an integer value read from standard input, stripped of any leading or trailing whitespace, split into individual strings based on whitespace, and then converted to integers.
#Overall this is what the function does:The function reads an integer value from standard input, removes any leading or trailing whitespace, splits the input into individual strings based on whitespace, converts these strings to integers, and returns the first integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n⋅(n - 1)/2⌋, 2⋅10^5), and m represents the number of edges in the graph. u, v, and w are integers such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6, representing the vertices and the weight of the edge between them.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program reads a line from standard input, strips any trailing whitespace, splits the line into individual strings, converts each string to an integer, and returns a list of these integers.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, splits the line into individual strings, converts each string to an integer, and returns a list of these integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(\frac{n\cdot(n - 1)}{2}, 2 \cdot 10^5), and m represents the number of edges in the graph. Each of the next m lines contains three integers u, v, and w such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6, representing an edge between vertices u and v with weight w.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, each string representing a line from the standard input, stripped of any trailing whitespace.
#Overall this is what the function does:The function reads a single line from the standard input, splits it into a list of strings based on whitespace, and strips any trailing whitespace from each string. It returns this list of strings.

#State of the program right berfore the function call: (n, m) is a tuple of two integers where 3 ≤ n ≤ m ≤ min(⌊n(n - 1)/2⌋, 2 * 10^5), edges is a list of tuples where each tuple (u, v, w) represents an edge between vertices u and v with weight w, and DSU is a data structure representing Disjoint Set Union with additional attributes like `find`, `union`, and `min_edge`.
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: Output State: `edges` is now a list containing tuples of the form `(w, u, v)` for each iteration of the loop, `n` is the return value of `func_3()`, `m` is the return value of `func_3()`, and `graph` is a defaultdict where the default factory is list. For each iteration `i` from `0` to `m-1`, `u`, `v`, and `w` are the return values of `func_3()`. After all iterations, `graph[u]` will contain all vertices `v` that are connected to `u` with their corresponding weights `w`, and vice versa for `graph[v]`. The length of `edges` will be equal to `m`, and `i` will be equal to `m - 1`.
    edges.sort(reverse=True)
    dsu = DSU(n + 1)
    _min_edge = float('inf')
    node_u = -1
    node_v = -1
    for (w, u, v) in edges:
        parent_u = dsu.find(u)
        
        parent_v = dsu.find(v)
        
        if parent_u == parent_v:
            dsu.union(u, v, w)
            if dsu.min_edge[parent_u] < _min_edge:
                _min_edge = dsu.min_edge[parent_u]
                node_u = u
                node_v = v
        else:
            dsu.union(u, v, w)
        
    #State: Output State: All nodes in the graph will be merged into connected components, and `node_u` and `node_v` will hold the values of the nodes that form the minimum spanning tree (MST) of the graph. Specifically, `node_u` and `node_v` will point to the two nodes that have the smallest edge weight among all the edges that were processed during the loop. The `dsu.min_edge` attribute will reflect the minimum edge weight within the connected component that `node_u` belongs to, and `_min_edge` will hold the overall minimum edge weight found during the entire execution of the loop.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge, len(res) (where _min_edge is the overall minimum edge weight found during the loop and len(res) is the number of nodes in the DFS traversal starting from node_u)
    print(*res)
    #This is printed: [node] ... [node] (where [node] represents the nodes visited during the DFS traversal starting from node_u)
#Overall this is what the function does:The function processes a graph represented by vertices and weighted edges using a Disjoint Set Union (DSU) data structure to find the minimum spanning tree (MST). It first constructs an adjacency list representation of the graph and sorts the edges in descending order of their weights. Then, it iteratively processes each edge, merging connected components and updating the minimum edge weight found so far. Finally, it performs a depth-first search (DFS) starting from one of the nodes involved in the MST to determine the connected component size and prints the minimum edge weight along with the number of nodes in the DFS traversal.

#State of the program right berfore the function call: curr is an integer representing the current vertex being visited, parent is an integer representing the previously visited vertex, and path is a list representing the current path of vertices being explored.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the list 'path' which represents the current path of vertices being explored.
    #State: `curr` is an integer representing the current vertex being visited, `parent` is an integer representing the previously visited vertex, and `path` is a list representing the current path of vertices being explored. The color of the vertex `curr` is not 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: Output State: The loop will continue to execute as long as there are unvisited neighbors (color != 2) of the current vertex (`curr`) that are not the parent vertex. For each such neighbor, the DFS function is called recursively. If at any point the DFS call returns a non-empty result containing `node_v`, the function will return that result. If no such result is found after all possible paths are explored, the function will eventually return `None`.
    #
    #This means that after all iterations of the loop, the output state will be determined by whether `node_v` was found in any of the DFS paths starting from the initial `curr` vertex and exploring through its neighbors, excluding the parent vertex, until all possible paths are exhausted. If `node_v` is found in any of these paths, the function will return that path (as a list of vertices). If `node_v` is not found in any path, the function will return `None`.
    colors[curr] = 2
    return []
    #The program returns an empty list
#Overall this is what the function does:The function performs a depth-first search (DFS) to explore the graph starting from the current vertex (`curr`). It maintains a list (`path`) representing the current path of vertices being explored and uses a `colors` array to keep track of the visiting status of each vertex. The function returns one of the following:
1. The list `path` if the current vertex is already visited.
2. A set `res` containing the return value from the DFS function call if `node_v` is found in any path.
3. An empty list if no valid path is found after exploring all possibilities.

#State of the program right berfore the function call: test_cases is an integer representing the number of test cases, and each test case consists of an undirected weighted graph described by integers n, m, u, v, and w as specified in the problem description.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: Output State: `test_cases` must be greater than 0.
    #
    #In natural language: The output state after the loop executes all its iterations is that `test_cases` must still be greater than 0. This is because the loop continues to run as long as `test_cases` is greater than 0, and there is no operation within the loop that changes the value of `test_cases`. Therefore, if the loop runs for 1, 2, or 3 times, it implies that `test_cases` was initially greater than 0 and remained so throughout the loop's execution.
#Overall this is what the function does:The function processes multiple test cases, each representing an undirected weighted graph. It iterates through the specified number of test cases (stored in `test_cases`) and calls `func_6()` for each iteration. After completing all iterations, the function ensures that `test_cases` remains greater than 0, indicating that all specified test cases were successfully processed. The function does not return any value.

