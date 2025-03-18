#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of integers n and m such that 3 ≤ n ≤ m ≤ min(⌊n⋅(n−1)/2⌋, 2⋅10^5), and m lines describing the edges with u, v, and w representing vertices and their connecting edge weight respectively.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program reads an integer from standard input, strips any trailing whitespace, and returns it as an integer.
#Overall this is what the function does:The function reads an integer from standard input, removes any trailing whitespace, and returns it as an integer.

#State of the program right berfore the function call: None of the variables in the provided function signature are present in the given function `func_2()`. The function reads a line from standard input and returns it stripped of leading and trailing whitespace.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips it of any leading or trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any leading or trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of n and m, where 3 ≤ n ≤ m ≤ min(⌊n(n - 1)/2⌋, 2 ⋅ 10^5), and m lines describing the edges of the graph, each containing three integers u, v, and w such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns an integer 't' that is between 1 and 10^4 inclusive.
#Overall this is what the function does:The function reads an integer `t` from standard input, which represents the number of test cases, and ensures that `t` is within the range of 1 to 10^4 inclusive. After reading `t`, the function returns this integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(\frac{n\cdot(n - 1)}{2}, 2 \cdot 10^5), and the subsequent m lines contain three integers u, v, and w representing an edge between vertices u and v with weight w, where 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers read from the standard input. The list contains three integers (u, v, and w) for each test case, representing an edge between vertices u and v with weight w.
#Overall this is what the function does:The function reads a series of test cases from the standard input, where each test case consists of an edge between two vertices with a weight. It returns a list containing these edges as tuples of integers (u, v, w).

#State of the program right berfore the function call: The function `func_5()` reads a line from standard input, splits it into a list of strings, and returns it. Each string in the returned list represents a value from the input line.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings obtained by reading a line from standard input, stripping any leading or trailing whitespace, and splitting the line into a list at the whitespace boundaries.
#Overall this is what the function does:The function `func_5()` reads a line from standard input, strips any leading or trailing whitespace, and splits the line into a list of strings based on whitespace boundaries. It returns this list of strings.

#State of the program right berfore the function call: (n, m) is a tuple of two integers where 3 ≤ n ≤ m ≤ min(⌊n(n - 1)/2⌋, 2⋅10^5), edges is a list of tuples where each tuple contains three integers (u, v, w) representing an edge between vertices u and v with weight w, and dsu is an instance of a DSU (Disjoint Set Union) class initialized with n + 1 elements.
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: Output State: The loop will have executed `m` times since `m` is the number of iterations specified in the `range(m)` function. After all iterations, the variable `i` will be equal to `m-1`. The variable `m` remains the value returned by `func_3()`. The variables `u`, `v`, and `w` will hold the values returned by `func_3()` during the last iteration of the loop. The `graph` will contain all the vertices and their corresponding edges as appended in each iteration. Specifically, for every pair `(u, v)` added to the graph, both `graph[u]` and `graph[v]` will include the other vertex. The `edges` list will contain `m` tuples, each representing an edge with its weight and the two vertices it connects.
    #
    #In summary, the final state will have `i` set to `m-1`, `m` unchanged from its initial value, `u`, `v`, and `w` holding the values from the last call to `func_3()`, the `graph` fully populated with all the edges added, and the `edges` list containing all the weights and connections as tuples.
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
        
    #State: All vertices in the graph are connected, and the minimum edge weight among all connected components is stored in \_min\_edge. Node\_u and Node\_v store the vertices of the minimum edge.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge, len(res)
    print(*res)
    #This is printed: [Node_u, Node_v, ...] (where the list contains nodes visited during the DFS starting from Node_u)
#Overall this is what the function does:The function processes a graph represented by vertices and weighted edges. It first constructs the graph and sorts the edges in descending order of their weights. Then, it uses the Disjoint Set Union (DSU) data structure to find the minimum spanning tree (MST) of the graph. Specifically, it identifies the minimum-weight edge that connects different components of the graph. After finding the MST, it performs a depth-first search (DFS) starting from one of the vertices involved in the minimum-weight edge to determine the path in the MST. Finally, it prints the weight of the minimum-weight edge and the sequence of nodes visited during the DFS traversal.

#State of the program right berfore the function call: curr is the current vertex being visited (an integer), parent is the parent vertex in the DFS traversal (an integer), and path is a list representing the current path in the DFS traversal (a list of integers).
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the list 'path' which represents the current path in the DFS traversal.
    #State: curr is the current vertex being visited (an integer), parent is the parent vertex in the DFS traversal (an integer), and path is a list representing the current path in the DFS traversal (a list of integers). The color of the current vertex is not 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: Output State: `curr` is the final vertex being visited (an integer), `parent` is the parent vertex in the DFS traversal (an integer), `path` is a list representing the final path in the DFS traversal (a list of integers) with `curr` appended to it, `graph[curr]` is either empty or none of its neighbors have been processed further (i.e., their `colors` are not 2), and `res` is either empty or contains the vertex `node_v` if it was found during the traversal.
    #
    #This output state describes the condition where the loop has completed all its iterations, meaning no more unvisited neighbors of the current vertex exist, or the traversal has reached a point where further exploration does not find the vertex `node_v`. The `res` variable will hold the path to `node_v` if it was found, otherwise it will be empty.
    colors[curr] = 2
    return []
    #The program returns an empty list
#Overall this is what the function does:The function performs a Depth-First Search (DFS) traversal starting from the given vertex `curr`. It maintains a list `path` representing the current path in the traversal. If the current vertex `curr` is already being visited (color 1), it returns the current path. Otherwise, it marks the current vertex as visited, appends it to the path, and recursively explores its unvisited neighbors (excluding the parent vertex). If the target vertex `node_v` is found during the traversal, it returns the path to `node_v`. After completing the traversal or finding the target vertex, it marks the current vertex as fully visited and returns either the path to `node_v`, the current path, or an empty list if the target vertex is not found.

#State of the program right berfore the function call: test_cases is an integer such that 1 ≤ test_cases ≤ 10^4. Each test case consists of two integers n and m such that 3 ≤ n ≤ m ≤ min(\frac{n\cdot(n - 1)}{2}, 2 \cdot 10^5), and m lines describing the edges of the graph, where each line contains three integers u, v, and w representing an edge between vertices u and v with weight w (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 10^6).
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` is an integer such that \(1 \leq \text{test_cases} \leq 10^4\)
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers n and m, followed by m lines describing the edges of a graph. It does not return any value but ensures that for each test case, n and m adhere to specified constraints (3 ≤ n ≤ m ≤ min(\frac{n\cdot(n - 1)}{2}, 2 \cdot 10^5)), and each edge is represented by integers u, v, and w (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 10^6).

